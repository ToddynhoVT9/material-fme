"""w5 — verificação independente das respostas da Unidade 2 (força bruta).
Uso: python3 verif_unid2.py   → imprime OK/FALHA por item e o total."""
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

V = "V"; F = "F"
b = lambda x: V if x else F
div = lambda a, n: n % a == 0
prime = lambda n: n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

# ---------- Exemplo 2.1 ----------
ex21 = [prime(2) and 2 % 2 == 0, 7 < 5 or 7 % 2 == 1, isqrt(9) == 3 and div(3, 10),
        (-1)**3 == 1 or (-1)**2 == -1, True or 2 + 2 == 5, Fr(1, 2) == Fr(5, 10) and 2**3 == 3**2]
chk("Ex 2.1", "".join(b(x) for x in ex21), "VVFFVF")

# ---------- Exemplo 2.3: (p∧q)∨~r ----------
linhas = list(product([1, 0], repeat=3))
col = [int((p and q) or not r) for p, q, r in linhas]
chk("Ex 2.3 coluna (ordem VVV..FFF)", "".join(b(x) for x in col), "VVFVFVFV")
chk("Ex 2.3 linhas V", sum(col), 5)
chk("Ex 2.3 2^4, 2^5, 2^10", (len(list(product([0,1], repeat=4))), 2**5, 2**10), (16, 32, 1024))

# ---------- Exemplo 2.4: OBMEP 2005 (bolas) ----------
vals = [n for n in range(101, 140)
        if (100 < n < 120) + (105 < n < 130) + (120 < n < 140) == 1]
chk("Ex 2.4 quantidade", len(vals), 16)
chk("Ex 2.4 blocos", (vals[:5], [v for v in vals if 119 < v < 121], len([v for v in vals if v > 129])),
    ([101, 102, 103, 104, 105], [120], 10))
alts_prova = {"A": 16, "B": 13, "C": 11, "D": 5, "E": 1}
chk("Ex 2.4 alternativa (prova)", [k for k, v in alts_prova.items() if v == len(vals)], ["A"])

# ---------- Exemplo 2.5: circuitos ----------
chk("Ex 2.5a a∧(b∨c) acende", sum(1 for a, bb, c in product([0, 1], repeat=3) if a and (bb or c)), 3)
chk("Ex 2.5c maioria acende", sum(1 for a, bb, c in product([0, 1], repeat=3)
                                  if (a and bb) or (a and c) or (bb and c)), 4)
chk("Ex 2.5c maioria ⇔ a+b+c≥2", all(bool((a and bb) or (a and c) or (bb and c)) == (a + bb + c >= 2)
                                     for a, bb, c in product([0, 1], repeat=3)), True)

# ---------- Q1: FME ex. 3 ----------
q1 = [3 > 1 and 4 > 2, 3 > 1 or 3 == 1, div(2, 4) or div(2, 5),
      3*(5+2) == 3*5 + 3*2 and div(3, 7), Fr(1, 2) < Fr(3, 4) or div(5, 11),
      (-1)**6 == -1 and 2**5 < (-2)**7, isqrt(16) == 6 or gcd(4, 7) == 2]
chk("Q1 FME ex.3", "".join(b(x) for x in q1), "VVVFVFF")

# ---------- Q2: p = '6 é par' (V), q = '6 é primo' (F) ----------
p, q = True, prime(6)
q2 = [p and not q, (not p) and (not q), q and p, p or q, p and not q]
chk("Q2", "".join(b(x) for x in q2), "VFFVV")

# ---------- Q3 ----------
estudante, idade = True, 65
chk("Q3a meia-entrada (inclusivo)", estudante or idade >= 60, True)
chk("Q3 b,c,d", "".join(b(x) for x in [True or 7 % 2 == 0, True and prime(10), 2+2 == 4 or 2*2 == 4]), "VFV")

# ---------- Q4 ----------
A = lambda x: -2 < x <= 3
B = lambda x: x >= 1
xs = [-2, 0, 1, 3, 5]
chk("Q4 ∧", "".join(b(A(x) and B(x)) for x in xs), "FFVVF")
chk("Q4 ∨", "".join(b(A(x) or B(x)) for x in xs), "FVVVV")
grade = [k / 100 for k in range(-1000, 1001)]
chk("Q4 A∩B = [1,3]", all((A(x) and B(x)) == (1 <= x <= 3) for x in grade), True)
chk("Q4 A∪B = x>-2", all((A(x) or B(x)) == (x > -2) for x in grade), True)

# ---------- Q7: OBMEP 2009 (casais) ----------
# idades: permutação; casais: Arnaldo e Beto são homens, Celina e Dalila mulheres
sol = []
for idades in product(range(4), repeat=4):
    if len(set(idades)) < 4: continue
    Ar, Be, Ce, Da = idades
    for esp_celina in ("Arnaldo", "Beto"):
        esp = {"Celina": esp_celina, "Dalila": "Beto" if esp_celina == "Arnaldo" else "Arnaldo"}
        ida = {"Arnaldo": Ar, "Beto": Be, "Celina": Ce, "Dalila": Da}
        if Ar > Ce and Ar < Da and ida[esp["Celina"]] == 3:
            sol.append((idades, esp_celina))
