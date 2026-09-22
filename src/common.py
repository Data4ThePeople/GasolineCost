"""Shared paths and helpers. Every script imports from here so no path is written twice."""
import json, os, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
PROCESSED = ROOT / 'data' / 'processed'
SRC = ROOT / 'src'
DIST = ROOT / 'dist'

# BLS rejects anything that does not start like a browser, and asks callers to
# identify themselves. Do both.
UA = {'User-Agent': 'Mozilla/5.0 Data4ThePeople-GasolineCost/1.0 (eric@asaltollc.com)'}


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
