#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
bad_ext = {".csv",".tsv",".xlsx",".xls",".xml",".zip",".parquet",".feather",".sqlite",".db",".json"}
patterns = [
    r"trackman", r"api[_-]?key", r"password", r"authorization:\s*bearer",
    r"secret", r"access[_-]?token"
]
hits=[]
for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts: continue
    if p.suffix.lower() in bad_ext:
        hits.append((p, "sensitive data-like extension"))
        continue
    if p.stat().st_size > 2_000_000: continue
    try: txt=p.read_text(errors="ignore")
    except Exception: continue
    for pat in patterns:
        if re.search(pat, txt, re.I):
            hits.append((p, f"matched {pat}"))
            break
print("Potential review items:")
for p,why in hits:
    print(f"- {p.relative_to(ROOT)}: {why}")
print(f"Total: {len(hits)}")
print("Note: this is a review aid, not proof that a repository is safe.")
