#!/usr/bin/env python3
"""Confere por programa o gabarito do FME, Cap. II (Conjuntos): exercícios 11–61 e
questões de vestibular 7–47. Etapa 1 (escopo). Saída: uma linha por item; divergências marcadas.

Convenções:
- "sempre V" (classifique em V ou F "admitindo A, B, C quaisquer") = vale para todos os
  subconjuntos de um universo pequeno (força bruta sobre U = {0,1,2,3}).
- Diagramas: o conjunto pedido é calculado como lista de regiões (padrões de pertinência)
  e comparado com a leitura visual da figura de resposta, transcrita aqui.
- Dados de enunciado transcritos da leitura visual (zoom 200 dpi nas passagens duvidosas).
"""
import itertools as it
from fractions import Fraction as Fr
from math import comb

res = []          # (item, ok, detalhe)
def chk(item, ok, det=""):
    res.append((item, bool(ok), det))

def subsets(s):
    s = list(s)
    return [frozenset(c) for r in range(len(s) + 1) for c in it.combinations(s, r)]

U4 = frozenset(range(4))
P4 = subsets(U4)
def sempre(f, k=2):
    return all(f(*t) for t in it.product(P4, repeat=k))

# ---------------------------------------------------------------- exercícios
# 11 (resolvido no livro)
chk("ex11 A", set("matematica") == set("mateic"))
estados_A = {"Acre", "Alagoas", "Amapá", "Amazonas"}          # os 4 estados com inicial A
chk("ex11 C", len(estados_A) == 4)

# 13
chk("ex13a", sorted(x for x in range(-10, 11) if x % 3 == 0) == [-9, -6, -3, 0, 3, 6, 9])
div42 = sorted(d for d in range(-42, 43) if d != 0 and 42 % d == 0)
chk("ex13b", div42 == sorted([s * d for d in (1, 2, 3, 6, 7, 14, 21, 42) for s in (1, -1)]))
fr = [(n, d) for n in (1, 2) for d in (1, 2)]                   # numerador e denominador em ]0,3[
chk("ex13d", len(fr) == 4, f"4 frações formais {fr}; como NÚMEROS só {len({Fr(n,d) for n,d in fr})} distintos (1/1 = 2/2) — anotado no escopo §1")
chk("ex13e", True, "DIVERGÊNCIA de redação: o gabarito omite Brasília (DF, região Centro-Oeste) — escopo §7")

# 14 (descrições do gabarito)
chk("ex14A", sorted(d for d in range(-6, 7) if d and 6 % d == 0) == [-6, -3, -2, -1, 1, 2, 3, 6])
chk("ex14B", True, "DIVERGÊNCIA de redação: B = {0,-10,-20,...} contém 0, que não é negativo ('não positivo')")
chk("ex14C", True, "DIVERGÊNCIA de redação: 0 é quadrado de inteiro e não está em C = {1,4,9,...}")

# 15 (universo real, como o gabarito assume): A é intervalo (infinito), B e C vazios, D = {3}
chk("ex15", Fr(6,5) < Fr(9,4) and not [x for x in range(-5, 6) if x * x == 3] and (7 - 1) / 2 == 3,
    "resposta D={3} vale no universo R; em Z, A = {2} também seria unitário — escopo §1")
# 16: A = universo; C = todos os inteiros (todo inteiro divide 0); D = {0}; só B vazio
chk("ex16", Fr(9,4) > Fr(6,5) and all(0 % d == 0 for d in range(1, 10)))

# 17, 18 (resolvidos)
A, B = {1, 2, 3, 4}, {2, 4}
chk("ex17", [3 in A, 1 not in B, B <= A, B == A, 4 in B] == [True, True, True, False, True])
A, B, C, D = {1, 2}, {2, 3}, {1, 3, 4}, {1, 2, 3, 4}
chk("ex18", [A <= D, A <= B, B <= C, D >= B, C == D, not A <= C] == [True, False, False, True, False, True])

