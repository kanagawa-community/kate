#!/usr/bin/env python3
"""Write themes/kanagawa-<variant>.theme (KSyntaxHighlighting) from the shared palette.

Usage: scripts/generate.py [path/to/palette.json]   (default: ../.github/palette.json)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VARIANTS = ["wave", "dragon", "lotus"]

# KSyntaxHighlighting text style -> (palette role, extra attributes). Follows the
# Neovim plugin: italic comments and keywords, bold statements.
TEXT = {
    "Normal": ("ui.fg", {}),
    "Keyword": ("syn.keyword", {"italic": True}),
    "Function": ("syn.fun", {}),
    "Variable": ("syn.identifier", {}),
    "ControlFlow": ("syn.statement", {"bold": True}),
    "Operator": ("syn.operator", {}),
    "BuiltIn": ("syn.special1", {}),
    "Extension": ("syn.type", {}),
    "Preprocessor": ("syn.preproc", {}),
    "Attribute": ("syn.constant", {}),
    "Char": ("syn.string", {}),
    "SpecialChar": ("syn.regex", {}),
    "String": ("syn.string", {}),
    "VerbatimString": ("syn.string", {}),
    "SpecialString": ("syn.regex", {}),
    "Import": ("syn.constant", {}),
    "DataType": ("syn.type", {}),
    "DecVal": ("syn.number", {}),
    "BaseN": ("syn.number", {}),
    "Float": ("syn.number", {}),
    "Constant": ("syn.constant", {}),
    "Comment": ("syn.comment", {"italic": True}),
    "Documentation": ("syn.comment", {"italic": True}),
    "Annotation": ("syn.special1", {}),
    "CommentVar": ("syn.parameter", {}),
    "RegionMarker": ("ui.special", {}),
    "Information": ("diag.info", {}),
    "Warning": ("diag.warning", {}),
    "Alert": ("diag.error", {"bold": True}),
    "Error": ("diag.error", {"underline": True}),
    "Others": ("syn.special1", {}),
}
EDITOR = {
    "BackgroundColor": "ui.bg",
    "BracketMatching": "ui.bg_search",
    "CodeFolding": "ui.bg_p1",
    "CurrentLine": "ui.bg_p2",
    "CurrentLineNumber": "diag.warning",
    "IconBorder": "ui.bg_gutter",
    "IndentationLine": "ui.whitespace",
    "LineNumbers": "ui.nontext",
    "MarkBookmark": "syn.fun",
    "MarkBreakpointActive": "diag.error",
    "MarkBreakpointDisabled": "syn.deprecated",
    "MarkBreakpointReached": "diag.warning",
    "MarkError": "diag.error",
    "MarkExecution": "diag.info",
    "MarkWarning": "diag.warning",
    "ModifiedLines": "vcs.changed",
    "ReplaceHighlight": "diff.text",
    "SavedLines": "vcs.added",
    "SearchHighlight": "ui.bg_search",
    "Separator": "ui.nontext",
    "SpellChecking": "diag.error",
    "TabMarker": "ui.whitespace",
    "TemplateBackground": "ui.bg_m1",
    "TemplateFocusedPlaceholder": "ui.bg_p2",
    "TemplatePlaceholder": "ui.bg_p1",
    "TemplateReadOnlyPlaceholder": "ui.bg_m1",
    "TextSelection": "ui.bg_visual",
    "WordWrapMarker": "ui.nontext",
}


def roles(variant):
    """Map each role to its hex; a role missing from the palette raises KeyError later."""
    return {role: color["hex"] for color in variant["colors"].values() for role in color["usage"]}


def theme(name, r):
    text = {k: {"text-color": r[role], "selected-text-color": r[role], **extra} for k, (role, extra) in TEXT.items()}
    return json.dumps(
        {
            "metadata": {
                "name": f"Kanagawa {name}",
                "revision": 1,
                "license": "MIT",
                "author": "Kanagawa Community contributors",
            },
            "text-styles": text,
            "editor-colors": {k: r[role] for k, role in EDITOR.items()},
        },
        indent=2,
    ) + "\n"


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / ".github" / "palette.json"
    variants = json.loads(path.read_text())["variants"]
    for v in VARIANTS:
        out = ROOT / "themes" / f"kanagawa-{v}.theme"
        out.parent.mkdir(exist_ok=True)
        out.write_text(theme(v.capitalize(), roles(variants[v])))
        print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
