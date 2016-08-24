Skin Converter [0.1.0]
======================

**Requirements:** Python, Python Imaging Library (PIL)

Simple batch conversion tools for migration between compatible skin formats.

format17.py
-----------

Convert format 1.8 to format 1.7

**Usage:** format17.py \<file|dir>

**Example:** Convert a single file in the current working directory.

```
python format17.py character.png
```
format18.py
-----------

Convert format 1.7 to format 1.8

**Usage:** format18.py \<file|dir>

**Example:** Convert all compatible files within a directory, non-recursively.

```
python format18.py skins/textures
```

Notes
-----

Output images are RGBA mode PNG and will overwrite the original image without warning.
Be sure you have a backup just in case things go wrong. 
