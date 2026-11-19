# q1 — Plano estruturado de pesquisa (e coleta) · Cap. I — Noções de lógica

Piloto · FME vol. 1, Cap. I · 2026-11-17
Depende de: `00-decisoes.md` · Alimenta: q2 (estruturação) e q3 (revisão do material coletado)

---

## 0. Escopo do q1

O q1 tem três produtos:

1. **Passo zero (ingestão):** inventário fiel do material de entrada.
2. **Plano de pesquisa:** para cada seção da didática × cada unidade, o que precisa ser descoberto, onde procurar e quando a pesquisa está suficiente.
3. **Coleta executada:** o material encontrado, com etiqueta de procedência (w4), pronto para o q3 revisar.

Convenções de etiqueta usadas neste documento:

| Etiqueta | Significado |
|---|---|
| `[documentado]` | fato histórico com fonte primária ou acadêmica consultada |
| `[anedota]` | relato tradicional sem base documental firme |
| `[a verificar]` | conhecimento prévio plausível, ainda sem fonte consultada no q1 — não entra no material sem verificação no q3 |
| `[fonte primária]` / `[fonte secundária]` | para questões: prova original consultada / só transcrição de terceiros |

Os IDs de matriz (U, E, O) aparecem aqui como **candidatos** (`U1.a`, `E3.b`…). A numeração definitiva é do q2.

---

## 1. Passo zero — ingestão

### 1.1 Método
- PDF de 22 páginas renderizado a 110 dpi e lido **visualmente**, página a página.
- A camada de texto (`pdftotext`) foi usada só para localizar seções. **Não serve como fonte**, por dois motivos:
  1. Perde os símbolos (∧, ∨, ~, ≠, ∈, |, ≤…), que saem como espaços ou caracteres trocados.
  2. **Contém texto oculto.** A página de respostas dos vestibulares mostra só as respostas 1–6, mas a camada de texto traz as respostas 1–67 do volume inteiro (conjuntos, funções etc.). Quem extrair só o texto importa respostas de outros capítulos.
- **Regra para a skill:** a leitura visual é a autoridade; a camada de texto é só índice.

### 1.2 Estrutura do material de entrada

| Páginas (livro) | Conteúdo |
|---|---|
| 1–17 | Teoria (itens I–X, numerados 1–18) + exercícios 1–10 |
| 270–271 | Respostas dos exercícios do Cap. I |
| 313–314 | Questões de vestibulares — "Lógica" (6 questões) |
| 404 | Respostas das questões de vestibulares (visíveis: 1–6) |

### 1.3 Mapa do capítulo → unidades

| Unidade | Itens do FME | Conteúdo no livro | Exercícios FME | Vestibulares FME (candidatos) |
|---|---|---|---|---|
| **U1 Proposição e negação** | I (1), II (2) | definição de proposição (3 características), exemplos e não exemplos, negação ~p, tabela-verdade de ~p | 1, 2 | V2 |
| **U2 Conectivos ∧ e ∨** | III (3, 4) | conjunção e disjunção, tabelas, 4 exemplos cada | 3 | V3, V5 |
| **U3 Condicional e bicondicional** | IV (5, 6) | →, antecedente/consequente, "suficiente/necessária"; ↔ | 4, 5, 6 | V4, V6 |
| **U4 Tautologia, contradição, implicação, equivalência** | V (7), VI (8), VII (9), VIII (10) | tautologia e proposição logicamente falsa (exemplos com tabela), ⇒ (teorema = hipótese ⇒ tese), ⇔ | 7 | — |
| **U5 Sentenças abertas e quantificadores** | IX (11–14) | sentença aberta, ∀, ∃, ∃\| (existe um único) | 8 | V1 (parcial) |
| **U6 Negação de proposições** | X (15–18) | ~(p∧q), ~(p∨q), ~(p→q), negação de ∀ e ∃ | 9, 10 | V1 |

Observações de ingestão:
- **O livro não cobre a negação do bicondicional** (~(p↔q)). É uma lacuna a decidir no q2: completar ou deixar para observações.
- O exercício 7 do FME é, na prática, a lista de leis da álgebra de Boole (comutativa, associativa, idempotente, identidade, distributiva, absorção, dupla negação, De Morgan). É o elo natural com Shannon (U4) e com o Cap. II (Conjuntos).
- A notação ∃| ("existe um único") do FME difere da usual ∃!. Vale uma observação.