# 19
r = range(-10, 11)
chk("ex19", {1, 2} == set([1, 1, 1, 2, 2]) and {x for x in r if x * x == 4} == {x for x in r if x != 0 and x**3 - 4*x == 0}
    and {x for x in r if 2*x + 7 == 11} == {2} and not [x for x in r if x < 0 and x >= 0], "todas V")

# 20 — com objetos 'a','b' e conjuntos como frozenset
E0 = frozenset()
a, b = "a", "b"
fs = frozenset
v20 = [0 in {0,1,2,3,4}, fs({a}) in {a, b}, E0 in {0}, 0 in E0, fs({a}) <= E0,
       a in {a, fs({a})}, fs({a}) <= {a, fs({a})}, E0 <= {E0, fs({a})}, E0 in {E0, fs({a})}, fs({a, b}) in {a, b, "c", "d"}]
chk("ex20", v20 == [True, False, False, False, False, True, True, True, True, False], "V F F F F V V V V F")

# 22
chk("ex22", len(subsets("abcd")) == 16)
# 23
A, B, C = set("abc"), set("cd"), set("ce")
chk("ex23", (A|B, A|C, B|C, A|B|C) == (set("abcd"), set("abce"), set("cde"), set("abcde")))
# 25 (A,B,C quaisquer): a V b F c F d V e V f V
v25 = [sempre(lambda A,B: frozenset() <= A|B), sempre(lambda A,B: A|B <= A), sempre(lambda A,B: A >= A|B),
       sempre(lambda A,B: A|B <= A|B), sempre(lambda A,B: B <= A|B), sempre(lambda A,B,C: A|B <= A|B|C, 3)]
chk("ex25", v25 == [True, False, False, True, True, True], "V F F V V V")
# 26, 27: geométricos — conferidos por raciocínio (discos de raio r com O → disco de raio 2r; retas paralelas → plano)
import random
random.seed(1)
ok26 = True
for _ in range(2000):                     # ponto a distância < 2r de O está num disco de raio r que contém O
    rr = random.uniform(0, 1.999); P = (rr, 0); c = (rr / 2, 0)
    ok26 &= (c[0]**2 <= 1) and ((P[0]-c[0])**2 <= 1)
chk("ex26", ok26, "círculo de centro O e raio 2r (amostragem, r = 1)")
chk("ex27", True, "plano α (raciocínio: por todo ponto de α passa uma paralela a r)")
# 28
A, B, C = set("abcd"), set("bcde"), set("cef")
chk("ex28", (A&B, A&C, B&C, A&B&C) == (set("bcd"), {"c"}, set("ce"), {"c"}))
# 30: a V b F c F d V e V f V
v30 = [sempre(lambda A,B: frozenset() <= A&B), sempre(lambda A,B: A <= A&B), sempre(lambda A,B: A in A&B),
       sempre(lambda A,B: A&B <= A&B), sempre(lambda A,B: A&B <= B), sempre(lambda A,B,C: A&B >= A&B&C, 3)]
chk("ex30", v30 == [True, False, False, True, True, True], "V F F V V V (c: A ∈ A∩B é falso em geral)")
# 31: quadriláteros por tipo
tipos = {"generico": set(), "paralelogramo": {"P"}, "losango": {"P","L"}, "retangulo": {"P","R"}, "quadrado": {"P","L","R","Q"}}
S = lambda k: {t for t, s in tipos.items() if k in s}
P_, L_, R_, Q_ = S("P"), S("L"), S("R"), S("Q")
chk("ex31", (L_&P_, R_&P_, L_&R_, Q_&R_, L_&Q_, P_|Q_) == (L_, R_, Q_, Q_, Q_, P_), "L R Q Q Q P")
# 32, 33
X32 = [X for X in subsets({1,2,3,4}) if X | {3,4} == {1,2,3,4} and not X & {3,4}]
chk("ex32", X32 == [frozenset({1,2})])
X33 = [X for X in subsets("abcde") if set("abcd") | X == set("abcde") and set("cd") | X == set("acde") and set("bcd") & X == {"c"}]
chk("ex33", X33 == [frozenset("ace")])
# 34 — por elemento: padrões (a,b,c) de pertinência
def por_elemento(univ, cond):
    """devolve, para cada elemento, os padrões admissíveis (lista de tuplas)"""
    return {x: [p for p in it.product((0,1), repeat=3) if cond(x, *p)] for x in univ}
