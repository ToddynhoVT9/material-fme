#!/usr/bin/env python3
"""Folhas de contato de páginas do PDF, para a conferência visual.

Uso:
  python3 kit/scripts/paginas.py <pdf> --paginas 3,10-12 [--saida /tmp/folha]
  python3 kit/scripts/paginas.py <pdf> --buscar "Exemplo 2.3" "Síntese de domínio" [--saida /tmp/folha]
  python3 kit/scripts/paginas.py <pdf> --unidade 2            (todas as páginas da unidade 2)

Gera PNGs com até 4 páginas lado a lado (folha-1.png, folha-2.png, …) e imprime os caminhos.
Abra cada folha com a ferramenta de leitura de imagens e confira: caixas cortadas, tabelas
estouradas, listas mal quebradas, símbolos errados, página quase vazia.
"""
import sys, os, re, subprocess, tempfile
from PIL import Image


def n_paginas(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def texto_paginas(pdf):
    t = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    return t.split("\f")


def intervalo(spec, maximo):
    out = []
    for parte in spec.split(","):
        if "-" in parte:
            a, b = map(int, parte.split("-")); out += range(a, b + 1)
        elif parte.strip():
            out.append(int(parte))
    return [p for p in out if 1 <= p <= maximo]


def main(a):
    pdf = a[0]
    saida = a[a.index("--saida") + 1] if "--saida" in a else os.path.join(tempfile.gettempdir(), "folha")
    total = n_paginas(pdf)
    pags = []
    if "--paginas" in a:
        pags = intervalo(a[a.index("--paginas") + 1], total)
    if "--buscar" in a:
        termos = []
        for x in a[a.index("--buscar") + 1:]:
            if x.startswith("--"): break
            termos.append(x)
        txt = texto_paginas(pdf)
        for i, t in enumerate(txt, 1):
            if any(term in t for term in termos): pags.append(i)
    if "--unidade" in a:
        u = a[a.index("--unidade") + 1]
        txt = texto_paginas(pdf)
        # início de unidade = título da seção ("Unidade 2  Título", sem o travessão do cabeçalho)
        inicio = lambda k, t: re.search(r"^\s*Unidade %d\s+(?!—)\S" % k, t, re.M)
        dentro = False
        for i, t in enumerate(txt, 1):
            if not dentro and inicio(int(u), t): dentro = True
            elif dentro and (inicio(int(u) + 1, t) or re.search(r"^\s*Glossário do capítulo", t, re.M)): break
            if dentro: pags.append(i)
    pags = sorted(set(pags))
    if not pags:
        print("nenhuma página selecionada"); return 1
    tmp = tempfile.mkdtemp()
    imgs = []
    for p in pags:
        base = os.path.join(tmp, f"p{p:04d}")
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "60", "-png", "-singlefile", pdf, base], check=True)
        imgs.append(Image.open(base + ".png"))
    for k in range(0, len(imgs), 4):
        lote = imgs[k:k + 4]
        w = sum(i.width for i in lote) + 10 * (len(lote) - 1); h = max(i.height for i in lote)
        folha = Image.new("RGB", (w, h), "white"); x = 0
        for i in lote:
            folha.paste(i, (x, 0)); x += i.width + 10
        nome = f"{saida}-{k // 4 + 1}.png"
        folha.save(nome)
        print(nome, "← páginas", ", ".join(str(p) for p in pags[k:k + 4]))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1:]))