### 1.4 Problemas encontrados no material de entrada
| # | Onde | Problema | Tratamento proposto |
|---|---|---|---|
| P1 | p. 13 | "funções **proporcionais**" no lugar de "funções **proposicionais**" | corrigir no material e citar em observações (U5) |
| P2 | p. 314, V4 | alternativas impressas na ordem a, b, c, **e, d** | reordenar ao transcrever; o gabarito (a) não muda |
| P3 | camada de texto | respostas ocultas de outros capítulos | regra de ingestão (§1.1) |
| P4 | V1–V6 | as 5 questões OBMEP vêm **sem ano** | pendência de procedência (§5.3) |

### 1.5 Verificação do gabarito (w5)
Resolução independente por força bruta (`scripts/verif_fme_cap1.py`, `scripts/verif_vest_cap1.py`):

| Item | Resultado |
|---|---|
| Exercícios 1–7 e 10 | **todos conferem** com o gabarito do FME |
| Ex. 6 | solução única: p V, q V, r F, s F (confere) |
| Ex. 7 | todas as 9 equivalências testadas são tautologias (confere) |
| V1 (UF-RS) | a defasagem real pode ir de 61 s a 179 s → os três estão errados → **opção V** (confere) |
| V2 (OBMEP) | única atribuição consistente: 3 tamanduás → **d** (confere) |
| V3 (OBMEP) | única ordenação: Celina é a mais nova, casada com Beto → **c** (confere) |
| V4 (OBMEP) | dias possíveis: (A,A,A), (A,A,S), (A,S,S) → só Ari repete sempre, água → **a** (confere) |
| V5 (OBMEP) | 16 valores possíveis → **e** (confere) |
| V6 (OBMEP) | só "ovos e laranja, sem leite e sem creme" satisfaz as três regras → **d** (confere) |

Os exercícios 8 e 9 têm resposta textual. A conferência deles é qualitativa e fica para o q6.

---

## 2. Plano de pesquisa por seção da didática

Cada seção tem: **perguntas que a pesquisa precisa responder**, **fontes previstas** e **critério de suficiência**, que diz quando parar. As particularidades por unidade estão no §3.

### 2.1 Abertura geral do capítulo (decisão do q2)
- **Perguntas:** por que um livro de matemática começa por lógica? Qual o arco histórico da disciplina (Aristóteles → estoicos → Boole/De Morgan → Frege/Peirce → Peano/Russell → Wittgenstein/Post → Shannon)? Como as 6 unidades se encadeiam? O que vem depois (Cap. II, Conjuntos)?
- **Fontes:** SEP, MacTutor (Jeff Miller), Britannica e as próprias referências das unidades.
- **Suficiente quando:** houver uma linha do tempo com ≥ 8 marcos `[documentado]` e um mapa das unidades.

### 2.2 Prefácio (por unidade)
- **Perguntas:** qual a pergunta-gancho que a unidade responde? Quais os pré-requisitos (w7)?
- **Fontes:** o próprio inventário + os achados de "de onde vem".
- **Suficiente quando:** houver 1 gancho e a lista de pré-requisitos.

### 2.3 De onde vem? (por unidade)
- **Perguntas:** quem formulou, quando, em que contexto e para resolver qual problema? Qual experimento ou debate marcou o conceito? De onde vem a notação? Como construir o conceito do zero (definição → tabela → propriedade)?
- **Fontes:** SEP (lógica antiga, Peirce, emergência da lógica de 1ª ordem), MacTutor/Jeff Miller (notação), Britannica, textos originais (Aristóteles *Da Interpretação*, Tractatus, Carroll *Symbolic Logic*), literatura de psicologia do raciocínio (Wason).
- **Suficiente quando:** cada unidade tiver ≥ 2 marcos `[documentado]`, a origem da notação e um roteiro de construção do zero.

### 2.4 Onde é usado? (w6: texto analítico + tabela de gatilhos)
- **Perguntas:** em que tipos de prova e contexto o conceito aparece (vestibular, OBMEP, concurso, demonstração, computação)? Como o enunciado "denuncia" a ferramenta? Que padrão de raciocínio resolve?
- **Fontes:** as questões coletadas (§5), material da OBMEP, bancos de questões e a literatura de aplicação (Shannon, buscas booleanas).
- **Suficiente quando:** por unidade, houver ≥ 3 contextos com exemplo real e ≥ 4 gatilhos.

### 2.5 Erros comuns
- **Perguntas:** que erros são documentados? Por que acontecem (linguagem natural × lógica, intuição causal, viés de confirmação)? Como evitar?
- **Fontes:** literatura sobre a tarefa de Wason, falácias clássicas (afirmação do consequente, negação do antecedente), quadrado das oposições (contrário × contraditório), distratores das questões coletadas.
- **Suficiente quando:** houver ≥ 3 erros por unidade, cada um com causa e antídoto.

