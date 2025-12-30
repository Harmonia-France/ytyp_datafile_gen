# 🚀 YTYP DataFile Generator

A lightweight utility to automatically generate FiveM
`data_file 'DLC_ITYP_REQUEST'` entries from a folder containing `.ytyp` files.

Designed for **drag & drop usage** and **clean FiveM resource integration**.

---

## ✨ Features

- Recursive scan of all `.ytyp` files
- Automatic `stream/` path prefix
- Clean Lua output, ready for `fxmanifest.lua`
- Drag & drop compatible (EXE)
- Zero configuration

---

## ⚙️ Exact behavior (per-file)

For each `.ytyp` file found, the script applies the following rule:

- If the file is directly inside the provided root folder (i.e. `f.parent == root`), write:

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/<resource_name>/<filename>.ytyp'
```

Example: `my_resource/a.ytyp` → `stream/my_resource/a.ytyp`.

- Otherwise (file is inside a subfolder), write the full relative path prefixed with `stream/`:

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
```

Notes:
- There is no global wildcard aggregation (no `stream/<resource>/*`).
- Identical lines are deduplicated to avoid duplicates.
- Files are sorted (case-insensitive alphabetical order).

---

## 🧾 Examples

No-subfolders case (all `.ytyp` in the root):

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/a.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/b.ytyp'
```

With subfolders:

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chairs/chair_set.ytyp'
```

Mixed case (2 at root + 3 in subfolders):

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/a.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/b.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chair_set.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/table_set.ytyp'
```

---

## 🛠️ Quick use (EXE)

1. Launch `YTYP_DataFile_Generator.exe`
2. Drag and drop your FiveM resource folder onto the executable
3. A file `ytyp_datafiles.lua` is generated inside the dropped folder

> The file is overwritten on every run.

---

## 🔎 Quick test (PowerShell)

```powershell
# create test structure
Remove-Item -Recurse -Force .\test_mix -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path .\test_mix | Out-Null
New-Item -Path .\test_mix\a.ytyp -ItemType File | Out-Null
New-Item -Path .\test_mix\b.ytyp -ItemType File | Out-Null
New-Item -ItemType Directory -Path .\test_mix\stream\interiors -Force | Out-Null
New-Item -Path .\test_mix\stream\interiors\c.ytyp -ItemType File | Out-Null
# run
python .\main.py .\test_mix
Get-Content .\test_mix\ytyp_datafiles.lua -Raw
```

---

## 🔗 FiveM integration

Include the generated file in your `fxmanifest.lua`:

```lua
files {
    'ytyp_datafiles.lua'
}
```

---

**Harmonia Tools** — tools for FiveM development
