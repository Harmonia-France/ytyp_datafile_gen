from __future__ import annotations
import sys
from pathlib import Path

def to_stream_rel(root: Path, file_path:Path) -> str:
    rel = file_path.relative_to(root).as_posix()
    if rel.startswith("stream/"):
        return rel
    return f"stream/{rel}"

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: glisse un dossier sur ce script, ou lance:")
        print("  python ytyp_datafile_gen.py <dossier>")
        return 1

    root = Path(sys.argv[1]).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Erreur: \"{root}\" n'est pas un dossier.")
        return 1

    ytyps = sorted(root.rglob("*.ytyp"), key=lambda p: p.as_posix().lower())

    lines = []
    seen = set()

    for f in ytyps:
        if f.parent == root:
            line = f"data_file 'DLC_ITYP_REQUEST' 'stream/{root.name}/{f.name}'"
        else:
            stream_path = to_stream_rel(root, f)
            line = f"data_file 'DLC_ITYP_REQUEST' '{stream_path}'"
        if line in seen:
            print(f"Avertissement: ligne de data_file dupliquée pour \"{f}\": {line}")
            continue
        lines.append(line)
        seen.add(line)

    out_file = root / "ytyp_datafiles.lua"
    out_file.write_text("\n".join(lines)+("\n" if lines else ""), encoding="utf-8")

    print(f"Trouvé: {len(ytyps)} fichier(s) .ytyp")
    print(f"Sortie: {out_file}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())