### 2.6 Observações
- **Perguntas:** que pontos ficam fora das seções, mas enriquecem? Paradoxos, limites (lógica de 3 valores), notações alternativas, erros do próprio livro.
- **Suficiente quando:** houver ≥ 2 por unidade.

### 2.7 Exemplos (3 níveis, w2)
- **Perguntas:** que problemas históricos e de vestibular cobrem os IDs? Há pelo menos um por nível?
- **Fontes:** §5 + problemas históricos (Wason, Carroll, Smullyan, Crisipo/Hiparco).
- **Suficiente quando:** a matriz preliminar estiver coberta com N1, N2 e N3 em cada unidade.

### 2.8 Questões e respostas
- **Perguntas:** que questões reais existem por unidade? Qual a procedência verificável de cada uma? Há resposta conferida?
- **Fontes (em ordem de prioridade):** FME (exercícios e vestibulares) → vestibulares com prova original → OBMEP (banco público) → concursos (como fonte complementar, ver §6) → autorais.
- **Suficiente quando:** cada unidade tiver um pool com folga sobre a meta que o q2 vai definir.

---

## 3. Coleta executada — dossiê por unidade

### Abertura geral — linha do tempo (todos `[documentado]`, salvo indicação)

| Época | Marco |
|---|---|
| séc. IV a.C. | Aristóteles, *Da Interpretação*: nem toda frase é proposição; só as que têm verdade ou falsidade. Uma prece é frase, mas não é verdadeira nem falsa. Também é nesse texto que aparecem as relações entre "todo/algum/nenhum" (base do quadrado das oposições). |
| séc. IV–III a.C. | Fílon (escola dialética) × Diodoro Cronos: o debate sobre quando um "se… então" é verdadeiro. Fílon propõe o critério que hoje é a tabela do →. |
| séc. III a.C. | Crisipo (estoico) sistematiza uma lógica de **proposições** (não de termos), com conectivos "se", "e", "ou". |
| 1847 | De Morgan, *Formal Logic*. Boole, *Mathematical Analysis of Logic* (1847) `[a verificar]`; *Laws of Thought* (1854) `[documentado]`. |
| 1864 | Jevons torna a "soma" lógica **inclusiva** (Boole usava a exclusiva). |
| 1879 | Frege, *Begriffsschrift*: quantificadores e variáveis ligadas. |
| 1883–1885 | Peirce (e seu aluno O. H. Mitchell) chegam aos quantificadores de forma independente. Matriz de tabela-verdade em manuscrito de 1883. |
| 1889–1897 | Peano: ∈ (1889), ~ e o ∃ invertido (1897). |
| 1906–1910 | Russell: ∨; Whitehead e Russell, *Principia Mathematica*. |
| 1921 | Wittgenstein (*Tractatus*) e Post, independentemente, publicam as tabelas-verdade. Wittgenstein define tautologia e contradição (4.46). |
| 1922 | Hilbert usa → |
| 1930 | Heyting: ¬ e ∧ |
| 1933 | A. Becker: ↔ |
| 1935 | Gentzen: ∀ |
| 1937–1938 | Shannon mostra que a álgebra de Boole projeta circuitos de relés (base da eletrônica digital). |
| 1954 | Bourbaki: ⇒ e ⇔ |
| 1966–1968 | Wason: a tarefa de seleção mostra que a maioria das pessoas raciocina mal com "se… então". |

---

### U1 — Proposição e negação

**Prefácio — gancho candidato:** "Uma prece é uma frase. É verdadeira?" (Aristóteles). Ou: "Esta frase é falsa." — é proposição?
**Pré-requisitos:** símbolos =, ≠, <, ≤, ∈, | (divide); conjuntos numéricos ℕ, ℤ, ℚ.

**De onde vem**
- Aristóteles separa as frases que afirmam ou negam algo (e por isso são verdadeiras ou falsas) das demais (preces, perguntas, ordens). As 3 características do FME — oração, declarativa, um único valor lógico — são a versão escolar dessa ideia `[documentado]`.
- Os princípios da **não contradição** e do **terceiro excluído** sustentam a 3ª característica (Aristóteles, *Metafísica* IV) `[documentado — fonte secundária UFS]`.
- O símbolo ~ é de Peano (1897). O ¬ é de Heyting (1930) `[documentado]`.
- Os estoicos chamavam a proposição de *axíoma* ("assertível"). O valor dela podia mudar com o tempo: "é dia" é verdadeira de dia `[documentado]`.
- **Construção do zero:** frase → frase declarativa → valor V/F → negação como operação que inverte o valor → tabela de ~p (2 linhas).

**Onde é usado (candidatos)**
- `U1.a` Classificar se algo é proposição. Gatilhos: "quais são proposições", frase sem verbo, pergunta, sentença com variável.
- `U1.b` Negar relações (=/≠, </≥, ∈/∉, |/∤). Gatilho: "negação de 7 > 3".
- `U1.c` Puzzles de veracidade (quem mente, quem fala a verdade) — OBMEP V2.

