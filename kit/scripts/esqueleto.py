#!/usr/bin/env python3
"""Cria o esqueleto de um capítulo, ou acrescenta uma unidade, a partir de kit/modelos/.

Uso:
  python3 kit/scripts/esqueleto.py capitulo capitulos/v1c2-conjuntos \\
          --volume 1 --numero 2 --titulo "Conjuntos" \\
          --unidades "Noção de conjunto" "Subconjuntos e operações" "Conjuntos numéricos"
  python3 kit/scripts/esqueleto.py unidade capitulos/v1c2-conjuntos --n 4 --titulo "Intervalos"

O capítulo recebe: ESTADO.md, escopo.md, matriz.yaml, dossies/, verif/, revisoes/, saida/,
tex/ (main, abertura, glossário, fontes, estilo.sty copiado do kit, uN_artigo/uN_partes/unidadeN)
e verif/uN.py por unidade. Nada é sobrescrito: arquivo existente fica como está.
"""
import sys, os, re, shutil, datetime, argparse

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(KIT, "modelos")
MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()


def romano(n):
    out = ""
    for v, s in ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
                 (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")):
        while n >= v:
            out += s; n -= v
    return out


def preencher(txt, d):
    for k, v in d.items():
        txt = txt.replace("{{" + k + "}}", str(v))
    return txt


def escrever(dest, conteudo):
    if os.path.exists(dest):
        print(f"  mantido (já existe): {dest}"); return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(conteudo)
    print(f"  criado: {dest}")


def ler_modelo(nome):
    return open(os.path.join(MOD, nome), encoding="utf-8").read()


def dados_capitulo(cap):
    """lê volume/número/título do ESTADO.md já criado"""
    t = open(os.path.join(cap, "ESTADO.md"), encoding="utf-8").read()
    g = lambda k: re.search(r"^- %s: (.*)$" % k, t, re.M).group(1).strip()
    return dict(VOLUME=g("volume"), NUMERO=g("número"), TITULO_CAPITULO=g("título"))


def unidade(cap, n, titulo, d):
    d = dict(d, N=n, TITULO=titulo)
    tex = os.path.join(cap, "tex")
    escrever(os.path.join(tex, f"u{n}_artigo.tex"), preencher(ler_modelo("tex/uN_artigo.tex"), d))
    escrever(os.path.join(tex, f"u{n}_partes.tex"), preencher(ler_modelo("tex/uN_partes.tex"), d))
    escrever(os.path.join(tex, f"unidade{n}.tex"), f"\\input{{u{n}_artigo}}\n\\input{{u{n}_partes}}\n")
    escrever(os.path.join(cap, "verif", f"u{n}.py"), preencher(ler_modelo("verif_uN.py"), d))
    # \input no main.tex
    mp = os.path.join(tex, "main.tex")
    m = open(mp, encoding="utf-8").read()
    linha = f"\\input{{unidade{n}}}\n"
    if linha not in m:
        m = m.replace("% %% FIM UNIDADES %%", linha + "% %% FIM UNIDADES %%")
        open(mp, "w", encoding="utf-8").write(m)
    # matriz.yaml
    mz = os.path.join(cap, "matriz.yaml")
    z = open(mz, encoding="utf-8").read()
    if not re.search(r"^- n: %d$" % n, z, re.M):
        z = z.rstrip("\n") + "\n" + preencher(ler_modelo("matriz_unidade.yaml"), d)
        open(mz, "w", encoding="utf-8").write(z)
    # ESTADO.md: linha na tabela de unidades
    ep = os.path.join(cap, "ESTADO.md")
    e = open(ep, encoding="utf-8").read()
    if not re.search(r"^\| %d \|" % n, e, re.M):
        e = e.replace("<!-- FIM UNIDADES -->", f"| {n} | {titulo} | escopo | — | — |\n<!-- FIM UNIDADES -->")
        open(ep, "w", encoding="utf-8").write(e)


def capitulo(a):
    cap = a.destino
    hoje = datetime.date.today()
    d = dict(VOLUME=a.volume, NUMERO=a.numero, CAP_ROMANO=romano(a.numero), CAP_ANTERIOR=a.numero - 1,
             TITULO_CAPITULO=a.titulo, DATA=f"{MESES[hoje.month - 1]} de {hoje.year}",
             MES_ANO=f"{MESES[hoje.month - 1]} de {hoje.year}", HOJE=hoje.isoformat(), SLUG=os.path.basename(cap.rstrip("/")))
    for sub in ("dossies", "verif", "revisoes", "saida", "tex"):
        os.makedirs(os.path.join(cap, sub), exist_ok=True)
    escrever(os.path.join(cap, "ESTADO.md"), preencher(ler_modelo("ESTADO.md"), d))
    escrever(os.path.join(cap, "escopo.md"), preencher(ler_modelo("escopo.md"), d))
    escrever(os.path.join(cap, "matriz.yaml"), preencher(ler_modelo("matriz_capitulo.yaml"), d))
    for f in ("main.tex", "abertura.tex", "glossario.tex", "fontes.tex"):
        escrever(os.path.join(cap, "tex", f), preencher(ler_modelo("tex/" + f), d))
    est = os.path.join(cap, "tex", "estilo.sty")
    if not os.path.exists(est):
        shutil.copy(os.path.join(KIT, "tex", "estilo.sty"), est); print(f"  criado: {est}")
    for i, t in enumerate(a.unidades or [], 1):
        unidade(cap, i, t, d)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("capitulo"); c.add_argument("destino")
    c.add_argument("--volume", type=int, required=True); c.add_argument("--numero", type=int, required=True)
    c.add_argument("--titulo", required=True); c.add_argument("--unidades", nargs="*")
    u = sp.add_parser("unidade"); u.add_argument("destino"); u.add_argument("--n", type=int, required=True)
    u.add_argument("--titulo", required=True)
    a = p.parse_args()
    if a.cmd == "capitulo":
        capitulo(a)
    else:
        d = dados_capitulo(a.destino)
        unidade(a.destino, a.n, a.titulo, d)


if __name__ == "__main__":
    main()
