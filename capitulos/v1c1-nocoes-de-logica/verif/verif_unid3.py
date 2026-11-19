"""w5 — verificação independente das respostas da Unidade 3 (força bruta)."""
from itertools import product
from math import gcd, isqrt
from fractions import Fraction as Fr

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

imp = lambda a, b: (not a) or b
iff = lambda a, b: a == b
b = lambda x: "V" if x else "F"
div = lambda a, n: n % a == 0
prime = lambda n: n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
lcm = lambda a, c: a * c // gcd(a, c)

# ---------- construções ----------
chk("3-H1 tabela →", "".join(b(imp(p, q)) for p, q in product([1, 0], repeat=2)), "VFVV")
chk("3-H2 tabela ↔", "".join(b(iff(p, q)) for p, q in product([1, 0], repeat=2)), "VFFV")
chk("3-H2 ↔ = (→)∧(←)", all(iff(p, q) == (imp(p, q) and imp(q, p)) for p, q in product([0, 1], repeat=2)), True)
chk("3-H3 contrapositiva", all(imp(p, q) == imp(not q, not p) for p, q in product([0, 1], repeat=2)), True)
chk("3-H3 recíproca ≠", all(imp(p, q) == imp(q, p) for p, q in product([0, 1], repeat=2)), False)
chk("3-H3 recíproca = inversa", all(imp(q, p) == imp(not p, not q) for p, q in product([0, 1], repeat=2)), True)

# ---------- Exemplo 3.1 ----------
e31 = [imp(div(3, 12), div(3, 24)), imp(2 + 2 == 4, 2 % 2 == 1), imp(1 > 2, prime(2)),
       imp(7 % 2 == 0, 7 == 0), imp(True, isqrt(9) ** 2 == 9), imp(False, False)]
chk("Ex 3.1", "".join(b(x) for x in e31), "VFVVVV")

# ---------- Exemplo 3.2: múltiplo de 4 → par ----------
N = range(-200, 201)
chk("Ex 3.2 m4→par", all(imp(n % 4 == 0, n % 2 == 0) for n in N), True)
chk("Ex 3.2 par→m4 (falha em 6)", [n for n in (2, 6, 10) if not imp(n % 2 == 0, n % 4 == 0)], [2, 6, 10])
chk("Ex 3.2 x=3 → x²=9; recíproca falha em -3", (imp(3 == 3, 9 == 9), imp((-3) ** 2 == 9, -3 == 3)), (True, False))

# ---------- Exemplo 3.3 ----------
chk("Ex 3.3a", "".join(b(x) for x in [iff(2 * 6 == 12, 2 * 6 + 7 == 19), iff(5 > 9, 2 == 3),
                                       iff(div(2, 7), prime(7)), iff(3 ** 2 == 9, 3 % 2 == 0)]), "VVFF")
chk("Ex 3.3b n par ↔ n² par", all(iff(n % 2 == 0, (n * n) % 2 == 0) for n in N), True)
chk("Ex 3.3b m6 ↔ m3 falha", [n for n in (3, 9) if not iff(n % 6 == 0, n % 3 == 0)], [3, 9])
chk("Ex 3.3c ↔ com F,F", (iff(False, False), False and False), (True, False))

# ---------- Exemplo 3.4: (p∧q) → (r∨~s) falsa ----------
sols = [(p, q, r, s) for p, q, r, s in product([1, 0], repeat=4) if not imp(p and q, r or not s)]
chk("Ex 3.4 valores", sols, [(1, 1, 0, 1)])
p, q, r, s = sols[0]
chk("Ex 3.4 itens", "".join(b(x) for x in [imp(r, p), iff(p, s), imp(q, r), (not p) or s]), "VVFV")

# ---------- Exemplo 3.5: bolo de César (OBMEP 2007) ----------
alts = dict(a=(1, 1, 0, 0), b=(0, 1, 1, 1), c=(1, 0, 1, 0), d=(1, 0, 0, 1), e=(0, 1, 0, 1))  # ovos, leite, creme, laranja
okb = [k for k, (o, l, c, la) in alts.items() if imp(o, not c) and imp(l, not la) and imp(not c, not l)]
chk("Ex 3.5 OBMEP 2007", okb, ["d"])
chk("Ex 3.5 regra 3 contrapositiva", all(imp(not c, not l) == imp(l, c) for c, l in product([0, 1], repeat=2)), True)
# combinações permitidas (16 possíveis)
perm = [t for t in product([0, 1], repeat=4) if imp(t[0], not t[2]) and imp(t[1], not t[3]) and imp(not t[2], not t[1])]
chk("Ex 3.5 nº de bolos permitidos", len(perm), 7)

