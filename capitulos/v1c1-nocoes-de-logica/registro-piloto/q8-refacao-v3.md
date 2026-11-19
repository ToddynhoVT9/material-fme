# q8 — Refação do Cap. I na didática v3

Data: 2026-11-18 · Base: `00-didatica-v3.md` · Ordem decidida pelo usuário: R1 → R2 → R3.

A divisão é por **esforço**, não por seção. R1 reúne o que é mecânico ou local (estilo, estrutura, regras de verificação, caixas de texto curto). R2 reúne o que exige reescrever texto ou repensar itens, unidade por unidade. R3 é a revisão independente do Cap. I v3.

## R1 — pouco esforço

| # | Mudança | Base v3 | Onde |
|---|---|---|---|
| R1.1 | Glossário vai para o fim do capítulo, antes das Fontes | §5 | `main.tex` |
| R1.2 | Observações como camada opcional: selo "opcional" na caixa + fonte menor | §2.5, A2 | `estilo.sty` |
| R1.3 | Caixa **Síntese de domínio** (amarela) ao fim das Questões de cada unidade: o que você deveria saber agora + as 4 perguntas; gabarito = "Para lembrar" + seções indicadas | §2.8, A1 | `estilo.sty`, `uN_partes.tex` |
| R1.4 | Linha da Síntese nas Respostas, remetendo ao gabarito | §2.8, A1 | `uN_partes.tex` |
| R1.5 | Matriz: IDs O deixam de ser obrigatórios (R1 do `matriz.py` passa a valer só para H, U e E) | §6 | `scripts/matriz.py` |
| R1.6 | Brief do q7 ampliado com as cinco conferências da v3 | §7 | `q7/BRIEF-v3.md` |
| R1.7 | Abertura: "Como usar" e legenda das caixas atualizados para a arquitetura v3, a camada opcional e a síntese (níveis e roteiro de erros ficam para R2.12, quando os itens forem reclassificados e os erros reescritos) | §5 | `abertura.tex` |
| R1.8 | Pendência C3 do q7 (edição do FME) encerrada | A4 | `q7-revisao.md` |

## R2 — muito esforço (unidade por unidade, U1 → U6)

| # | Mudança | Base v3 |
|---|---|---|
| R2.1 | **q2 atualizado**: especificação v3 por seção e por unidade (antes de reescrever) | §7 |
| R2.2 | **Prefácio**: reescrito em torno de uma pergunta aberta; mais curto | §2.1 |
| R2.3 | **De onde vem?**: filtro P5 em cada trecho histórico (cortar ou mover para Observações); três camadas em texto corrido (A3), a começar pela bivalência em Aristóteles (U1); separar origem histórica de reconstrução matemática | §2.2, P5 |
| R2.4 | **Onde é usado?**: mapa do problema (2–3 casos enunciado → estrutura → ferramenta) como núcleo; tabela de gatilhos como resumo; aplicações que não ensinam a reconhecer (Shannon, circuitos, SAT…) movidas para De onde vem? ou Observações | §2.3 |
| R2.5 | **Erros comuns**: roteiro de 5 passos (erro → por que parece plausível → onde quebra → como detectar → como corrigir), com contraexemplo concreto e teste de detecção em todos | §2.4 |
| R2.6 | **Observações**: teste de pertença (o que é necessário sai da caixa e vai para a seção certa); só os tipos admitidos | §2.5 |
| R2.7 | **Níveis por função**: reclassificar todos os exemplos e questões (N1 reconhecimento, N2 seleção/combinação, N3 transferência); repor os níveis que ficarem descobertos | §3 |
| R2.8 | **Questões**: ordem dentro do nível do mais guiado ao menos guiado; renumeração, respostas e remissões | §2.7 |
| R2.9 | **Integradoras**: teste de necessidade em cada uma; trocar as que se resolvem sem o assunto da unidade | §2.7 |
| R2.10 | **Tipos de problema**: conferir a função de cada item (histórico / vestibular / autoral) e trocar onde o vestibular só preenche | §4 |
| R2.11 | **Fontes frágeis**: primária → nota de acesso → remoção | A5 |
| R2.12 | Matriz, verificadores e abertura (linha do tempo, mapa, notação) atualizados com o que mudou | — |

