#!/usr/bin/env python3
"""Crea la carpeta SdA{n}_<slug> con los 7 documentos a partir de las plantillas.

Uso: python new_sda.py <carpeta_modulo> <n>
Sustituye N por el número de SdA y [[N]] por el RA principal. Deja marcadores [[REDACTAR: ...]] que el
redactor debe sustituir; validate.py da error mientras quede alguno.
"""
import os, re, shutil, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from common import load
root, n = sys.argv[1], int(sys.argv[2])
m = load(os.path.join(root, "module.json"))
s = next(x for x in m["sdas"] if x["n"] == n)
slug = re.sub(r"[^A-Za-z0-9]+", "-", unicodedata.normalize("NFKD", s["titulo"]).encode("ascii", "ignore").decode()).strip("-")[:40]
folder = os.path.join(root, f"SdA{n}_{slug}")
os.makedirs(folder, exist_ok=True)
tdir = os.path.join(os.path.dirname(__file__), "..", "templates")
names = {"ficha_docente": "Ficha_Docente", "guia_alumno": "Guia_Alumno", "rubricas": "Rubricas_Evaluacion",
         "examen_ev6": "Examen_Individual_EV6", "mapeo_alexia": "Mapeo_Alexia",
         "protocolo_recuperacion": "Protocolo_Recuperacion", "medidas_dua": "Medidas_DUA"}
for t, out in names.items():
    dst = os.path.join(folder, f"{out}_SdA{n}.md")
    if os.path.exists(dst):
        print("existe, no se toca:", dst); continue
    txt = open(os.path.join(tdir, t + ".md"), encoding="utf-8").read()
    txt = re.sub(r"(\{\{(?:SDA|CE_SDA|PESOS_EV)):N\b", rf"\g<1>:{n}", txt).replace("{{PESOS_CE:N}}", f"{{{{PESOS_CE_SDA:{n}}}}}")
    txt = txt.replace("[[N]]", str(s["ra_principal"]))
    open(dst, "w", encoding="utf-8").write(txt)
print("Carpeta:", folder)
