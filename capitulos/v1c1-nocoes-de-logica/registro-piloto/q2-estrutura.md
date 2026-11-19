> **Atenção (2026-11-18):** este plano segue a didática v2. A refação do Cap. I na v3 começa por atualizá-lo conforme [`00-didatica-v3.md`](00-didatica-v3.md) §7.

# q2 — Plano de estruturação do material · Cap. I — Noções de lógica

Piloto · FME vol. 1, Cap. I · 2026-11-17
Depende de: `00-decisoes.md`, `q1-pesquisa.md` · Fonte de verdade da cobertura: `matriz.yaml` · Validador: `scripts/matriz.py`

---

## 0. Decisões tomadas neste quesito

| # | Decisão | Origem |
|---|---|---|
| e1 | **Questões de concurso entram como fonte complementar**, com etiqueta `[concurso — BANCA/ÓRGÃO ANO]`. Nos exemplos, só quando não houver vestibular ou problema histórico equivalente. | proposta do q1 §6.1 — **confirmada pelo usuário em 2026-11-17**. |
| e2 | Questões da OBMEP recebem a etiqueta `[OBMEP]`, não "vestibular". | q1 §6.2 |
| e3 | A negação do ↔, que o livro não cobre, entra na Unidade 6 como observação (`6-O1`), com exemplo. | q1 §1.3 |
| e4 | Uma questão usada como **exemplo** sai do banco de **questões**, para não haver repetição. | este quesito |
| e5 | Um exercício do FME com subitens (a–h) conta como **uma** questão, com subitens. | este quesito |
| e6 | Os IDs aparecem no material, discretos: o estudante vê, por exemplo, que o exemplo 3.6 trabalha o erro 3-E2. Isso ajuda a revisar e liga cada exemplo à teoria. | este quesito |
| e7 | Fim do livro: **lista de fontes** (fora das unidades). Não é uma seção da didática; é material de apoio exigido por p3 e w4. | este quesito |

### 0.1 Correção de nomenclatura em relação ao q1
No q1, "U1…U6" designava tanto as unidades quanto os candidatos de uso (`U1.a`). A partir daqui:
- **Unidades:** "Unidade 1" … "Unidade 6".
- **IDs:** `n-Xk`, com n = unidade e X = tipo:
  - **H** — construção ou resultado de "de onde vem"
  - **U** — contexto de uso
  - **E** — erro comum
  - **O** — observação

  Exemplo: `3-E2` = Unidade 3, erro 2.

Fatos históricos narrativos (datas, nomes) **não** são IDs. Só entram na matriz as **construções** que o estudante precisa saber refazer (H), porque são essas que os exemplos devem exercitar.

---

## 1. Arquitetura do documento

```
Capítulo I — Noções de lógica
├── Abertura geral do capítulo
│   ├── Por que começar por lógica
│   ├── Linha do tempo (Aristóteles → Wason)
│   ├── Mapa das unidades (o que cada uma resolve e como se encadeiam)
│   ├── Tabela de notação (símbolo · leitura · quem introduziu · quando)
│   └── Como usar este material (níveis, etiquetas, IDs, respostas)
├── Unidade 1 — Proposição e negação            ┐
├── Unidade 2 — Conectivos ∧ e ∨                │ cada uma com as 8 seções:
├── Unidade 3 — Condicional e bicondicional     │ 1 Prefácio · 2 De onde vem? · 3 Onde é usado?
├── Unidade 4 — Tautologia, contradição,        │ 4 Erros comuns · 5 Observações · 6 Exemplos
│               implicação e equivalência       │ 7 Questões · 8 Respostas
├── Unidade 5 — Sentenças abertas e quantif.    │
├── Unidade 6 — Negação de proposições          ┘
└── Fontes
```

**Arquivos (estado em disco, d2):**
```
cap1/
├── main.tex              preâmbulo + \input de tudo
├── estilo.sty            ambientes e macros (§5)
├── abertura.tex
├── unidade1.tex … unidade6.tex
├── fontes.tex
└── build/                saída do latexmk
```
Uma unidade por arquivo permite produzir, revisar e recompilar uma unidade de cada vez no q5 e no q6.

---

## 2. Especificação de cada seção (vale para todas as unidades)

