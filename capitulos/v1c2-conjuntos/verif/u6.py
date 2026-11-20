"""Verificação independente das respostas da Unidade 6 — Três conjuntos e as regiões do diagrama.

Regra (w5): toda resposta calculável é RECALCULADA aqui pelas OITO REGIÕES (sistema linear nas regiões
+ busca nas variáveis livres, exigindo regiões inteiras ≥ 0), e não pela fórmula do texto.
Rótulos finais do LaTeX (montagem).
Rodar:  python3 verif/u6.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
import itertools as it
from fractions import Fraction as Fr
import sympy as sp

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

# regiões: tupla (a, b, c) ∈ {0,1}³ — pertence a A?, a B?, a C?   (0,0,0) = nenhum
REG = list(it.product((0, 1), repeat=3))
r = {g: sp.Symbol("r%d%d%d" % g, integer=True, nonnegative=True) for g in REG}
def S(pred):
    """soma das regiões que satisfazem pred(a, b, c)"""
    return sum(r[g] for g in REG if pred(*g))
nA = lambda: S(lambda a, b, c: a);  nB = lambda: S(lambda a, b, c: b);  nC = lambda: S(lambda a, b, c: c)
AB = lambda: S(lambda a, b, c: a and b); BC = lambda: S(lambda a, b, c: b and c); AC = lambda: S(lambda a, b, c: a and c)
ABC = lambda: r[(1, 1, 1)]; NEN = lambda: r[(0, 0, 0)]; TOT = lambda: S(lambda a, b, c: True)
UNI = lambda: S(lambda a, b, c: a or b or c)
EX = lambda k: S(lambda a, b, c: a + b + c == k)

def solucoes(eqs, limite=400):
    """todas as atribuições inteiras ≥ 0 das 8 regiões que satisfazem eqs (lista de expr == 0)"""
    sol = sp.linsolve([e for e in eqs], list(r.values()))
    if not sol: return []
    (expr,) = sol
    livres = sorted(set().union(*[e.free_symbols for e in expr]), key=str)
    fs = [sp.lambdify(livres, e) for e in expr]
    out = []
    for vals in it.product(range(limite + 1), repeat=len(livres)):
        v = [f(*vals) for f in fs]
        if all(float(x).is_integer() and x >= 0 for x in v):
            out.append(dict(zip(r.keys(), [int(x) for x in v])))
    return out

def val(sol, f):
    return int(f().subs({r[g]: sol[g] for g in REG}))

# ---- construções, erros, história -----------------------------------------------------
P = [frozenset(x) for k in range(5) for x in it.combinations(range(4), k)]
chk("H3 fórmula de n(A∪B∪C) vale para todos os trios de subconjuntos de {0..3}",
    all(len(A | B | C) == len(A) + len(B) + len(C) - len(A & B) - len(B & C) - len(A & C) + len(A & B & C) for A in P for B in P for C in P), True)
chk("H3 soma n(A)+n(B)+n(C) = e1 + 2 e2 + 3 e3 (todos os trios)",
    all(len(A) + len(B) + len(C) == sum(sum((x in A, x in B, x in C)) for x in A | B | C) for A in P for B in P for C in P), True)
chk("H3 mínimo de n(A∩B) = n(A)+n(B)−N (todos os pares em U de 5 elementos, quando positivo)",
    all(len(A & B) >= len(A) + len(B) - 5 for A in [frozenset(x) for k in range(6) for x in it.combinations(range(5), k)]
        for B in [frozenset(x) for k in range(6) for x in it.combinations(range(5), k)]), True)
y = solucoes([TOT() - 1000, nA() - 525, nB() - 312, nC() - 470, AB() - 42, AC() - 147, BC() - 86, ABC() - 25], 0)
chk("Yule §5: os dados de 1000 observações não têm solução com regiões ≥ 0", y, [])
yr = 1000 - 525 - 312 - 470 + 42 + 147 + 86 - 25
chk("Yule §5: a região 'nenhum' daria −57", yr, -57)
chk("E1 quebra: 'A e B' = 10 com 4 nos três → só A e B = 6", 10 - 4, 6)
chk("E2 quebra: três conjuntos de 10, 4 em cada par, 2 nos três → 20 (e não 18)",
    [val(s, UNI) for s in solucoes([nA() - 10, nB() - 10, nC() - 10, AB() - 4, BC() - 4, AC() - 4, ABC() - 2, NEN()])], [20])
s = solucoes([nA() - 20, AB() - 8, AC() - 6, ABC() - 3, nB() - 8, nC() - 6, BC() - 3, NEN()])[0]
chk("E3 quebra: n(A) 20, AB 8, AC 6, ABC 3 → só A = 9 (e não 6)", (r[(1, 0, 0)].subs({r[g]: s[g] for g in REG}), 20 - 8 - 6), (9, 6))
s = solucoes([AB() - 8, BC() - 7, AC() - 6, ABC() - 3, r[(1, 0, 0)], r[(0, 1, 0)], r[(0, 0, 1)], NEN()])[0]
chk("E4 quebra: pares 8, 7, 6 e três 3 → exatamente dois 12; pelo menos dois 15", (val(s, lambda: EX(2)), val(s, lambda: EX(2) + EX(3))), (12, 15))

# ---- exemplos -------------------------------------------------------------
s = solucoes([TOT() - 100, nA() - 50, nB() - 40, nC() - 30, AB() - 15, BC() - 10, AC() - 12, ABC() - 5])
chk("ex:u6:streaming regiões: só A 28, só B 20, só C 13, só AB 10, só BC 5, só AC 7; reunião 88; nenhum 12",
    [(t[(1,0,0)], t[(0,1,0)], t[(0,0,1)], t[(1,1,0)], t[(0,1,1)], t[(1,0,1)], val(t, UNI), t[(0,0,0)]) for t in s], [(28, 20, 13, 10, 5, 7, 88, 12)])
s = solucoes([r[(1,0,0)] - 8, r[(0,1,0)] - 10, r[(0,0,1)] - 6, AB() - 9, BC() - 7, AC() - 5, ABC() - 3, TOT() - nB() - 25])
chk("ex:u6:clubes clubes: não participam de M = 25 → nenhum 9; total 48", [(t[(0,0,0)], val(t, TOT)) for t in s], [(9, 48)])
s = solucoes([nA() - 30, nB() - 25, nC() - 20, EX(2) - 12, ABC() - 4], 60)
chk("ex:u6:linguas línguas: exatamente uma 39; pelo menos uma 55; pelo menos duas 16 (para toda solução)",
    sorted({(val(t, lambda: EX(1)), val(t, UNI), val(t, lambda: EX(2) + EX(3))) for t in s}), [(39, 55, 16)])
mins = [max(0, 35 + 30 - 50)]; inter = [k for k in range(51) if any(a + k == 35 and b + k == 30 and a + b + k + d == 50 for a in range(51) for b in range(51) for d in range(51) if True)]
chk("ex:u6:cafe café 35, chá 30 em 50: mínimo 15, máximo 30", (min(inter), max(inter)), (15, 30))
U7 = set(range(1, 8))
# X5 por elemento: cada elemento escolhe uma das 7 regiões não vazias (está na reunião)
regs = [g for g in REG if g != (0, 0, 0)]
cand = {e: [g for g in regs] for e in U7}
def cond5(A, B, C):
    return (A | B | C == U7 and A & B == {1, 2} and B & C == {1, 3} and A & C == {1, 4}
            and A - (B | C) == {5} and B - (A | C) == {6})
def por_elemento(U, cond_elem):
    """cada elemento escolhe a sua região de modo independente; devolve as escolhas possíveis por elemento"""
    return {e: [g for g in regs if cond_elem(e, *g)] for e in sorted(U)}
def monta(esc):
    A = {e for e, gs in esc.items() if gs[0][0]}; B = {e for e, gs in esc.items() if gs[0][1]}; C = {e for e, gs in esc.items() if gs[0][2]}
    return A, B, C
c5 = por_elemento(U7, lambda e, a, b, c: ((a and b) == (e in {1, 2})) and ((b and c) == (e in {1, 3})) and ((a and c) == (e in {1, 4}))
                  and ((a and not b and not c) == (e == 5)) and ((b and not a and not c) == (e == 6)))
A5, B5, C5 = monta(c5)
sol5 = [(sorted(A5), sorted(B5), sorted(C5))] if all(len(v) == 1 for v in c5.values()) else [c5]
chk("ex:u6:elementos A, B, C determinados (solução única)", sol5, [([1, 2, 4, 5], [1, 2, 3, 6], [1, 3, 4, 7])])
n60 = range(1, 61); d = lambda k: {x for x in n60 if x % k == 0}
chk("ex:u6:divisiveis de 1 a 60: divisíveis por 2, 3 ou 5 = 44; por nenhum = 16", (len(d(2) | d(3) | d(5)), 60 - len(d(2) | d(3) | d(5))), (44, 16))
chk("ex:u6:divisiveis interseções = múltiplos de 6, 10, 15, 30", (d(2) & d(3) == d(6), d(2) & d(5) == d(10), d(3) & d(5) == d(15), d(2) & d(3) & d(5) == d(30)), (True,) * 4)

# ---- questões --------------------------------------------------------------
chk("u6:fme50 (FME 50) fórmula — ver H3", True, True)
s = solucoes([nA() - 109, nB() - 203, nC() - 162, AB() - 25, BC() - 41, AC() - 28, ABC() - 5, NEN() - 115])
chk("u6:fme56 (FME 56) (a) 500 (b) só A 61 (c) nem A nem C 257 (d) ao menos duas 84",
    [(val(t, TOT), t[(1,0,0)], t[(0,1,0)] + t[(0,0,0)], val(t, lambda: EX(2) + EX(3))) for t in s], [(500, 61, 257, 84)])
s = solucoes([TOT() - 100, nA() - 65, nB() - 60, nC() - 50, AB() - 35, BC() - 30, AC() - 20, ABC() - 10])
chk("u6:ufpa24 (vest 24) nenhum → 0 (a)", [t[(0,0,0)] for t in s], [0])
s = solucoes([ABC() - 10, AC() - 20, BC() - 40, AB() - 30, nC() - 120, nB() - 160, nA() - 90, NEN() - 50])
chk("u6:fei23 (vest 23) não consomem A → 250 (a)", [val(t, lambda: TOT() - nA()) for t in s], [250])
# P5 mínimo/máximo (autoral U3)
k5 = [k for k in range(41) if 32 - k >= 0 and 25 - k >= 0 and 40 - (32 + 25 - k) >= 0]
chk("u6:natacao (autoral) natação 32, judô 25, turma 40: mínimo 17, máximo 25", (min(k5), max(k5)), (17, 25))
# P6 (vest 29) jornais C, D, F → usar A=C, B=D, C=F
s = solucoes([nA() - 30, nB() - 25, nC() - 30, AB() - 10, BC() - 9, AC() - 11, ABC() - 6, NEN()])
t = s[0]
chk("u6:ufpe29 (vest 29) 0-0 F, 1-1 V, 2-2 V, 3-3 V, 4-4 F",
    (val(t, lambda: EX(2)) == 11, val(t, lambda: EX(2) + EX(3)) == 18, val(t, lambda: EX(1)) == 43, val(t, UNI) == 61, t[(0,1,0)] == 13),
    (False, True, True, True, False))
# P7 (FME 54): C ⊂ B (regiões fora de B dentro de C são vazias)
s = solucoes([r[(0,0,1)], r[(1,0,1)], S(lambda a, b, c: a or b) - 24, AB() - 4, S(lambda a, b, c: b or c) - 16,
              S(lambda a, b, c: a and not c) - 11, S(lambda a, b, c: b and not c) - 10, NEN()], 40)
chk("u6:fme54 (FME 54) (a) 8 (b) 1 (c) 7 (d) 3 (e) 12",
    sorted({(val(t, lambda: S(lambda a, b, c: a and not b)), t[(1,1,1)], t[(0,1,0)], t[(1,1,0)], val(t, lambda: S(lambda a, b, c: b and not a))) for t in s}),
    [(8, 1, 7, 3, 12)])
# P8 (vest 20) adaptado, leitura inclusiva: A = bovina, B = frango, C = peixe
s = solucoes([r[(0,1,0)] - 9, r[(0,0,1)] - 3, AB() - 7, AC() - 9, ABC() - 4, NEN() - 20, TOT() - nA() - 36, TOT() - nC() - 42])
chk("u6:uel20 (vest 20, leitura inclusiva) entrevistados → 58 (c)", [val(t, TOT) for t in s], [58])
s = solucoes([r[(0,1,0)] - 9, r[(0,0,1)] - 3, r[(1,1,0)] - 7, r[(1,0,1)] - 9, ABC() - 4, NEN() - 20, TOT() - nA() - 36, TOT() - nC() - 42])
chk("u6:uel20 nota M9: leitura exclusiva → 62 (d)", [val(t, TOT) for t in s], [62])
# P9 (vest 36) FGV: porcentagens
s = solucoes([TOT() - 100, nA() - 37, nB() - 40, nC() - 30, AB() - 25, BC() - 8, AC() - 3, ABC() - 1])
chk("u6:fgv36 (vest 36) nem X nem Y → 48% (e; gabarito do FME: d)", [val(s[0], lambda: TOT() - S(lambda a, b, c: a or b))], [48])
# P10 (vest 28): A, B, C = sem água, sem esgoto, sem lixo; universo = os 103 que carecem de algum
s = solucoes([nA() - 18, nB() - 93, nC() - 14, UNI() - 103, ABC() - 6, NEN()], 110)
chk("u6:ufes28 (vest 28) usufruem de exatamente um = carecem de exatamente dois → 10 (b)", sorted({val(t, lambda: EX(2)) for t in s}), [10])
s = solucoes([EX(1) - 150, UNI() - 190, r[(1,0,1)] - 7, r[(0,1,1)] - 6, AB() - ABC() - 5, NEN()], 200)
chk("u6:ufpe34 (vest 34) as três → 22", sorted({t[(1,1,1)] for t in s}), [22])
# P12 (FME 57) por elemento
E57 = set("pqrstuvxz")
c57 = por_elemento(E57, lambda e, a, b, c: ((a and b) == (e in "rs")) and ((b and c) == (e in "sx")) and ((c and a) == (e in "st"))
                   and ((a or c) == (e in "pqrstuvx")) and ((a or b) == (e in "pqrstxz")))
A57, B57, C57 = monta(c57)
sol57 = [("".join(sorted(A57)), "".join(sorted(B57)), "".join(sorted(C57)))] if all(len(v) == 1 for v in c57.values()) else [c57]
chk("u6:fme57 (FME 57) A, B, C (única)", sol57, [("pqrst", "rsxz", "stuvx")])
# P13 (vest 37) mínimo de A∩B∩C com 82%, 78%, 75% — busca em todas as distribuições inteiras de 100
mn = 101
for e3 in range(0, 76):
    # resto: 235 − 3 e3 pertenças em 100 − e3 pessoas, cada uma em no máximo 2 conjuntos e respeitando cada total
    rest = 235 - 3 * e3; pessoas = 100 - e3
    if rest <= 2 * pessoas and all(x - e3 <= pessoas for x in (82, 78, 75)):
        mn = e3; break
chk("u6:ufmg37 (vest 37) mínimo da interseção tripla → 35% (c)", mn, 35)
s = solucoes([UNI() - 93, NEN(), AB(), EX(2) - 12, r[(1,0,0)] - 2 * nC(), ], 93)
s = [t for t in s if t[(0,1,0)] >= 4]
chk("u6:ufes30 (vest 30) máximo de torcedores do Palmeiras → 29 (b)", max(val(t, nC) for t in s), 29)
s = solucoes([NEN() - 150, r[(1,0,0)] - 40, r[(0,1,0)] - 70, r[(0,0,1)] - 100, TOT() - NEN() - nA() - 190 + 0 * ABC(),
              TOT() - NEN() - nC() - 110, r[(1,0,1)] - 10, ABC() - 10], 400)
chk("u6:unicamp35 (vest 35) (a) B e C sem A 20; não votariam em B 150 (b) 400; 1/10",
    [(t[(0,1,1)], val(t, lambda: TOT() - NEN() - nB()), val(t, TOT), Fr(val(t, lambda: EX(2) + EX(3)), val(t, TOT))) for t in s], [(20, 150, 400, Fr(1, 10))])

# ---- bloco "Mais questões de vestibular" --------------------------------------
s = solucoes([TOT() - 3000, nA() - 1450, nB() - 1150, nC() - 900, AB() - 350, AC() - 400, BC() - 300, ABC() - 100])
chk("u6:uel25 (vest 25) nenhuma novela → 450 (c)", [t[(0,0,0)] for t in s], [450])
s = solucoes([TOT() - 660, r[(1,0,0)] - 100, r[(0,1,0)] - 300, r[(0,0,1)] - 150, AB() - 80, AC() - 50, BC() - 60, ABC() - 40])   # A = revistas, B = livros, C = jornais
t = s[0]
chk("u6:udesc22 (vest 22) I F, II V, III F → d", (val(t, UNI) == 40, t[(1,1,0)] == 40, val(t, lambda: S(lambda a, b, c: a or b)) == 440), (False, True, False))
s = solucoes([nA() - 23, nB() - 23, nC() - 15, AC() - 6, BC() - 5, AB(), NEN()], 70)
chk("u6:ufpa26 (vest 26) n → 50 (b)", sorted({val(t, TOT) for t in s}), [50])
s = solucoes([TOT() - 590, nA() - 226, nB() - 147, nC() - 418, AB() - 53, BC() - 85, AC() - 116, ABC() - 44])
t = s[0]
chk("u6:ufpi27 (vest 27) só (b) é verdadeira",
    (t[(0,0,0)] == 12, val(t, lambda: EX(1)) == 415, val(t, lambda: EX(2) + EX(3)) == 167, t[(1,1,1)] == 45, val(t, nA) > t[(0,0,1)]),
    (False, True, False, False, False))
s = solucoes([EX(2) - 14, ABC() - 20, NEN() - 10, TOT() - 60], 60)
chk("u6:ufpe31 (vest 31) exatamente uma → 16 (c)", sorted({val(t, lambda: EX(1)) for t in s}), [16])
# vest 33 adaptado (leitura inclusiva): A = manhã, B = tarde, C = noite; 38 frequentaram
s = solucoes([TOT() - 38, NEN(), AB() - 20, r[(1,0,0)] - 12, r[(0,0,1)] - 3, ABC() - 8, r[(0,1,0)]], 40)
chk("u6:ufu33 (vest 33, leitura inclusiva) noite → 14 (c)", sorted({val(t, nC) for t in s}), [14])
# vest 19: pares de modalidades; regiões = 6 pares; proibidos F+B e H+FS
mods = ["FH", "FS", "HB", "BS"]   # F futebol, H handebol, B basquete, S futsal (só pares permitidos)
sol19 = [(fh, fs, hb, bs) for fh in range(201) for fs in range(201 - fh) for hb in range(201 - fh - fs)
         for bs in [200 - fh - fs - hb] if fh + fs == 130 and fs + bs == 120 and hb + bs == 70 and 4 * hb == fh + hb]
chk("u6:ufpe19 (vest 19) futebol e futebol de salão → 70", [x[1] for x in sol19], [70])

# ---- montagem: números intermediários das resoluções e respostas --------------------------
chk("6-H3 (4) exemplo N = 10, n(A) = 7, n(B) = 6 → interseção de 3 a 6",
    (min(k for k in range(11) if 7 - k >= 0 and 6 - k >= 0 and 10 - 13 + k >= 0), max(k for k in range(11) if 7 - k >= 0 and 6 - k >= 0 and 10 - 13 + k >= 0)), (3, 6))
chk("Yule pela fórmula: 1000 − 1307 + 275 − 25", 1000 - (525 + 312 + 470) + (42 + 147 + 86) - 25, -57)
chk("ex:u6:streaming fórmula 50+40+30−15−10−12+5", 50 + 40 + 30 - 15 - 10 - 12 + 5, 88)
s56 = solucoes([nA() - 109, nB() - 203, nC() - 162, AB() - 25, BC() - 41, AC() - 28, ABC() - 5, NEN() - 115])[0]
chk("u6:fme56 (c) só B 142 + nenhuma 115", (s56[(0,1,0)], s56[(0,0,0)]), (142, 115))
chk("u6:ufpa24 175 − 85 + 10", 65 + 60 + 50 - (35 + 30 + 20) + 10, 100)
chk("u6:fei23 comunidade 340", 90 + 160 + 120 - 30 - 40 - 20 + 10 + 50, 340)
t29 = solucoes([nA() - 30, nB() - 25, nC() - 30, AB() - 10, BC() - 9, AC() - 11, ABC() - 6, NEN()])[0]
chk("u6:ufpe29 exatamente dois 12; só D 12", (val(t29, lambda: EX(2)), t29[(0,1,0)]), (12, 12))
t20 = solucoes([r[(0,1,0)] - 9, r[(0,0,1)] - 3, AB() - 7, AC() - 9, ABC() - 4, NEN() - 20, TOT() - nA() - 36, TOT() - nC() - 42])[0]
chk("u6:uel20 regiões: só bov.-frango 3, só peixe-bov. 5, só peixe-frango 4, só bovina 10",
    (t20[(1,1,0)], t20[(1,0,1)], t20[(0,1,1)], t20[(1,0,0)]), (3, 5, 4, 10))
chk("u6:fgv36 n(X ∪ Y) = 52%", 37 + 40 - 25, 52)
chk("u6:ufes28 sistema e1 + e2 + 6 = 103, e1 + 2 e2 + 18 = 125", [(e1, e2) for e1 in range(104) for e2 in range(104) if e1 + e2 + 6 == 103 and e1 + 2 * e2 + 18 == 18 + 93 + 14], [(87, 10)])
tu = solucoes([NEN() - 150, r[(1,0,0)] - 40, r[(0,1,0)] - 70, r[(0,0,1)] - 100, TOT() - NEN() - nA() - 190, TOT() - NEN() - nC() - 110, r[(1,0,1)] - 10, ABC() - 10], 400)[0]
chk("u6:unicamp35 indecisos = 40 (só AB 0, só AC 10, só BC 20, três 10)", (tu[(1,1,0)], tu[(1,0,1)], tu[(0,1,1)], tu[(1,1,1)], val(tu, lambda: EX(2) + EX(3))), (0, 10, 20, 10, 40))

chk("ex:u6:streaming sem devolver os três: 83", 50 + 40 + 30 - 15 - 10 - 12, 83)

t36 = solucoes([TOT() - 100, nA() - 37, nB() - 40, nC() - 30, AB() - 25, BC() - 8, AC() - 3, ABC() - 1])[0]
chk("u6:fgv36 só Z 20%, nenhuma 28%, reunião 72%", (t36[(0,0,1)], t36[(0,0,0)], val(t36, UNI)), (20, 28, 72))

print(f"\n{ok} OK, {falhas} falha(s)")
