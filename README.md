# YTYP DataFile Generator

A small utility to generate FiveM
`data_file 'DLC_ITYP_REQUEST'` entries from `.ytyp` files.

This repository contains:
- the source code
- a drag & drop Windows executable (release)
- documentation in English and French

---

## 📚 Documentation

Choose your language:

- 🇬🇧 English documentation → [README_EN.md](./README_EN.md)
- 🇫🇷 Documentation française → [README_FR.md](./README_FR.md)

---

## ⚙️ Behaviour summary (exact)

- The script applies a per-file rule:
  - If a `.ytyp` is directly under the provided root, emit `data_file 'DLC_ITYP_REQUEST' 'stream/<resource>/<filename>.ytyp'`.
  - Otherwise emit the per-file relative path prefixed by `stream/`.
- No wildcard aggregation is performed.
- Lines are deduplicated and files are sorted.

---

## 🛠️ Quick usage

Run the script or use the EXE and drop your resource folder onto it. The generated `ytyp_datafiles.lua` should be included in your `fxmanifest.lua`.

---

## ⚖️ License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

**Harmonia Tools** — Clean tooling for FiveM development