## R3 — revisão do Cap. I v3

- q7 com `q7/BRIEF-v3.md`, com 3 revisores independentes em paralelo.
- Correções → `q7-revisao-v3.md` → PDF final.
- Só depois: extrair a skill.

## Registro
- R1: §1 abaixo.
- R2: uma seção por unidade.
- R3: em `q7-revisao-v3.md` (§3 abaixo, resumo).

---

## 1. Execução do R1

Concluído em 2026-11-18.

| # | Feito |
|---|---|
| R1.1 | `main.tex`: glossário depois da Unid. 6, em página nova; abertura → Unid. 1 direto. |
| R1.2 | `estilo.sty`: `\opcional` (selo cinza "aprofundamento opcional") no título da caixa `obs`; corpo em `\small`. |
| R1.3 | `estilo.sty`: caixa `sintese` (amarela, inquebrável) + `\perguntasintese` (espaço para resposta). Em cada `uN_partes.tex`, antes das Respostas: 3 itens de "você deveria saber" + as 4 perguntas da v3, escritas para o conceito da unidade, cada uma com a seção onde está a resposta. `\label{lembrar-uN}` na caixa Para lembrar. |
| R1.4 | Em cada unidade, linha `[ S. Síntese de domínio: confira com a caixa Para lembrar (p. n)… ]` no fim das Respostas. |
| R1.5 | `scripts/matriz.py`: a regra R1 só exige exemplo para H, U e E. |
| R1.6 | `q7/BRIEF-v3.md`: critério por função de cada seção + as cinco conferências da v3. O BRIEF v2 fica como registro. |
| R1.7 | `abertura.tex`: "A ordem de cada unidade" reescrito pela função de cada seção (incluindo P4) e glossário no fim; "As caixas" com observação opcional e síntese. **Adiado para R2.12:** parágrafo dos níveis (os itens ainda estão classificados pela w2) e roteiro dos erros (ainda em 4 campos). |
| R1.8 | `q7-revisao.md` §4.1 encerrada (A4). |

Verificação: XeLaTeX com 0 erros, 0 overfull e 0 indefinidas; 103 páginas (eram 98: +6 caixas de síntese). `matriz.py` sem falhas. Verificadores das 6 unidades OK.

---

## 2. Execução do R2

**R2.1 (q2 na v3).** A especificação por seção está em `00-didatica-v3.md` §2. O plano por unidade é feito no início de cada unidade, nesta seção (o que muda, por quê, por qual regra da v3), em vez de um q2 inteiro reescrito antes. Assim, o plano de cada unidade aproveita o que a unidade anterior ensinou.

**Infraestrutura (estilo).**
- Ambiente `caso` + `\mapa{enunciado}{procure}{ferramenta}` + `\reconhecer`, para o mapa do problema.
- A tabela de gatilhos ganha a 4ª coluna "ID · treino", que aponta o exemplo ou a questão.

