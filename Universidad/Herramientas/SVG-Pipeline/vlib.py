# -*- coding: utf-8 -*-
import os

BASE = os.environ.get("VAULT_ROOT") or os.path.join(
    os.path.expanduser("~"), "OneDrive", "OneSyncFiles"
)

def vault():
    return BASE

def materia(sem, letter):
    folders = {
        ("1er", "C"): "Universidad/1er Semestre/C\u00e1lculo de una Variable",
        ("1er", "F"): "Universidad/1er Semestre/F\u00edsica Mec\u00e1nica",
        ("2do", "V"): "Universidad/2do Semestre/C\u00e1lculo Vectorial",
    }
    key = (sem, letter)
    if key not in folders:
        raise KeyError(key)
    return os.path.join(BASE, folders[key])
