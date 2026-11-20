"""Verificação independente das respostas da Unidade 4 — Diferença e complementar.

Regra (w5): toda resposta calculável é RECALCULADA aqui. Etapa 2 (dossiê): rótulos PROVISÓRIOS (X*, P*, V*).
Rodar:  python3 verif/u4.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
import itertools as it
from math import comb

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
U4 = fs(range(4)); P4 = partes(U4)
c = lambda X: U4 - X                         # complementar em U
def sempre(f, k=2):
    return all(f(*t) for t in it.product(P4, repeat=k))
S = set

# ---- exemplos -------------------------------------------------------------------
chk("X1 diferenças e complementar (FME itens 38, 39)",
    (S("abc") - S("bcde"), S("bcde") - S("abc"), S("ab") - S("cdef"), S("ab") - S("abcde"), S("abcde") - S("cde")),
    ({"a"}, S("de"), S("ab"), set(), S("ab")))
chk("X2 (FME 39) A − B ⊂ A sempre", sempre(lambda A, B: A - B <= A), True)
chk("X3 (FME 43) A − B̄ = A ∩ B sempre", sempre(lambda A, B: A - c(B) == A & B), True)
U6 = set(range(1, 7)); A, B = {1, 2, 3}, {3, 4}; cc = lambda X: U6 - X
chk("X4 De Morgan: (A∩B)ᶜ, Āᶜ∩B̄ᶜ errado, Ā∪B̄ certo",
    (cc(A & B), cc(A) & cc(B), cc(A) | cc(B)), ({1, 2, 4, 5, 6}, {5, 6}, {1, 2, 4, 5, 6}))
chk("X4 De Morgan vale sempre (U = {0..3})", (sempre(lambda A, B: c(A & B) == c(A) | c(B)), sempre(lambda A, B: c(A | B) == c(A) & c(B))), (True, True))
T = {"Ana", "Bia", "Caio", "Davi", "Eva"}; F = {"Bia", "Caio"}
chk("X5 turma − futebol", T - F, {"Ana", "Davi", "Eva"})
N = set(range(0, 20)); Zs = set(range(-9, 10))
chk("X5 complementar dos pares em ℕ e em ℤ (amostra)", ({x for x in N if x % 2}, {x for x in Zs if x % 2}),
    ({1, 3, 5, 7, 9, 11, 13, 15, 17, 19}, {-9, -7, -5, -3, -1, 1, 3, 5, 7, 9}))
chk("X6 A − B = B − A ⇔ A = B (todos os pares)", all((A - B == B - A) == (A == B) for A in P4 for B in P4), True)

# ---- questões -------------------------------------------------------------------
A, B, C = S("abcd"), S("cdefg"), S("bdeg")
chk("P1 (FME 38)", (A - B, B - A, C - B, (A | C) - B, A - (B & C), (A | B) - (A & C)),
    (S("ab"), S("efg"), {"b"}, S("ab"), S("abc"), S("acefg")))
v40 = [sempre(lambda A, B: A - B >= fs()), sempre(lambda A, B: (A - B) | (A & B) == A), sempre(lambda A, B: A - B <= B), sempre(lambda A, B: A - B <= A | B)]
chk("P2 (FME 40) V V F V", "".join("V" if v else "F" for v in v40), "VVFV")
reg2 = list(it.product((0, 1), repeat=2)); R = lambda f: sorted(r for r in reg2 if f(*r))
p42 = {"a": R(lambda a, b: not a and not b), "b": R(lambda a, b: (not a) and not (a or b)), "c": R(lambda a, b: (not b) or a),
       "d": R(lambda a, b: not (a or b)), "e": R(lambda a, b: not (a and b)), "f": R(lambda a, b: (not b) and a)}
chk("P3 (FME 42) regiões (a, b): (1,0)=só A, (0,1)=só B, (1,1)=A∩B, (0,0)=fora",
    p42, {"a": [(0, 0)], "b": [(0, 0)], "c": [(0, 0), (1, 0), (1, 1)], "d": [(0, 0)], "e": [(0, 0), (0, 1), (1, 0)], "f": [(1, 0)]})
E = set(range(1, 9)); Fy = {y for y in E if y + 1 <= 6}
chk("P4 (FME 45) F e F̄ em E", (Fy, E - Fy), ({1, 2, 3, 4, 5}, {6, 7, 8}))
A = {1, 2, 3, 4, 5}; BC = {1, 2, 4, 6, 8} & {2, 4, 5, 7}
chk("P5 (FME 41) X ⊂ A com A − X = B ∩ C", [X for X in partes(A) if A - X == BC], [fs({1, 3, 5})])
v44 = [sempre(lambda A, B: (A - B) | (B - A) == (A | B) - (A & B)), sempre(lambda A, B: (not A <= B) or c(B) <= c(A)),
       sempre(lambda A, B: A - B <= c(A)), sempre(lambda A, B: A - B <= c(B))]
chk("P6 (FME 44) V V F V", "".join("V" if v else "F" for v in v44), "VVFV")
chk("P7 (FME 53) P′ ∪ (P∩Q) = P′ ∪ Q", sempre(lambda P, Q: c(P) | (P & Q) == c(P) | Q), True)
Ab = S("efghi"); AiB = S("cd"); AuB = S("abcdef"); Uu = Ab | AuB
sol55 = [(X, Y) for X in partes(Uu) for Y in partes(Uu) if Uu - X == Ab and X & Y == AiB and X | Y == AuB]
chk("P8 (FME 55) n(A), n(B) (U = {a..i})", sorted({(len(X), len(Y)) for X, Y in sol55}), [(4, 4)])
v42 = (sempre(lambda A, B, C: (A - c(B)) - c(C) == A & (B | C), 3), sempre(lambda A, B, C: (A - c(B)) - C == A | c(B & c(C)), 3),
       sempre(lambda A, B: c(A) | c(B) == c(A & B)))
chk("P9 (ITA 42) I F, II F, III V → c", v42, (False, False, True))
Uh = S("abcdefgh")
sol43 = [(X, Y) for X in partes(Uh) for Y in partes(Uh) if Uh - ((Uh - Y) | X) == S("fgh") and (Uh - Y) & X == S("ab") and (Uh - X) - Y == S("de")]
chk("P10 (ITA 43) n(𝒫(A∩B)) → c", sorted({2 ** len(X & Y) for X, Y in sol43}), [2])
chk("P11 (FME 60a) {a,b,c,d} △ {c,d,e,f,g}", (S("abcd") - S("cdefg")) | (S("cdefg") - S("abcd")), S("abefg"))
chk("P11 (FME 60b–d) A△∅=A, A△A=∅, A△B=B△A", (sempre(lambda A, B: (A - fs()) | (fs() - A) == A), sempre(lambda A, B: (A - A) | (A - A) == fs()),
    sempre(lambda A, B: (A - B) | (B - A) == (B - A) | (A - B))), (True, True, True))
reg = lambda pos: sorted(r for r in reg2 if (r[0] and not r[1]) or (r[1] and not r[0]))
chk("P11 (FME 60e) A△B = só A + só B", reg(None), [(0, 1), (1, 0)])
chk("P12 (ITA 39) não existem A, B ≠ ∅ com (A−B)∪(B−A) = A", [(A, B) for A in P4 for B in P4 if A and B and (A - B) | (B - A) == A], [])
pad = {}
for e in range(1, 10):
    ps = [p for p in it.product((0, 1), repeat=4)
          if bool(p[0] and not p[1] and p[2]) == (e in {1, 2, 3, 4}) and bool(p[1]) == (e in {5, 6}) and not (p[2] and p[1])
          and bool(p[3] and p[0] and not p[2]) == (e in {7, 8}) and bool(p[0] and p[3] and p[2]) == (e in {2, 4})]
    pad[e] = {bool((x and (z or w)) and not (w and (y or z))) for x, y, z, w in ps}
chk("P13 (ITA 47) resultado determinado e = {1,3,7,8} → c", (all(len(v) == 1 for v in pad.values()), sorted(e for e, v in pad.items() if True in v)), (True, [1, 3, 7, 8]))

# ---- bloco "Mais questões de vestibular" ------------------------------------------------
v38 = (sempre(lambda A, B: bool(A & B) or not A or not B), sempre(lambda A, B: all(x in A or x in B for x in A | B)),
       sempre(lambda A, B: all(x in c(A) and x in c(B) for x in c(A | B))))
chk("V1 (UF-PI 38) I F, II V, III V → d", v38, (False, True, True))
v44i = (sempre(lambda A, B: all((x not in A & B) == (x not in A or x not in B) for x in U4)),
        sempre(lambda A, B, C: A & (B | C) == (A & B) | (A & C), 3), sempre(lambda A, B: (A - B) | (B - A) == (A | B) - (A & B)))
chk("V2 (ITA 44) todas V → nenhuma falsa → e", v44i, (True, True, True))
k46 = [k for k in range(20) if 2 ** k == 128]
chk("V3 (ITA 46) I V (n(B)−n(A)=7), II F, III F → a", (k46, any(m + (m + 7) > 128 for m in range(100)), len({(m, m + 7) for m in range(1, 5)}) > 1), ([7], True, True))
chk("V4 (ITA 40) subconjuntos de A−B (8 el.) com ≤ 6 elementos = 2^8 − 9 → a", (sum(comb(8, k) for k in range(7)), 2 ** 8 - 9), (247, 247))

print(f"\n{ok} OK, {falhas} falha(s)")
