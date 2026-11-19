#!/usr/bin/env python3
"""Conferência automática de um capítulo: compila e aplica as regras mecânicas da didática.

Uso:
  python3 kit/scripts/checar.py capitulos/<cap> [--sem-compilar] [--unidades 1,2]

Faz, nesta ordem:
  1. Compila tex/main.tex com XeLaTeX até estabilizar (máx. 4 passadas).
     FALHA: erro de LaTeX, overfull, referência ou citação indefinida, rótulo duplicado.
  2. Fontes: toda \\src{chave} tem \\bibitem (FALHA); todo \\bibitem é citado (AVISO).
  3. Matriz: roda matriz.py --tex (FALHA se ele falhar).
  4. Regras de texto, por unidade:
     - remissão por número digitado ("questão 9", "q.~8", "exemplo 4.5") fora da etiqueta
       de procedência (AVISO: use \\ref/\\qref/\\exref);
     - lista em linha com \\mbox + \\hspace (FALHA, E-R3-4);
     - questão ou exemplo sem \\label (AVISO); questão sem \\resp quando a unidade usa \\resp (FALHA);
     - "Treino:" ou linha da tabela de gatilhos apontando para item N3 (FALHA, E-R3-1);
       observação ou caso do mapa apontando para item N3 (AVISO: conferir se antecipa);
     - pergunta da síntese apontando para "Definição" sem caixa de definição na unidade,
       ou para construção inexistente (FALHA, E-R3-4);
     - ID de observação (O) declarado em exemplo ou questão (AVISO: conferir se o item a treina, E-R3-2);
     - afirmação de frequência sem fonte ("mais pedido", "sempre cai"...) (AVISO, E-R3-5).
Código de saída 1 se houver FALHA.
"""
import sys, os, re, subprocess, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texparse as tp

FALHAS, AVISOS = [], []
def falha(m): FALHAS.append(m)
def aviso(m): AVISOS.append(m)

REM = re.compile(r"(?<![\\\w])([Qq]uest(?:ão|ões)|[Ee]xemplos?|[Ee]x\.~|q\.~)[ ~]*\d")
FREQ = re.compile(r"mais (?:pedid|cobrad|comum nas provas)|sempre cai|cai muito|bloco fixo|tema preferido", re.I)


def compilar(texdir):
    env = dict(os.environ)
    for i in range(4):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                           cwd=texdir, capture_output=True, text=True, env=env)
        log = open(os.path.join(texdir, "main.log"), encoding="utf-8", errors="replace").read()
        if r.returncode != 0:
            erro = re.findall(r"^! .*(?:\n.*){0,3}", log, re.M)
            falha("LaTeX não compilou: " + (erro[0].replace("\n", " ") if erro else "ver main.log"))
            return None
        if not re.search(r"Rerun to get|Label\(s\) may have changed|There were undefined references", log) or i == 3:
            break
    paginas = re.search(r"Output written on main\.pdf \((\d+) page", log)
    for m in re.finditer(r"^Overfull \\hbox \(([\d.]+)pt too wide\) .*?lines? (\d+)", log, re.M):
        falha(f"overfull {m.group(1)}pt (main.log, linha {m.group(2)} do arquivo então aberto)")
    for m in re.finditer(r"(?:Reference|Citation) `([^']*)' on page (\d+) undefined", log):
        falha(f"indefinida: {m.group(1)} (p. {m.group(2)})")
    for m in re.finditer(r"Label `([^']*)' multiply defined", log):
        falha(f"rótulo duplicado: {m.group(1)}")
    return int(paginas.group(1)) if paginas else None


def fontes(texdir):
    todos = "".join(tp.ler(f) for f in glob.glob(os.path.join(texdir, "*.tex")))
    citadas = set(re.findall(r"\\src\{([^}]*)\}", todos))
    bib = re.findall(r"\\bibitem\{([^}]*)\}", tp.ler(os.path.join(texdir, "fontes.tex")))
    for k in sorted(citadas - set(bib)):
        falha(f"fonte citada sem \\bibitem: {k}")
    for k in sorted(set(bib) - citadas):
        aviso(f"\\bibitem nunca citado: {k}")
    dup = {k for k in bib if bib.count(k) > 1}
    for k in sorted(dup):
        falha(f"\\bibitem duplicado: {k}")
    return len(bib)