# ---------- Exemplo 3.6: Wason ----------
cartas = {"A": ("letra", "A"), "K": ("letra", "K"), "4": ("num", 4), "7": ("num", 7)}
def pode_violar(c):
    tipo, v = cartas[c]
    if tipo == "letra":   # outro lado: qualquer número
        return any(not imp(v in "AEIOU", n % 2 == 0) for n in range(10))
    return any(not imp(L in "AEIOU", v % 2 == 0) for L in "AEIKU")
chk("Ex 3.6 cartas a virar", [c for c in cartas if pode_violar(c)], ["A", "7"])
beb = {"cerveja": ("bebida", True), "refrigerante": ("bebida", False), "25 anos": ("idade", 25), "16 anos": ("idade", 16)}
def viola2(c):
    t, v = beb[c]
    if t == "bebida": return any(not imp(v, i >= 18) for i in (10, 30))
    return any(not imp(x, v >= 18) for x in (True, False))
chk("Ex 3.6 versão social", [c for c in beb if viola2(c)], ["cerveja", "16 anos"])

# ---------- Q1: FME ex. 4 ----------
q1 = [imp(2 - 1 == 1, 5 + 7 == 3 * 4), iff(2 ** 2 == 4, (-2) ** 2 == 4), imp(5 + 7 * 1 == 10, 3 * 3 == 9),
      iff(gcd(3, 6) == 1, prime(4)), imp(div(2, 8), lcm(2, 8) == 2), iff(6 <= 2, 6 - 2 >= 0),
      imp(Fr(3, 5) < Fr(2, 7), 3 * 7 == 2 * 5)]
chk("Q1 FME ex.4", "".join(b(x) for x in q1), "VVVVFFV")

# ---------- Q2: FME ex. 5 (p, q V; r F) ----------
p, q, r = True, True, False
q2 = [imp(p, r), iff(p, q), imp(r, p), iff(p or r, q), imp(p, imp(q, r)), imp(p, q or r), iff(not p, not q), iff(not p, r)]
chk("Q2 FME ex.5", "".join(b(x) for x in q2), "FVVVFVVV")

# ---------- Q3 ----------
alts3 = {
    "a": lambda n: imp(n % 2 == 0, n % 6 == 0),   # par é suficiente p/ múltiplo de 6
    "b": lambda n: imp(n % 2 == 0, n % 6 == 0),   # múltiplo de 6 é necessário p/ par  (par → m6)
    "c": lambda n: imp(n % 6 == 0, n % 2 == 0),   # par é necessário p/ m6  (m6 → par)
    "d": lambda n: imp(n % 2 == 0, n % 6 == 0),   # n par somente se n m6  (par → m6)
    "e": lambda n: imp(n % 2 == 0, n % 6 == 0),   # n m6 se n par  (par → m6)
}
orig3 = lambda n: imp(n % 6 == 0, n % 2 == 0)
chk("Q3", [k for k, f in alts3.items() if all(f(n) == orig3(n) for n in N)], ["c"])

# ---------- Q4: quadrado → 4 ângulos retos ----------
# figuras: (é quadrado, tem 4 ângulos retos)
fig = {"quadrado": (1, 1), "retângulo não quadrado": (0, 1), "losango não quadrado": (0, 0)}
val = lambda f: all(f(Q, R) for Q, R in fig.values())
chk("Q4 recíproca/inversa/contrapositiva", (val(lambda Q, R: imp(R, Q)), val(lambda Q, R: imp(not Q, not R)),
                                           val(lambda Q, R: imp(not R, not Q))), (False, False, True))

# ---------- Q6: FME ex. 6 ----------
s5 = [(p, q, r, s) for p, q, r, s in product([1, 0], repeat=4) if not imp(p, r or s) and iff(q and not s, p)]
chk("Q6 FME ex.6", s5, [(1, 1, 0, 0)])

