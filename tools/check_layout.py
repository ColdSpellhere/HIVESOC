#!/usr/bin/env python3
"""Validate public metadata without fetching private repositories."""
import configparser
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"napcatbot": "HIVESOC-NapCatBot", "web": "HIVESOC-Web", "algorithm": "HIVESOC-Algorithm"}


def main():
    manifest = json.loads((ROOT / "versions.lock.json").read_text())
    assert manifest["format"] == 1
    assert set(manifest["components"]) == set(EXPECTED)
    modules = configparser.ConfigParser()
    modules.read(ROOT / ".gitmodules")
    assert len(modules.sections()) == 3
    index = subprocess.check_output(["git", "ls-files", "--stage", "-z"], cwd=ROOT).decode().split("\0")
    links = {}
    for row in filter(None, index):
        metadata, path = row.split("\t", 1)
        mode, sha, stage = metadata.split()
        assert stage == "0", "unmerged index"
        if mode == "160000":
            links[path] = sha
        else:
            assert path in {"README.md", ".gitignore", ".gitmodules", "versions.lock.json"} or path.startswith(("docs/", "tools/", ".github/")), f"unexpected public file: {path}"
            assert mode == "100644", f"unexpected file mode: {path}"
    assert set(links) == set(EXPECTED)
    for path, repo in EXPECTED.items():
        item = manifest["components"][path]
        assert item["repository"] == f"ColdSpellhere/{repo}"
        assert re.fullmatch(r"[0-9a-f]{40}", item["commit"])
        assert links[path] == item["commit"], f"lock mismatch: {path}"
        module = modules[f'submodule "{path}"']
        assert module["path"] == path
        assert module["url"] == f"git@github.com:ColdSpellhere/{repo}.git"
    print("Public layout and three exact component pins verified; private source was not fetched.")


if __name__ == "__main__":
    main()
