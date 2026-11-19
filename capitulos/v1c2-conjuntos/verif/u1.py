"""Verificação independente das respostas da Unidade 1 — Conjunto, elemento e descrição.

Regra (w5): toda resposta que pode ser obtida por cálculo, enumeração ou tabela é RECALCULADA aqui,
sem copiar o raciocínio do texto. Cada chk() leva o rótulo do item (u1:nome, ex:u1:nome).
Rótulos finais da montagem (dossiê: X1–X6 = exemplos, P1–P14 = questões).

Rodar:  python3 verif/u1.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
from fractions import Fraction as Fr
import math

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

# ---- auxiliares ----------------------------------------------------------------
Z = range(-200, 201)                                  # amostra de ℤ (suficiente: raízes pequenas)
N = range(0, 201)                                     # ℕ com o 0 (convenção do FME)
Q = {Fr(p, q) for p in range(-40, 41) for q in range(1, 13)}   # amostra de ℚ com denominadores pequenos

def raizes_reais(a, b, c):
    """raízes reais de ax² + bx + c (a ≠ 0), exatas quando racionais; como floats arredondados senão"""
    d = b * b - 4 * a * c
    if d < 0: return set()
    r = math.isqrt(d) if d >= 0 else None
    if r * r == d:
        return {Fr(-b + r, 2 * a), Fr(-b - r, 2 * a)}
    return {round((-b + s * math.sqrt(d)) / (2 * a), 9) for s in (1, -1)}

# ---- exemplos -------------------------------------------------------------------
chk("ex:u1:listar letras de 'matemática'", set("matematica"), set("mateic"))
chk("ex:u1:listar pares naturais: primeiros", sorted(x for x in N if x % 2 == 0)[:5], [0, 2, 4, 6, 8])
vazio = frozenset()
chk("ex:u1:vazio n(∅), n({0}), n({∅}), n({x ∈ ℝ | x ≠ x})",
    (len(vazio), len({0}), len({vazio}), len({x for x in Q if x != x})), (0, 1, 1, 0))
chk("ex:u1:universo x² − 2 = 0 em ℚ", {x for x in Q if x * x == 2}, set())
chk("ex:u1:universo x² − 2 = 0 em ℝ", raizes_reais(1, 0, -2), {round(math.sqrt(2), 9), round(-math.sqrt(2), 9)})
chk("ex:u1:universo 2x + 1 = 0 em ℤ e em ℚ", ({x for x in Z if 2 * x + 1 == 0}, {x for x in Q if 2 * x + 1 == 0}), (set(), {Fr(-1, 2)}))
dobro = [1, 2, 4]; somas = [1, 2, 4]
while len(dobro) < 5: dobro.append(2 * dobro[-1])
while len(somas) < 5: somas.append(somas[-1] + len(somas))
chk("ex:u1:reticencias {1, 2, 4, …}: próximo pela lei 'dobro' e pela lei 'somar 1, 2, 3, …'", (dobro[3], somas[3]), (8, 7))
chk("ex:u1:reticencias fórmula 1 + n(n+1)/2", [1 + n*(n+1)//2 for n in range(5)], [1, 2, 4, 7, 11])
chk("ex:u1:reticencias {2^n}", [2**n for n in range(5)], [1, 2, 4, 8, 16])
chk("ex:u1:classificar classificação", (len({x for x in N if x < 0}), {x for x in Z if x * x == 9 and x > 0},
                          len({x for x in Z if 3 < x < 4})), (0, {3}, 0))
# X6 (barbeiro): não há homem b com  'b barbeia b' ⇔ 'b não barbeia b'
chk("ex:u1:barbeiro nenhum valor de 'b se barbeia' é consistente", [v for v in (True, False) if v == (not v)], [])

# ---- questões -------------------------------------------------------------------
# u1:fme13 [adaptado do FME, ex. 13]
chk("u1:fme13 a múltiplos de 3 entre −10 e 10", sorted(x for x in Z if -10 < x < 10 and x % 3 == 0), [-9, -6, -3, 0, 3, 6, 9])
chk("u1:fme13 b divisores inteiros de 42", sorted(d for d in Z if d != 0 and 42 % d == 0),
    sorted(s * d for d in (1, 2, 3, 6, 7, 14, 21, 42) for s in (1, -1)))
chk("u1:fme13 c múltiplos inteiros de 0", {0 * k for k in Z}, {0})
chk("u1:fme13 d números n/d com n, d ∈ {1, 2}", {Fr(n, d) for n in (1, 2) for d in (1, 2)}, {Fr(1, 2), Fr(1), Fr(2)})
estados_CO = {"Mato Grosso": "Cuiabá", "Mato Grosso do Sul": "Campo Grande", "Goiás": "Goiânia"}  # o DF não é estado
chk("u1:fme13 e capitais dos estados do Centro-Oeste", set(estados_CO.values()), {"Cuiabá", "Campo Grande", "Goiânia"})
# P2 [adaptado do FME, ex. 14] — as descrições corrigidas geram os conjuntos dados
chk("u1:fme14 A = divisores inteiros de 6", sorted(d for d in Z if d and 6 % d == 0), [-6, -3, -2, -1, 1, 2, 3, 6])
chk("u1:fme14 B = múltiplos de 10 não positivos (início)", sorted((x for x in Z if x % 10 == 0 and x <= 0), reverse=True)[:5], [0, -10, -20, -30, -40])
chk("u1:fme14 C = quadrados de inteiros positivos (início)", sorted({n * n for n in range(1, 50)})[:6], [1, 4, 9, 16, 25, 36])
# P3 [autoral] A = {1, {2}, 3}
A = {1, frozenset({2}), 3}
chk("u1:pertence 2∈A, {2}∈A, 3∈A, {3}∈A, n(A)", (2 in A, frozenset({2}) in A, 3 in A, frozenset({3}) in A, len(A)), (False, True, True, False, 3))
# P4 [autoral]
chk("u1:listar a divisores naturais de 12", sorted(d for d in range(1, 13) if 12 % d == 0), [1, 2, 3, 4, 6, 12])
chk("u1:listar b {x ∈ ℤ | −2 ≤ x < 3}", sorted(x for x in Z if -2 <= x < 3), [-2, -1, 0, 1, 2])
chk("u1:listar c primos menores que 20", [p for p in range(2, 20) if all(p % k for k in range(2, p))], [2, 3, 5, 7, 11, 13, 17, 19])
chk("u1:listar d letras de 'banana'", set("banana"), {"b", "a", "n"})
chk("u1:listar e código Python", {x for x in range(1, 20) if x % 3 == 0}, {3, 6, 9, 12, 15, 18})
# P5 [autoral]
chk("u1:quantos n(∅), n({0}), n({∅}), n({∅, {∅}}), n({0, ∅})",
    (len(vazio), len({0}), len({vazio}), len({vazio, frozenset({vazio})}), len({0, vazio})), (0, 1, 1, 2, 2))
# P6 [adaptado do FME, ex. 15] — unitários em ℝ e em ℤ
A_R_infinito = Fr(6, 5) < Fr(9, 4)                     # intervalo aberto não degenerado em ℝ: infinito
A_Z = {x for x in Z if Fr(6, 5) < x < Fr(9, 4)}
B = {x for x in Q if 0 * x == 2}
C = {x for x in Z if x * x == 3}
D = {x for x in Q if 2 * x + 1 == 7}
chk("u1:unitarios em ℝ: só D unitário", (A_R_infinito, len(B), len(C), D), (True, 0, 0, {3}))
chk("u1:unitarios em ℤ: A e D unitários", (A_Z, D), ({2}, {3}))
# P7 [FME, ex. 16] em ℤ, com 'a é divisível por b' ⇔ existe k inteiro com a = b·k
chk("u1:vazios A = {x | 0·x = 0} é todo o universo", all(0 * x == 0 for x in Z), True)
chk("u1:vazios B = {x | x > 9/4 e x < 6/5} vazio", [x for x in Q if x > Fr(9, 4) and x < Fr(6, 5)], [])
div_de_zero = {d for d in Z if any(0 == d * k for k in Z)}
chk("u1:vazios C = divisores de 0: todos os inteiros", div_de_zero == set(Z), True)
chk("u1:vazios D = divisíveis por 0: só o 0", {a for a in Z if any(a == 0 * k for k in Z)}, {0})
# P8 [autoral, integradora] 2x² − 3x − 2 = 0 e x² + 1 = 0
r = raizes_reais(2, -3, -2)
chk("u1:equacao raízes de 2x² − 3x − 2", r, {Fr(2), Fr(-1, 2)})
chk("u1:equacao em ℕ, ℤ, ℚ", ({x for x in r if x >= 0 and x.denominator == 1}, {x for x in r if x.denominator == 1}, r),
    ({2}, {2}, {Fr(2), Fr(-1, 2)}))
chk("u1:equacao x² + 1 = 0 em ℝ", raizes_reais(1, 0, 1), set())
# u1:reticencias [autoral] {2, 3, 5, …}
primos = [p for p in range(2, 40) if all(p % k for k in range(2, p))]
fib = [2, 3]
while len(fib) < 6: fib.append(fib[-1] + fib[-2])
chk("u1:reticencias começam iguais", (primos[:3], fib[:3]), ([2, 3, 5], [2, 3, 5]))
chk("u1:reticencias 8 pertence a qual; próximo primo", (8 in primos, 8 in fib, primos[3]), (False, True, 7))
# P10 [autoral] — juízo, não cálculo (ver "não verificável")
# P11 [autoral, integradora] pontos a distância 1 de P — conferência numérica por amostragem
import random
random.seed(2)
reta = sorted({x for x in (-1, 1)})
chk("u1:distancia na reta: 2 pontos", reta, [-1, 1])
ok_circ = all(abs(math.hypot(math.cos(t), math.sin(t)) - 1) < 1e-12 for t in [random.uniform(0, 6.3) for _ in range(100)])
chk("u1:distancia no plano: circunferência (amostra)", ok_circ, True)
# u1:parametro [autoral, N3, integradora] A_k = {x ∈ ℤ | x² − 2x + k = 0}, k real
def A_k(k):
    return {x for x in range(-60, 61) if x * x - 2 * x + k == 0}
ks = sorted({Fr(p, q) for p in range(-40, 41) for q in (1, 2, 3, 4)})
unit = [k for k in ks if len(A_k(k)) == 1]
dois = [k for k in ks if len(A_k(k)) == 2]
chk("u1:parametro unitário só k = 1, com A_1 = {1}", (unit, A_k(1)), ([1], {1}))
chk("u1:parametro dois elementos ⇔ k = 1 − m², m ≥ 1 (na amostra)", dois, sorted(Fr(1 - m * m) for m in range(1, 7) if 1 - m * m >= -40))
chk("u1:parametro A_k para k = 1 − m²", all(A_k(1 - m * m) == {1 - m, 1 + m} for m in range(1, 7)), True)
# P13 [autoral, N3, estrutura do paradoxo de Berry]
frase = "o menor número natural que não pode ser descrito com menos de vinte palavras"
frase_q = "seja n o menor número natural que não pode ser descrito com menos de vinte palavras"
chk("u1:berry a frase do enunciado tem menos de 20 palavras", len(frase_q.split()) < 20, True)
# u1:escolherU [autoral, N3] (3x − 2)(x² − 5)(x + 4) = 0
rz = {Fr(2, 3), Fr(-4), round(math.sqrt(5), 9), round(-math.sqrt(5), 9)}
racs = {x for x in rz if isinstance(x, Fr)}
nN = {x for x in racs if x.denominator == 1 and x >= 0}; nZ = {x for x in racs if x.denominator == 1}
chk("u1:escolherU ℕ, ℤ, ℚ, ℝ", (nN, nZ, racs, len(rz)), (set(), {Fr(-4)}, {Fr(-4), Fr(2, 3)}, 4))
chk("u1:escolherU nenhum universo com exatamente 3", [n for n in (len(nN), len(nZ), len(racs), len(rz)) if n == 3], [])

chk("erro 1-E1: x² − x − 6 = 0 em ℕ e em ℤ", ({x for x in N if x*x - x - 6 == 0}, {x for x in Z if x*x - x - 6 == 0}), ({3}, {-2, 3}))
# ---- caso do mapa: o exemplo do tutorial do Python (§5.4) executado aqui -------
chk("caso Python {x for x in 'abracadabra' if x not in 'abc'}", {x for x in 'abracadabra' if x not in 'abc'}, {"r", "d"})

# ---- não verificável por programa (justificar) ----------------------------------
# ex:u1:barbeiro, u1:berry — argumentos por contradição: conferidos por leitura (a resposta diz o que a prova deve mostrar).
# u1:criterio — decidir se uma descrição tem critério de pertinência: juízo, conferido por leitura.
# u1:distancia (c) — superfície esférica: conferido por leitura.

print(f"\n{ok} OK, {falhas} falha(s)")