### 2.1 Unidade 1 — Proposição e negação

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | Novo gancho: "Toda frase é verdadeira ou falsa?". Pergunta aberta explícita: o que "esta frase é falsa" tem de errado? Saiu o parágrafo-roteiro com a lista de personagens. | §2.1 |
| De onde vem? | **Três camadas** na nova subseção "Exatamente um valor": o que Aristóteles formulou (sobre coisas e predicados, afirmar e negar) / como lemos hoje (não contradição, terceiro excluído para frases) / o que a lógica clássica convenciona (bivalência, uma decisão). O terceiro filtro passa a citar a bivalência, não "os dois princípios". | §2.2, A3; achado p7 |
| De onde vem? | **Filtro P5.** Cortados: biografia de Aristóteles (Estagira, Alexandre, Liceu, Andrônico, *Organon*), lista dos 7 argumentos de Eubulides (foi para 1-O1), os 705 livros e a dialética dos deuses de Crisipo, e a curiosidade Heyting–Brouwer (foi para 1-O2). Batalha naval, Brouwer e Łukasiewicz saíram da narrativa e foram para 1-O2 (camada opcional); a narrativa guarda só a conclusão: a bivalência é uma escolha. O Mentiroso foi reduzido a 3 frases. | P5, §2.5 |
| De onde vem? | Fecho reescrito para responder à nova pergunta do prefácio. | §2.1 |
| Onde é usado? | **Mapa do problema** com 3 casos (classificar, negar uma relação, verdade/mentira), cada um com "como reconhecer" e "treino". "Dentro da matemática" (absurdo) saiu: é a Unid. 6, e ficou como gatilho → 6-U4. "Nos computadores" virou a nova observação 1-O5. "Na língua portuguesa" ficou no caso 2 e em 1-O3. Na tabela de gatilhos, cada linha aponta onde treinar. | §2.3 |
| Erros | Os 4 erros no roteiro de 5 passos. 1-E2 agora usa o exemplo do usuário (x > 3 → x < 3, quebra em x = 3). 1-E3 ficou só com palavras e figuras (alto/baixo, acutângulo/obtusângulo), para não duplicar 1-E2. | §2.4 |
| Observações | 1-O2 reescrita como "Exatamente um valor: uma escolha, e não uma lei". 1-O5 é nova. Todas com o selo de opcional. | §2.5 |
| Níveis | Ex. 1.5 (histórico) **N3 → N2**: as quatro frases estão resolvidas no texto. **Novo Ex. 1.6 (N3, transferência)**: "Eu sou valete" na ilha, que é o Mentiroso em 1ª pessoa. Questões: a Q9 v2 (3 moradores, mesmo método do Ex. 1.4) e a Q10 v2 (demonstração, técnica no texto) passam para **N2**. **Novas N3**: Q11, a pergunta encaixada na bifurcação (dupla negação em situação nova), e Q12, frases autorreferentes e o cartão de duas faces (o critério não exclui a autorreferência, e sim a falta de valor). | §3 |
| Ordem | N2 do mais guiado ao menos guiado: Q5 s(x) · Q6 · Q7 integradora · Q8 demonstração guiada · Q9 OBMEP · Q10 três moradores. Respostas renumeradas; "Onde aparece" de 1-E4 → questões 3 e 5. | §2.7 |
| Integradoras | Q7 (mdc, potências, raízes): sem negação não se resolve. Passa. | §2.7 |
| Fontes (A5) | `fatec` (página de tag) saiu: a afirmação passa a citar as próprias provas (`fatec2013`, `fatec2014s2`, `fatec2015`, `fatec2019`). `goldbach` (espelho da Wikipédia) → Oliveira e Silva, Herzog e Pardi, *Math. Comp.* 2014 (verificação até 4·10¹⁸); saiu o "1742" sem fonte. `dlDouble` (blog) → Diógenes Laércio VII, 69, Perseus. `obmep2010`: nenhuma prova oficial encontrada; a etiqueta "via FME" fica, com a nota de acesso. | A5 |
| Síntese | Pergunta 2 ajustada para ter resposta na narrativa ("por que ela é uma escolha?"). | §2.8 |

**Verificação:** `verif_unid1.py` 27/27 OK (+6 checagens: Ex. 1.6, Q11, Q12); `matriz.py` sem falhas; XeLaTeX com 0 erros e 0 overfull.