**Erros comuns (candidatos)**
- `E1.a` Achar que proposição **falsa** "não é proposição". O FME ex. 1 f) é proposição falsa. Causa: confundir "ter valor" com "ser verdadeira".
- `E1.b` Negar ">" com "<", esquecendo a igualdade. O livro mostra 7 > 3 → 7 ≤ 3. Causa: pensar no "oposto" e não no "complemento".
- `E1.c` Negar com o **contrário** em vez do **contraditório** ("João é alto" → "João é baixo"). Causa: na língua, "o contrário de" ≠ negação lógica. O quadrado das oposições formaliza a diferença.
- `E1.d` Tratar sentença aberta (3x − 1 = 11) como proposição.

**Observações (candidatos)**
- `O1.a` O paradoxo do mentiroso, atribuído a Eubulides (escola megárica) `[documentado — fonte secundária UVM]`: uma frase declarativa que não pode receber valor sem contradição.
- `O1.b` Lógicas com mais de dois valores (Peirce explorou três valores) `[documentado — SEP Peirce]`; Łukasiewicz 1920 `[a verificar]`.

---

### U2 — Conectivos ∧ e ∨

**Prefácio — gancho candidato:** "Café ou chá?" — e se a pessoa quiser os dois? O "ou" do garçom não é o "ou" da matemática.
**Pré-requisitos:** U1.

**De onde vem**
- Crisipo trabalhou com os conectivos "e", "ou" e "se" `[documentado]`.
- Os estoicos preferiam a disjunção **exclusiva** (exatamente uma verdadeira). Conheciam a inclusiva, mas pouco a usavam `[documentado — Britannica]`.
- Boole também usou a união exclusiva. Frege o criticou por isso. Jevons, em *Pure Logic* (1864), adotou a leitura inclusiva, a que ficou `[documentado]`.
- Notação: ∨ de Russell (1902–06); ∧ de Heyting (1930); o ponto (p.q) dos *Principia* `[documentado]`. A origem de ∨ no latim *vel* (inclusivo) × *aut* (exclusivo) `[a verificar]`.
- **Problema histórico (N3/observação):** Crisipo teria afirmado que, com 10 proposições simples, dá para formar mais de um milhão de conjunções. Hiparco o refutou com números bem menores (relato de Plutarco) `[documentado — Bobzien]`. Os números exatos (103 049 / 310 952) e a ligação com os números de Schröder `[a verificar]`.
- **Construção do zero:** "e" exige as duas partes → 4 casos → tabela. "Ou" falha só quando as duas falham → tabela. 2 variáveis → 4 linhas; n variáveis → 2ⁿ linhas.

**Onde é usado (candidatos)**
- `U2.a` Classificar compostas (FME ex. 3).
- `U2.b` Problemas de restrições simultâneas — conjunção de condições (OBMEP V3).
- `U2.c` "Apenas uma é verdadeira" = disjunção exclusiva (OBMEP V5).
- `U2.d` Computação e circuitos: &&/||, portas AND/OR, buscas booleanas `[documentado — Shannon; De Morgan em buscas]`.
- `U2.e` Ponte com Conjuntos: ∧ ↔ ∩, ∨ ↔ ∪ (Cap. II).

**Erros comuns (candidatos)**
- `E2.a` Ler o "ou" como exclusivo. Causa: uso cotidiano.
- `E2.b` Exigir relação de sentido entre as partes ("2 > 0 e Paris é capital" é proposição legítima). Causa: a língua pede coesão; a lógica só olha valores.
- `E2.c` Não reconhecer "mas", "porém", "nem" como conjunções lógicas.
- `E2.d` Montar tabela com linhas faltando (n variáveis ≠ 2n linhas).

**Observações (candidatos)**
- `O2.a` Crisipo × Hiparco: contar conjunções possíveis é um problema combinatório antigo (ver "de onde vem").
- `O2.b` A disjunção exclusiva (⊻) existe e é útil, mas não é o ∨. Ela é a negação do ↔, o que liga a U2 à U6 (`O6.a`).

---

### U3 — Condicional e bicondicional

**Prefácio — gancho candidato:** o teste das 4 cartas de Wason — menos de 10% acerta.
**Pré-requisitos:** U1, U2.

