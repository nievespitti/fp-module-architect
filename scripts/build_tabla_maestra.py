#!/usr/bin/env python3
"""Genera la Tabla maestra (xlsx + docx + md) desde module.json. Los pesos se calculan, no se escriben a mano.

Uso: python build_tabla_maestra.py <carpeta_modulo>
Cada CE de module.json lleva: id, texto (oficial), peso (dentro del RA, suma 100), y opcionalmente
  "evalua" (resumen operativo), "evidencia" (qué entrega el alumno), "instrumento".
Peso en módulo = peso_ce × peso_ra / 100 (fórmula viva en el Excel).
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import load, all_ce
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

HF, HFont = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid"), Font(bold=True, color="FFFFFF")
S = Side(style="thin", color="BFBFBF")
BD = Border(left=S, right=S, top=S, bottom=S)

def sdas_of(m, ra_n):
    prim = [s for s in m["sdas"] if s["ra_principal"] == ra_n]
    comp = [s for s in m["sdas"] if ra_n in s.get("ras_complementarios", [])]
    return prim, comp

def pc(x):
    return f"{x:g}".replace(".", ",") + " %"

def main():
    root = sys.argv[1]
    m = load(os.path.join(root, "module.json"))
    mod = m["modulo"]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Distribución RA"
    ws.append([f"Tabla maestra de evaluación · {mod['nombre']} {mod['codigo']} · {mod['curso']} · {mod['anio']}"])
    ws["A1"].font = Font(bold=True, size=13, color="1F4E79")
    ws.append([])
    hdr = ["RA", "Título (oficial)", "SdA principal", "Evaluaciones", "Transversal", "Peso módulo (%)"]
    ws.append(hdr)
    for c in ws[3]:
        c.fill, c.font, c.border = HF, HFont, BD
    md = [f"# Tabla maestra de evaluación — {mod['nombre']} {mod['codigo']} · {mod['curso']} · {mod['anio']}", "",
          "Los pesos de CE en el módulo se calculan: peso CE en RA × peso RA / 100. Generado por `build_tabla_maestra.py` desde `module.json`.", "",
          "## Distribución global de los RA", "", "| RA | SdA principal | Evaluaciones | Peso módulo |", "|---|---|---|---|"]
    r0 = 4
    for i, ra in enumerate(m["ras"]):
        prim, _ = sdas_of(m, ra["n"])
        sd = ", ".join(f"SdA{s['n']} · {s['titulo']}" for s in prim) or "—"
        ev = ", ".join(f"{e}ª" for e in ra.get("evaluaciones", []))
        ws.append([f"RA{ra['n']}", ra["titulo"], sd, ev, "Sí" if ra.get("transversal") else "No", ra["peso_ra"]])
        md.append(f"| RA{ra['n']} | {sd} | {ev} | {pc(ra['peso_ra'])} |")
    rl = r0 + len(m["ras"]) - 1
    ws.append(["", "", "", "", "TOTAL", f"=SUM(F{r0}:F{rl})"])
    md.append(f"| | | TOTAL | {pc(sum(r['peso_ra'] for r in m['ras']))} |")
    for row in ws.iter_rows(min_row=4, max_row=rl + 1):
        for c in row:
            c.border = BD
            c.alignment = Alignment(wrap_text=True, vertical="center")
    for col, w in zip("ABCDEF", [8, 60, 46, 14, 12, 16]):
        ws.column_dimensions[col].width = w
    ra_row = {ra["n"]: r0 + i for i, ra in enumerate(m["ras"])}
    for ra in m["ras"]:
        w2 = wb.create_sheet(f"RA{ra['n']}")
        prim, comp = sdas_of(m, ra["n"])
        w2.append([f"RA{ra['n']} · {ra['titulo']}"])
        w2["A1"].font = Font(bold=True, size=12, color="1F4E79")
        w2.append(["Peso global en el módulo (%)", f"='Distribución RA'!F{ra_row[ra['n']]}"])
        w2.append([])
        w2.append(["CE", "Texto oficial", "Qué se evalúa", "Evidencia principal", "Instrumento", "Peso en RA (%)", "Peso módulo (%)"])
        for c in w2[4]:
            c.fill, c.font, c.border = HF, HFont, BD
        md += ["", f"## RA{ra['n']} · {ra['titulo']}", f"Peso global en el módulo: {pc(ra['peso_ra'])}"
               + (" · RA transversal" if ra.get("transversal") else ""), "",
               "| CE | Texto oficial | Qué se evalúa | Evidencia | Instrumento | Peso en RA | Peso módulo |", "|---|---|---|---|---|---|---|"]
        a = 5
        for ce in ra["ces"]:
            r = w2.max_row + 1
            w2.append([f"{ra['n']}.{ce['id']}", ce["texto"], ce.get("evalua", ""), ce.get("evidencia", ""), ce.get("instrumento", ""), ce["peso"], f"=F{r}*$B$2/100"])
            md.append(f"| {ra['n']}.{ce['id']} | {ce['texto']} | {ce.get('evalua','')} | {ce.get('evidencia','')} | {ce.get('instrumento','')} | {pc(ce['peso'])} | {pc(round(ce['peso']*ra['peso_ra']/100, 4))} |")
        b = w2.max_row
        w2.append(["", "", "", "", "TOTAL", f"=SUM(F{a}:F{b})", f"=SUM(G{a}:G{b})"])
        md.append(f"| | | | | TOTAL | {pc(sum(c['peso'] for c in ra['ces']))} | {pc(ra['peso_ra'])} |")
        for row in w2.iter_rows(min_row=5, max_row=w2.max_row):
            for c in row:
                c.border = BD
                c.alignment = Alignment(wrap_text=True, vertical="center")
        for col, w in zip("ABCDEFG", [8, 60, 30, 34, 24, 14, 16]):
            w2.column_dimensions[col].width = w
        info = "SdA principal: " + (", ".join(f"SdA{s['n']}" for s in prim) or "—") + (" · SdA complementarias: " + ", ".join(f"SdA{s['n']}" for s in comp) if comp else "")
        w2.append([]); w2.append([info])
        md += ["", info]
    # evidencias por SdA
    w3 = wb.create_sheet("Evidencias por SdA")
    w3.append(["SdA", "Evidencia", "Nombre", "Tipo", "CE evaluados", "Peso en SdA (%)"])
    for c in w3[1]:
        c.fill, c.font, c.border = HF, HFont, BD
    md += ["", "## Evidencias por SdA", ""]
    for s in m["sdas"]:
        md += [f"### SdA{s['n']} · {s['titulo']} (RA{s['ra_principal']}, {s['horas']} h)", "", "| Evidencia | Nombre | CE | Peso |", "|---|---|---|---|"]
        a = w3.max_row + 1
        for e in s["evidencias"]:
            w3.append([f"SdA{s['n']}", e["id"], e["nombre"], e.get("tipo", ""), ", ".join(e["ces"]), e["peso"]])
            md.append(f"| {e['id']} | {e['nombre']} | {', '.join(e['ces'])} | {pc(e['peso'])} |")
        w3.append(["", "", "", "", "TOTAL", f"=SUM(F{a}:F{w3.max_row})"])
        md.append(f"| | | TOTAL | {pc(sum(e['peso'] for e in s['evidencias']))} |")
        md.append("")
    for col, w in zip("ABCDEF", [8, 10, 46, 20, 30, 16]):
        w3.column_dimensions[col].width = w
    base = f"Tabla_Maestra_{mod['nombre'].replace(' ', '_')}"
    wb.save(os.path.join(root, base + ".xlsx"))
    open(os.path.join(root, base + ".md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    print("Generados:", base + ".xlsx,", base + ".md")

if __name__ == "__main__":
    main()