### 2.2 Unidade 2 — Conectivos ∧ e ∨

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | O gancho do café foi mantido. Pergunta aberta explícita: "Quando uma frase com 'ou' é verdadeira, e quem decide isso: a língua ou a matemática?". Saiu o parágrafo-roteiro com a lista de personagens e da história do ∨. | §2.1 |
| De onde vem? | **Filtro P5.** Saíram: Teofrasto; o cão de Crisipo [anedota]; a subseção "Quantas frases cabem em dez?" (já contada em 2-O1); o piano lógico de Jevons e a convenção invertida de Shannon (foram para a nova 2-O5); a história do nome "diagrama de Venn" (foi para 2-O3); o detalhe do mito do *vel* (fica em 2-O3, e a narrativa só remete). Nova subseção "Por que alguém precisou disso": o valor tem de ser regra, e não opinião sobre o assunto. O fecho responde à pergunta do prefácio com a definição. | P5, §2.2 |
| De onde vem? | **Três camadas:** a disjunção estoica "como eles a formularam" (exatamente uma) / leitura de hoje (⊻) / convenção (∨ inclusivo, de Jevons). Elas já estavam no texto e ganharam marcação verbal. | A3 |
| Onde é usado? | **Mapa do problema com 5 casos** (classificar compostas; condições simultâneas, que absorveram intervalos, sistemas e produto nulo; "apenas uma"; circuitos e código; conjuntos). "Dentro da matemática", "Nos computadores" e "Na língua" foram absorvidos pelos casos ou foram para 2-O5. Gatilhos com coluna de treino. | §2.3 |
| Erros | Os 4 no roteiro de 5 passos. Pontos de quebra: produto nulo, 0·0 = 0 (E1); valor que dependeria do leitor (E2); "7 não é primo nem par" com ~(p∧q) dá V (E3); a linha que falta pode ser a única F (E4). | §2.4 |
| Observações | 2-O3 ganhou os nomes de Venn. 2-O5 é nova (piano lógico, convenção de Shannon, portas, curto-circuito, buscadores). | §2.5 |
| Níveis | Ex. 2.5 continua **N3**: o item (c), projetar um circuito de maioria, é transferência; o plano agora diz isso. Q9 v2 (circuito "exatamente um", mesmo método do 2.5c) e Q10 v2 (demonstração 0/1, que o texto faz) → **N2**. **Novas N3:** Q11 (as 16 colunas possíveis e a forma normal disjuntiva) e Q12 (∨ como 1 − (1−p)(1−q) e generalização para n letras: V em 2ⁿ − 1 linhas). | §3 |
| Ordem | N2: Q5 tabela incompleta · Q6 integradora · Q7 OBMEP 2009 · Q8 "apenas uma" · Q9 demonstração 0/1 · Q10 circuito "exatamente um". "Onde aparece" de 2-E4 → questão 5. | §2.7 |
| Integradoras | Q6: sem ∧/∨ não se resolve. Passa. | §2.7 |

**Verificação:** `verif_unid2.py` 35/35 OK (+5: Q11 a–c com a FND testada nas 16 colunas, Q12 a–b); `matriz.py` sem falhas; 0 erros, 0 overfull.

### 2.3 Unidade 3 — Condicional e bicondicional

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | O gancho das cartas foi mantido. Pergunta aberta explícita: "Quando, exatamente, um 'se' é falso, e por que isso decide quais cartas virar?". Saiu o parágrafo-roteiro (corvos do poeta, lista de personagens). A frase sobre Wason ganhou fonte. | §2.1 |
| De onde vem? | **Filtro P5.** Saíram: a amizade de Fílon com Zenão e as obras de Crisipo contra Fílon; os corvos de Calímaco (foram para 3-O3, "Corvos na lógica"); os critérios da coesão e da inclusão (foram para 3-O1); o *iff* de Halmos; a recusa de Lewis à palavra "paradoxo". Nova abertura "Por que alguém precisou disso": sem regra para o "se", não há como julgar argumentos. | P5 |
| De onde vem? | **Três camadas:** "Os nomes são de hoje": o critério de Fílon *como ele o formulou* × o nome moderno "implicação material"; Diodoro × "implicação estrita". | A3 |
| Onde é usado? | **Mapa com 6 casos:** "se" em V ou F (com teoremas e o "se" da fala); suficiente/necessária/somente se; regras; "sabe-se que é falsa"; contrapositiva em provas e verificações; definições e ↔. "Nos computadores" virou a nova 3-O4. Gatilhos com coluna de treino. | §2.3 |
| Erros | Os 5 no roteiro de 5 passos. Pontos de quebra: teorema com n = 6 (E1); retângulo (E2); n = 2 (E3); definição de primo em n = 1, F ↔ F (E4); "múltiplo de 4 não causa ser par" (E5). | §2.4 |
| Níveis | Ex. 3.6 (Wason) continua **N3**: a contrapositiva é usada para decidir o que verificar, e o plano diz isso. Q10 v2 (Simulado OBMEP, mesmo método do Ex. 3.5) → **N2**. Q12 v2 (prova mod 3, que o texto anunciava como "do mesmo tipo") → **N2**. Q11 v2 (Tia Geralda) continua **N3**: combina os mentirosos da Unid. 1 com o condicional falso, sem que nenhum exemplo faça isso. **Nova N3:** Q13, o teste de primalidade (primos até √n) justificado pela contrapositiva. | §3 |
| Ordem | N2: Q5 ↔ × ∧ · Q6 FME ex. 6 · Q7 integradora · Q8 concurso · Q9 cartas numéricas · Q10 prova mod 3 · Q11 Simulado OBMEP. Remissões: 3-E1 → questões 1 e 8; 3-E4 → questão 5; "FME ex. 6 (questão 6)". | §2.7 |
| Integradoras | Q7 (potências e inequações): a contrapositiva é necessária no item (b). Passa. | §2.7 |
| Fontes | Sem citação depois dos cortes de U1–U3, removidas da lista: `britAris`, `organon`, `iepChrys`, `dlHicks`, `theophrastus`, `aberdein`, `hplFourth` (frágil), `shieh`, `iffWiki`. | P5, A5 |

