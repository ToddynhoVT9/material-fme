"""w5 — verificação independente das respostas da Unidade 4 (força bruta)."""
from itertools import product

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

imp = lambda a, b: (not a) or b
iff = lambda a, b: bool(a) == bool(b)
def tipo(f, n):
    vals = [bool(f(*t)) for t in product([True, False], repeat=n)]
    return "tautologia" if all(vals) else "contradição" if not any(vals) else "contingência"
def equiv(f, g, n):
    return all(bool(f(*t)) == bool(g(*t)) for t in product([True, False], repeat=n))
def implica(f, g, n):
    return all(imp(f(*t), g(*t)) for t in product([True, False], repeat=n))

# construções
chk("4-H1 p∨~p", tipo(lambda p: p or not p, 1), "tautologia")
chk("4-H1 p∧~p", tipo(lambda p: p and not p, 1), "contradição")
chk("4-H2 modus ponens", implica(lambda p, q: imp(p, q) and p, lambda p, q: q, 2), True)
chk("4-H2 modus tollens", implica(lambda p, q: imp(p, q) and not q, lambda p, q: not p, 2), True)
chk("4-H2 afirmar consequente NÃO", implica(lambda p, q: imp(p, q) and q, lambda p, q: p, 2), False)
chk("4-H3 p→q ⇔ ~p∨q", equiv(lambda p, q: imp(p, q), lambda p, q: (not p) or q, 2), True)
chk("4-H4 absorção (0/1)", all(p * (p + q - p * q) == p and p + p * q - p * p * q == p for p, q in product([0, 1], repeat=2)), True)

# Ex 4.1
chk("Ex 4.1", [tipo(lambda p: p or not p, 1), tipo(lambda p, q: imp(p, q) and (p and not q), 2),
               tipo(lambda p, q: imp(p or q, p), 2)], ["tautologia", "contradição", "contingência"])
chk("Ex 4.1c linhas F", [t for t in product([True, False], repeat=2) if not imp(t[0] or t[1], t[0])], [(False, True)])

# Ex 4.2 FATEC 2013: (x<3 → y=-4)
alts = {"A": lambda x, y: imp(x > 3, y != -4), "B": lambda x, y: imp(x >= 3, y != 4),
        "C": lambda x, y: imp(y != 4, x >= 3), "D": lambda x, y: imp(y != -4, x > 3),
        "E": lambda x, y: imp(y != -4, x >= 3)}
orig = lambda x, y: imp(x < 3, y == -4)
pts = [(x, y) for x in (-1, 2, 2.5, 3, 3.5, 4) for y in (-4, 4, 0)]
chk("Ex 4.2 FATEC 2013", [k for k, f in alts.items() if all(f(x, y) == orig(x, y) for x, y in pts)], ["E"])

# Ex 4.3
chk("Ex 4.3a", equiv(lambda p, q: (p and q) or (p and not q), lambda p, q: p, 2), True)
chk("Ex 4.3b", equiv(lambda p, q: (not (not p)) and (p or q), lambda p, q: p, 2), True)
chk("Ex 4.3c ~(~p∨~q) ⇔ p∧q", equiv(lambda p, q: not ((not p) or (not q)), lambda p, q: p and q, 2), True)

# Ex 4.4
N = range(-300, 301)
chk("Ex 4.4 n par ⇔ n² par", all(iff(n % 2 == 0, n * n % 2 == 0) for n in N), True)
chk("Ex 4.4 m4 ⇒ par, não ⇐", (all(imp(n % 4 == 0, n % 2 == 0) for n in N), all(imp(n % 2 == 0, n % 4 == 0) for n in N)), (True, False))
chk("Ex 4.4 2|4 → 3|5", imp(4 % 2 == 0, 5 % 3 == 0), False)

# Ex 4.5 Carroll (b: bebê, l: lógico, d: desprezado, c: lida com crocodilo)
prem = lambda b, l, d, c: imp(b, not l) and imp(c, not d) and imp(not l, d)
concl = lambda b, l, d, c: imp(b, not c)
chk("Ex 4.5 Carroll válido", implica(prem, concl, 4), True)
chk("Ex 4.5 linhas da tabela", len(list(product([0, 1], repeat=4))), 16)
chk("Ex 4.5 recíproca não vale", implica(concl, prem, 4), False)

# Q1
chk("Q1", [tipo(lambda p, q: imp(imp(p, q) and p, q), 2), tipo(lambda p: p and not p, 1),
           tipo(lambda p, q: imp(p, p and q), 2), tipo(lambda p, q: iff(imp(p, q), imp(not q, not p)), 2)],
    ["tautologia", "contradição", "contingência", "tautologia"])

# Q2 (c: chove, m: molha / f: frio)
q2 = [equiv(lambda c, m: imp(c, m), lambda c, m: imp(not m, not c), 2),
      equiv(lambda c, m: imp(c, m), lambda c, m: (not c) or m, 2),
      equiv(lambda c, f: not (c and f), lambda c, f: (not c) and (not f), 2),
      equiv(lambda c, m: imp(c, m), lambda c, m: imp(m, c), 2)]
