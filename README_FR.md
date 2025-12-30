# 🚀 YTYP DataFile Generator

Un utilitaire léger permettant de générer automatiquement les déclarations FiveM
`data_file 'DLC_ITYP_REQUEST'` à partir d’un dossier contenant des fichiers `.ytyp`.

Conçu pour une utilisation **glisser-déposer** et une **intégration FiveM propre**.

---

## ✨ Fonctionnalités

- Scan récursif de tous les fichiers `.ytyp`
- Préfixe automatique `stream/`
- Sortie Lua propre, prête pour `fxmanifest.lua`
- Drag & drop compatible (EXE)
- Zéro configuration

---

## ⚙️ Comportement exact (par fichier)

Pour chaque fichier `.ytyp` trouvé, le script applique la règle suivante :

- Si le fichier est directement dans le dossier racine fourni (c.-à-d. `f.parent == root`), on écrit :

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/<resource_name>/<filename>.ytyp'
```

Exemple : `my_resource/a.ytyp` → `stream/my_resource/a.ytyp`.

- Sinon (le fichier est dans un sous-dossier), on écrit le chemin relatif complet préfixé par `stream/` :

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
```

Remarques :

- Il n’y a pas d’agrégation wildcard globale (pas de `stream/<resource>/*`).
- Les lignes identiques sont dédupliquées pour éviter les doublons.
- Les fichiers sont triés (ordre alphabétique insensible à la casse).

---

## 🧾 Exemples

Cas sans sous-dossiers (tous les `.ytyp` à la racine) :

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/a.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/b.ytyp'
```

Cas avec sous-dossiers :

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chairs/chair_set.ytyp'
```

Cas mixte (2 à la racine + 3 en sous-dossiers) :

```lua
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/a.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/my_resource/b.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/interiors/school.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/chair_set.ytyp'
data_file 'DLC_ITYP_REQUEST' 'stream/props/table_set.ytyp'
```

---

## 🛠️ Utilisation rapide (EXE)

1. Lance `YTYP_DataFile_Generator.exe`
2. Glisse-dépose ton dossier de ressource FiveM sur l’exécutable
3. Un fichier `ytyp_datafiles.lua` est généré dans le dossier déposé

> Le fichier est remplacé à chaque exécution.

---

## 🔎 Test rapide (PowerShell)

Pour reproduire localement :

```powershell
# créer structure de test
Remove-Item -Recurse -Force .\test_mix -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path .\test_mix | Out-Null
New-Item -Path .\test_mix\a.ytyp -ItemType File | Out-Null
New-Item -Path .\test_mix\b.ytyp -ItemType File | Out-Null
New-Item -ItemType Directory -Path .\test_mix\stream\interiors -Force | Out-Null
New-Item -Path .\test_mix\stream\interiors\c.ytyp -ItemType File | Out-Null
# lancer
python .\main.py .\test_mix
Get-Content .\test_mix\ytyp_datafiles.lua -Raw
```

---

## 🔗 Intégration FiveM

Inclure le fichier généré dans le `fxmanifest.lua` :

```lua
files {
    'ytyp_datafiles.lua'
}
```

---

**Harmonia Tools** — outils pour le développement FiveM