**Verificação:** `verif_unid3.py` 44/44 OK (+3: Q13); `matriz.py` sem falhas; 0 erros, 0 overfull; 104 páginas.

### 2.4 Unidade 4 — Tautologia, contradição, implicação e equivalência

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | O gancho da previsão do tempo foi mantido. Pergunta aberta explícita: "Para que a matemática quer frases que não dizem nada?". Saiu o parágrafo-roteiro. | §2.1 |
| De onde vem? | **Filtro P5.** A disputa sobre quem inventou a tabela (Shosky, Peirce, Anellis) saiu da narrativa e ficou só em 4-O2. A biografia de Carroll (Dodgson, *Alice*) foi cortada. Sheffer/Nicod foram para a nova 4-O4. Nova abertura "Por que alguém precisou disso": a demonstração precisa de passagens que valham em todas as situações, e a tabela as reconhece. | P5 |
| De onde vem? | **Três camadas:** a tese de Wittgenstein ("não dizem nada") é apresentada como conclusão *filosófica*; a classificação matemática (tautologia/contradição/contingência) é a convenção. | A3 |
| Onde é usado? | **Mapa com 5 casos:** "é tautologia?"; "é equivalente a…"; teorema, recíproco e passos de uma resolução (com o caso de elevar ao quadrado); simplificar; argumentos. "Nos computadores" foi absorvido pelo caso 4. "Na língua" foi para 4-O1. Novo gatilho: equação resolvida elevando ao quadrado → q. 11. | §2.3 |
| Erros | Os 4 no roteiro de 5 passos. Pontos de quebra: "2∣4 ⇒ 3∣5" é afirmação errada, não proposição F (E1); p → ~p (E2); chove sem frio (E3); p→(q→r) × (p→q)→r nas linhas com p F (E4). E2 ganhou a ligação com contrárias × contraditórias da Unid. 1. | §2.4 |
| Níveis | Ex. 4.5 (Carroll) continua **N3**: premissas sem sentido, em que só a forma guia; o plano diz isso. As três N3 da v2 → **N2**: Q8 (transitividade, anunciada no texto), Q9 (distributiva 0/1, técnica de 4-H4), Q10 (circuito, método do Ex. 4.3). **Novas N3:** Q11 (equação irracional: o passo "elevar ao quadrado" é só ⇒, por isso aparece −1 e nada se perde) e Q12 (premissa contraditória implica qualquer coisa; por que isso não torna a matemática inconfiável). | §3 |
| Integradoras | **A Q6 v2 falhava no teste p17**: com x de 1 a 10, bastava testar cada valor, sem lei nenhuma. Foi reescrita com x real e a restrição "sem resolver inequação do 2º grau": a proposição se reduz a x > 0 por distributiva + q ∨ ~q. A Q11 também é integradora (equações). | §2.7 |
| Ordem | N2: Q4 FME ex. 7 · Q5 casos perdidos · Q6 integradora · Q7 PUC-GO · Q8 transitividade · Q9 demonstração 0/1 · Q10 circuito. 4-E4 → questão 5; PUC-GO → questão 7. | §2.7 |

**Verificação:** `verif_unid4.py` 37/37 OK (+4: Q6 v3 em 20 mil reais, Q11, Q12; saiu a checagem da Q6 v2); `matriz.py` sem falhas; 0 erros, 0 overfull; 106 páginas.

