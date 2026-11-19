"""Leitura do LaTeX do capítulo: exemplos, questões, rótulos, níveis, IDs.

Usado por matriz.py e checar.py. Trabalha sobre os arquivos uN_artigo.tex / uN_partes.tex.
"""
import re, glob, os

G = r"\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}"   # grupo {…} com até dois níveis de chaves internas


def ids_de(txt):
    return [x.strip() for x in txt.split(",") if x.strip()]


def arquivos_unidade(texdir):
    """{n: [caminhos]} para uN_artigo.tex e uN_partes.tex"""
    out = {}
    for f in sorted(glob.glob(os.path.join(texdir, "u*_*.tex"))):
        m = re.match(r"u(\d+)_", os.path.basename(f))
        if m:
            out.setdefault(int(m.group(1)), []).append(f)
    return out


def sem_comentarios(t):
    """remove comentários LaTeX (% não escapado até o fim da linha)"""
    return "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in t.split("\n"))


def ler(f, comentarios=False):
    t = open(f, encoding="utf-8").read()
    return t if comentarios else sem_comentarios(t)


def itens(texto, unidade):
    """Lista de dicts {tipo, n, nivel, fonte, ids, rotulo, integradora, corpo, pos}
    para exemplos e questões, na ordem do texto. n é o número de ordem (questões) ou o
    número explícito/automático (exemplos)."""
    res = []
    nq = ne = 0
    pat = re.compile(
        r"\\begin\{(?P<tipo>questao|exemplo)\}(?P<opt>\[[^\]]*\])?"
        r"(?P<a1>" + G + r")(?P<a2>" + G + r")(?P<a3>" + G + r")(?P<a4>" + G + r")?")
    for m in pat.finditer(texto):
        tipo = m.group("tipo")
        fim = texto.find("\\end{%s}" % tipo, m.end())
        corpo = texto[m.end():fim]
        rot = re.search(r"\\label\{([^}]*)\}", corpo)
        g = lambda k: (m.group(k) or "{}")[1:-1]
        if tipo == "questao":
            nq += 1
            nivel, fonte, ids = g("a1"), g("a2"), g("a3")
            res.append(dict(tipo="questao", n=str(nq), nivel=int(nivel), fonte=fonte, ids=ids_de(ids),
                            rotulo=rot.group(1) if rot else None, integradora=bool(m.group("opt")),
                            corpo=corpo, pos=m.start()))
        else:
            ne += 1
            num, nivel, fonte, ids = g("a1"), g("a2"), g("a3"), g("a4")
            res.append(dict(tipo="exemplo", n=num or f"{unidade}.{ne}", nivel=int(nivel), fonte=fonte,
                            ids=ids_de(ids), rotulo=rot.group(1) if rot else None, integradora=False,
                            corpo=corpo, pos=m.start()))
    return res


def outros_ids(texto):
    """IDs que aparecem em erro, obs, construcao, caso, \\cobre, \\idH"""
    s = set()
    for pat in [r"\\begin\{erro\}" + G + r"\{([^}]*)\}", r"\\begin\{obs\}\{([^}]*)\}",
                r"\\begin\{construcao\}(?:\[[^\]]*\])?\{([^}]*)\}", r"\\begin\{caso\}" + G + r"\{([^}]*)\}",
                r"\\(?:cobre(?:\[[^\]]*\])?|idH)\{([^}]*)\}"]:
        for mm in re.finditer(pat, texto):
            s |= set(ids_de(mm.group(1)))
    return s


def capitulo(texdir):
    """{n: {'texto': str, 'arquivos': [...], 'itens': [...]}}"""
    out = {}
    for n, fs in arquivos_unidade(texdir).items():
        t = "\n".join(ler(f) for f in fs)
        out[n] = dict(texto=t, arquivos=fs, itens=itens(t, n))
    return out