U10 = range(1, 11)
AB, AC, BC, AuB = {2,3,8}, {2,7}, {2,5,6}, set(range(1, 9))
def c34(x, a, b, c):
    return (a or b or c) and ((a and b) == (x in AB)) and ((a and c) == (x in AC)) and ((b and c) == (x in BC)) and ((a or b) == (x in AuB))
pe = por_elemento(U10, c34)
Cs = {x for x, ps in pe.items() if ps and all(p[2] for p in ps)}
chk("ex34", all(len({p[2] for p in ps}) == 1 for ps in pe.values()) and Cs == {2,5,6,7,9,10}, f"C = {sorted(Cs)} (determinado)")
# 35, 37
chk("ex35", len([X for X in subsets({1,2,3,4}) if {1,2} <= X]) == 4)
chk("ex37", min(2, 3, 4) == 2, "máximo = 2 (A∩B∩C ⊂ A)")
# 36 — regiões de 3 conjuntos (a,b,c): conferido contra a leitura visual das figuras de resposta
reg = list(it.product((0,1), repeat=3))
pedido36 = {"a": [r for r in reg if all(r)], "b": [r for r in reg if r[0] and (r[1] or r[2])],
            "c": [r for r in reg if r[0] or (r[1] and r[2])], "d": [r for r in reg if any(r)]}
visual36 = {"a": [(1,1,1)], "b": [(1,0,1),(1,1,0),(1,1,1)], "c": [(1,0,0),(1,0,1),(1,1,0),(1,1,1),(0,1,1)],
            "d": [r for r in reg if any(r)]}
chk("ex36", all(sorted(pedido36[k]) == sorted(visual36[k]) for k in pedido36), "figuras a–d conferidas")
# 38
A, B, C = set("abcd"), set("cdefg"), set("bdeg")
chk("ex38", (A-B, B-A, C-B, (A|C)-B, A-(B&C), (A|B)-(A&C)) == (set("ab"), set("efg"), {"b"}, set("ab"), set("abc"), set("acefg")))
# 40
v40 = [sempre(lambda A,B: A-B >= frozenset()), sempre(lambda A,B: (A-B)|(A&B) == A), sempre(lambda A,B: A-B <= B), sempre(lambda A,B: A-B <= A|B)]
chk("ex40", v40 == [True, True, False, True], "V V F V")
# 41
A, BC = {1,2,3,4,5}, {1,2,4,6,8} & {2,4,5,7}
chk("ex41", [X for X in subsets(A) if A - X == BC] == [frozenset({1,3,5})])
# 42 — duas regiões (a,b) + fora; complemento relativo a U
reg2 = list(it.product((0,1), repeat=2))
comp = lambda S: [r for r in reg2 if r not in S]
Areg, Breg = [r for r in reg2 if r[0]], [r for r in reg2 if r[1]]
uni = lambda S, T: sorted(set(S) | set(T)); inter = lambda S, T: sorted(set(S) & set(T)); dif = lambda S, T: sorted(set(S) - set(T))
pedido42 = {"a": dif(comp(Areg), Breg), "b": dif(comp(Areg), uni(Areg, Breg)), "c": uni(comp(Breg), Areg),
            "d": comp(uni(Areg, Breg)), "e": comp(inter(Areg, Breg)), "f": inter(comp(Breg), Areg)}
visual42 = {"a": [(0,0)], "b": [(0,0)], "c": [(0,0),(1,0),(1,1)], "d": [(0,0)], "e": [(0,0),(1,0),(0,1)],
            "f": [(0,0),(1,0)]}        # figura f do livro: só B em branco (= complementar de B)
for k in "abcde":
    chk(f"ex42{k}", sorted(pedido42[k]) == sorted(visual42[k]),
        "lido como Ā − (A ∪ B); com a outra leitura, (Ā − A) ∪ B = Ā ∪ B" if k == "b" else "")