### 2.5 Unidade 5 — Sentenças abertas e quantificadores

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | O gancho "x + 1 = 7" foi mantido. Pergunta aberta explícita: como dizer algo V ou F sobre x + 1 = 7 sem escolher x. Saiu o parágrafo-roteiro (Frege, Peirce, Fermat). | §2.1 |
| De onde vem? | "Todo e algum antes dos quantificadores" virou "Por que alguém precisou disso", com **três camadas**: como Aristóteles usava "todo/algum" (parte da frase) / a leitura de hoje (operações sobre variáveis, séc. XIX). **P5:** saiu a frase sobre a notação bidimensional de Frege e a adoção por Peano (`sowa1885`). Os demais trechos passam no filtro: Fermat/Euler explicam o contraexemplo; Π/Σ de Peirce motivam 5-H2. | A3, P5 |
| Onde é usado? | **Mapa com 5 casos:** "transforme em proposição" e "todo…" em V ou F; identidade × equação; domínio (com definições de crescente/par); "no máximo / pelo menos / exatamente", com o sinal "pode-se garantir" = todos os casos compatíveis com os dados; dois quantificadores (com a ambiguidade de "todo aluno leu um livro"). "Nos computadores" virou a nova 5-O3. | §2.3 |
| Erros | Os 4 no roteiro de 5 passos. Pontos de quebra: x = −3 e a = 0 (E1); o −2 em x² = 4 (E2); n = 40 → 41² (E3); ∀x∃y × ∃y∀x nos inteiros (E4). | §2.4 |
| Níveis | Ex. 5.6 → **N2**: o item (a) é literalmente o exemplo do erro 5-E4. Ex. 5.5 (relógios da UF-RS) continua **N3**: dados imprecisos são situação nova, e o plano diz isso. Q9 v2 (termômetro, mesmo método do Ex. 5.5) e Q10 v2 (∃| em ax + b = 0, cuja raiz está no "mínimo") → **N2**. **Novas N3:** Q11 (∃| em x³ + x = 2, unicidade por monotonia) e Q12 ("tem máximo" × "limitada superiormente" com quantificadores; x²/(x² + 1) é limitada e não tem máximo). | §3 |
| Ordem | N2: Q5 domínio finito · Q6 ordem dos quantificadores · Q7 contraexemplos · Q8 integradora · Q9 demonstração ∃| · Q10 termômetro. Remissões: 5-E1 → questões 1 e 8; 5-E3 → 7 e 10; 5-E4 → 6. | §2.7 |
| Integradoras | Q8 (inequação do 2º grau e domínios): sem quantificar sobre o domínio a pergunta nem existe. Passa. | §2.7 |
| Fontes | Removidas por ficarem sem citação: `sowa1885` (U5) e `anellis2004` (corte da U4). | — |

**Verificação:** `verif_unid5.py` 46/46 OK (+5: Q11 e Q12); `matriz.py` sem falhas; 0 erros, 0 overfull; 107 páginas.

### 2.6 Unidade 6 — Negação de proposições

