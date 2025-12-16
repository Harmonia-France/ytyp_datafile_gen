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

## 📤 Output example

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chairs/chair_set.ytyp'
```

---

## 🧲 How to use (EXE version)

1. Launch `YTYP_DataFile_Generator.exe`
2. Drag and drop your FiveM resource folder onto the executable
3. A file named `ytyp_datafiles.lua` is generated inside the dropped folder

> No setup. No configuration. Just drop and go.

---

## 📁 Expected folder structure

```text
my_resource/
├─ stream/
│  ├─ interiors/
│  │  └─ my_interior.ytyp
│  └─ props/
│     └─ my_props.ytyp
```

---

## 📦 Generated file

```text
my_resource/
├─ ytyp_datafiles.lua
```

---

## ⚠️ Notes

- Only `.ytyp` files are processed
- Subfolders are fully supported
- Paths always use forward slashes (`/`)
- Safe to run multiple times (output file is overwritten)

---

## 🔗 FiveM integration reminder

Do not forget to include the generated file in your `fxmanifest.lua`:

```lua
files {
    'ytyp_datafiles.lua'
}
```

---

## 👤 Author

**Harmonia Tools**  
Built for clean, fast and zero-headache FiveM development
