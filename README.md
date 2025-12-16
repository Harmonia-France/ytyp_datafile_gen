# YTYP DataFile Generator

A small utility to generate FiveM  
`data_file 'DLC_ITYP_REQUEST'` entries from `.ytyp` files.

This repository contains:
- the source code
- a drag & drop Windows executable (release)
- detailed documentation in English and French

---

## 📘 Documentation

Choose your language:

- 🇬🇧 **English documentation**  
  → [README_EN.md](./README_EN.md)

- 🇫🇷 **Documentation française**  
  → [README_FR.md](./README_FR.md)

---

## 🔧 What this tool does (short version)

- Recursively scans a folder for `.ytyp` files
- Generates a `ytyp_datafiles.lua` file
- Automatically prefixes paths with `stream/`
- Ready to be included in `fxmanifest.lua`

---

## 📦 Project structure (simplified)

```text
.
├─ main.py
├─ README.md
├─ README_EN.md
├─ README_FR.md
└─ LICENSE
```

---

## 🧾 License

This project is licensed under the **MIT License**.  
See [LICENSE](./LICENSE) for details.

---

**Harmonia Tools**  
Clean tooling for FiveM development
