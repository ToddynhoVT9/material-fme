"""Verificação independente das respostas da Unidade 2 — Igualdade, inclusão e conjunto das partes.

Regra (w5): toda resposta que pode ser obtida por cálculo, enumeração ou tabela é RECALCULADA aqui,
sem copiar o raciocínio do texto. Rótulos finais da montagem (dossiê: X1–X6 = exemplos, P1–P14 = questões).

Rodar:  python3 verif/u2.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
"""
import itertools as it

ok = falhas = 0
def chk(nome, obtido, esperado):
    global ok, falhas
    if obtido == esperado:
        ok += 1; print(f"OK     {nome}: {obtido}")
    else:
        falhas += 1; print(f"FALHA  {nome}: obtido {obtido!r}, esperado {esperado!r}")

fs = frozenset
V = fs()
def partes(S):
    S = list(S)
    return {fs(c) for r in range(len(S) + 1) for c in it.combinations(S, r)}
def sub(X, Y):            # X ⊂ Y (X e Y conjuntos)
    return all(x in Y for x in X)
Z = range(-300, 301)

# ---- exemplos -------------------------------------------------------------------
A, B = {1, 2, 3, 4}, {2, 4}
chk("ex:u2:fme17 (FME 17): 3∈A, 1∉B, B⊂A, B=A, 4∈B", (3 in A, 1 not in B, sub(B, A), B == A, 4 in B), (True, True, True, False, True))
A, B, C, D = {1, 2}, {2, 3}, {1, 3, 4}, {1, 2, 3, 4}
chk("ex:u2:fme18 (FME 18): A⊂D, A⊂B, B⊂C, D⊃B, C=D, A⊄C", (sub(A, D), sub(A, B), sub(B, C), sub(B, D), C == D, not sub(A, C)),
    (True, False, False, True, False, True))
E = {1, fs({1}), fs({2, 3})}
chk("ex:u2:chaves 1∈E, {1}∈E, {1}⊂E, {2}⊂E, {2,3}∈E, {2,3}⊂E, ∅⊂E, ∅∈E",
    (1 in E, fs({1}) in E, sub({1}, E), sub({2}, E), fs({2, 3}) in E, sub({2, 3}, E), sub(V, E), V in E),
    (True, True, True, False, True, False, True, False))
chk("ex:u2:multiplos múltiplos de 2 e de 3 = múltiplos de 6 (amostra)", {x for x in Z if x % 2 == 0 and x % 3 == 0}, {x for x in Z if x % 6 == 0})
chk("ex:u2:partes n(𝒫({a,b,c})) e subconjuntos de {1..5} com o 1", (len(partes("abc")), sum(1 for X in partes(range(1, 6)) if 1 in X)), (8, 16))
# X6 (unicidade do vazio): argumento por dupla inclusão — por leitura

# ---- questões -------------------------------------------------------------------
A = {2, 4, 6}
chk("u2:completar 2∈A, {2}⊂A, {2,5}⊄A, {6,4,2}=A, 5∉A", (2 in A, sub({2}, A), not sub({2, 5}, A), {6, 4, 2} == A, 5 not in A), (True,) * 5)
R = range(-50, 51)
chk("u2:fme19 (FME 19) a,b,c,d todas V",
    ({"a", "a", "a", "b", "b"} == {"a", "b"},
     {x for x in R if x * x == 4} == {x for x in R if x != 0 and x**3 - 4 * x == 0},
     {x for x in R if 2 * x + 7 == 11} == {2},
     {x for x in R if x < 0 and x >= 0} == set()), (True,) * 4)
# P3 (FME 21): diagrama D ⊂ C ⊂ B ⊂ A — conferido por leitura
chk("u2:fme22 (FME 22) n(𝒫({a,b,c,d}))", len(partes("abcd")), 16)
a_, b_ = "a", "b"
v20 = [0 in {0, 1, 2, 3, 4}, fs({a_}) in {a_, b_}, V in {0}, 0 in V, sub({a_}, V),
       a_ in {a_, fs({a_})}, sub({a_}, {a_, fs({a_})}), sub(V, {V, fs({a_})}), V in {V, fs({a_})}, fs({a_, b_}) in {a_, b_, "c", "d"}]