**De onde vem**
- Fílon: o condicional é falso só quando o antecedente é verdadeiro e o consequente falso, ou seja, três modos de ser verdadeiro e um de ser falso. É a primeira definição funcional-verdade do "se… então" `[documentado]`.
- Diodoro exigia mais: que nunca fosse possível ter antecedente verdadeiro e consequente falso. Pelo critério dele, "se é dia, eu converso" é falso, mesmo que Fílon o aceite enquanto a pessoa conversa de dia `[documentado]`.
- O debate era tão famoso que o poeta Calímaco escreveu que **até os corvos nos telhados** grasnavam "o que se segue de quê?" `[documentado — SEP, Kurzová, White]`.
- Crisipo propôs um critério ainda mais forte (conexão entre antecedente e consequente) `[documentado — fonte secundária]`.
- Notação: → de Hilbert (1922); ↔ de A. Becker (1933) `[documentado]`.
- **Experimento:** Wason (1966; artigo de 1968, *Quarterly Journal of Experimental Psychology*). Quatro cartas, regra "se há uma vogal de um lado, há um número par do outro". A resposta correta (a carta p e a carta não-q) é escolhida por cerca de 10% dos participantes, ou menos (Wason & Shapiro, 1971, relatam ~4%) `[documentado — várias fontes secundárias]`.
- **Construção do zero:** "promessa" — "se chover, levo guarda-chuva". Só a quebro se chover e eu não levar. Isso fecha os 4 casos.

**Onde é usado (candidatos)**
- `U3.a` Enunciados de teoremas (hipótese → tese); "condição suficiente/necessária".
- `U3.b` Problemas de regras e restrições (OBMEP V4, V6 — bolo).
- `U3.c` "Se… é falsa, então é verdade que…" — condicional falso força p V e q F (VUNESP TJ-SP; FME ex. 6).
- `U3.d` Contrapositiva como equivalente (FATEC 2013).
- `U3.e` Bicondicional em definições ("se, e somente se").

**Erros comuns (candidatos)**
- `E3.a` Achar que p → q é falso quando p é falso. Causa: intuição de causalidade; é o "paradoxo da implicação material".
- `E3.b` Confundir **recíproca** (q → p) e **inversa** (~p → ~q) com **contrapositiva** (~q → ~p). Formas de falácia: afirmar o consequente, negar o antecedente. A tarefa de Wason mede exatamente isso.
- `E3.c` Inverter "necessária/suficiente" e "somente se" ("p somente se q" = p → q).
- `E3.d` Ler ↔ como "e".

**Observações (candidatos)**
- `O3.a` Por que aceitar "se 5 < 2, então 2 ∈ ℤ" como verdadeiro (FME, 3º exemplo): a convenção de Fílon preserva as leis algébricas, e as alternativas (Diodoro, Crisipo) não são funcionais-verdade.
- `O3.b` Versões da tarefa de Wason com conteúdo social ("se bebe álcool, tem mais de 18") são resolvidas bem mais vezes (Griggs & Cox 1983; Cosmides 1989) `[documentado — fonte secundária]`.

---

### U4 — Tautologia, contradição, implicação, equivalência

**Prefácio — gancho candidato:** "Ou chove ou não chove" é sempre verdade — então não diz nada sobre o tempo. Para que serve uma frase que não informa?
**Pré-requisitos:** U1–U3 e tabelas com 3 variáveis.

**De onde vem**
- Wittgenstein (Tractatus 4.46): tautologia é verdadeira em todas as possibilidades; contradição, em nenhuma. A tautologia "não diz nada" sobre o mundo `[documentado]`.
- As tabelas-verdade: Peirce (matriz em manuscrito de 1883; outro de 1893) → Wittgenstein e Post (1921, independentes). Em 1997 achou-se uma matriz em transcrição de palestra de Russell de 1912 `[documentado — fonte secundária]`.
- O ex. 7 do FME = leis da álgebra de Boole. Shannon (1937) as usou para simplificar circuitos de relés `[documentado]`.
- Distinção → × ⇒: o FME separa o conectivo (que forma proposição) da relação entre proposições (p ⇒ q quando p → q é tautologia). Notação ⇒/⇔ de Bourbaki (1954) `[documentado]`.
- **Construção do zero:** tabela completa → coluna final toda V (tautologia), toda F (contradição) ou mista (contingência — termo não usado pelo FME).

**Onde é usado (candidatos)**
- `U4.a` Verificar equivalências por tabela (FME ex. 7).
- `U4.b` Reconhecer "é equivalente a" em questões (contrapositiva; p → q ⇔ ~p ∨ q).
- `U4.c` Teorema = implicação; recíproco verdadeiro = equivalência.
- `U4.d` Simplificar expressões e circuitos.
- `U4.e` Validar argumentos (silogismos de Carroll).

