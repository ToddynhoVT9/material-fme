"""w5 — verificação independente das respostas da Unidade 5 (força bruta em domínios finitos/amostras)."""
from fractions import Fraction as Fr
from math import isqrt, sqrt

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

prime = lambda n: n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
# amostra de "reais": racionais de -20 a 20 com passo 1/8, mais alguns irracionais
R = [Fr(k, 8) for k in range(-160, 161)]
Rf = [float(x) for x in R] + [sqrt(2), -sqrt(3), 3.14159]
def quant(pred, dom):
    v = [x for x in dom if pred(x)]
    return ("∀" if len(v) == len(dom) else "∃" if v else "nenhum"), len(v)

# Ex 5.1
chk("Ex 5.1 x+1=7", quant(lambda x: x + 1 == 7, R)[0], "∃")
chk("Ex 5.1 x>2", quant(lambda x: x > 2, R)[0], "∃")
chk("Ex 5.1 x³=2x²", sorted(x for x in R if x ** 3 == 2 * x ** 2), [0, 2])
chk("Ex 5.1 (a+1)²=a²+2a+1", quant(lambda a: (a + 1) ** 2 == a * a + 2 * a + 1, R)[0], "∀")
chk("Ex 5.1 y²+1>0", quant(lambda y: y * y + 1 > 0, R)[0], "∀")

# Ex 5.2 (existe / existe um único)
unico = lambda pred, dom: len([x for x in dom if pred(x)]) == 1
chk("Ex 5.2", [unico(lambda x: x + 1 == 7, R), unico(lambda x: x ** 3 == 2 * x * x, R),
               unico(lambda x: x + 2 > 3, R), quant(lambda x: x * x == -1, R)[0]], [True, False, False, "nenhum"])

# Ex 5.3 domínio
chk("Ex 5.3 √(x²)=x em R", quant(lambda x: abs(x) == x, R)[0], "∃")
chk("Ex 5.3 √(x²)=x em x≥0", quant(lambda x: abs(x) == x, [x for x in R if x >= 0])[0], "∀")
chk("Ex 5.3 (a²−a)/a=a−1 em R*", quant(lambda a: (a * a - a) / a == a - 1, [a for a in R if a != 0])[0], "∀")
chk("Ex 5.3 x²=2 em Q", any(Fr(p, q) ** 2 == 2 for p in range(-50, 51) for q in range(1, 51)), False)

# Ex 5.4 Euler e Fermat
chk("Ex 5.4 n²+n+41 primo n=0..39", all(prime(n * n + n + 41) for n in range(40)), True)
chk("Ex 5.4 n=40", (40 * 40 + 40 + 41, 41 ** 2, prime(1681)), (1681, 1681, False))
chk("Ex 5.4 Fermat F0..F4 primos", [prime(2 ** (2 ** n) + 1) for n in range(5)], [True] * 5)
chk("Ex 5.4 F5 = 641·6700417", (2 ** 32 + 1, 641 * 6700417, (2 ** 32 + 1) % 641), (4294967297, 4294967297, 0))

# Ex 5.6 UF-RS (relógios): A em [11:51, 11:52), B em [11:53, 11:54) — segundos inteiros
difs = {b - a for a in range(0, 60) for b in range(120, 180)}  # segundos após 11:51:00
chk("Ex 5.6 defasagem mín/máx", (min(difs), max(difs)), (61, 179))
manuel = all(d == 120 for d in difs); joaquim = all(d <= 120 for d in difs); antonio = all(d >= 120 for d in difs)
chk("Ex 5.6 os três errados", (manuel, joaquim, antonio), (False, False, False))

# Ex 5.5 ordem dos quantificadores (inteiros de -50 a 50; y livre até 60)
X = range(-50, 51); Y = range(-60, 61)
chk("Ex 5.5 ∀x∃y y>x", all(any(y > x for y in Y) for x in X), True)
chk("Ex 5.5 ∃y∀x y>x em Z (falha: y+1)", all(any(z > y for z in range(y + 1, y + 2)) for y in Y), True)
A = [1, 2, 3]
P = lambda x: x * x < 10
chk("Ex 5.5 ∀ como ∧ em {1,2,3}", all(P(x) for x in A) == (P(1) and P(2) and P(3)), True)

# Q1 FME ex. 8
q1 = [quant(lambda x: x * x - 5 * x + 4 == 0, R)[0], quant(lambda a: (a + 1) * (a - 1) == a * a - 1, R)[0],
      quant(lambda y: y / 3 + y / 4 != y / 7, R)[0], quant(lambda m: abs(m) + 9 != m + 3, R)[0],
      quant(lambda x: -(-x) == x, R)[0], quant(lambda a: 5 * a + 4 <= 11, R)[0],
      quant(lambda x: abs(x) == x, R)[0], quant(lambda a: (a * a - a) / a == a - 1, [a for a in R if a != 0])[0]]
chk("Q1 FME ex.8", q1, ["∃", "∀", "∃", "∀", "∀", "∃", "∃", "∀"])
# (h): em R, 0 fora do domínio da expressão → o FME responde (∃a); conferimos que vale para algum a
chk("Q1 h) vale para algum a ≠ 0", any((a * a - a) / a == a - 1 for a in R if a != 0), True)