Extensão em páginas A4, corpo 11 pt; serve de referência, não de limite rígido.

### 2.1 Prefácio · ~½ página
- **Objetivo:** apresentar o propósito da unidade e despertar curiosidade. **Não faz parte da narrativa**: não ensina nem antecipa a resposta.
- **Obrigatório:**
  1. uma pergunta-gancho;
  2. o que o estudante vai conseguir fazer ao final (2–3 itens);
  3. **pré-requisitos** (w7), com remissão à unidade ou ao assunto.
  4. *(q4/D4)* Nas **Unidades 1 e 5**, uma caixa **"O mínimo que você precisa"** (≤ ½ página), para manter o p3:
     - Unid. 1: ℕ, ℤ, ℚ, ℝ; divisibilidade (a | b); mdc e mmc; potências e raízes — o que os exercícios do FME usam.
     - Unid. 5: conjunto universo; ∈ e ∉; intervalos; conjunto-verdade. O Cap. II (Conjuntos) vem depois no livro.
- **Formato:** caixa de abertura, visualmente distinta do corpo.
- **Proibido:** definições formais e resolução do gancho (a resposta aparece em "de onde vem").

### 2.2 De onde vem? · 2–3 páginas
- **Objetivo:** dominar o significado — quem, quando, por quê, em que contexto — e **construir o conceito do zero**.
- **Obrigatório, nesta ordem:**
  1. **Contexto e problema:** que pergunta as pessoas tentavam responder.
  2. **Personagens e debate:** ≥ 2 marcos `[documentado]` (do q1).
  3. **Construção:** da intuição à definição, à tabela e à propriedade. Cada construção que é ID `H` é marcada.
  4. **Notação:** de onde vem o símbolo.
  5. **Fecho:** a resposta à pergunta-gancho do prefácio.
  6. *(q4/D3)* **"Para lembrar"** — caixa final: a ideia central em **1 frase** + a construção em **≤ 3 passos**. É o que torna operacional o objetivo de facilitar a memorização pelo significado.
- **Etiquetas:** fato histórico com `[anedota]` aparece como tal, ou não aparece; `[a verificar]` não entra sem passar no q3.
- **Formato:** narrativa em prosa, com caixas de **definição** e **construção**. A linha do tempo da unidade é opcional (a geral está na abertura).

### 2.3 Onde é usado? · 1½–2 páginas (w6)
- **Parte A — texto analítico (quase um estudo).** Como o conceito costuma aparecer: em que provas (vestibular, OBMEP, concurso), em que formatos (classificar, negar, traduzir, deduzir), com que frequência relativa, quais as armadilhas típicas do enunciado. Cada contexto é um ID `U`, citado no texto.
- **Parte B — tabela de gatilhos:**

| Sinal no enunciado | Ferramenta | Raciocínio | ID |
|---|---|---|---|

- **Mínimo:** ≥ 3 contextos e ≥ 4 linhas de gatilho por unidade.
- **Regra de honestidade:** afirmações sobre frequência ("aparece muito em…") só com base no q1/q3; caso contrário, são formuladas como observação qualitativa.

### 2.4 Erros comuns · 1–1½ página
- **Formato fixo por erro (ID `E`):**
  - **O erro** — um exemplo concreto do raciocínio errado.
  - **Por que acontece** — o mecanismo: linguagem natural, intuição causal, analogia indevida…
  - **Como evitar** — um teste ou procedimento verificável, não um "preste atenção".
  - **Exemplo onde aparece** — remissão ao exemplo e às questões que o exercitam.

### 2.5 Observações · ½–1 página
- Itens `O` curtos e independentes: paradoxos, notações alternativas, erros do próprio livro, ligações com outros capítulos.

### 2.6 Exemplos · 3–4 páginas
- **Formato de cada exemplo:**
  - cabeçalho: `Exemplo n.k · Nível N · [procedência] · \cobre{IDs}`
  - enunciado (fiel à fonte, ou marcado `[adaptado de …]`)
  - **plano** (1–2 linhas: o que reconhecer e qual ferramenta usar — liga com a tabela de gatilhos)
  - resolução passo a passo
  - **comentário** (por que funciona; que erro o estudante evitou; variação possível)
- **Regras:** ≥ 1 por nível; o conjunto cobre todos os IDs da unidade (R1, R2); ordem crescente de nível.