chk("u2:fme20 (FME 20) a–j", "".join("V" if v else "F" for v in v20), "VFFFFVVVVF")
E = {a_, fs({a_})}
v47 = {"a": a_ in E, "b": fs({a_}) in E, "c": False,  # 'a ⊂ E': a não é conjunto (urelemento, convenção do FME)
       "d": sub({a_}, E), "e": V in E, "f": sub(V, E)}
chk("u2:fme47 (FME 47) verdadeiras", sorted(k for k, v in v47.items() if v), ["a", "b", "d", "f"])
chk("u2:fme35 (FME 35) nº de X com {1,2} ⊂ X ⊂ {1,2,3,4}", sum(1 for X in partes({1, 2, 3, 4}) if {1, 2} <= X), 4)
chk("u2:multiplos4 múltiplos de 4 ⊂ pares; pares ⊄ múltiplos de 4 (testemunha 2)",
    (all(x % 2 == 0 for x in Z if x % 4 == 0), 2 % 2 == 0 and 2 % 4 != 0), (True, True))
# P9 exemplos: (a) A⊄B e B⊂A; (b) A⊄B e B⊄A; (c) A⊂B e B⊂A
ex9 = {"a": ({1, 2}, {1}), "b": ({1}, {2}), "c": ({1}, {1})}
chk("u2:exemplos exemplos-modelo", (not sub(*ex9["a"]) and sub(ex9["a"][1], ex9["a"][0]),
                           not sub(*ex9["b"]) and not sub(ex9["b"][1], ex9["b"][0]),
                           sub(*ex9["c"]) and sub(ex9["c"][1], ex9["c"][0]) and ex9["c"][0] == ex9["c"][1]), (True, True, True))
chk("u2:exemplos (c) obriga A = B (todos os pares em 𝒫({0,1,2}))",
    all(X == Y for X in partes(range(3)) for Y in partes(range(3)) if X <= Y and Y <= X), True)
chk("u2:contar n(𝒫(A)) = 64 → n(A); subconjuntos de 5 elementos sem ∅ e sem o todo",
    ([n for n in range(20) if 2**n == 64], len(partes(range(5))) - 2), ([6], 30))
D12 = {d for d in range(1, 13) if 12 % d == 0}
chk("u2:divisores (integradora) subconjuntos dos divisores de 12 que contêm 1 e 12", sum(1 for X in partes(D12) if {1, 12} <= X), 16)
# P12 (ITA, vest. 45): maior cadeia em 𝒫(U) tem n + 1 elementos
def cadeia_max(n):
    P = sorted(partes(range(n)), key=len); best = 0
    def ext(ch, rest):
        nonlocal best
        best = max(best, len(ch))
        for i, X in enumerate(rest):
            if all(X <= Y or Y <= X for Y in ch):
                ext(ch + [X], rest[i + 1:])
    ext([], P); return best
chk("u2:cadeias (ITA 45) cadeia máxima = n + 1 (n = 1..4)", [cadeia_max(n) for n in range(1, 5)], [2, 3, 4, 5])
alts = {"a": lambda n: 2**(n-1), "b": lambda n: n//2 if n % 2 == 0 else (n+1)//2, "c": lambda n: n+1, "d": lambda n: 2**(n-1)+1, "e": lambda n: 2**n-1}
chk("u2:cadeias só a alternativa c vale para n = 1..4", [k for k, f in alts.items() if all(f(n) == cadeia_max(n) for n in range(1, 5))], ["c"])
chk("u2:paridade subconjuntos de {1..n} com nº par de elementos = 2^(n−1) (n = 1..8)",
    [sum(1 for X in partes(range(n)) if len(X) % 2 == 0) for n in range(1, 9)], [2**(n - 1) for n in range(1, 9)])
P0 = partes(V); P1 = partes(P0); P2 = partes(P1)
chk("u2:vazios3 𝒫(∅), 𝒫(𝒫(∅)), 𝒫(𝒫(𝒫(∅))): tamanhos", (len(P0), len(P1), len(P2)), (1, 2, 4))
chk("u2:vazios3 elementos de 𝒫(𝒫(𝒫(∅)))", P2, {V, fs({V}), fs({fs({V})}), fs({V, fs({V})})})

# ---- não verificável por programa -----------------------------------------------
# ex:u2:vazio (unicidade de ∅) e u2:paridade (argumento de pareamento): provas — conferidas por leitura.
# u2:fme21 (diagrama) — conferido por leitura.

print(f"\n{ok} OK, {falhas} falha(s)")