# Q2
N = range(0, 200); Z = range(-200, 201)
q2 = [all(x * x >= 0 for x in R), any(x * x < 0 for x in R), unico(lambda x: x + 3 == 5, N),
      all(n + 1 > n for n in N), any(2 * x == 5 for x in Z)]
chk("Q2", q2, [True, False, True, True, False])

# Q3
chk("Q3 x²=4: único em R? em N?", (unico(lambda x: x * x == 4, R), unico(lambda x: x * x == 4, N)), (False, True))
chk("Q3 x²=4 existe em R", any(x * x == 4 for x in R), True)
chk("Q3 x²=−4 existe em R", any(x * x == -4 for x in R), False)

# Q4
raizes = [x for x in range(-20, 21) if x * x - 5 * x + 6 == 0]
chk("Q4 raízes", raizes, [2, 3])
chk("Q4 pelo menos uma inteira; no máximo uma positiva", (len(raizes) >= 1, len([r for r in raizes if r > 0]) <= 1), (True, False))

# Q8 (integradora): (∀x ∈ D)(x² > x)
P5 = lambda x: x * x > x
D = {"A={2,3,4}": [2, 3, 4], "N": list(range(0, 100)), "(1,+∞)": [x for x in R if x > 1],
     "R−": [x for x in R if x < 0], "[0,1]": [x for x in R if 0 <= x <= 1]}
chk("Q8", {k: all(P5(x) for x in v) for k, v in D.items()},
    {"A={2,3,4}": True, "N": False, "(1,+∞)": True, "R−": True, "[0,1]": False})

# Q7 contraexemplos
chk("Q7a n²−n+41 em n=41", (41 * 41 - 41 + 41, prime(41 * 41)), (1681, False))
chk("Q7b 2^11−1", (2 ** 11 - 1, 23 * 89, prime(2047)), (2047, 2047, False))
chk("Q7c menor n primo com 2^n−1 composto", min(p for p in range(2, 40) if prime(p) and not prime(2 ** p - 1)), 11)

# Q6
Nn = range(0, 60)
chk("Q6a ∀x∃y y=x+1 (N)", all(any(y == x + 1 for y in range(0, 61)) for x in Nn), True)
chk("Q6b ∃y∀x y=x+1 (N)", any(all(y == x + 1 for x in Nn) for y in range(0, 61)), False)
chk("Q6c ∀x∃y x+y=0 (R)", all(any(x + y == 0 for y in R) for x in R), True)
chk("Q6d ∃y∀x x·y=0 (R)", any(all(x * y == 0 for x in R) for y in R), True)

# Q5
A8 = [1, 2, 3, 4]
chk("Q5 ∀x x²<10", all(x * x < 10 for x in A8), False)
chk("Q5 ∃x (x>3 ∧ x ímpar)", any(x > 3 and x % 2 == 1 for x in A8), False)
chk("Q5 ∃x (x>2 ∧ x ímpar)", any(x > 2 and x % 2 == 1 for x in A8), True)

# Q10 termômetro (truncamento): T1 ∈ [21,22), T2 ∈ [24,25) — décimos
inc = {Fr(b - a, 10) for a in range(210, 220) for b in range(240, 250)}
chk("Q10 aumento mín/máx (décimos)", (min(inc), max(inc)), (Fr(21, 10), Fr(39, 10)))
chk("Q10 alternativa d (2 < Δ < 4)", all(2 < d < 4 for d in inc) and not all(d == 3 for d in inc)
    and not all(d <= 3 for d in inc) and not all(d >= 3 for d in inc), True)

# Q9
chk("Q9 2x+3=7 único em R", (unico(lambda x: 2 * x + 3 == 7, R), [x for x in R if 2 * x + 3 == 7]), (True, [2]))

# ---------- v3 ----------
import random as _r
_r.seed(5)
_ok=[t for t in [1] if t**3+t==2]
chk("Q11 x=1 é solução", _ok, [1])
chk("Q11 x³+x estritamente crescente (amostra)", all((a**3+a)<(b**3+b) for a,b in [sorted((_r.uniform(-50,50),_r.uniform(-50,50))) for _ in range(20000)] if a<b), True)
g=lambda t: t*t/(t*t+1)
chk("Q12 -x² ≤ 0 (amostra)", all(-t*t<=0 for t in [_r.uniform(-1e3,1e3) for _ in range(5000)]), True)
chk("Q12 g < 1 (amostra)", all(g(t)<1 for t in [_r.uniform(-1e3,1e3) for _ in range(5000)]), True)
chk("Q12 g sem máximo: g(|a|+1) > g(a)", all(g(abs(a)+1)>g(a) for a in [_r.uniform(-100,100) for _ in range(5000)]), True)

chk("Q12d ∀x∃M f(x)≤M vale para qualquer f (M=f(x))", all(any(f(x)<=M for M in [f(x)]) for f in (lambda t:t**3, lambda t:-t*t, lambda t:2**t) for x in range(-20,21)), True)
print(f"\n{ok} OK, {falhas} falha(s)")