# ---------- Q8: "Se Ana viajou, então Bruno ficou ou Carla saiu" é falsa ----------
s6 = [(a, bb, c) for a, bb, c in product([1, 0], repeat=3) if not imp(a, bb or c)]
chk("Q8 valores", s6, [(1, 0, 0)])

# ---------- Q5 ----------
xs = [-2, -1, 0, 1, 2]
chk("Q5 ↔", [x for x in xs if iff(x * x == 1, x == 1)], [-2, 0, 1, 2])
chk("Q5 ∧", [x for x in xs if (x * x == 1 and x == 1)], [1])

# ---------- Q7 (integradora) ----------
X = range(-3, 4)
chk("Q7 se x²>4 então x>2", [x for x in X if imp(x * x > 4, x > 2)], [-2, -1, 0, 1, 2, 3])
chk("Q7 contrapositiva igual", [x for x in X if imp(not (x > 2), not (x * x > 4))], [-2, -1, 0, 1, 2, 3])
chk("Q7 recíproca", [x for x in X if imp(x > 2, x * x > 4)], [-3, -2, -1, 0, 1, 2, 3])

# ---------- Q10: cartas numéricas ----------
c9 = {"3": ("num", 3), "8": ("num", 8), "vermelha": ("cor", "v"), "azul": ("cor", "a")}
def viola9(c):
    t, v = c9[c]
    if t == "num": return any(not imp(v % 2 == 0, cor == "v") for cor in "va")
    return any(not imp(n % 2 == 0, v == "v") for n in range(10))
chk("Q10", [c for c in c9 if viola9(c)], ["8", "azul"])

# ---------- Q11: Ari, Bruna, Carlos ----------
# A = água (1) / suco (0)
dias = [(a, bb, c) for a, bb, c in product([1, 0], repeat=3)
        if imp(a == c, bb == 1) and imp(a != bb, c == 0) and imp(bb != c, a == 1)]
const = [(nome, dias[0][i]) for i, nome in enumerate(["Ari", "Bruna", "Carlos"]) if len({d[i] for d in dias}) == 1]
chk("Q11 dias possíveis", dias, [(1, 1, 1), (1, 1, 0), (1, 0, 0)])
chk("Q11 quem repete sempre", const, [("Ari", 1)])

# ---------- Q13: Tia Geralda (adaptada) ----------
kids = "ABCDE"; meninas = set("ACD")
culp = [X for X in kids
        if all(st == (X != k) for k, st in {"B": X in "ED", "E": X in meninas, "D": imp(X == "B", X != "C")}.items())]
chk("Q13 culpado", culp, ["E"])

# ---------- Q9 ----------
chk("Q9 n² par → n par (amostra)", all(imp((n * n) % 2 == 0, n % 2 == 0) for n in N), True)
chk("Q9b (q7) n² múlt. de 3 → n múlt. de 3 (amostra)", all(imp((n * n) % 3 == 0, n % 3 == 0) for n in N), True)
chk("Q9b (q7) n=3k+1,3k+2 ⇒ n² ≡ 1 (mod 3)", all((n*n) % 3 == 1 for n in N if n % 3 != 0), True)
# Q5 (q7): definição de primo como bicondicional, para n = 1
primo = lambda n: n > 1 and all(n % d for d in range(2, n))
dois_div = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0) == 2
chk("Q5 n=1: partes F, F; ↔ V", (primo(1), dois_div(1), primo(1) == dois_div(1)), (False, False, True))
chk("Q5 definição de primo ↔ dois divisores (1..200)", all(primo(n) == dois_div(n) for n in range(1, 201)), True)

# ---------- v3: Q12 (teste de primalidade) ----------
from math import isqrt
def teste(n): return all(n % p for p in range(2, isqrt(n)+1) if all(p % d for d in range(2, isqrt(p)+1)))
def primo(n): return n > 1 and all(n % d for d in range(2, n))
chk("Q12 teste ≡ primalidade (2..2000)", all(teste(n) == primo(n) for n in range(2, 2001)), True)
chk("Q12 contrapositiva: composto tem divisor primo ≤ √n (4..2000)", all(any(n % p == 0 and primo(p) for p in range(2, isqrt(n)+1)) for n in range(4, 2001) if not primo(n)), True)
chk("Q12c 97 primo, 91 = 7·13", (primo(97), 91 == 7*13), (True, True))

print(f"\n{ok} OK, {falhas} falha(s)")