**Erros comuns (candidatos)**
- `E4.a` Confundir → (conectivo) com ⇒ (relação).
- `E4.b` Achar que toda proposição é tautologia ou contradição (esquecer a contingência).
- `E4.c` Achar que proposições equivalentes "dizem a mesma coisa em palavras".
- `E4.d` Errar a ordem padrão das linhas e perder casos.

**Observações (candidatos)**
- `O4.a` Exemplo histórico de silogismo: Carroll, *Symbolic Logic* (1896) — "bebês são ilógicos…" → "bebês não sabem lidar com crocodilos" `[documentado]`.
- `O4.b` O termo "contingência".

---

### U5 — Sentenças abertas e quantificadores

**Prefácio — gancho candidato:** "x + 1 = 7" não é verdadeira nem falsa. Como transformá-la em proposição sem escolher um valor para x?
**Pré-requisitos:** U1; noção de conjunto universo.

**De onde vem**
- A lógica de Aristóteles já operava com "todo/algum/nenhum", mas como termos e não como operadores sobre variáveis `[documentado]`.
- Frege (*Begriffsschrift*, 1879) e Peirce (1885), independentemente, criam quantificadores com variáveis ligadas: o grande salto da lógica tradicional para a moderna `[documentado]`.
- Peirce lia o ∀ (que escrevia Π) como uma conjunção possivelmente infinita ("a é P e b é P e…") e o ∃ (Σ) como uma disjunção. É a ponte para a negação na U6 `[documentado — SEP]`.
- Notação: ∃ — Peano (1897) usou o E invertido; Russell o usou como operador ligando variável; ∀ — Gentzen (1935), por analogia ao ∃; Russell escrevia (x) `[documentado]`.
- **Construção do zero:** sentença aberta → (1) atribuir valor ou (2) quantificar → ∀ = "todos os casos", ∃ = "pelo menos um caso" → ∃| = "exatamente um".

**Onde é usado (candidatos)**
- `U5.a` Transformar sentença aberta em proposição verdadeira (FME ex. 8).
- `U5.b` Identidades (∀) × equações (∃): (a + 1)² = a² + 2a + 1 vale ∀a; x + 1 = 7 vale ∃x.
- `U5.c` Definições matemáticas (função, limite) e domínios.
- `U5.d` "No máximo/pelo menos" (UF-RS V1).

**Erros comuns (candidatos)**
- `E5.a` Ignorar o universo/domínio: √(x²) = x (vale só para x ≥ 0); (a² − a)/a = a − 1 (falha em a = 0). Os dois estão no ex. 8 do FME.
- `E5.b` Ler "existe" como "existe exatamente um".
- `E5.c` "Provar" um ∀ com exemplos; não aceitar que um contraexemplo derruba um ∀.
- `E5.d` Trocar a ordem dos quantificadores (∀x∃y × ∃y∀x). Vai além do FME → observação.

**Observações (candidatos)**
- `O5.a` P1: "funções proporcionais" é erro tipográfico de "proposicionais".
- `O5.b` A notação ∃| do FME × a usual ∃!.
- `O5.c` Paradoxo de Russell (1901) / versão do barbeiro `[a verificar]`.

---

### U6 — Negação de proposições

**Prefácio — gancho candidato:** qual é o contrário de "todo político mente"? "Nenhum político mente"? (Não.)
**Pré-requisitos:** U2–U5.

**De onde vem**
- As leis levam o nome de De Morgan (*Formal Logic*, 1847), mas observações equivalentes já estavam em Aristóteles e nos medievais. Ockham escreveu por extenso as frases que resultam das leis; Buridan também tratou do tema `[documentado — fonte secundária Wikipedia]`.
- O quadrado das oposições (Aristóteles, *Da Interpretação* 6–7): A "todo S é P" × O "algum S não é P" são **contraditórias** (uma é a negação da outra); A × E "nenhum S é P" são **contrárias** (podem ser ambas falsas) `[documentado]`.
- A negação dos quantificadores é De Morgan generalizado, pela leitura de Peirce (∀ como "e" infinito, ∃ como "ou" infinito).
- **Construção do zero:** derivar ~(p ∧ q) ⇔ ~p ∨ ~q pela tabela; ~(p → q) ⇔ p ∧ ~q a partir da tabela do →; ~∀ ⇔ ∃~ pelo argumento "e infinito".

**Onde é usado (candidatos)**
- `U6.a` "Qual a negação de…" com conectivos (VUNESP/PC-SP 2018 — Marluce).
- `U6.b` Negação de quantificados (FGV/TJ-SC 2018 — "nenhum médico é cego").
- `U6.c` Negação de condicional (p ∧ ~q).
- `U6.d` Demonstração por contraexemplo e por absurdo (material OBMEP).
- `U6.e` Buscas e código (NOT (A AND B) = NOT A OR NOT B).