### 2.7 Questões · ~2 páginas
- Numeração **reinicia em cada unidade** (1, 2, 3…).
- Cada questão traz: nível `[N1]`/`[N2]`/`[N3]` + procedência + IDs (`\cobre`).
- Ordem por nível, e dentro do nível pela sequência dos IDs.
- *(q4/D2)* **≥ 1 questão integradora por unidade:** ela envolve outro conteúdo (inequações, divisibilidade, potências, intervalos) além da lógica. Marcada com `\integradora` e com `integradora: true` na matriz (regra R6).
- **Metas por unidade** (`matriz.yaml → questoes_meta`):

| Unidade | N1 | N2 | N3 | Total |
|---|---|---|---|---|
| 1 | 4 | 4 | 2 | 10 |
| 2 | 4 | 4 | 2 | 10 |
| 3 | 4 | 5 | 3 | 12 |
| 4 | 3 | 4 | 3 | 10 |
| 5 | 4 | 4 | 2 | 10 |
| 6 | 4 | 5 | 3 | 12 |
| **Total** | 23 | 26 | 15 | **64** |

### 2.8 Respostas · ¼–½ página
- **Só a resposta final**, sem caminho. Formatos:
  - múltipla escolha: `[ 3. (c) ]`
  - discursiva: `[ 5. 5√3 ]`
  - com subitens: `[ 1. a) V  b) F  c) V ]`
  - texto curto (negações): `[ 9. g) (∃x)(x > 2 ∧ 3ˣ ≤ 3²) ]`
- Toda resposta passa por verificação independente (w5), com registro no q6.

---

## 3. Abertura geral do capítulo · 3–4 páginas
1. **Por que lógica primeiro:** a matemática é feita de afirmações (proposições) e de passagens entre elas (implicações). O capítulo dá a gramática dessas duas coisas.
2. **Linha do tempo:** os marcos `[documentado]` do q1 (§3, abertura).
3. **Mapa das unidades:** um diagrama de dependência (1 → 2 → 3 → 4; 1 → 5; 2, 3, 5 → 6) e uma frase por unidade.
4. **Tabela de notação:** ~, ∧, ∨, →, ↔, ⇒, ⇔, ∀, ∃, ∃| — leitura, autor e ano (do q1).
5. **Como usar:** significado de N1/N2/N3, das etiquetas de procedência e dos IDs; como as respostas funcionam.

---

## 4. Plano por unidade

Detalhe completo (IDs, exemplos e cobertura) em `matriz.yaml`. Abaixo, o que a matriz não captura: o gancho, o roteiro de "de onde vem" e os temas do texto analítico.

### Unidade 1 — Proposição e negação
- **Gancho:** "Uma prece é uma frase. Ela é verdadeira ou falsa?"
- **De onde vem — roteiro:** Aristóteles separa frases que afirmam/negam das demais → os estoicos e o "assertível" cujo valor muda ("é dia") → os princípios de não contradição e do terceiro excluído → as 3 características (**1-H1**) → a negação como operação e a tabela de ~p (**1-H2**) → Peano (~) e Heyting (¬).
- **Texto analítico:** questões de "o que é proposição" testam definição e não cálculo; a negação de relações é o tijolo de todas as unidades seguintes; puzzles de veracidade (OBMEP) treinam o raciocínio de casos.
- **Exemplos:** 1.1 N1 · 1.2 N1 · 1.3 N2 · 1.4 N2 · 1.5 N3 (histórico).

### Unidade 2 — Conectivos ∧ e ∨
- **Gancho:** "Café ou chá?" — e se a pessoa quiser os dois?
- **De onde vem:** Crisipo e os conectivos → os estoicos preferiam o "ou" exclusivo → Boole também; Jevons (1864) torna o "ou" inclusivo, e é o que fica → construção das tabelas (**2-H1, 2-H2**) → contagem de linhas 2ⁿ (**2-H3**) → notação: ∨ de Russell/Whitehead (c. 1903 — **não** do latim *vel*, ver `2-O3`); ∧ de Heyting (1930).
- **Texto analítico:** classificar compostas; restrições simultâneas; o "apenas uma é verdadeira" das olimpíadas; circuitos e código; a ponte com conjuntos (Cap. II).
- **Exemplos:** 2.1 N1 · 2.2 N1 (cobre também **2-O3**, o mito do *vel*) · 2.3 N2 · 2.4 N2 (OBMEP 2005, texto original) · 2.5 N3 (Shannon).

