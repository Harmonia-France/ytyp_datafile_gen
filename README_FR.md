# 🚀 YTYP DataFile Generator

Un utilitaire léger permettant de générer automatiquement les déclarations FiveM  
`data_file 'DLC_ITYP_REQUEST'` à partir d’un dossier contenant des fichiers `.ytyp`.

Conçu pour une utilisation **glisser-déposer** et une **intégration FiveM propre**.

---

## ✨ Fonctionnalités

- Scan récursif de tous les fichiers `.ytyp`
- Préfixe automatique `stream/`
- Sortie Lua propre, prête pour `fxmanifest.lua`
- Compatible glisser-déposer (EXE)
- Aucune configuration requise

---

## 📤 Exemple de sortie

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chairs/chair_set.ytyp'
```

---

## 🧲 Utilisation (version EXE)

1. Lance `YTYP_DataFile_Generator.exe`
2. Glisse-dépose ton dossier de ressource FiveM sur l’exécutable
3. Un fichier nommé `ytyp_datafiles.lua` est généré dans le dossier déposé

> Aucun setup. Aucune configuration. Tu déposes, ça génère.

---

## 📁 Structure attendue

```text
my_resource/
├─ stream/
│  ├─ interiors/
│  │  └─ my_interior.ytyp
│  └─ props/
│     └─ my_props.ytyp
```

---

## 📦 Fichier généré

```text
my_resource/
├─ ytyp_datafiles.lua
```

---

## ⚠️ Notes

- Seuls les fichiers `.ytyp` sont pris en compte
- Les sous-dossiers sont entièrement supportés
- Les chemins utilisent toujours des `/`
- L’outil peut être relancé sans risque (fichier remplacé)

---

## 🔗 Rappel d’intégration FiveM

Ne pas oublier d’inclure le fichier généré dans le `fxmanifest.lua` :

```lua
files {
    'ytyp_datafiles.lua'
}
```

---

## 👤 Auteur

**Harmonia Tools**  
Pensé pour un développement FiveM propre, rapide et sans prise de tête
