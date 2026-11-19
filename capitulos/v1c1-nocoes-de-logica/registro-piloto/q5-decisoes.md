# q4 — Decisões: o que mudar e onde · Cap. I — Noções de lógica

Piloto · FME vol. 1, Cap. I · 2026-11-17
Depende de: `q3-revisao.md` (divergências D1–D12) · Altera: `q2-estrutura.md` (emendas *(q4/Dn)*), `matriz.yaml` (versão q4), `scripts/matriz.py` (regra R6) · Alimenta: q5

**Aprovação:** o usuário aprovou as recomendações do q3 para D1–D12 (2026-11-17).
**Invariante (p1):** a didática não foi alterada. Toda mudança cai sobre o **plano** (q2/matriz) ou sobre o **material** (o que entra e de onde vem).

---

## 1. Registro das decisões

Formato: o que muda · onde · se é mudança de **plano** ou de **material** · motivo.

### D1 — Exemplos: trocar autorais e de concurso por vestibulares onde houver material
- **Muda (plano):**

  | Exemplo | Antes | Agora | Cobre |
  |---|---|---|---|
  | 4.2 | autoral | **FATEC 1º sem/2013, q13** (contrapositiva); p → q ⇔ ~p ∨ q vai para o comentário | 4-H3, U1, U2, E3 |
  | 6.1 | concurso VUNESP/PC-SP 2018 | **FATEC 1º sem/2014** (negar ~M ∨ J) | 6-H1, U1, E2 |
  | 6.2 | concurso FGV/TJ-SC 2018 | **FATEC 1º sem/2019, q11** (negar "todas as vagas…") | 6-H4, U2, E1, E4 |
  | 6.3 | autoral | autoral + **FATEC 2011, prova 1** (negar −3 < x ≤ 2), marcado como integrador | 6-H2, U1, U3, E3, E5 |

- **Muda (material):** os 4 itens saem do banco de questões (e4). As 2 questões de concurso que eram exemplo voltam para o banco da Unid. 6.
- **Motivo:** a didática manda priorizar problemas históricos e de vestibular nos exemplos, e a regra e1 só admite concurso em exemplo quando não há vestibular equivalente. Havia.
- **Efeito:** autorais puros caem de 18 para **16 de 32**; nenhum exemplo de concurso.

### D2 — Questões integradoras
- **Muda (plano):** meta de **≥ 1 questão integradora por unidade** (`questoes_meta.integradoras: 1`). Nova regra **R6** no `matriz.py`; macro `\integradora`; spec no q2 §2.7.
- **Conflito resolvido:** o q3 citava a FATEC 2011 como integradora candidata, mas o D1 a levou para o exemplo 6.3. Ela fica no exemplo (o exemplo pode ser integrador), e a questão integradora da Unid. 6 será outra, provavelmente autoral. **Exemplo integrador não conta para a R6.**
- **Motivo:** a didática prevê questões que envolvem outros assuntos, e o plano não usava isso.

### D3 — "Para lembrar" ao fim de "De onde vem?"
- **Muda (plano):** spec do q2 §2.2, item 6: caixa com a ideia em 1 frase + a construção em ≤ 3 passos. Ambiente `paralembrar`.
- **Motivo:** a didática define o objetivo da seção (facilitar a memorização pelo significado), e o plano não dizia como cumpri-lo.

### D4 — Caixa "O mínimo que você precisa"
- **Muda (plano):** prefácio das **Unidades 1 e 5** (q2 §2.1, item 4). Ambiente `minimo`.
  - Unid. 1: conjuntos numéricos, divisibilidade, mdc/mmc, potências e raízes.
  - Unid. 5: universo, ∈/∉, intervalos, conjunto-verdade.
- **Motivo:** p3 (autocontido). Os exercícios do FME pressupõem esses itens, e o capítulo de Conjuntos vem depois.

