#!/usr/bin/env python3
"""Extrae RA y criterios de evaluación LITERALES de un PDF oficial (BOC/BOE/currículo autonómico).

Uso: python extract_official_ce.py <pdf> [--out ra_oficiales.json]

Reconoce dos formatos:
  A) "RA1. Título ..." seguido de "a) criterio"   (fichas de currículo autonómico)
  B) "1. Título ..." + "Criterios de evaluación:" + "a) criterio"   (BOE / BOC)
Se detiene en "Contenidos" / "Orientaciones" / "Duración".
Salida: JSON {"modulo": ..., "codigo": ..., "ras": [{"n":1,"titulo":...,"ces":[{"id":"a","texto":...}]}]}
"""
import json, re, shutil, subprocess, sys

def pdf_text(path):
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", path, "-"], capture_output=True, encoding="utf-8", errors="replace")
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    import fitz
    return "\n".join(p.get_text() for p in fitz.open(path))

STOP = re.compile(r"^\s*(\d+\.\s*)?(contenidos|orientaciones|duraci[oó]n)\b", re.I)
RA_A = re.compile(r"^\s*RA\s?(\d+)\.\s*(.+)")
RA_B = re.compile(r"^\s*(\d+)\.\s+([A-ZÁÉÍÓÚ][^\n]{12,})")
CE = re.compile(r"^\s*([a-z])\)\s+(.+)")

def parse(text):
    ras, cur_ra, cur_ce, in_ce = [], None, None, False
    code = re.search(r"C[oó]digo:\s*(\d{4})", text)
    name = re.search(r"^\s*([A-ZÁÉÍÓÚ][^\n]{3,60})\n\s*C[oó]digo:", text, re.M)
    for raw in text.splitlines():
        line = raw.strip()
        if not line or re.fullmatch(r"\d{1,3}\.?", line) or line.startswith("Resultados de aprendizaje"):
            continue
        if re.match(r"^criterios de evaluaci[oó]n:?$", line, re.I):
            in_ce = True
            continue
        if STOP.match(line) and ras and ras[-1]["ces"]:
            break
        m = RA_A.match(line) or (None if in_ce and cur_ra and False else RA_B.match(line))
        mce = CE.match(line)
        if m and not mce and (RA_A.match(line) or int(m.group(1)) == len(ras) + 1):
            cur_ra = {"n": int(m.group(1)), "titulo": m.group(2).strip(), "ces": []}
            ras.append(cur_ra); cur_ce = None; in_ce = False
            continue
        if cur_ra is None:
            continue
        if mce:
            cur_ce = {"id": mce.group(1), "texto": mce.group(2).strip()}
            cur_ra["ces"].append(cur_ce); in_ce = True
        elif cur_ce is not None:
            cur_ce["texto"] += " " + line
        else:
            cur_ra["titulo"] += " " + line
    return {"modulo": (name.group(1).strip() if name else None),
            "codigo": (code.group(1) if code else None), "ras": ras}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    data = parse(pdf_text(sys.argv[1]))
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    if out:
        json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Módulo: {data['modulo']}  Código: {data['codigo']}")
    total = 0
    for ra in data["ras"]:
        total += len(ra["ces"])
        print(f"\nRA{ra['n']} ({len(ra['ces'])} CE): {ra['titulo']}")
        for ce in ra["ces"]:
            print(f"  {ra['n']}.{ce['id']}) {ce['texto']}")
    print(f"\nTOTAL: {len(data['ras'])} RA, {total} CE")
