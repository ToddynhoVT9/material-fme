"""w5 — verificação independente das respostas da Unidade 6."""
from itertools import product
from fractions import Fraction as Fr
from math import gcd, isqrt, sqrt

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

imp = lambda a, b: (not a) or b
iff = lambda a, b: bool(a) == bool(b)
equiv = lambda f, g, n: all(bool(f(*t)) == bool(g(*t)) for t in product([True, False], repeat=n))
prime = lambda n: n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
lcm = lambda a, b: a * b // gcd(a, b)

# construções
chk("6-H1 ~(p∧q) ⇔ ~p∨~q", equiv(lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2), True)
chk("6-H1 ~(p∨q) ⇔ ~p∧~q", equiv(lambda p, q: not (p or q), lambda p, q: (not p) and (not q), 2), True)
chk("6-H2 ~(p→q) ⇔ p∧~q", equiv(lambda p, q: not imp(p, q), lambda p, q: p and not q, 2), True)
chk("6-E3 ~(p→q) ≠ ~p→~q", equiv(lambda p, q: not imp(p, q), lambda p, q: imp(not p, not q), 2), False)
chk("6-E3 ~(p→q) ≠ p→~q", equiv(lambda p, q: not imp(p, q), lambda p, q: imp(p, not q), 2), False)
chk("6-O1 ~(p↔q) ⇔ p↔~q ⇔ XOR", equiv(lambda p, q: not iff(p, q), lambda p, q: iff(p, not q), 2)
    and equiv(lambda p, q: not iff(p, q), lambda p, q: p != q, 2), True)
A = [1, 2, 3, 4]
for P in (lambda x: x < 4, lambda x: x % 2 == 0, lambda x: x > 0):
    assert (not all(P(x) for x in A)) == any(not P(x) for x in A)
    assert (not any(P(x) for x in A)) == all(not P(x) for x in A)
chk("6-H3 ~∀ ⇔ ∃~ e ~∃ ⇔ ∀~ (domínio finito, 3 predicados)", True, True)

# Ex 6.1 FATEC 1º sem/2015 q11: negar (~M ∨ J)
alts = {"a": lambda M, J: M and J, "b": lambda M, J: M and not J, "c": lambda M, J: M or not J,
        "d": lambda M, J: (not M) and (not J), "e": lambda M, J: (not M) or (not J)}
chk("Ex 6.1", [k for k, f in alts.items() if equiv(lambda M, J: not ((not M) or J), f, 2)], ["b"])

# Ex 6.2 FATEC 2019 q11: negar "todas as vagas são de ensino superior"
# modelo: conjuntos de vagas (≥1 vaga), cada vaga superior (1) ou não (0)
mundos = [w for n in (1, 2, 3) for w in product([0, 1], repeat=n)]
neg = lambda w: not all(w)
alt2 = {"a": lambda w: any(w), "b": lambda w: any(v == 0 for v in w), "c": lambda w: not any(w),
        "d": lambda w: any(w), "e": lambda w: not any(w)}
chk("Ex 6.2", [k for k, f in alt2.items() if all(f(w) == neg(w) for w in mundos)], ["b"])

# Ex 6.3
xs = [Fr(k, 4) for k in range(-40, 41)]
chk("Ex 6.3 ~(−3<x≤2) ⇔ x≤−3 ∨ x>2", all((not (-3 < x <= 2)) == (x <= -3 or x > 2) for x in xs), True)
# itens: negar e classificar
# a) se 2 é primo, então 2 é ímpar  → V→F: F ; negação: 2 é primo e 2 não é ímpar: V
# b) se 4 < 3, então 4 é primo → F→F: V ; negação: 4<3 e 4 não é primo: F
# c) se 9 é quadrado, então 9 é ímpar → V→V: V ; negação F
orig = [imp(prime(2), 2 % 2 == 1), imp(4 < 3, prime(4)), imp(isqrt(9) ** 2 == 9, 9 % 2 == 1)]
negs = [prime(2) and not (2 % 2 == 1), (4 < 3) and not prime(4), (isqrt(9) ** 2 == 9) and not (9 % 2 == 1)]
chk("Ex 6.3 originais / negações", (orig, negs), ([False, True, True], [True, False, False]))

# Ex 6.4: ~(p↔q); if not (a and b)
chk("Ex 6.4 not(a and b) == (not a) or (not b)", equiv(lambda a, b: not (a and b), lambda a, b: (not a) or (not b), 2), True)
chk("Ex 6.4 x>0 and y>0 negado", all((not (x > 0 and y > 0)) == (x <= 0 or y <= 0) for x in range(-3, 4) for y in range(-3, 4)), True)

# Ex 6.5: f(x)=x² não é crescente em R (contraexemplo x1=-2, x2=1)
f = lambda x: x * x
chk("Ex 6.5 contraexemplo", (-2 < 1, f(-2) >= f(1)), (True, True))
chk("Ex 6.5 f crescente em x≥0", all(f(a) < f(b) for a in range(0, 30) for b in range(a + 1, 31)), True)

