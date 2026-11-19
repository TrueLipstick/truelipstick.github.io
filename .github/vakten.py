#!/usr/bin/env python3
"""Vakten: fångar en enhet som skriver över sajten med en gammal kopia.

Körs av .github/workflows/vakten.yml efter varje push till main.

Mönstret den letar efter är det som hände 2026-09-12 (8ce632e): en enhet
committar en inaktuell arbetskopia ovanpå den senaste versionen. Det syns
på att flera filer i ett och samma commit sätts tillbaka till en version
de redan har haft, ofta tillsammans med att nyare filer raderas. Vanliga
ändringar och vanliga raderingar ser aldrig ut så, så Vakten håller tyst
om dem.

Signalen räknas per commit (merge-commits hoppas över, det är i enhetens
eget commit som överskrivningen sker):
  - ÅTERGÅTT: filen blir byte för byte en tidigare version av sig själv.
  - RADERAD:  filen tas bort. Räknas bara om commitet också har ÅTERGÅTT.
Två signaler eller fler, varav minst en ÅTERGÅTT, flaggar commitet. En
ensam ångrad ändring i en fil flaggas alltså inte.

Commits vars meddelande innehåller "revert", "återställ" eller
"[avsiktligt]" lämnas alltid i fred. Det är så en människa (eller Vakten
själv) säger att en återgång är menad.

Vad Vakten gör med ett flaggat commit: varje fil det rörde läggs tillbaka
som den var före commitet, men bara om filen inte har ändrats igen
efteråt. Allt annat redovisas i rapporten och lämnas orört.

Dessutom: filer som .gitignore säger aldrig ska publiceras men som ändå
ligger spårade (en .md i en kategorimapp, Obsidians layoutfiler) slutar
spåras. De raderas inte från någon enhet förrän den hämtar ändringen.

Användning:
  vakten.py BEFORE AFTER [--dry-run]
Skriver rapporten till vakten-rapport.md och sätter ändrat=true i
$GITHUB_OUTPUT om något återställdes. Med --dry-run skrivs bara vad som
skulle ha flaggats.
"""
import os
import re
import subprocess
import sys

SKIP_PREFIXES = (".obsidian/", ".github/")
EXEMPT = re.compile(r"revert|återställ|\[avsiktligt\]", re.IGNORECASE)
NOLL = "0" * 40


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def blob(rev, path):
    r = subprocess.run(["git", "rev-parse", "-q", "--verify", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.stdout.strip() or None


def tidigare_blobbar(rev, path):
    """Alla versioner filen har haft fram till och med rev."""
    ut = git("log", "--raw", "--no-abbrev", "--format=", rev, "--", path)
    return {rad.split()[3] for rad in ut.splitlines() if rad.startswith(":")}


def granska(c):
    """Returnerar (signaler, ändringar) för ett commit."""
    p = c + "^"
    signaler, andringar = [], []
    for rad in git("diff-tree", "-r", "--no-renames", "--no-commit-id", c).splitlines():
        meta, path = rad.split("\t", 1)
        _, _, gammal, ny, status = meta.split()
        if path.startswith(SKIP_PREFIXES):
            continue
        andringar.append((status, path))
        if status == "M" and ny in tidigare_blobbar(p, path):
            signaler.append(("ÅTERGÅTT", path))
        elif status == "A" and ny in tidigare_blobbar(p, path):
            signaler.append(("ÅTERUPPSTÅNDEN", path))
        elif status == "D":
            signaler.append(("RADERAD", path))
    aterg = [s for s in signaler if s[0] != "RADERAD"]
    if not aterg or len(signaler) < 2:
        return [], andringar
    return signaler, andringar


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    before, after = sys.argv[1], sys.argv[2]
    dry = "--dry-run" in sys.argv

    if before == NOLL or subprocess.run(["git", "cat-file", "-e", before + "^{commit}"]).returncode:
        intervall = [after]          # ny gren eller okänd bas: granska bara toppen
    else:
        intervall = git("rev-list", "--no-merges", "--reverse", f"{before}..{after}").split()

    rapport, atgarder = [], 0
    for c in intervall:
        if not git("rev-list", "--parents", "-n1", c).split()[1:]:
            continue                 # rotcommit
        if len(git("rev-list", "--parents", "-n1", c).split()) > 2:
            continue                 # merge
        meddelande = git("log", "-1", "--format=%s", c).strip()
        if EXEMPT.search(meddelande):
            continue
        signaler, andringar = granska(c)
        if not signaler:
            continue
        vem = git("log", "-1", "--format=%an, %ad", "--date=format:%Y-%m-%d %H:%M", c).strip()
        rapport.append(f"### `{c[:7]}` · {meddelande}\n\n{vem}\n")
        rapport.append("Det här commitet satte tillbaka filer till äldre versioner, vilket är "
                       "kännetecknet på en enhet som har committat en gammal kopia.\n")
        for typ, path in signaler:
            rapport.append(f"- {typ}: `{path}`")
        rapport.append("")
        if dry:
            continue
        for status, path in andringar:
            if blob(after, path) != blob(c, path):
                rapport.append(f"- Rörde inte `{path}`: den har ändrats igen efter `{c[:7]}`.")
                continue
            if blob(c + "^", path) is None:
                git("rm", "-q", "--", path)
                rapport.append(f"- Tog bort `{path}` igen.")
            else:
                git("checkout", c + "^", "--", path)
                rapport.append(f"- Återställde `{path}` till versionen före `{c[:7]}`.")
            atgarder += 1
        rapport.append("")

    # Övrig .obsidian/ spåras med avsikt; bara layoutfilerna läcker utkastnamn.
    spårade_ignorerade = [p for p in git("ls-files", "-ci", "--exclude-standard").splitlines()
                          if p and (not p.startswith(SKIP_PREFIXES)
                                    or re.fullmatch(r"\.obsidian/workspace[^/]*\.json", p))]
    if spårade_ignorerade:
        rapport.append("### Filer som aldrig ska publiceras\n")
        rapport.append(".gitignore säger att de här inte hör hemma på sajten, men de låg ändå med:\n")
        for path in spårade_ignorerade:
            rapport.append(f"- `{path}`")
            if not dry:
                git("rm", "-q", "--cached", "--", path)
                atgarder += 1
        rapport.append("\nDe ligger kvar på den enhet som lade dit dem, men syns inte längre på sajten.\n")

    text = "\n".join(rapport)
    if dry:
        print(text or "Inget att anmärka.")
        return
    with open("vakten-rapport.md", "w", encoding="utf-8") as f:
        f.write(text)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"andrat={'true' if atgarder else 'false'}\n")
            f.write(f"anmarkning={'true' if text else 'false'}\n")
    print(text or "Inget att anmärka.")


if __name__ == "__main__":
    main()
