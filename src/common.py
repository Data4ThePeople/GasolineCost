"""Shared paths and helpers. Every script imports from here so no path is written twice."""
# Contact address for the User-Agent: read at run time, never hardcoded in the repo.
# Set D4TP_CONTACT_EMAIL in the environment or in ~/.claude/d4tp-process/.env.
import os as _os


def _d4tp_contact():
    v = _os.environ.get("D4TP_CONTACT_EMAIL")
    if v:
        return v
    try:
        with open(_os.path.expanduser("~/.claude/d4tp-process/.env"), encoding="utf-8") as fh:
            for line in fh:
                if line.strip().startswith("D4TP_CONTACT_EMAIL="):
                    return line.split("=", 1)[1].strip().strip("'\"")
    except OSError:
        pass
    return ""


D4TP_CONTACT = _d4tp_contact()


import json, os, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
PROCESSED = ROOT / 'data' / 'processed'
SRC = ROOT / 'src'
DIST = ROOT / 'dist'

# BLS rejects anything that does not start like a browser, and asks callers to
# identify themselves. Do both.
UA = {'User-Agent': f'Mozilla/5.0 Data4ThePeople-GasolineCost/1.0 ({D4TP_CONTACT})'}


def keys():
    """Load the central D4TP keys. Never print a key."""
    sys.path.insert(0, os.path.expanduser('~/.claude/d4tp-process'))
    from d4tp_env import load_env, get_key
    load_env()
    return get_key


def get(url, tries=4, timeout=60, data=None, headers=None):
    h = dict(UA, **(headers or {}))
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=timeout).read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def write_json(path, obj, indent=None):
    Path(path).write_text(json.dumps(obj, indent=indent, separators=None if indent else (',', ':')))
