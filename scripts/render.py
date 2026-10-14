#!/usr/bin/env python3
"""Rellena marcadores en los .md con datos de module.json (CE oficiales, pesos, horas, fechas).

Uso: python render.py <carpeta_modulo>
El redactor escribe marcadores; los datos oficiales y las cifras NUNCA se teclean a mano:
  {{CE:1.a}}        texto literal del CE (en línea)
  {{CE_SDA:3}}      lista de todos los CE evaluados en la SdA 3, con texto literal
  {{PESOS_EV:3}}    tabla de evidencias de la SdA 3 con pesos (suman 100 %)
  {{PESOS_CE:2}}    tabla de pesos de CE dentro del RA 2 (para Tabla maestra / programación)
  {{PESOS_CE_SDA:3}} pesos (en su RA y en el módulo) de los CE evaluados en la SdA 3
  {{CE_RA:2}}       todos los CE del RA 2 con texto literal
  {{PESOS_RA:0}}, {{SDAS_TABLA:0}}, {{DUAL_TABLA:0}}  tablas globales (RA, SdA, CE dualizados)
  {{SDA:3:horas}}   dato de la SdA 3: horas | inicio | fin | titulo | ra_principal
  {{MOD:nombre}}    dato de modulo: nombre | codigo | curso | centro | anio | horas_nominales
Idempotente: tras renderizar, el bloque queda entre <!--...--> y se puede volver a renderizar.
"""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import load, all_ce, d, fmt

def pc(x):
    return f"{x:g}".replace(".", ",") + " %"

def block_ce_sda(m, n):
    s = next(x for x in m["sdas"] if x["n"] == n)
    ces = all_ce(m)
    ids = []
    for e in s["evidencias"]:
        for c in e["ces"]:
            if c not in ids:
                ids.append(c)
    ids.sort(key=lambda c: (int(c.split(".")[0]), c.split(".")[1]))
    return "\n".join(f"- **CE{c})** <!--CE:{c}-->{ces[c][1]['texto']}<!--/CE-->" for c in ids)

def block_pesos_ev(m, n):
    s = next(x for x in m["sdas"] if x["n"] == n)
    L = ["| Evidencia | Nombre | CE | Peso |", "|---|---|---|---|"]
    for e in s["evidencias"]:
        L.append(f"| {e['id']} | {e['nombre']} | {', '.join('CE' + c for c in e['ces'])} | {pc(e['peso'])} |")
    L.append(f"| | | **TOTAL** | **{pc(sum(e['peso'] for e in s['evidencias']))}** |")
    return "\n".join(L)

def block_pesos_ce(m, n):
    ra = next(r for r in m["ras"] if r["n"] == n)
    L = [f"| CE | Peso en RA{n} | Peso en el módulo |", "|---|---|---|"]
    for c in ra["ces"]:
        L.append(f"| CE{n}.{c['id']} | {pc(c['peso'])} | {pc(round(c['peso'] * ra['peso_ra'] / 100, 4))} |")
    L.append(f"| **TOTAL** | **{pc(sum(c['peso'] for c in ra['ces']))}** | **{pc(ra['peso_ra'])}** |")
    return "\n".join(L)

def block_pesos_ce_sda(m, n):
    s = next(x for x in m["sdas"] if x["n"] == n)
    ces = all_ce(m)
    ids = sorted({c for e in s["evidencias"] for c in e["ces"]}, key=lambda c: (int(c.split(".")[0]), c.split(".")[1]))
    L = ["| CE | Peso en su RA | Peso en el módulo |", "|---|---|---|"]
    sa = sm = 0
    for c in ids:
        ra, ce = ces[c]
        pm = round(ce["peso"] * ra["peso_ra"] / 100, 4)
        sa += ce["peso"]; sm += pm
        L.append(f"| CE{c} | {pc(ce['peso'])} | {pc(pm)} |")
    L.append(f"| **Suma de los CE de esta SdA** | {pc(round(sa, 4))} (de sus RA) | **{pc(round(sm, 4))}** |")
    return "\n".join(L)

def block_ce_ra(m, n):
    ra = next(r for r in m["ras"] if r["n"] == n)
    return "\n".join(f"- **CE{n}.{c['id']})** <!--CE:{n}.{c['id']}-->{c['texto']}<!--/CE-->" for c in ra["ces"])

def block_pesos_ra(m, n):
    L = ["| RA | Título | SdA principal | Evaluaciones | Peso en el módulo |", "|---|---|---|---|---|"]
    for ra in m["ras"]:
        sd = ", ".join(f"SdA{s['n']}" for s in m["sdas"] if s["ra_principal"] == ra["n"]) or "—"
        ev = ", ".join(f"{e}ª" for e in ra.get("evaluaciones", []))
        L.append(f"| RA{ra['n']} | {ra['titulo']} | {sd} | {ev} | {pc(ra['peso_ra'])} |")
    L.append(f"| | | | **TOTAL** | **{pc(sum(r['peso_ra'] for r in m['ras']))}** |")
    return "\n".join(L)