alts = {
    "a": lambda i, e: i[0] > i[1] and e == "Beto",              # Arnaldo > Beto e esposa de Arnaldo é Dalila
    "b": lambda i, e: e == "Beto" and i[0] > i[3],               # Arnaldo mais velho que a esposa Dalila
    "c": lambda i, e: i[2] == 0 and e == "Beto",                 # Celina a mais nova e marido Beto
    "d": lambda i, e: i[3] > i[2] and e == "Arnaldo",            # Dalila > Celina e marido de Dalila é Beto
    "e": lambda i, e: e == "Arnaldo" and i[2] > i[0],            # Celina mais velha que marido Arnaldo
}
certas = [k for k, f in alts.items() if all(f(i, e) for i, e in sol)]
chk("Q7 OBMEP 2009", certas, ["c"])

# ---------- Q6 (integradora) ----------
q6 = [x for x in range(-50, 51) if (-3 < x <= 2 and x != 0) or x**2 == 16]
chk("Q6 inteiros", q6, [-4, -2, -1, 1, 2, 4])

# ---------- Q5 ----------
feitas = {(1,1,1), (1,1,0), (1,0,1), (0,1,1), (0,1,0), (0,0,0)}
faltam = [t for t in product([1, 0], repeat=3) if t not in feitas]
chk("Q5 linhas que faltam", faltam, [(1, 0, 0), (0, 0, 1)])
chk("Q5 valores nelas", [b((p or q) and not r) for p, q, r in faltam], ["V", "F"])

# ---------- Q8 ----------
q8 = [n for n in range(1, 31)
      if (n % 2 == 0 and n > 10) + (n % 3 == 0 or n < 5) + (n % 5 == 0 or n > 25) == 1]
chk("Q8 valores", (len(q8), q8), (14, [1, 2, 3, 4, 5, 6, 9, 10, 14, 16, 21, 22, 25, 29]))

# ---------- Q10: exatamente um ----------
f1 = lambda a, bb, c: (a and not bb and not c) or (not a and bb and not c) or (not a and not bb and c)
f2 = lambda a, bb, c: (a or bb or c) and not (a and bb) and not (a and c) and not (bb and c)
chk("Q10 forma 1 = exatamente um", all(bool(f1(*t)) == (sum(t) == 1) for t in product([0, 1], repeat=3)), True)
chk("Q10 forma 2 = forma 1", all(bool(f1(*t)) == bool(f2(*t)) for t in product([0, 1], repeat=3)), True)

# ---------- Q9: contas 0/1 ----------
chk("Q9 ∧ = pq", all(int(p and q) == p*q for p, q in product([0, 1], repeat=2)), True)
chk("Q9 ∨ = p+q-pq", all(int(p or q) == p+q-p*q for p, q in product([0, 1], repeat=2)), True)
chk("Q9 ⊻ = p+q-2pq = ∨ - ∧", all(int(p != q) == p+q-2*p*q == (p+q-p*q) - p*q
                                   for p, q in product([0, 1], repeat=2)), True)

# ---------- 2-O1: números de Plutarco ----------
def schroder_pequeno(n):
    # s(1)=s(2)=1; (n+1)s(n+1) = 3(2n-1)s(n) - (n-2)s(n-1)
    s = {1: 1, 2: 1}
    for k in range(2, n):
        s[k+1] = (3*(2*k-1)*s[k] - (k-2)*s[k-1]) // (k+1)
    return s[n]
chk("2-O1 s(10)", schroder_pequeno(10), 103049)
chk("2-O1 (s10+s11)/2", (schroder_pequeno(10) + schroder_pequeno(11)) // 2, 310954)

# ---------- v3: Q11 e Q12 ----------
chk("Q11a 16 colunas", 2**4, 16)
chk("Q11b (p∧q)∨(~p∧~q) = V,F,F,V", [bool((p and q) or (not p and not q)) for p, q in [(1,1),(1,0),(0,1),(0,0)]], [True, False, False, True])
chk("2.2d 7 primo ou ímpar: V∨V = V", bool(True or True), True)
def fnd(col):
    linhas=[(1,1),(1,0),(0,1),(0,0)]
    return lambda p,q: any((p==a and q==b) for (a,b),c in zip(linhas,col) if c)
chk("Q11c FND reproduz todas as 16 colunas", all([bool(fnd(col)(p,q)) for p,q in [(1,1),(1,0),(0,1),(0,0)]]==list(col) for col in product([True,False],repeat=4)), True)
chk("Q12a 1-(1-p)(1-q) = p∨q", all(1-(1-p)*(1-q)==int(p or q) for p,q in product([0,1],repeat=2)), True)
chk("Q12b n letras: V em 2^n-1 linhas (n=1..8)", all(sum(1 for t in product([0,1],repeat=n) if any(t))==2**n-1 for n in range(1,9)), True)

print(f"\n{ok} OK, {falhas} falha(s)")
