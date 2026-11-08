# Contributing to Kanagawa for Kate

Thanks for helping. This port follows the
[Kanagawa community contributing guide](https://github.com/kanagawa-community/.github/blob/main/.github/CONTRIBUTING.md),
which explains conventional commits, the checks every pull request runs, and how
changes are reviewed. This page covers only what is specific to this port.

## Where to report what

- Problems with the theme in Kate, such as wrong colors, poor
  contrast, or a missing variant, belong in this repository's
  [issue tracker](https://github.com/kanagawa-community/kate/issues).
- Problems in Kate itself belong with its maintainers, not here. Start
  from the [application's page](https://kate-editor.org).
- Changes to the colors themselves belong in the
  [shared palette](https://github.com/kanagawa-community/.github/blob/main/docs/PALETTE.md),
  not in this port. Open an issue in the
  [.github repository](https://github.com/kanagawa-community/.github/issues)
  so every port stays in step.

## Colors

Take colors from the shared [palette](https://github.com/kanagawa-community/.github/blob/main/docs/PALETTE.md)
and follow the [style guide](https://github.com/kanagawa-community/.github/blob/main/docs/STYLE-GUIDE.md).
Do not sample colors from screenshots or add new ones. Every change must work in
Wave, Dragon, and Lotus.

To read the colors from a script, use the machine-readable
[palette.json](https://raw.githubusercontent.com/kanagawa-community/.github/main/palette.json).

## Working on this port

`themes/` is generated. Do not edit it by hand. `scripts/generate.py` reads the
shared `palette.json` from a sibling checkout of the
[.github repository](https://github.com/kanagawa-community/.github) (or from a path
given as its first argument) and maps each KSyntaxHighlighting style to a palette role. The
README lists the mapping. After changing the mapping, regenerate and commit the
result:

```sh
python3 scripts/generate.py
```

A pull request also runs the **Generated** check (`.github/workflows/generated.yml`). It
regenerates the files from the current shared palette and fails if anything differs, so
commit the regenerated files with your change. When the palette itself changes, the check
fails until someone regenerates.

To try a change, copy `themes/kanagawa-wave.theme` to
`~/.local/share/org.kde.syntax-highlighting/themes/` and pick it under Settings > Configure Kate > Color Themes. `ksyntaxhighlighter6 --theme "Kanagawa Wave" -f html <file>` renders a file with it from the terminal.

Screenshots in `assets/` are real Kate windows. Take one per variant with
comparable content, then build the showcase and social preview with
`scripts/finish-previews.sh` from the .github repository. See the
[preview standard](https://github.com/kanagawa-community/.github/blob/main/docs/PREVIEWS.md).

## Pull requests

- Keep each pull request to one change, and include a screenshot of each variant
  it affects.
- Update the README when installation or usage changes.