chk("Q2", q2, [True, True, False, False])

# Q3
q3 = [implica(lambda p, q: p and q, lambda p, q: p, 2), implica(lambda p, q: p, lambda p, q: p or q, 2),
      implica(lambda p, q: p or q, lambda p, q: p, 2), implica(lambda p, q: imp(p, q) and not q, lambda p, q: not p, 2),
      imp(4 % 2 == 0, 5 % 3 == 0)]
chk("Q3", q3, [True, True, False, True, False])

# Q4 FME ex 7 (seleção)
q4 = [equiv(lambda p, q, r: p and (q or r), lambda p, q, r: (p and q) or (p and r), 3),
      equiv(lambda p, q, r: p or (q and r), lambda p, q, r: (p or q) and (p or r), 3),
      equiv(lambda p, q: p and (p or q), lambda p, q: p, 2),
      equiv(lambda p, q: p or (p and q), lambda p, q: p, 2),
      equiv(lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2),
      equiv(lambda p, q: not (p or q), lambda p, q: (not p) and (not q), 2)]
chk("Q4 FME ex.7 (seleção)", all(q4), True)

# Q8 PUC-GO adaptada (v: vegetariano, c: carnívoro, f: felino)
P5 = lambda v, c, f: imp(v, not c) and imp(f, c)
alt5 = {"a": lambda v, c, f: imp(f, not v), "c": lambda v, c, f: imp(c, f), "d": lambda v, c, f: imp(c, not f),
        "e": lambda v, c, f: imp(v, f)}
chk("Q8 conclusões universais válidas", [k for k, g in alt5.items() if implica(P5, g, 3)], ["a"])
# (b) "algum felino é vegetariano": em nenhum indivíduo f∧v é compatível com as premissas
chk("Q8 (b) incompatível", any(P5(v, c, f) and f and v for v, c, f in product([True, False], repeat=3)), False)

# Q7 (integradora) — lei usada na simplificação
chk("Q7 simplificação", equiv(lambda a, b: (a and b) or (a and not b), lambda a, b: a, 2), True)

# Q6
dif = [t for t in product([True, False], repeat=3) if imp(t[0], imp(t[1], t[2])) != imp(imp(t[0], t[1]), t[2])]
chk("Q6 linhas que diferem", dif, [(False, True, False), (False, False, False)])

# Q9
chk("Q9 transitividade", implica(lambda p, q, r: imp(p, q) and imp(q, r), lambda p, q, r: imp(p, r), 3), True)
chk("Q9 12|n ⇒ 2|n; recíproco falha em 2", (all(imp(n % 12 == 0, n % 2 == 0) for n in N), imp(2 % 2 == 0, 2 % 12 == 0)), (True, False))

# Q10
chk("Q10", equiv(lambda a, b: (a and b) or (a and not b) or ((not a) and b), lambda a, b: a or b, 2), True)

# Q5 (versão q7: distributiva)
chk("Q5 distributiva p∨(q∧r) ⇔ (p∨q)∧(p∨r)", equiv(lambda p, q, r: p or (q and r), lambda p, q, r: (p or q) and (p or r), 3), True)
import itertools
chk("Q5 leitura 0/1: (p+q-pq)(p+r-pr) = p+qr-pqr em {0,1}^3", all((p+q-p*q)*(p+r-p*r) == p+q*r-p*q*r for p, q, r in itertools.product((0, 1), repeat=3)), True)
# 4-H4 (absorção, construção do texto)
chk("Q5 absorções", (equiv(lambda p, q: p or (p and q), lambda p, q: p, 2), equiv(lambda p, q: p and (p or q), lambda p, q: p, 2)), (True, True))

# ---------- v3 ----------
import random
random.seed(1)
xs=[random.uniform(-20,20) for _ in range(20000)]+[0,2,3,1e-9,-1e-9]
chk("Q7 (v3 R3) proposição ⇔ 2<x<3", all((((x**5+x-1>0) and x*x-5*x+6<0) or ((x**5+x-1<=0) and x*x-5*x+6<0))==(2<x<3) for x in xs), True)
chk("Q7 2º grau: x²-5x+6<0 ⇔ 2<x<3 (raízes)", sorted(r for r in (2,3) if r*r-5*r+6==0), [2, 3])
from math import sqrt
chk("Q11 x=2 serve, x=-1 não", (sqrt(2+2)==2, sqrt(-1+2)==-1), (True, False))
chk("Q11 x+2=x² ⇔ x∈{2,-1}", sorted(r for r in (2,-1) if r+2==r*r), [-1, 2])
chk("Q12 (p∧~p)→q tautologia", all((not (p and not p)) or q for p in (0,1) for q in (0,1)), True)

print(f"\n{ok} OK, {falhas} falha(s)")
