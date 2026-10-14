#!/usr/bin/env python3
"""Crea module.json a partir de ra_oficiales.json (+ calendario/horario ya recogidos).

Uso: python init_module.py <carpeta_modulo> --nombre "Seguridad Informática" --codigo 0226 --curso "2.º SMR" \
        --centro "Centro de ejemplo" --anio 2026-2027 --horas 142 --docente "Docente de ejemplo"
Genera RA con peso igual y CE con peso igual (el docente los ajusta), SdA vacías y calendario/horario vacíos
que HAY QUE rellenar con los datos que aporta el docente (no se inventan).
"""
import argparse, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ap = argparse.ArgumentParser()
ap.add_argument("root"); ap.add_argument("--nombre", required=True); ap.add_argument("--codigo", required=True)
ap.add_argument("--curso", required=True); ap.add_argument("--centro", required=True); ap.add_argument("--anio", required=True)
ap.add_argument("--horas", type=int, required=True); ap.add_argument("--docente", required=True)
a = ap.parse_args()
off = json.load(open(os.path.join(a.root, "ra_oficiales.json"), encoding="utf-8"))
nr = len(off["ras"])
def split(n):
    w = [round(100 / n, 2)] * n
    w[-1] = round(100 - sum(w[:-1]), 2)
    return w
ras = []
for r, wr in zip(off["ras"], split(nr)):
    ras.append({"n": r["n"], "titulo": r["titulo"], "peso_ra": wr, "transversal": False, "evaluaciones": [],
                "ces": [{"id": c["id"], "texto": c["texto"], "peso": w, "evalua": "", "evidencia": "", "instrumento": ""}
                        for c, w in zip(r["ces"], split(len(r["ces"])))]})
m = {"modulo": {"nombre": a.nombre, "codigo": a.codigo, "curso": a.curso, "centro": a.centro, "anio": a.anio,
                "horas_nominales": a.horas},
     "docente": a.docente,
     "horario": [],      # [{"dia":"Lunes","inicio":"12:10","fin":"13:02","horas":1}]
     "calendario": {"inicio_clases": "", "fin_clases_modulo": "", "evaluaciones": [], "no_lectivos": [],
                    "periodos_sin_clase": [], "hitos": []},  # + "feoe": {"inicio","fin","tutorias"}
     "ras": ras, "sdas": []}
p = os.path.join(a.root, "module.json")
if os.path.exists(p):
    sys.exit(f"{p} ya existe; no se sobrescribe.")
json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"module.json creado: {nr} RA, {sum(len(r['ces']) for r in ras)} CE. Rellenar horario, calendario y sdas.")