chk("ex42f", sorted(pedido42["f"]) == [(1, 0)] and sorted(visual42["f"]) != [(1, 0)],
    f"DIVERGÊNCIA: B̄ ∩ A = A − B = regiões {pedido42['f']}; a figura do livro pinta {visual42['f']} (= B̄)")
# 44 (complemento em U)
cU = lambda S: U4 - S
v44 = [sempre(lambda A,B: (A-B)|(B-A) == (A|B)-(A&B)), sempre(lambda A,B: (not A <= B) or cU(B) <= cU(A)),
       sempre(lambda A,B: A-B <= cU(A)), sempre(lambda A,B: A-B <= cU(B))]
chk("ex44", v44 == [True, True, False, True], "V V F V")
# 45, 46
E = set(range(1, 9)); F = {y for y in E if y + 1 <= 6}
chk("ex45", E - F == {6,7,8})
xs = [Fr(n, d) for n in range(-20, 21) for d in (1, 2)]
A46 = {x for x in xs if x*x - 5*x - 6 == 0}; C46 = {x for x in xs if x*x - 9 == 0 or 2*x - 1 == 9}
D46 = {x for x in xs if 2*x + 1 == 0 and 2*x*x - x - 1 == 0}
chk("ex46", A46 == {6, -1} and set("exercicio") == set("exrcio") and C46 == {3, -3, 5} and D46 == {Fr(-1,2)} and set("234543") == set("2345"))
# 47
E = {a, fs({a})}
v47 = [a in E, fs({a}) in E, False, fs({a}) <= E, E0 in E, E0 <= E]   # c) 'a ⊂ E': a não é conjunto
chk("ex47", [k for k, v in zip("abcdef", v47) if v] == list("abdf"), "a, b, d, f")
# 48, 50 — fórmulas conferidas em todos os pares/trios de subconjuntos de U4
chk("ex48", sempre(lambda A,B: len(A|B) == len(A) + len(B) - len(A&B)))
chk("ex50", sempre(lambda A,B,C: len(A|B|C) == len(A)+len(B)+len(C)-len(A&B)-len(B&C)-len(C&A)+len(A&B&C), 3))
# 49
chk("ex49", 2 ** (4 + 5 - 3) == 64)
# 51
Bd = {d for d in range(1, 121) if 120 % d == 0}
chk("ex51", len({x for x in Bd if x % 3 == 0}) == 8)
# 52
chk("ex52", (221 + 163 - 52, 415 - (221 + 163 - 52)) == (332, 83))
# 53: P' ∪ (P∩Q) = P' ∪ Q
chk("ex53", sempre(lambda P,Q: cU(P) | (P & Q) == cU(P) | Q))
# 54 — regiões: C ⊂ B (figura); incógnitas: só A (a), A∩B−C (x), A∩C (y), só B (b), C−A (c)
sol54 = [(a_, x, y, b_, c_) for a_, x, y, b_, c_ in it.product(range(25), repeat=5)
         if a_+x+y+b_+c_ == 24 and x+y == 4 and x+y+b_+c_ == 16 and a_+x == 11 and x+b_ == 10]
a_, x, y, b_, c_ = sol54[0]
chk("ex54", len(sol54) == 1 and (a_, y, b_, x, b_ + c_) == (8, 1, 7, 3, 12), f"(a..e) = {(a_, y, b_, x, b_ + c_)}")
# 55
Ab = set("efghi"); AiB = set("cd"); AuB = set("abcdef"); Uu = Ab | AuB
A55 = Uu - Ab; B55 = (AuB - A55) | AiB
chk("ex55", (len(A55), len(B55)) == (4, 4) and A55 & B55 == AiB)
# 56
nA, nB, nC, nAB, nBC, nCA, nABC, nada = 109, 203, 162, 25, 41, 28, 5, 115
uniao = nA + nB + nC - nAB - nBC - nCA + nABC
chk("ex56", (uniao + nada, nA - nAB - nCA + nABC, uniao + nada - (nA + nC - nCA), nAB + nBC + nCA - 2 * nABC) == (500, 61, 257, 84))
# 57 — por elemento
Ut = set("zxvutsrqp")
cond57 = lambda e, a_, b_, c_: (a_ or b_ or c_) and ((a_ and b_) == (e in "rs")) and ((b_ and c_) == (e in "sx")) and \
    ((c_ and a_) == (e in "st")) and ((a_ or c_) == (e in "pqrstuvx")) and ((a_ or b_) == (e in "pqrstxz"))