def regras_unidade(n, u, niveis):
    texto = u["texto"]
    usa_resp = "\\resp{" in texto
    for f in u["arquivos"]:
        nome = os.path.basename(f)
        for ln, linha in enumerate(tp.ler(f).split("\n"), 1):
            if not (linha.startswith("\\begin{questao}") or linha.startswith("\\begin{exemplo}")):
                for m in REM.finditer(linha):
                    aviso(f"U{n} {nome}:{ln}: remissão por número digitado «{linha[m.start():m.end()+6].strip()}» — use \\ref (se for procedência, ignore)")
            if re.search(r"\\mbox\{[^}]*\}\\hspace\{[^}]*plus", linha):
                falha(f"U{n} {nome}:{ln}: lista em linha com \\mbox+\\hspace — use enumerate/multicols")
            if FREQ.search(linha) and "\\src{" not in linha:
                aviso(f"U{n} {nome}:{ln}: afirmação de frequência sem \\src — conferir (E-R3-5)")
            if "Treino:" in linha:
                for r in re.findall(r"\\(?:ref|qref|exref)\{([^}]*)\}", linha.split("Treino:", 1)[1]):
                    if niveis.get(r) == 3:
                        falha(f"U{n} {nome}:{ln}: \"Treino:\" aponta para item N3 ({r}) — E-R3-1")
    for it in u["itens"]:
        nome = it["rotulo"] or f"{it['tipo']} {it['n']}"
        if not it["rotulo"]:
            aviso(f"U{n}: {it['tipo']} {it['n']} sem \\label")
        if it["tipo"] == "questao" and usa_resp and it["corpo"].count("\\resp{") != 1:
            falha(f"U{n}: questão {it['n']} ({nome}) com {it['corpo'].count(chr(92)+'resp{')} \\resp (esperado 1)")
        for i in it["ids"]:
            if re.match(r"\d+-O\d", i):
                aviso(f"U{n}: {nome} declara {i} — o item treina a observação, ou só a menciona? (E-R3-2)")
    for amb, nivel_msg in (("gatilhos", falha), ("obs", aviso), ("caso", aviso)):
        for m in re.finditer(r"\\begin\{%s\}(.*?)\\end\{%s\}" % (amb, amb), texto, re.S):
            for r in re.findall(r"\\(?:ref|qref|exref)\{([^}]*)\}", m.group(1)):
                if niveis.get(r) == 3:
                    nivel_msg(f"U{n}: {amb} remete a item N3 ({r}) — " +
                              ("aponte só para N1/N2 (E-R3-1)" if amb == "gatilhos" else "conferir se antecipa a solução (E-R3-1)"))
    m = re.search(r"\\begin\{sintese\}(.*?)\\end\{sintese\}", texto, re.S)
    if not m:
        falha(f"U{n}: sem caixa de síntese de domínio")
    else:
        alvos = re.findall(r"\\ondever\{([^}]*)\}", m.group(1)) + re.findall(r"\(→ ([^)]*)\)", m.group(1))
        for a in alvos:
            if a.strip().startswith("Definição") and "\\begin{definicao}" not in texto:
                falha(f"U{n}: síntese aponta para «Definição», mas a unidade não tem caixa de definição")
            for idc in re.findall(r"\d+-H\d+", a):
                if not re.search(r"\\begin\{construcao\}(?:\[[^\]]*\])?\{%s\}" % re.escape(idc), texto):
                    falha(f"U{n}: síntese aponta para a construção {idc}, que não existe")
    if "\\begin{paralembrar}" not in texto:
        falha(f"U{n}: sem caixa «Para lembrar»")
    if "\\begin{minimo}" not in texto:
        falha(f"U{n}: sem caixa «O mínimo que você precisa»")


def main(capdir, compila=True, unid=None):
    texdir = os.path.join(capdir, "tex")
    pag = compilar(texdir) if compila else None
    nbib = fontes(texdir)
    mz = os.path.join(capdir, "matriz.yaml")
    if os.path.exists(mz):
        cmd = [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "matriz.py"), mz, "--tex", texdir]
        if unid:
            cmd += ["--unidades", ",".join(map(str, sorted(unid)))]
        r = subprocess.run(cmd, capture_output=True, text=True)
        bloco = r.stdout.split("FALHAS:", 1)[1] if "FALHAS:" in r.stdout else r.stdout
        for l in bloco.split("PENDÊNCIAS")[0].splitlines():
            if l.strip().startswith("- "):
                falha("matriz: " + l.strip()[2:])
        for l in bloco.split("PENDÊNCIAS", 1)[-1].splitlines() if "PENDÊNCIAS" in bloco else []:
            if l.strip().startswith("- "):
                aviso("matriz (pendência): " + l.strip()[2:])
    cap = tp.capitulo(texdir)
    niveis = {}
    for n, u in cap.items():
        for it in u["itens"]:
            if it["rotulo"]:
                niveis[it["rotulo"]] = it["nivel"]
    for n, u in sorted(cap.items()):
        if unid and n not in unid:
            continue
        regras_unidade(n, u, niveis)
    print(f"Capítulo: {capdir}")
    print(f"  páginas: {pag if pag is not None else '—'} · fontes: {nbib} · unidades: {sorted(cap)}")
    print(f"\nFALHAS ({len(FALHAS)}):" if FALHAS else "\nFALHAS: nenhuma")
    for f in FALHAS: print("  -", f)
    print(f"\nAVISOS ({len(AVISOS)}) — conferir um a um:" if AVISOS else "\nAVISOS: nenhum")
    for a in AVISOS: print("  -", a)
    return 1 if FALHAS else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    uni = {int(x) for x in a[a.index("--unidades") + 1].split(",")} if "--unidades" in a else None
    sys.exit(main(a[0], "--sem-compilar" not in a, uni))
