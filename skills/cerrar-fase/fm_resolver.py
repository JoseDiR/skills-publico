"""Resuelve los bloques de conflicto que solo contienen campos de frontmatter.
fuentes/relacionados/tags: unión (orden: main y luego lo nuevo de HEAD); resumen y demás: main;
fecha_actualizacion: la mayor. Deja intactos los bloques con cuerpo. Uso: python fm_resolver.py archivos..."""
import re, sys, json
BLOQ = re.compile(r"^<<<<<<< [^\n]*\n(.*?)^(?:\|\|\|\|\|\|\| [^\n]*\n.*?)?^=======\n(.*?)^>>>>>>> [^\n]*\n", re.S | re.M)
CAMPO = re.compile(r"^([a-z_]+): ?(.*)$")
LISTAS = {"fuentes", "relacionados", "tags"}
def campos(txt):
    d = {}
    for l in txt.splitlines():
        m = CAMPO.match(l)
        if not m: return None
        d[m[1]] = m[2]
    return d
def lista(v):
    try: return json.loads(v)
    except Exception:
        return [x.strip() for x in v.strip("[]").split(",") if x.strip()]
def resolver(m):
    a, b = campos(m[1]), campos(m[2])  # a=HEAD (local), b=main
    if a is None or b is None: return m[0]
    out = []
    for k in list(b) + [k for k in a if k not in b]:
        if k in LISTAS and k in a and k in b:
            la, lb = lista(a[k]), lista(b[k])
            v = lb + [x for x in la if x not in lb]
            out.append(f"{k}: " + (json.dumps(v, ensure_ascii=False) if k != "tags" else "[" + ", ".join(v) + "]"))
        elif k == "fecha_actualizacion" and k in a:
            out.append(f"{k}: {max(a[k], b.get(k, ''))}")
        else:
            out.append(f"{k}: {b.get(k, a.get(k))}")
    return "\n".join(out) + "\n"
pend = 0
for f in sys.argv[1:]:
    raw = open(f, encoding="utf-8", newline="").read()
    crlf = "\r\n" in raw
    t = raw.replace("\r\n", "\n")
    n = BLOQ.sub(resolver, t)
    if n != t:
        open(f, "w", encoding="utf-8", newline="").write(n.replace("\n", "\r\n") if crlf else n)
    r = len(re.findall(r"^<<<<<<< ", n, re.M)); pend += bool(r)
    print(("QUEDAN %d" % r) if r else "OK", f)
print("archivos con cuerpo en conflicto:", pend)
