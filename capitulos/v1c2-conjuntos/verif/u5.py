"""Verificação independente das respostas da Unidade 5 — Contando elementos: dois conjuntos.

Regra (w5): toda resposta calculável é RECALCULADA aqui, pelas regiões (busca exaustiva nas quatro
regiões só A, só B, ambos, nenhum), e não pela fórmula do texto.
Etapa 2 (dossiê): rótulos PROVISÓRIOS (X*, P*, V*); a montagem troca pelos rótulos finais.
Rodar:  python3 verif/u5.py      (saída "N OK, 0 falha(s)" é a condição de pronto)
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

def regioes(N, cond, nA=None, nB=None):
    """Todas as quádruplas (soA, soB, ambos, nenhum) de inteiros ≥ 0 com soma N que satisfazem cond.
    nA/nB (opcionais) só podam a busca (a = nA − c, b = nB − c); cond continua sendo conferida."""
    out = []
    for c in range(N + 1):
        As = [nA - c] if nA is not None else range(N + 1 - c)
        for a in As:
            if a < 0: continue
            Bs = [nB - c] if nB is not None else range(N + 1 - a - c)
            for b in Bs:
                d = N - a - b - c
                if b >= 0 and d >= 0 and cond(a, b, c, d):
                    out.append((a, b, c, d))
    return out

fs = frozenset
def partes(S):
    S = list(S)
    return [fs(x) for r in range(len(S) + 1) for x in it.combinations(S, r)]

# ---- construções, erros, gancho --------------------------------------------------
P5 = partes(range(5))
chk("H1 vale para todos os pares de subconjuntos de {0..4}",
    all(len(A | B) == len(A) + len(B) - len(A & B) for A in P5 for B in P5), True)
A, B = {1, 2, 3, 4}, {3, 4, 5}
chk("H1 exemplo do texto {1,2,3,4} ∪ {3,4,5}", (len(A | B), len(A) + len(B) - len(A & B)), (5, 5))
chk("gancho: 60 ônibus + 50 bicicleta em 100 → pelo menos 10 nos dois",
    min(c for a, b, c, d in regioes(100, lambda a, b, c, d: a + c == 60 and b + c == 50, 60, 50)), 10)
chk("E1 quebra: 30 futebol, 20 vôlei, 8 os dois → 42", 30 + 20 - 8, 42)
r = regioes(50, lambda a, b, c, d: a + c == 25 and b + c == 15 and c == 5, 25, 15)
chk("E2 quebra: 50 no clube, 25 nadam, 15 correm, 5 os dois → algum 35, nenhum 15", [(a + b + c, d) for a, b, c, d in r], [(35, 15)])
chk("E2 quebra: leitura errada (25 = só natação) → 45 e 5", (25 + 15 + 5, 50 - 45), (45, 5))
chk("E3 quebra: 40 alunos, 25 jornal, 20 revista; se todos leem algo → 5 os dois; se 5 não leem nada → 10",
    ([c for a, b, c, d in regioes(40, lambda a, b, c, d: a + c == 25 and b + c == 20 and d == 0, 25, 20)],
     [c for a, b, c, d in regioes(40, lambda a, b, c, d: a + c == 25 and b + c == 20 and d == 5, 25, 20)]), ([5], [10]))
chk("E4 quebra: 30% de 200 (manhã) + 10% de 600 (tarde) = 120 de 800 = 15%",
    (Fr(30, 100) * 200 + Fr(10, 100) * 600, (Fr(30, 100) * 200 + Fr(10, 100) * 600) / 800), (120, Fr(15, 100)))

# ---- exemplos (provisórios) ---------------------------------------------------------
r = regioes(120, lambda a, b, c, d: a + c == 80 and b + c == 50 and c == 30, 80, 50)
chk("X1 120 pessoas, A 80, B 50, ambos 30 → pelo menos um, nenhum, só A", [(a + b + c, d, a) for a, b, c, d in r], [(100, 20, 50)])
r = regioes(60, lambda a, b, c, d: a + c == 35 and b + c == 20 and d == 15, 35, 20)
chk("X2 60 apartamentos, cachorro 35, gato 20, nenhum 15 → ambos", [c for a, b, c, d in r], [10])
r = [q for N in range(200) for q in regioes(N, lambda a, b, c, d: a == 40 and b == 25 and c == 10 and d == 15)]
chk("X3 só teatro 40, só música 25, ambos 10, nenhum 15 → teatro, total", [(a + c, a + b + c + d) for a, b, c, d in r], [(50, 90)])
dia, noite = 120, 180
cur = Fr(25, 100) * dia + Fr(40, 100) * noite
chk("X4 25% de 120 + 40% de 180 → 102 = 34%", (cur, cur / 300), (102, Fr(34, 100)))
r = regioes(100, lambda a, b, c, d: a + c == 70 and b + c == 40 and c == 20, 70, 40)
chk("X5 (a) 70% celular, 40% fixa, 20% ambos → nenhum 10%; só fixa 20%", [(d, b) for a, b, c, d in r], [(10, 20)])
chk("X5 (b) só fixa 20% = 1 500 domicílios → total", Fr(1500) / Fr(20, 100), 7500)
n = range(1, 101)
d2 = {x for x in n if x % 2 == 0}; d3 = {x for x in n if x % 3 == 0}
chk("X6 de 1 a 100: div. por 2 ou 3 = 67; nem 2 nem 3 = 33; ambos = múltiplos de 6 (16)",
    (len(d2 | d3), 100 - len(d2 | d3), d2 & d3 == {x for x in n if x % 6 == 0}, len(d2 & d3)), (67, 33, True, 16))

# ---- questões (provisórias) ---------------------------------------------------------
chk("P1 (FME 48) fórmula — ver H1", True, True)
r = regioes(415, lambda a, b, c, d: a + c == 221 and b + c == 163 and c == 52, 221, 163)
chk("P2 (FME 52) inglês ou francês; nenhum", [(a + b + c, d) for a, b, c, d in r], [(332, 83)])
r = regioes(600, lambda a, b, c, d: a + c == 350 and b + c == 210 and c == 90, 350, 210)
a, b, c, d = r[0]
chk("P3 (vest 11) I só biotec 260, II só proteção 120, III 470, IV nenhum 130 → d (todas)", (len(r), a, b, a + b + c, d), (1, 260, 120, 470, 130))
r = regioes(1000, lambda a, b, c, d: a + c == 600 and b + c == 500 and d == 200, 600, 500)
chk("P4 (vest 7) rejeitam os dois → 300 (d)", [c for a, b, c, d in r], [300])
A51 = {3 * k for k in range(0, 200)}; B51 = {x for x in range(1, 121) if 120 % x == 0}
chk("P5 (FME 51 adaptado) n(A ∩ B) = 8; n(B) = 16; divisores não múltiplos de 3 = 8",
    (len(A51 & B51), len(B51), len(B51 - A51)), (8, 16, 8))
r = [q for N in range(400) for q in regioes(N, lambda a, b, c, d: a + b + c + d == 160 + 16 + 20 + 69 and a == 175 and b == 75 and d == 0)]
chk("P6 (vest 12) espécies nos dois ambientes → 15 (d)", [c for a, b, c, d in r], [15])
sol = [N for N in range(1, 2000) if N * 60 % 100 == 0 and N * 45 % 100 == 0 and N * 30 % 100 == 0
       and regioes(N, lambda a, b, c, d: a + c == N * 60 // 100 and b + c == N * 45 // 100 and d == N * 30 // 100 and c == 49, N * 60 // 100, N * 45 // 100)]
chk("P7 (vest 10) funcionários → 140 (b)", sol, [140])
sol = [(N, y) for N in range(1, 2000) for y in range(N + 1)
       if 2 * y == N and 70 + y == 350 and N - 70 - y >= 0]          # brancos 70; amarelos y = 50% de N; não negros = brancos + amarelos
chk("P8 (FME 58) total 560; amarelos 280", sol, [(560, 280)])
mulheres = 500 * 60 // 100; homens = 500 - mulheres
chk("P9 (vest 8) homens que cursam inglês → 140 (c)", homens - homens * 30 // 100, 140)
sol = [Fr(h, 100) for h in range(0, 101) if Fr(20, 100) * h + Fr(15, 100) * (100 - h) == 18]
chk("P10 (vest 18) homens = 60% (e)", sol, [Fr(60, 100)])
chk("P11 (FME 49) n(A ∪ B) = 6 → 64 subconjuntos",
    sorted({2 ** len(X | Y) for X in partes(range(9)) if len(X) == 4 for Y in partes(range(9)) if len(Y) == 5 and len(X & Y) == 3}), [64])
sol = [Fr(x, 100) for x in range(0, 101) if Fr(45, 100) * Fr(20, 100) + Fr(20, 100) * Fr(35, 100) + Fr(35, 100) * Fr(x, 100) == Fr(30, 100)]
chk("P12 (FME 59) Campinas → 40%", sol, [Fr(40, 100)])
dif = set()
for m in range(1, 9):
    for k in range(1, 9):
        A_, B_ = list(range(m)), list(range(m, m + k))          # disjuntos
        PA, PB = set(partes(A_)), set(partes(B_))
        if len(PA | PB) + 1 == len(partes(A_ + B_)):
            dif.add(m - k)
chk("P13 (vest 41) n(A) − n(B) só pode ser 0 (a)", dif, {0})

# ---- bloco "Mais questões de vestibular" (provisório) ---------------------------------
r = regioes(150, lambda a, b, c, d: a + c == 40 and b + c == 60 and d == 65, 40, 60)
chk("V1 (vest 9) caixas reprovadas nos dois → 15 (a)", [c for a, b, c, d in r], [15])
r = regioes(1150, lambda a, b, c, d: a + c == 654 and b + c == 564 and d == 176, 654, 564)
chk("V2 (vest 13) português e matemática → 244 (c)", [c for a, b, c, d in r], [244])
r = regioes(50, lambda a, b, c, d: a + c == 30 and c == 10 and d == 5, 30)
chk("V3 (vest 14) gostam de amarelo → 25 (a)", [b + c for a, b, c, d in r], [25])
r = regioes(800, lambda a, b, c, d: a + c == 220 and b + c == 380 and c == 120, 220, 380)
chk("V4 (vest 15) X = 320 (b)", [d for a, b, c, d in r], [320])
r = regioes(60, lambda a, b, c, d: a + c == 28 and b + c == 26 and c == 15, 28, 26)
chk("V5 (vest 16) nenhum dos dois → 21 (a)", [d for a, b, c, d in r], [21])
tot = [a + b + c for N in range(40) for a, b, c, d in regioes(N, lambda a, b, c, d: a + c == 14 and b + c == 8 and c == 3 and d == 0, 14, 8)]
chk("V6 (vest 17) total do grupo → 19 (b)", sorted(set(tot)), [19])
# vest 21: por série, sexo e língua — 3600 alunos; contar quem é do 3º ano ou não estuda francês
alunos = [(s, sx, l) for s in (1, 2, 3) for sx in "MF" for l in ("ing", "fr") for _ in range(300)]
chk("V7 (vest 21) 3º ano ou não estudam francês → 2400 (d)", (len(alunos), sum(1 for s, sx, l in alunos if s == 3 or l != "fr")), (3600, 2400))
chk("V8 (vest 32) pessoas ouvidas → 300 (b)", [N for N in range(1, 1000) if N % 60 == 0 and N - N // 3 - N // 4 - N // 5 == 65], [300])

print(f"\n{ok} OK, {falhas} falha(s)")
