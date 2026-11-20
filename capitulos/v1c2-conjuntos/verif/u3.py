"""Verificação independente das respostas da Unidade 3 — Reunião e interseção.

Regra (w5): toda resposta calculável é RECALCULADA aqui. Rótulos finais da montagem.
Rodar:  python3 verif/u3.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
import itertools as it
from fractions import Fraction as Fr

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

fs = frozenset
def partes(S):
    S = list(S)
    return [fs(c) for r in range(len(S) + 1) for c in it.combinations(S, r)]
P4 = partes(range(4))
def sempre(f, k=2):
    return all(f(*t) for t in it.product(P4, repeat=k))
S = lambda txt: set(txt)

# ---- exemplos -------------------------------------------------------------------
chk("ex:u3:operar (FME itens 32/34) {a,b,c}∪{c,d,e}; {a,b,c}∩{b,c,d,e}; {a,b}∩{c,d}; {a,b}∪∅",
    (S("abc") | S("cde"), S("abc") & S("bcde"), S("ab") & S("cd"), S("ab") | set()), (S("abcde"), S("bc"), set(), S("ab")))
chk("ex:u3:inclusoes (FME 24, 29) A ⊂ A∪B e A∩B ⊂ A para quaisquer A, B", (sempre(lambda A, B: A <= A | B), sempre(lambda A, B: A & B <= A)), (True, True))
A, B, C = {1, 2, 3}, {3, 4}, {1, 2, 4}
X3 = [X for X in partes({1, 2, 3, 4}) if X | B == A | C and not X & B]
chk("ex:u3:fme32 (FME 32) X ∪ B = A ∪ C e X ∩ B = ∅", X3, [fs({1, 2})])
R = [Fr(n, 4) for n in range(-40, 41)]
chk("ex:u3:solucoes (x−1)(x+2)=0 → {1} ∪ {−2}; x²=4 e x>0 → {2}",
    ({x for x in R if (x - 1) * (x + 2) == 0}, {x for x in R if x * x == 4 and x > 0}), ({1, -2}, {2}))
chk("ex:u3:solucoes 1 < x < 4 e x ∈ ℤ", {x for x in range(-10, 10) if 1 < x and x < 4}, {2, 3})
A, B, C = {1}, {2}, {3}
chk("ex:u3:distributiva contraexemplo de E3: A ∪ (B∩C) × (A∪B) ∩ C", (A | (B & C), (A | B) & C), ({1}, set()))
chk("ex:u3:distributiva distributivas valem sempre (U = {0,1,2,3})",
    (sempre(lambda A, B, C: A | (B & C) == (A | B) & (A | C), 3), sempre(lambda A, B, C: A & (B | C) == (A & B) | (A & C), 3)), (True, True))
chk("ex:u3:iguais A∪B = A∩B ⇒ A = B (todos os pares)", all(A == B for A in P4 for B in P4 if A | B == A & B), True)

# ---- questões -------------------------------------------------------------------
A, B, C = S("abc"), S("cd"), S("ce")
chk("u3:fme23 (FME 23)", (A | B, A | C, B | C, A | B | C), (S("abcd"), S("abce"), S("cde"), S("abcde")))
A, B, C = S("abcd"), S("bcde"), S("cef")
chk("u3:fme28 (FME 28)", (A & B, A & C, B & C, A & B & C), (S("bcd"), {"c"}, S("ce"), {"c"}))
v25 = [sempre(lambda A, B: fs() <= A | B), sempre(lambda A, B: A | B <= A), sempre(lambda A, B: A in A | B),
       sempre(lambda A, B: A | B <= A | B), sempre(lambda A, B: B <= A | B), sempre(lambda A, B, C: A | B <= A | B | C, 3)]
chk("u3:fme25 (FME 25) V F F V V V", "".join("V" if v else "F" for v in v25), "VFFVVV")
v30 = [sempre(lambda A, B: fs() <= A & B), sempre(lambda A, B: A <= A & B), sempre(lambda A, B: A in A & B),
       sempre(lambda A, B: A & B <= A & B), sempre(lambda A, B: A & B <= B), sempre(lambda A, B, C: A & B >= A & B & C, 3)]
chk("u3:fme30 (FME 30) V F F V V V", "".join("V" if v else "F" for v in v30), "VFFVVV")
reg = list(it.product((0, 1), repeat=3))
pedido36 = {"a": [r for r in reg if all(r)], "b": [r for r in reg if r[0] and (r[1] or r[2])],
            "c": [r for r in reg if r[0] or (r[1] and r[2])], "d": [r for r in reg if any(r)]}
chk("u3:fme36 (FME 36) nº de regiões sombreadas a–d (de 7 internas)", {k: len(v) for k, v in pedido36.items()}, {"a": 1, "b": 3, "c": 5, "d": 7})
# P6 (FME 27) — plano α (raciocínio)
tipos = {"generico": set(), "paralelogramo": {"P"}, "losango": {"P", "L"}, "retangulo": {"P", "R"}, "quadrado": {"P", "L", "R", "Q"}}
T = lambda k: {t for t, s in tipos.items() if k in s}
P_, L_, R_, Q_ = T("P"), T("L"), T("R"), T("Q")
chk("u3:fme31 (FME 31) L∩P, R∩P, L∩R, Q∩R, L∩Q, P∪Q", (L_ & P_, R_ & P_, L_ & R_, Q_ & R_, L_ & Q_, P_ | Q_), (L_, R_, Q_, Q_, Q_, P_))
chk("u3:fme33 (FME 33)", [X for X in partes("abcde") if S("abcd") | X == S("abcde") and S("cd") | X == S("acde") and S("bcd") & X == {"c"}], [fs("ace")])
chk("u3:fme37 (FME 37) máx n((A∩B)∩C) com n = 2, 3, 4", max(len(set(A) & set(B) & set(C)) for A in it.combinations(range(6), 2)
    for B in it.combinations(range(6), 3) for C in it.combinations(range(6), 4)), 2)
xs = [Fr(n, d) for n in range(-30, 31) for d in (1, 2)]
chk("u3:fme46 (FME 46) A, B, C, D, E",
    ({x for x in xs if x * x - 5 * x - 6 == 0}, set("exercicio"), {x for x in xs if x * x - 9 == 0 or 2 * x - 1 == 9},
     {x for x in xs if 2 * x + 1 == 0 and 2 * x * x - x - 1 == 0}, set("234543")),
    ({6, -1}, set("exrcio"), {3, -3, 5}, {Fr(-1, 2)}, set("2345")))
# P11 (FME 61) — diagrama, por leitura
A, B, C = {1, 2}, {2, 3}, {3, 4}
chk("u3:comparar (a) A∪(B∩C) ≠ (A∪B)∩C", (A | (B & C), (A | B) & C), ({1, 2, 3}, {3}))
chk("u3:comparar (b) A∩B=∅ ⇒ A∩(B∩C)=∅", sempre(lambda A, B, C: bool(A & B) or not (A & (B & C)), 3), True)
U6 = set(range(1, 7))
ex12c = ({1, 2}, {3, 4}, {5, 6})
chk("u3:comparar (c) exemplo-modelo: não vazios, dois a dois disjuntos, reunião {1..6}",
    (all(ex12c), not (ex12c[0] & ex12c[1]) and not (ex12c[0] & ex12c[2]) and not (ex12c[1] & ex12c[2]), set().union(*ex12c) == U6), (True, True, True))
# P13 (FME 26) — disco de centro O e raio 2r (raciocínio; amostragem)
import math, random
random.seed(3)
ok26 = all((lambda d: (d <= 2) == any(math.dist((t * d / 2, 0), (0, 0)) <= 1 and math.dist((t * d / 2, 0), (d, 0)) <= 1 for t in (1.0,)))(random.uniform(0, 2.5)) for _ in range(500))
chk("u3:discos ponto P a distância d de O está em algum disco de raio 1 que contém O ⇔ d ≤ 2 (amostra)", ok26, True)
AB, AC, BC, AuB = {2, 3, 8}, {2, 7}, {2, 5, 6}, set(range(1, 9))
pad = {x: [p for p in it.product((0, 1), repeat=3) if any(p) and bool(p[0] and p[1]) == (x in AB) and bool(p[0] and p[2]) == (x in AC)
           and bool(p[1] and p[2]) == (x in BC) and bool(p[0] or p[1]) == (x in AuB)] for x in range(1, 11)}
chk("u3:fme34 (FME 34) C determinado", (all(len({p[2] for p in v}) == 1 for v in pad.values()), {x for x, v in pad.items() if v[0][2]}), (True, {2, 5, 6, 7, 9, 10}))
pares = [(X, Y) for X in partes({1, 2, 3}) for Y in partes({1, 2, 3}) if X | Y == {1, 2, 3}]
chk("u3:pares pares (X, Y) de subconjuntos de {1,2,3} com X ∪ Y = {1,2,3}", len(pares), 27)
chk("u3:pares generalização 3^n (n = 1..4)", [sum(1 for X in partes(range(n)) for Y in partes(range(n)) if X | Y == set(range(n))) for n in range(1, 5)], [3, 9, 27, 81])

a_ = set("abracadabra"); b_ = set("alacazam")
chk("caso 1 (Python, tutorial §5.4) a | b e a & b", (a_ | b_, a_ & b_), (set("abrcdlzm"), set("ac")))
print(f"\n{ok} OK, {falhas} falha(s)")