**Erros comuns (candidatos)**
- `E6.a` Negar "todo" com "nenhum" (contrário ≠ contraditório).
- `E6.b` Negar a conjunção mantendo o "e" ("não é A e não é B").
- `E6.c` Negar p → q como ~p → ~q ou p → ~q.
- `E6.d` Negar "alguns são" como "alguns não são".
- `E6.e` Negar a desigualdade sem trocar estrita/não estrita (≤ ↔ >).

**Observações (candidatos)**
- `O6.a` A negação do bicondicional (~(p ↔ q) ⇔ p ↔ ~q, a disjunção exclusiva) não está no FME (lacuna §1.3).
- `O6.b` A regra "quebre a barra, troque o sinal" da engenharia.

---

## 4. Problemas históricos candidatos (para exemplos N3)

| Problema | Unidade | Procedência |
|---|---|---|
| Tarefa de seleção de Wason (1966/68) | U3 | `[documentado]` |
| Os corvos de Calímaco / Fílon × Diodoro (como discussão guiada) | U3 | `[documentado]` |
| Sorites de Lewis Carroll (*Symbolic Logic*, 1896) | U4/U5 | `[documentado — domínio público]` |
| Cavaleiros e valetes — Smullyan (*What Is the Name of This Book?*, 1978). A OBMEP V2 descende desse tipo | U1/U3 | `[documentado]` · autoria protegida: usar a estrutura, não o texto |
| Conjunções de Crisipo × Hiparco | U2 (obs./N3) | relato `[documentado]`; números `[a verificar]` |
| "Enigma de Einstein" | — | **evitar**: a atribuição a Einstein é `[anedota]` sem base conhecida |

---

## 5. Banco de questões coletado

### 5.1 Do FME (gabarito verificado — §1.5)
- Exercícios 1–10, distribuídos conforme §1.3.
- Vestibulares V1 (UF-RS) e V2–V6 (OBMEP).

### 5.2 Externas (candidatas)

| Questão | Unidade | Status | Resposta (conferida no q1) |
|---|---|---|---|
| FATEC 2013 — contrapositiva de "Se x < 3, então y = −4" | U3/U4 | `[fonte secundária]` — a transcrição tem erros de sinal nas alternativas; **exige a prova original** | "Se y ≠ −4, então x ≥ 3" (alternativa E na transcrição) |
| VUNESP / PC-SP 2018 — negação de "Marluce é a secretária e Rogério não é o presidente" | U6 | `[fonte secundária]` — **concurso** | C (~M ∨ R) |
| VUNESP / TJ-SP — "Se Ana é gerente, então Carlos é diretor" é falsa | U3 | `[fonte secundária]` — concurso, **ano desconhecido** | C (Ana é gerente) |
| FGV / TJ-SC 2018 — negação de "Nenhum médico é cego" | U6 | `[fonte secundária]` — concurso | A (há pelo menos um médico cego) |

### 5.3 Pendências de procedência
- Ano das questões OBMEP V2–V6 (o FME não informa).
- Prova original da FATEC 2013.
- Ano da VUNESP/TJ-SP.

---

## 6. Achados que pedem decisão (vão para q2/q3/q4)

1. **Escassez de lógica formal em vestibular.** As buscas acharam pouca questão de lógica proposicional em vestibulares tradicionais. A maior parte do material real é de **concursos** (VUNESP, FGV, CESPE, FCC) e de **olimpíadas** (OBMEP). Isso afeta "onde é usado" (contexto real do assunto) e o pool de questões. **Decisão para q4:** aceitar questões de concurso com etiqueta própria (`[concurso — VUNESP/PC-SP 2018]`)? Elas não mudam a didática, que só pede *priorizar* vestibulares nos exemplos.
2. **OBMEP é olimpíada, não vestibular.** O FME agrupa as questões como "vestibulares". Proposta: manter a etiqueta real (`[OBMEP]`).
3. **Lacuna do livro:** negação do bicondicional (§1.3).
4. **Verificação na fonte primária.** Nenhuma questão externa foi conferida na prova original. O q3 precisa fazer isso, ou elas viram `[adaptada de …]`.
5. **Volume.** Com 6 unidades × 8 seções + abertura, o material deve passar de 60 páginas. O q2 deve definir metas por seção (exemplos e questões por nível).

---

## 7. Fontes consultadas