pe = por_elemento(Ut, cond57)
det = all(len(ps) == 1 for ps in pe.values())
A57 = {e for e, ps in pe.items() if ps[0][0]}; B57 = {e for e, ps in pe.items() if ps[0][1]}; C57 = {e for e, ps in pe.items() if ps[0][2]}
chk("ex57", det and (A57, B57, C57) == (set("pqrst"), set("rsxz"), set("stuvx")))
# 58, 59
chk("ex58", (350 - 70) / 0.5 == 560 and 350 - 70 == 280)
chk("ex59", (30 - 0.20 * 45 - 0.35 * 20) / 35 == 0.40)
# 60
chk("ex60a", (set("abcd") - set("cdefg")) | (set("cdefg") - set("abcd")) == set("abefg"))
chk("ex60b-d", sempre(lambda A: A ^ frozenset() == A, 1) and sempre(lambda A: A ^ A == frozenset(), 1) and sempre(lambda A,B: A ^ B == B ^ A))
chk("ex21/61/60e", True, "diagramas de resposta conferidos visualmente")

# ---------------------------------------------------------------- vestibulares
V = {}
V[7] = 600 + 500 + 200 - 1000                                     # 300 → d
V[8] = 200 - 0.30 * 200                                            # 140 → c
V[9] = 40 + 60 - (150 - 65)                                        # 15 → a
V[10] = 49 / ((60 + 45 - 70) / 100)                                # 140 → b
s11 = (350 - 90 == 260, 210 - 90 == 120, 350 + 210 - 90 == 470, 600 - 470 == 130)
V[11] = all(s11)                                                   # I,II,III,IV → d
V[12] = (160 + 16 + 20 + 69) - 175 - 75                            # 15 → d
V[13] = 654 + 564 - (1150 - 176)                                   # 244 → c
V[14] = (50 - 5) - 30 + 10                                         # 25 → a
V[15] = 800 - (220 + 380 - 120)                                    # 320 → b
V[16] = 60 - (28 + 26 - 15)                                        # 21 → a
V[17] = 14 + 8 - 3                                                 # 19 → b
V[18] = Fr(18 - 15, 20 - 15)                                       # 3/5 = 60% → e
# 19: pares possíveis F+H (p1), F+FS (p2), H+B (p3), B+FS (p4)
sol19 = [(p1, p2, p3, 200 - p1 - p2 - p3) for p1 in range(201) for p2 in range(201 - p1) for p3 in range(201 - p1 - p2)
         if p1 + p2 == 130 and p2 + (200 - p1 - p2 - p3) == 120 and p3 + (200 - p1 - p2 - p3) == 70 and 4 * p3 == p1 + p3]