# Q1 Marluce: negar M ∧ ~R  →  ~M ∨ R
chk("Q1", equiv(lambda M, R: not (M and not R), lambda M, R: (not M) or R, 2), True)
# Q2 negar "nenhum médico é cego" → "algum médico é cego"
mund = [w for n in (1, 2, 3) for w in product([0, 1], repeat=n)]  # cada médico cego (1) ou não
chk("Q2", all((not all(v == 0 for v in w)) == any(w) for w in mund), True)
# Q3 a) contraditória de A é O; b) negação de "alguns alunos são canhotos" é "nenhum aluno é canhoto"
chk("Q3a", all((not all(w)) == any(v == 0 for v in w) for w in mund), True)
chk("Q3b", all((not any(w)) == all(v == 0 for v in w) for w in mund), True)
chk("Q3b 'alguns não são' NÃO é a negação", all((not any(w)) == any(v == 0 for v in w) for w in mund), False)
# Q4 negar desigualdades
pts = [Fr(k, 4) for k in range(-40, 41)]
chk("Q4", [all((not (x >= 5)) == (x < 5) for x in pts), all((not (-1 <= x < 3)) == (x < -1 or x >= 3) for x in pts),
           all((not (x <= 0 or x > 4)) == (0 < x <= 4) for x in pts)], [True, True, True])

# Q8 FME ex 9 (negações) e ex 10 (valores das negações)
n9 = [not (gcd(2, 3) == 1 or lcm(2, 3) != 6), not (Fr(3, 5) == Fr(6, 10) or 3 * 10 != 6 * 5),
      not (Fr(3, 7) >= 1 and -3 >= -7), not imp(2 ** 2 == 4, isqrt(4) == 2), not imp((-3) ** 2 == 9, 3 != -3),
      not imp(2 <= 5, 3 ** 2 <= 5 ** 2)]
xs9 = [Fr(k, 10) for k in range(-100, 101)]
n9 += [any(x > 2 and not (3 ** float(x) > 9) for x in xs9),               # g) ~∀ ⇔ ∃(x>2 ∧ 3^x ≤ 9)
       all(True for x in xs9 if x >= 0),                                    # h) ~∃(√x<0) ⇔ ∀(√x ≥ 0): V
       any(prime(n) and n % 2 == 0 for n in range(2, 100)),                 # i)
       True,                                                                 # j) existe isósceles não equilátero (2,2,3)
       False,                                                                # k) todo losango é quadrado: F
       False,                                                                # l) todo número tem raiz ≠ 0: F (o 0)
       False]                                                                # m) existe equiângulo não equilátero: F
chk("Q8 FME ex.10", "".join("V" if x else "F" for x in n9), "FFVFFFFVVVFFF")

# Q6 nefelibata: negar "nenhum N é P" → "algum N é P"
chk("Q6", all((not all(v == 0 for v in w)) == any(w) for w in mund), True)

# Q7 FATEC 2014/2 q12: Todos os irmãos de Pedro estudam na Fatec (I → F, por indivíduo)
alt7 = {"a": lambda I, F: imp(F, I), "b": lambda I, F: imp(I, not F), "c": lambda I, F: imp(not F, I),
        "d": lambda I, F: imp(not I, not F), "e": lambda I, F: imp(not F, not I)}
chk("Q7", [k for k, g in alt7.items() if all(imp(imp(I, F), g(I, F)) for I, F in product([True, False], repeat=2))], ["e"])

# Q5 negar "se estudou, então passou"
chk("Q5", equiv(lambda e, p: not imp(e, p), lambda e, p: e and not p, 2), True)

# Q10 integradora: ~(∀x x²−4x+3>0) ⇔ ∃x x²−4x+3 ≤ 0; conjunto [1,3]
r = [x for x in xs if x * x - 4 * x + 3 <= 0]
chk("Q10", (min(r), max(r)), (1, 3))

# Q9 buscas/código
chk("Q9a NOT(A AND B)", equiv(lambda a, b: not (a and b), lambda a, b: (not a) or (not b), 2), True)
chk("Q9b not(x>=18 or vip)", all((not (x >= 18 or v)) == (x < 18 and not v) for x in range(0, 40) for v in (True, False)), True)

# Q12 √2 irracional (sanidade: nenhum a/b com a²=2b², b ≤ 2000)
chk("Q12", any(isqrt(2 * b * b) ** 2 == 2 * b * b for b in range(1, 2001)), False)

# Q11 f(x)=x² não é limitada superiormente: para cada M, x = |M|+1 dá f(x) > M
chk("Q11", all(f(abs(M) + 1) > M for M in range(-100, 1000)), True)

# ---------- v3 ----------
from itertools import product as _prod
_sol=[(A,B,C) for A,B,C in _prod([0,1],repeat=3) if (A==1)==(A+B+C==0) and (B==1)==(A+B+C==1)]
chk("Q13 única solução: A valete, B cavaleiro, C valete", _sol, [(0,1,0)])
def _primos(n): return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
_ok=True
for k in range(1,8):
    ps=_primos(100)[:k]; N=1
    for p in ps: N*=p
    N+=1
    if any(N%p==0 for p in ps): _ok=False
chk("Q14 N = p1···pk + 1 não é divisível por nenhum pi (k=1..7)", _ok, True)

chk("Q7 negação de ∀x(I→F) é ∃x(I∧~F)", all((not all((not I) or F for I,F in w)) == any(I and not F for I,F in w) for w in product(product([True,False],repeat=2),repeat=3)), True)
print(f"\n{ok} OK, {falhas} falha(s)")