### Unidade 3 — Condicional e bicondicional
- **Gancho:** as 4 cartas de Wason — "cerca de 1 em cada 10 pessoas acerta, ou menos. Tente." *(q4/D12)*
- **De onde vem:** Fílon × Diodoro e os corvos de Calímaco → o critério de Fílon (**3-H1**) → a construção pela "promessa quebrada" → a contrapositiva (**3-H3**) → o ↔ (**3-H2**) → notação (Hilbert →, Becker ↔) → fecho: a solução das cartas fica para o exemplo 3.6, e o fecho só explica o que torna o problema difícil.
- **Texto analítico:** enunciados de teoremas (suficiente/necessária); regras em problemas de olimpíada; "considerando falsa a afirmação…" em concursos; contrapositiva como equivalente.
- **Exemplos:** 3.1 N1 · 3.2 N1 · 3.3 N2 · 3.4 N2 · 3.5 N2 (OBMEP) · 3.6 N3 (Wason).

### Unidade 4 — Tautologia, contradição, implicação e equivalência
- **Gancho:** "'Ou chove ou não chove' é sempre verdade — então não informa nada. Para que serve?"
- **De onde vem:** as tabelas como método de decisão (Peirce 1883 → Wittgenstein/Post 1921) → tautologia/contradição no Tractatus (**4-H1**) → do conectivo à relação: ⇒ e ⇔ (**4-H2, 4-H3**) → as leis de Boole (**4-H4**) e Shannon.
- **Texto analítico:** "é equivalente a" em provas; demonstrações (teorema e recíproco); simplificação; validade de argumentos.
- **Exemplos:** 4.1 N1 · 4.2 N1 (**FATEC 2013**) · 4.3 N2 · 4.4 N2 · 4.5 N3 (Carroll).

### Unidade 5 — Sentenças abertas e quantificadores
- **Gancho:** "'x + 1 = 7' não é verdadeira nem falsa. Como torná-la uma afirmação sem escolher x?"
- **De onde vem:** Aristóteles e o "todo/algum" como termos → Frege (1879) e Peirce (1885), de forma independente → ∀ como "e" generalizado e ∃ como "ou" generalizado (**5-H2**) → sentença aberta e as duas saídas (**5-H1**) → ∃| (**5-H3**) → notação (Peano ∃, Gentzen ∀).
- **Texto analítico:** identidades × equações; domínio; definições matemáticas; "no máximo/pelo menos".
- **Exemplos:** 5.1 N1 · 5.2 N1 · 5.3 N2 · 5.4 N2 (Euler 1772) · 5.5 N3 (UF-RS, via FME) · 5.6 N3.

### Unidade 6 — Negação de proposições
- **Gancho:** "Qual é a negação de 'todo político mente'? (Não é 'nenhum político mente'.)"
- **De onde vem:** o quadrado das oposições (**6-H4**) → De Morgan e seus antecessores medievais → as leis pela tabela (**6-H1**) → negação do condicional (**6-H2**) → negação de quantificadores como De Morgan generalizado (**6-H3**).
- **Texto analítico:** "qual a negação de…" é o formato mais frequente em concursos (afirmação a confirmar no q3); contraexemplo e absurdo em demonstrações; código e buscas.
- **Exemplos:** 6.1 N1 (**FATEC 2014**) · 6.2 N1 (**FATEC 2019**) · 6.3 N2 (autoral + **FATEC 2011**, integrador) · 6.4 N2 · 6.5 N3. *(q4/D1: os de concurso passaram para o banco de questões.)*

---

## 5. Convenções LaTeX

- **Motor:** `lualatex` via `latexmk` (Unicode direto: ∧, ∨, ∀ no fonte).
- **Fonte:** TeX Gyre (Pagella ou Termes) + `unicode-math`, ou Latin Modern. Decisão estética no q5.
- **Idioma:** o `babel` português **não está instalado** no ambiente. q5: tentar `texlive-lang-portuguese`; alternativa, `babel` com `\babelprovide{brazilian}`, ou `polyglossia`.
- **Ambientes (`estilo.sty`, `tcolorbox`):**