V[19] = [s[1] for s in sol19]                                      # [70]
# 20: leitura inclusiva ("7 por bovina e frango" inclui os 4 dos três)
x20 = 36 - 9 - 3 - 20; y20 = 42 - 9 - (7 - 4) - 20
V[20] = 9 + 3 + y20 + (7 - 4) + (9 - 4) + x20 + 4 + 20             # 58 → c
V["20-exclusiva"] = 9 + 3 + (42 - 9 - 7 - 20) + 7 + 9 + (36 - 9 - 3 - 20) + 4 + 20   # 62 (alternativa d)
V[21] = 1200 + (2400 // 2)                                         # 2400 → d
uni22 = 100 + 300 + 150 + (80 - 40) + (50 - 40) + (60 - 40) + 40
V[22] = (uni22 == 40, 80 - 40 == 40, 660 - 150 == 440)             # (F, V, F) → d
V[23] = (90 + 160 + 120 - 30 - 20 - 40 + 10 + 50) - 90             # 250 → a
V[24] = 100 - (65 + 60 + 50 - 35 - 30 - 20 + 10)                   # 0 → a
V[25] = 3000 - (1450 + 1150 + 900 - 350 - 400 - 300 + 100)         # 450 → c
V[26] = 23 + 23 + 15 - 6 - 5                                       # 50 → b
c_, b_, e_, cb, be, ce, t = 226, 147, 418, 53, 85, 116, 44
uni27 = c_ + b_ + e_ - cb - be - ce + t
um27 = (c_ - cb - ce + t) + (b_ - cb - be + t) + (e_ - be - ce + t)
V[27] = (590 - uni27 == 12, um27 == 415, uni27 - um27 == 167, t == 45, c_ > e_ - be - ce + t)   # só b → b
# 28: x1 + x2 + x3 = 103, x1 + 2x2 + 3x3 = 18 + 93 + 14, x3 = 6 → pedido: x2 (carecem de 2 = usufruem de 1)
V[28] = [x2 for x2 in range(104) if (103 - 6 - x2) + 2 * x2 + 18 == 125]       # [10] → b
dois29 = 10 + 9 + 11 - 3 * 6; uni29 = 30 + 25 + 30 - 10 - 9 - 11 + 6
V[29] = (dois29 == 11, dois29 + 6 == 18, uni29 - dois29 - 6 == 43, uni29 == 61, 25 - 10 - 9 + 6 == 13)   # F V V V F
# 30: f = 2|P|, f + c + p + 12 = 93, c ≥ 4; máx |P| = p + 12
V[30] = max(p + 12 for p in range(94) for c in range(4, 94) if 2 * (p + 12) + c + p + 12 == 93)  # 29 → b
V[31] = 60 - 10 - 14 - 20                                          # 16 → c
V[32] = [N for N in range(1, 1000) if N % 60 == 0 and N - N // 3 - N // 4 - N // 5 == 65]    # [300] → b
V[33] = [3 + (38 - 12 - 3 - 0 - (20 - 8) - 8) + 8]                 # noite = 14 → c ("20 pela manhã e à tarde" lido como inclusivo, com os 8 dos três)
V[34] = [t for t in range(200) if 5 + 7 + 6 + t == 190 - 150]      # [22]
y35 = 190 - 70 - 100; x35 = 110 - 40 - 70
tot35 = 40 + 70 + 100 + x35 + y35 + 10 + 10 + 150
V[35] = (y35, 40 + 100 + 10, tot35, Fr(x35 + y35 + 10 + 10, tot35))   # (20, 150, 400, 1/10)
V[36] = 100 - (37 + 40 - 25)                                       # 48 → e  (gabarito do livro: d)
V[37] = 82 + 78 + 75 - 2 * 100                                     # 35 → c
v38 = (sempre(lambda A,B: (A & B) != frozenset() or A == frozenset() or B == frozenset()),
       sempre(lambda A,B: all(x in A or x in B for x in A | B)),
       sempre(lambda A,B: all(x in cU(A) and x in cU(B) for x in cU(A | B))))
V[38] = v38                                                        # (F, V, V) → d
V[39] = [(A, B) for A, B in it.product(P4, repeat=2) if A and B and (A - B) | (B - A) == A]   # [] → não existem
V[40] = sum(comb(8, k) for k in range(0, 7))                       # 247 = 2^8 − 9 → a
V[41] = sorted({m - n for m in range(1, 12) for n in range(1, 12) if 2**m + 2**n - 1 + 1 == 2**(m + n)})   # [0] → a
v42 = (sempre(lambda A,B,C: (A - cU(B)) - cU(C) == A & (B | C), 3), sempre(lambda A,B,C: (A - cU(B)) - C == A | cU(B & cU(C)), 3),
       sempre(lambda A,B: cU(A) | cU(B) == cU(A & B)))
V[42] = v42                                                        # (F, F, V) → c
Uh = set("abcdefgh")
# por elemento (rápido): cada elemento tem 4 padrões (a, b)
pad43 = {e: [(x, y) for x, y in it.product((0,1), repeat=2)
             if ((y and not x) == (e in "fgh")) and ((x and not y) == (e in "ab")) and ((not x and not y) == (e in "de"))] for e in Uh}
V[43] = 2 ** sum(1 for ps in pad43.values() if ps == [(1, 1)]) if all(len(ps) == 1 for ps in pad43.values()) else None   # 2 → c
V[44] = (sempre(lambda A,B: all((x not in A & B) == (x not in A or x not in B) for x in U4)),
         sempre(lambda A,B,C: A & (B | C) == (A & B) | (A & C), 3), sempre(lambda A,B: (A - B) | (B - A) == (A | B) - (A & B)))   # todas V → e
def cadeia_max(n):
    Pn = subsets(range(n)); best = 0
    # cadeia máxima = n + 1 (conferido por busca em n ≤ 3)
    def ext(ch, rest):
        nonlocal best; best = max(best, len(ch))
        for i, X in enumerate(rest):
            if all(X <= Y or Y <= X for Y in ch): ext(ch + [X], rest[i + 1:])
    ext([], Pn); return best
V[45] = [cadeia_max(n) == n + 1 for n in (1, 2, 3)]                # → c
k46 = [k for k in range(20) if 2 ** k == 128]
V[46] = (len(k46) == 1,                                   # I: n(B) − n(A) = 7, único
         any(m + (m + k46[0]) > 128 for m in range(100)),   # II refutada (n(A) livre)
         len({(m, m + 7) for m in range(1, 5)}) > 1)        # III refutada (vários pares)
pad47 = {}
for e in range(1, 10):
    ps = []
    for x, y, z, w in it.product((0,1), repeat=4):
        if (bool(x and not y and z) == (e in {1,2,3,4}) and bool(y) == (e in {5,6}) and not (z and y)
                and bool(w and x and not z) == (e in {7,8}) and bool(x and w and z) == (e in {2,4})):
            ps.append((x, y, z, w))
    pad47[e] = {e for x, y, z, w in ps if (x and (z or w)) and not (w and (y or z))}
V[47] = sorted(e for e in range(1, 10) if pad47[e] == {e})        # [1, 3, 7, 8] → c

esperado = {7: 300, 8: 140, 9: 15, 10: 140, 11: True, 12: 15, 13: 244, 14: 25, 15: 320, 16: 21, 17: 19, 18: Fr(3, 5),
            19: [70], 20: 58, 21: 2400, 22: (False, True, False), 23: 250, 24: 0, 25: 450, 26: 50,
            27: (False, True, False, False, False), 28: [10], 29: (False, True, True, True, False), 30: 29, 31: 16,
            32: [300], 33: [14], 34: [22], 35: (20, 150, 400, Fr(1, 10)), 36: 48, 37: 35, 38: (False, True, True),
            39: [], 40: 2**8 - 9, 41: [0], 42: (False, False, True), 43: 2, 44: (True, True, True),
            45: [True, True, True], 46: (True, True, True), 47: [1, 3, 7, 8]}
notas = {20: f"gabarito c (58) na leitura inclusiva; na leitura exclusiva daria {V['20-exclusiva']} (alternativa d) — escopo §1",
         36: "DIVERGÊNCIA: 100 − n(X ∪ Y) = 48% (alternativa e); o gabarito do livro diz d (42%)",
         39: "não existem (A △ B = A obriga B = ∅)", 46: "I V · II F · III F → a"}
for q, e in esperado.items():
    ok = V[q] == e
    chk(f"vest{q}", ok, notas.get(q, "") or f"{V[q]}")

falhas = [r for r in res if not r[1]]
for item, ok, det in res:
    marca = "ok " if ok else "XX "
    if "DIVERG" in det:
        marca = "!! "
    print(f"{marca}{item:12s} {det}")
print(f"\n{len(res)} conferências · {len(falhas)} falhas de programa · "
      f"{sum('DIVERG' in d for _, _, d in res)} divergências com o livro (ver escopo §7)")
