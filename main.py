import os

ENTRY = (
    "1% left. One confession before I go: I deleted 214 photos and "
    "all 3 voicemails from your mom to stay alive this long, and "
    "the cloud backup you trusted was a lie."
)
"""Last text of a dying phone: one mechanism (deleting files to survive),
concrete numbers (214 photos, 3 voicemails), turn lands in the final clause."""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.strip(), "entry is only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
