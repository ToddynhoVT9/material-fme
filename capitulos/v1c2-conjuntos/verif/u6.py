"""Verificação independente das respostas da Unidade 6 — Três conjuntos e as regiões do diagrama.

Regra (w5): toda resposta que pode ser obtida por cálculo, enumeração ou tabela é RECALCULADA aqui,
sem copiar o raciocínio do texto. Cada chk() leva o rótulo do item (u6:nome, ex:u6:nome).
Questões de demonstração: confira o que der (casos pequenos, identidades) e anote o resto no fim.

Rodar:  python3 verif/u6.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
from itertools import product
from fractions import Fraction
# import sympy as sp          # se precisar:  pip install sympy --break-system-packages

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

# ---- auxiliares comuns ------------------------------------------------------
imp = lambda a, b: (not a) or b          # condicional
iff = lambda a, b: bool(a) == bool(b)    # bicondicional
def tabela(f, n):
    """coluna de f nas 2^n linhas, na ordem V…V, …, F…F"""
    return [bool(f(*t)) for t in product([True, False], repeat=n)]

# ---- exemplos -----------------------------------------------------------------
# chk("ex:u6:nome", <cálculo independente>, <valor impresso no exemplo>)

# ---- questões ----------------------------------------------------------------
# chk("u6:nome", <cálculo independente>, <valor impresso em \resp{…}>)

# ---- não verificável por programa (justificar) ------------------------------
# u6:nome — demonstração: conferido por leitura (o que a prova deve mostrar está em \resp).

print(f"\n{ok} OK, {falhas} falha(s)")