| Seção | O que mudou | Regra v3 |
|---|---|---|
| Prefácio | O gancho da turma foi mantido. Pergunta aberta explícita: "O que basta para desmentir uma frase, e como escrever, sem errar, a frase que a desmente?". Saiu o parágrafo-roteiro. | §2.1 |
| De onde vem? | A abertura virou "Por que alguém precisou disso: contrário não é contraditório". **Três camadas** no quadrado: Aristóteles fez a distinção / o diagrama é posterior (Apuleio, Boécio) / a lógica moderna (ressalva do importe existencial). **P5:** o parágrafo de De Morgan/Ockham/Buridan foi reduzido a uma frase. "Cai tanto em prova" → "aparece em tantas questões de negação". | A3, P5 |
| Onde é usado? | **Mapa com 6 casos:** compostas; "todo/algum/nenhum" (com a ambiguidade de "todo aluno não passou"); condicional (com "equivalente × negação"); desigualdades e intervalos; contraexemplo, absurdo e definições negadas; código e buscas. A negação explícita de "crescente" saiu do texto, para o Ex. 6.5 continuar sendo transferência. | §2.3 |
| Erros | Os 5 no roteiro de 5 passos. Pontos de quebra: turma com metade aprovada (E1); Ana estuda e Beto trabalha (E2); linha p F (E3); turma com canhotos e destros (E4); fronteiras x = 3 e x = −3 (E5). | §2.4 |
| Observações | 6-O2: o trecho de Sheffer/Nicod virou remissão a 4-O4. | §2.5 |
| Níveis | Ex. 6.5 continua **N3**: a definição de "crescente" é nova e as regras não; o plano diz isso. As três N3 da v2 → **N2**: Q10 (código e buscas, caso 6 do mapa), Q11 (limitada superiormente, mesmo método do Ex. 6.5, agora com remissão à Q12 da Unid. 5) e Q12 (√2, anunciada e esboçada no texto). **Novas N3:** Q13 (ilha: "Todos nós três somos valetes" e "Exatamente um de nós é cavaleiro", resolvida pela negação de quantificadas, com solução única) e Q14 (infinitos primos: quantificar, negar, provar por absurdo). | §3 |
| Ordem | N2: Q5 FME 9–10 · Q6 o professor · Q7 integradora · Q8 FATEC 2017 · Q9 FATEC 2014 · Q10 código · Q11 limitada · Q12 √2. Remissões: 6-E3 → questões 5 e 6; 6-E5 → 4, 5 e 7; absurdo → questão 12; FATEC 2014 → questão 9; a remissão da Q12 à Unid. 3 aponta para o caso 5 do mapa. | §2.7 |
| Integradoras | Q7 (inequação do 2º grau): o item (a) pede a negação de um ∀. Passa. | §2.7 |

**Verificação:** `verif_unid6.py` 32/32 OK (+2: Q13 por força bruta, Q14); `matriz.py` sem falhas.

### 2.7 Fechamento do R2 (R2.12)
- **Abertura:** "Os níveis" reescrito pela função (N1 reconhecimento e aplicação, N2 seleção e combinação, N3 transferência; nenhum N3 resolvido no texto; ordem por grau de guia; integradoras só com o assunto necessário). Na legenda das caixas, os erros com o roteiro de 5 passos e a caixa "Mapa do problema". Linha do tempo, mapa das unidades e tabela de notação conferidos: todos os marcos continuam contados em alguma unidade (narrativa ou observação).
- **Estado final:** 110 páginas; 0 erros, 0 overfull, 0 indefinidas; `matriz.py` sem falhas; verificadores U1–U6 todos OK (27 · 35 · 44 · 37 · 46 · 32 = 221 checagens); toda chave `\src` existe e toda entrada de Fontes é citada.
- **Pendências passadas para o R3:**
  - `obmep2010` continua sem prova oficial (nota "via FME").
  - O q7 v3 deve conferir as cinco regras novas em todas as unidades.

---

## 3. R3 — fechamento (2026-11-18)
- **Revisão:** 3 revisores independentes (`q7/v3-revisor-A/B/C.md`), sem acesso aos registros da produção. Nenhum erro de resposta; 107 achados didáticos, históricos, de ID, de ordem, de ponteiro e de leiaute.
- **Correções:** todas aplicadas, exceto A19 (ordem do N3 da U1), mantida por decisão. Detalhe por achado em `q7-revisao-v3.md`.
- **Renumerações:** U4 (Q4 → N1; demonstração 0/1 → Q5; 9→5, 5→6, 6→7, 7→8, 8→9). U5 (exemplos 5.5 ↔ 5.6). U6 (N2 por grau de guia: 6→5, 8→6, 9→7, 5→8, 10→9, 7→10). Remissões, matriz e verificadores sincronizados.
- **Fontes (A5):** 12 primárias acrescentadas ou trocadas, 6 entradas removidas, o resto sob a nota de acesso; pendências de navegação listadas em `q7-revisao-v3.md` §6.
- **Emendas à v3:** E-R3-1 a E-R3-5 (`00-didatica-v3.md` §12).
- **Estado final:** `Cap1-v3-final.pdf`, 112 páginas; 0 erros, 0 overfull, 0 indefinidas; `matriz.py` sem falhas; verificadores 27 · 36 · 44 · 38 · 47 · 33 = 225 checagens, 0 falhas.
- **Próximo passo (decisão do usuário):** extrair a skill.