### D5 — Novo ID `2-O3`: o mito do *vel × aut*
- **Muda (plano):** ID novo na matriz, coberto pelo exemplo 2.2. A frase de notação em "de onde vem" (q2 §4, Unid. 2) foi corrigida: o ∨ vem de Russell/Whitehead (c. 1903), não do latim.
- **Motivo:** corrige um erro difundido em livros e é um bom exemplo de etiqueta `[anedota]` × `[documentado]` em ação.

### D6 — OBMEP 2005 (V5) pelo texto original
- **Muda (material):** o exemplo 2.4 usa o enunciado e a ordem de alternativas da prova; uma nota registra que o FME traz versão adaptada.
- **Motivo:** w4 — fonte primária acima da adaptação.

### D7 — Texto integral das questões só resumidas
- **Muda (material):** no q5, buscar o texto das FATEC 2011/2014/2017 e da PUC-GO 2010 nas provas oficiais (o CPS publica as da FATEC). **Fallback:** `[adaptada de FATEC 2014]`, com redação reconstruída e resposta verificada por script.
- **Motivo:** w4 sem bloquear a produção.

### D8 — `6-E2` generalizado
- **Muda (plano):** o erro passa a ser "manter o conectivo ao negar (∧ ou ∨)".
- **Motivo:** cobre a FATEC 2014 (negar um **ou**) sem criar ID redundante.

### D9 — UF-RS sem ano
- **Muda (material):** etiqueta `[UF-RS — via FME]` no exemplo 5.5.
- **Motivo:** a fonte verificável é o próprio livro-base.

### D10 / D11 — Déficit das Unidades 5 e 2
- **Muda (material):** completar com autorais + FME ex. 8 subdividido (Unid. 5); busca rápida no q5, sem bloquear.

### D12 — Redação do gancho da Unid. 3
- **Muda (plano):** "cerca de 1 em cada 10 pessoas acerta, ou menos" (Wason 1968; Wason & Shapiro 1971).

---

## 2. O que **não** mudou (e por quê)
- **A didática** (p1).
- **As metas de questões por nível** (64 no total): o déficit é de produção, não de plano.
- **Os critérios de nível** (w2).
- **O exemplo 2.3 (contagem de linhas):** o caso Crisipo × Hiparco continua só como observação (`2-O1`). Os números de Schröder estão além do escopo do capítulo.

---

## 3. Estado depois do q4 (entrada do q5)

`matriz.py` (versão q4): **sem falhas**. 85 IDs, 32 exemplos.

| Unid. | Pool (N1/N2/N3) | Faltam (N1/N2/N3) | U/E ainda sem questão (alvo das autorais) | Integradora |
|---|---|---|---|---|
| 1 | 2/2/0 | 2/2/2 → **6** | — | falta 1 |
| 2 | 1/1/0 | 3/3/2 → **8** | 2-U3, U4, U5, E1, E3, E4 | falta 1 |
| 3 | 3/1/2 | 1/4/1 → **6** | 3-U1, U4, U5, E2, E3, E4 | falta 1 |
| 4 | 1/2/0 | 2/2/3 → **7** | 4-U2, U3, U4, E1, E2, E3, E4 | falta 1 |
| 5 | 1/0/0 | 3/4/2 → **9** | 5-U3, U4, E2, E3, E4 | falta 1 |
| 6 | 3/2/0 | 1/3/3 → **7** | 6-U4, U5, E4 | falta 1 |
| **Total** | **21** | **43** | | **6** |

**Regra para as autorais do q5:** cada questão nova mira primeiro um U/E sem questão e um nível em falta. As 6 integradoras contam dentro dessas 43.

---

## 4. Ordem de produção proposta para o q5
1. Template LaTeX (`estilo.sty`, `main.tex`) + resolver o idioma (babel português ausente).
2. **Unidade 1 completa** como lote-piloto. Compilar, validar (`matriz.py --tex`) e mostrar ao usuário antes de seguir. Calibra tom, extensão e layout.
3. Unidades 2–6, uma por vez, com verificação de gabarito por script em cada uma.
4. Abertura geral por último (depende do que as unidades efetivamente contam).
