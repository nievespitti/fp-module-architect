"""Utilidades compartidas: carga de module.json, calendario y sesiones reales."""
import json, datetime as dt, sys

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def d(s):
    return dt.date.fromisoformat(s)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def fmt(date):
    return date.strftime("%d/%m/%Y")

def blocked_days(cal):
    """Conjunto de fechas sin clase del módulo: no lectivos, periodos (vacaciones, proyecto, FEOE...)."""
    out = {}
    for x in cal.get("no_lectivos", []):
        out[d(x["fecha"])] = x.get("motivo", "No lectivo")
    for p in cal.get("periodos_sin_clase", []):
        a, b = d(p["inicio"]), d(p["fin"])
        while a <= b:
            out[a] = p.get("motivo", "Sin clase")
            a += dt.timedelta(days=1)
    feo = cal.get("feoe")
    if feo:
        a, b = d(feo["inicio"]), d(feo["fin"])
        while a <= b:
            out[a] = "FEOE"
            a += dt.timedelta(days=1)
    return out

def sessions(mod, start=None, end=None):
    """Lista de sesiones reales [{fecha, dia, inicio, fin, horas}] entre start y end (ISO) según horario y calendario."""
    cal = mod["calendario"]
    a = d(start or cal["inicio_clases"])
    b = d(end or cal["fin_clases_modulo"])
    blk = blocked_days(cal)
    by_day = {}
    for h in mod["horario"]:
        by_day.setdefault(DIAS.index(h["dia"]), []).append(h)
    res = []
    cur = a
    while cur <= b:
        if cur.weekday() in by_day and cur not in blk and cur.weekday() < 5:
            for h in sorted(by_day[cur.weekday()], key=lambda x: x["inicio"]):
                res.append({"fecha": cur, "dia": DIAS[cur.weekday()], "inicio": h["inicio"],
                            "fin": h["fin"], "horas": h.get("horas", 1)})
        cur += dt.timedelta(days=1)
    return res

def all_ce(mod):
    return {f"{ra['n']}.{ce['id']}": (ra, ce) for ra in mod["ras"] for ce in ra["ces"]}

def say(msg=""):
    sys.stdout.reconfigure(encoding="utf-8")
    print(msg)