| Ambiente / macro | Uso |
|---|---|
| `prefacio` | caixa de abertura da unidade |
| `definicao`, `construcao` | caixas em "de onde vem"; `construcao` leva `\idH{…}` |
| `erro` | 4 campos fixos: erro / por que / como evitar / onde aparece |
| `obs` | observação curta com ID |
| `exemplo{nível}{procedência}{IDs}` | exemplo com plano, resolução e comentário |
| `questao{nível}{procedência}{IDs}` | questão numerada por unidade |
| `\cobre{IDs}` | marca de cobertura, lida por `matriz.py --tex` |
| `\fonte{…}`, `\doc`, `\anedota` | etiquetas de procedência |
| `minimo` | caixa "O mínimo que você precisa" (q4/D4) |
| `paralembrar` | caixa final de "de onde vem" (q4/D3) |
| `\integradora` | marca de questão ou exemplo integrador (q4/D2) |
| `\resposta{n}{texto}` | gera `[ n. texto ]` |

- **Tabelas-verdade:** `booktabs` + coluna centralizada; V/F em vez de 1/0 (convenção do FME).

---

## 6. Banco de questões — déficit e plano para completá-lo

O pool atual tem **15 de 64** questões (`matriz.py`, R4). Plano:

> *Atualização q4:* depois das substituições do D1, o pool está em **21/64** (questões viradas exemplo saíram, conforme e4). Situação por unidade em `q4-decisoes.md` §3.

| Etapa | Onde | Meta |
|---|---|---|
| q3 | buscar ≥ 2 questões externas **verificáveis** por unidade (vestibular > OBMEP > concurso), com prioridade para os IDs sem questão (R3) | +12 |
| q3 | conferir a prova original da FATEC 2013 e o ano das OBMEP e da VUNESP/TJ-SP | regularizar 6 |
| q5 | completar com `[autoral]`, mirando os IDs ainda descobertos e os níveis em falta | ~+37 |

IDs **sem questão** hoje (R3), a priorizar: 2-E1, 2-E3, 2-E4, 2-U3, 2-U4, 2-U5 · 3-E3, 3-E4, 3-U1, 3-U5 · 4-E1…E4, 4-U2…U5 · 5-E2, 5-E3, 5-E4, 5-U3, 5-U4 · 6-E1, 6-E2, 6-E4, 6-U4, 6-U5.

---

## 7. Critérios de aceitação (usados no q3 e no q6)

1. `matriz.py matriz.yaml` sem **FALHAS**; `--tex` sem divergências entre LaTeX e matriz.
2. Cada unidade com as 8 seções, na ordem da didática.
3. O prefácio não contém definição nem resolução.
4. "De onde vem" tem ≥ 2 marcos `[documentado]`, todas as construções `H` e o fecho do gancho.
5. "Onde é usado" tem texto analítico + tabela com ≥ 4 gatilhos.
6. Cada erro tem os 4 campos.
7. Cada exemplo tem plano, resolução e comentário.
8. Cada questão tem nível, procedência e IDs; cada resposta foi verificada (w5).
9. Nenhuma etiqueta `[a verificar]` no PDF final.
10. O PDF compila sem erros e as tabelas-verdade conferem por script.

---

## 8. Pendências que o q3 recebe

1. Verificar ou descartar os 7 itens `[a verificar]` do q1, mais o polinômio de Euler (n² + n + 41), que entrou no q2 como candidato ao exemplo 5.4. O que cair sai do plano: por exemplo, o 5.4 vira autoral se o polinômio de Euler não for confirmado, e o `2-O1` fica só com o relato se os números de Hiparco não forem confirmados.
2. Confirmar a afirmação "negação é o formato mais cobrado em concursos" ou reformulá-la.
3. Buscar e verificar as questões externas (§6).
4. Conferir se o plano cumpre a didática seção a seção (é o trabalho do q3).

---

## 9. Emendas do q4 (2026-11-17)
As decisões D1–D12 do q3 foram aprovadas pelo usuário e aplicadas neste documento (marcadas *(q4/Dn)*) e na `matriz.yaml` (versão q4). Registro completo, com motivo, em `q4-decisoes.md`. **A didática não foi alterada.**