**Notação e história geral**
- Jeff Miller, *Earliest Uses of Symbols of Set Theory and Logic* — MacTutor: https://mathshistory.st-andrews.ac.uk/Miller/mathsym/set/
- SEP, *The Emergence of First-Order Logic*: https://plato.stanford.edu/entries/logic-firstorder-emergence/
- SEP, *Peirce's Deductive Logic*: https://plato.stanford.edu/archives/spr2021/entries/peirce-logic/
- Peirce (1885), *On the Algebra of Logic*, nota introdutória (van Heijenoort): https://eclass-b.uoa.gr/modules/document/file.php/PHS651/Readings/Peirce%20CS%20%281885%29%20-%20On%20the%20Algebra%20of%20Logic.pdf
- Wikipedia, *Truth table* (histórico Peirce/Wittgenstein/Post): https://en.wikipedia.org/wiki/Truth_table

**Antiguidade**
- Aristóteles, *Da Interpretação* (trad. Edghill), cap. 4: https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/interpretation.asp?pg=4
- Encyclopedia.com, *Philo of Megara*: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/philo-megara-c-400s-bce
- SEP, *Diodorus Cronus*: https://plato.stanford.edu/archives/spr2020/entries/diodorus-cronus/
- M. J. White, *What Worried the Crows?* (Classical Quarterly): https://resolve.cambridge.org/core/journals/classical-quarterly/article/what-worried-the-crows/B202EADB2A9589F6F673E71FF5DE9D88
- H. Kurzová, *What worried the crows in Callimachus' epigram?*: https://digilib.phil.muni.cz/_flysystem/fedora/pdf/114977.pdf
- Wikipedia, *Stoic logic*: https://www.wikipedia.org/wiki/Stoic_logic
- Britannica, *exclusive disjunction* (estoicos): https://britannica.com/topic/exclusive-disjunction
- Britannica, *ancient logic*: https://www.britannica.com/topic/ancient-logic/Theophrastus-of-Eresus
- S. Bobzien, *The Combinatorics of Stoic Conjunction*: https://philarchive.org/archive/BOBTCO-2
- Notas de curso UVM (Eubulides, Crisipo): https://www.uvm.edu/~jbailly/courses/196Stoicism/notes/StoicLogic.html

**Séculos XIX–XX**
- Encyclopedia.com, *Modern Logic: The Boolean Period: Jevons*: https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/modern-logic-boolean-period-jevons
- *The basis of Boole's logical theory* (arXiv 1710.01542): https://arxiv.org/pdf/1710.01542.pdf
- Wikipedia, *De Morgan's laws* (Ockham/Buridan): https://static.hlt.bme.hu/semantics/external/pages/modus_ponens/en.wikipedia.org/wiki/De_Morgan%27s_laws.html
- MacTutor, De Morgan (DNB): https://mathshistory.st-andrews.ac.uk/DNB/De_Morgan.html
- Tractatus 4.46 (resumo SparkNotes): https://www.sparknotes.com/philosophy/tractatus/section7/
- Wikipedia, *A Symbolic Analysis of Relay and Switching Circuits*: https://en.wikipedia.org/wiki/A_Symbolic_Analysis_of_Relay_and_Switching_Circuits
- Lewis Carroll, *Symbolic Logic* (Project Gutenberg): https://gutenberg.org/cache/epub/28696/pg28696-images.html
- Wikipedia, *Knights and Knaves* (Smullyan 1978): https://en.wikipedia.org/wiki/Knights_and_Knaves

**Psicologia do raciocínio**
- Wason & Shapiro (1971), *Natural and contrived experience in a reasoning problem*: https://iphils.uj.edu.pl/~a.trybus/classes/logic/cs/15.Wason.Natural.And.Contrived.Reasoning.pdf
- Sperber, Cara & Girotto, sobre a tarefa de seleção: https://www.dan.sperber.fr/wp-content/uploads/2009/09/SperberCaraGirotto.pdf
- Psychology in Action, *Wason Selection Task*: https://psychologyinaction.org/?p=252

**Quadrado das oposições (pt)**
- UFS/CESAD, Lógica I, aula 5: https://cesad.ufs.br/ORBI/public/uploadCatalago/15403031102016Logica_I_Aula_05.pdf
- UFS/CESAD, Lógica I, aula 10: https://cesad.ufs.br/ORBI/public/uploadCatalago/15411431102016Logica_I_Aula_10.pdf

**Questões e uso**
- Quero Bolsa, *Lógica* (FATEC 2013): https://querobolsa.com.br/enem/matematica/logica
- Quero Bolsa, *Raciocínio lógico* (VUNESP, FGV): https://querobolsa.com.br/enem/matematica/raciocinio-logico
- Portal da OBMEP, material teórico *Introdução à Lógica Matemática*: https://cdnportaldaobmep.impa.br/portaldaobmep/uploads/material_teorico/shfg14yb1eok8.pdf
- EduCAPES, proposta didática com questões de lógica da OBMEP: https://educapes.capes.gov.br/bitstream/capes/1131738/2/Produto-Marcelo.pdf