def block_sdas_tabla(m, n):
    L = ["| SdA | Título | RA principal | Horas | Inicio | Fin | Evaluación |", "|---|---|---|---|---|---|---|"]
    ui = m.get("unidad_inicial")
    if ui:
        L.append(f"| UI | {ui['titulo']} | sin RA (evaluación inicial, sin peso) | {ui['horas']} | {fmt(d(ui['inicio']))} | {fmt(d(ui['fin']))} | Inicial |")
    for s in m["sdas"]:
        L.append(f"| SdA{s['n']} | {s['titulo']} | RA{s['ra_principal']} | {s['horas']} | {fmt(d(s['inicio']))} | {fmt(d(s['fin']))} | {', '.join(str(e) + 'ª' for e in s.get('evaluaciones', []))} |")
    L.append(f"| | **TOTAL AULA** | | **{sum(s['horas'] for s in m['sdas']) + (ui['horas'] if ui else 0)}** | | | |")
    return "\n".join(L)

def block_dual_tabla(m, n):
    ces = all_ce(m)
    L = ["| CE | Texto oficial | Horas en FEOE | Evidencia de empresa | Alternativa en el centro | Peso en su RA | Peso en el módulo |", "|---|---|---|---|---|---|---|"]
    th = tp = 0
    for x in m.get("dual", {}).get("ces", []):
        ra, ce = ces[x["ce"]]
        pm = round(ce["peso"] * ra["peso_ra"] / 100, 4)
        th += x["horas"]; tp += pm
        L.append(f"| CE{x['ce']} | {ce['texto']} | {x['horas']} | {x['evidencia_empresa']} | {x['alternativa_centro']} | {pc(ce['peso'])} | {pc(pm)} |")
    L.append(f"| **TOTAL** | | **{th}** | | | | **{pc(round(tp, 4))}** |")
    return "\n".join(L)

def value(m, kind, arg):
    if kind == "SDA":
        n, k = arg.split(":")
        s = next(x for x in m["sdas"] if x["n"] == int(n))
        v = s[k]
        return fmt(d(v)) if k in ("inicio", "fin") else str(v)
    return str(m["modulo"][arg])

PAT = re.compile(r"\{\{(CE_SDA|PESOS_EV|PESOS_CE_SDA|PESOS_CE|CE_RA|PESOS_RA|SDAS_TABLA|DUAL_TABLA|CE|SDA|MOD):([^}]+)\}\}"
                 r"|<!--BLOCK:(CE_SDA|PESOS_EV|PESOS_CE_SDA|PESOS_CE|CE_RA|PESOS_RA|SDAS_TABLA|DUAL_TABLA):(\d+)-->.*?<!--/BLOCK-->"
                 r"|<!--CE:(\d+\.[a-z])-->.*?<!--/CE-->", re.S)

def sub(m_json):
    def f(x):
        if x.group(1):
            kind, arg = x.group(1), x.group(2).strip()
        elif x.group(3):
            kind, arg = x.group(3), x.group(4)
        else:
            kind, arg = "CE", x.group(5)
        if kind == "CE":
            return f"<!--CE:{arg}-->{all_ce(m_json)[arg][1]['texto']}<!--/CE-->"
        if kind in ("CE_SDA", "PESOS_EV", "PESOS_CE", "PESOS_CE_SDA", "CE_RA", "PESOS_RA", "SDAS_TABLA", "DUAL_TABLA"):
            fn = {"CE_SDA": block_ce_sda, "PESOS_EV": block_pesos_ev, "PESOS_CE": block_pesos_ce, "PESOS_CE_SDA": block_pesos_ce_sda, "CE_RA": block_ce_ra, "PESOS_RA": block_pesos_ra, "SDAS_TABLA": block_sdas_tabla, "DUAL_TABLA": block_dual_tabla}[kind]
            return f"<!--BLOCK:{kind}:{arg}-->\n{fn(m_json, int(arg))}\n<!--/BLOCK-->"
        return value(m_json, kind, arg)
    return f

def main():
    root = sys.argv[1]
    m = load(os.path.join(root, "module.json"))
    n = 0
    for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        if os.path.basename(p).startswith("Informe_Validacion"):
            continue
        t = open(p, encoding="utf-8").read()
        t2 = PAT.sub(sub(m), t)
        if t2 != t:
            open(p, "w", encoding="utf-8").write(t2)
            n += 1
            print("renderizado:", os.path.relpath(p, root))
    print(f"{n} archivo(s) actualizados")

if __name__ == "__main__":
    main()
