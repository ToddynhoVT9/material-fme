# q7 (v3) — Revisor C · Unidades 5 e 6 + Fontes

**Escopo revisado:** `cap1/u5_artigo.tex`, `cap1/u5_partes.tex`, `cap1/u6_artigo.tex`, `cap1/u6_partes.tex` (PDF `cap1/main.pdf`, p. impressas 71–98 = páginas físicas 75–102) e `cap1/fontes.tex` (lista inteira, p. 102–110), contra `00-didatica-v3.md` (em vigor), `00-decisoes.md`, `q2-estrutura.md`, `q1-pesquisa.md`, `q3-pesquisa-unid5/6.md`, `q4-revisao.md`, `q5-decisoes.md`, `q45-unid5/6.md` e `matriz.yaml`.
**Método:** leitura do .tex e do PDF (texto e imagem das p. 79, 81, 82 e 91). Todos os exemplos e questões foram resolvidos de novo em Python (sympy, tabelas-verdade por força bruta, enumeração de modelos para frases com "todo/nenhum/algum", simulação para relógios e termômetro). Scripts de trabalho em `/tmp/rc/verif.py` (Unid. 5), `/tmp/rc/verif6.py` (Unid. 6) e `/tmp/rc/srckeys.py` (chaves `\src`), fora da árvore do projeto. Não li q6, q8, q7-revisao, os relatórios antigos nem `scripts/verif_*.py`.

**Resultado geral:** nenhuma divergência de resposta. Todas as 26 questões e os 11 exemplos das duas unidades conferem. Os achados se concentram em quatro pontos: conferência (a) da v3 (IDs declarados e não treinados), teste de pertença das Observações da Unid. 6, ponteiros (gatilhos e Síntese) que apontam para o lugar errado, e uma afirmação histórica cuja fonte citada não a sustenta (Apuleio).

---

## Tabela de achados

| # | Gravidade | Onde | Problema | Evidência | Correção proposta |
|---|---|---|---|---|---|
| 1 | importante | `u6_artigo.tex:39` (p. 84–85) | "o quadrado [...] organizado séculos depois por **Apuleio e Boécio**" não é sustentado pela fonte citada (`squareWiki`). | Wikipedia *Square of opposition* (versão de nov./2026, a que o cabeçalho das Fontes declara valer): "Aristotle did not draw any diagram; this was done several centuries later", e atribui o diagrama a Boécio; Apuleio aparece só no nome "square of Apuleius". SEP (Parsons, `sepSquare`): o diagrama "shows up already in the second century CE", depois em Boécio (c. 500), sem nomear Apuleio. | A5, passo 1: citar `sepSquare` e reescrever: "o diagrama já aparece num texto do século II d.C. e chega à Idade Média por Boécio". Para manter Apuleio, é preciso uma fonte que o nomeie (p. ex., a edição do *Peri Hermeneias* de Apuleio). |
| 2 | importante | `u6_artigo.tex:19` (objetivos) × `u6_partes.tex:52–62` (6-O1, 6-O2) × `u6_partes.tex:111–123` (ex. 6.4) × `u6_artigo.tex:170,186` | As Observações 6-O1 e 6-O2 **não passam no teste de pertença** (v3 §2.5). O prefácio promete "negar [...] bicondicionais", mas a negação do ↔ só é ensinada na camada opcional 6-O1. A notação da barra (6-O2) é gatilho do caso 6 e da tabela ("uma barra sobre uma expressão") e é exigida no ex. 6.4(c). O plano do 6.4 diz "Usar a observação 6-O1". | Quem pula as Observações não consegue fazer o ex. 6.4(a) e (c) nem cumprir o objetivo declarado no prefácio. | Passar a negação do ↔ para "De onde vem?" (um parágrafo ou uma construção curta depois de 6-H2) e manter em 6-O1 só a ligação com o "ou exclusivo". Ou tirar "bicondicionais" dos objetivos e o item (a) do 6.4. Fazer o mesmo com a barra: definir a notação no caso 6 ou tirar o 6.4(c) e o gatilho "barra". |
| 3 | importante | `u6_partes.tex:228` (Q9) · `matriz.yaml` U6 Q9 | Conferência (a): a Q9 (FATEC 2014/2, irmãos de Pedro) declara só **6-U2** (negar quantificadas), mas não pede negação nenhuma. Pede a conclusão válida, que é a contrapositiva de um ∀. O próprio caso 3 (`u6_artigo.tex:152`) a usa como exemplo de enunciado que pede a *equivalente*, "e não a negação". | Resolução por modelos: a única alternativa válida é (e), ∀x(I→F) ⇒ (~F→~I). Nenhum passo nega uma quantificada. | Acrescentar um item b): "Escreva a negação da afirmação e diga qual situação a tornaria verdadeira" (aí treina 6-U2). Ou trocar a declaração para os IDs que o item treina de fato (3-H3/4-U2, em ID transversal), registrando na matriz. |
| 4 | importante | `u5_partes.tex:62` (ex. 5.1, 5-O1) e `:80` (ex. 5.2, 5-O2) · `matriz.yaml` U5 exemplos | Conferência (a): as duas observações só são **mencionadas** no comentário ("é a função proposicional da observação 5-O1"; "aparece como ∃! (5-O2)"), não treinadas. A v3 §2.5 cita justamente "5-O1" como caso de ligação forçada achado no q7, e tirou os IDs O da cobertura obrigatória. | Nenhuma linha da resolução do 5.1 usa a ideia de função proposicional. O 5.2 não usa ∃! nem a forma por extenso de 5-O2. | Retirar 5-O1 e 5-O2 do `\cobre` e da matriz (a cobertura de O é livre). |
| 5 | importante | `u5_partes.tex:118–148` | Ordem dos exemplos: 5.5 é **N3** e vem antes do 5.6, que é **N2**. O q2 §2.6 (não substituído pela v3) pede "ordem crescente de nível", e a progressão P6 também. | Cabeçalhos no PDF, p. 79–80: 5.4 N2 → 5.5 N3 → 5.6 N2. | Renumerar: o atual 5.6 (ordem dos quantificadores) vira 5.5 e o dos relógios vira 5.6. Atualizar as remissões ("exemplo 5.5/5.6" nos casos 4 e 5, na tabela de gatilhos, nos erros 5-E4 e na Q10) e a matriz. |
| 6 | menor | `u5_artigo.tex:150` (tabela de gatilhos, 1ª linha) | O gatilho "letra sem valor na frase → sentença aberta → dê valor ou quantifique" aponta para a **q. 2**, mas a Q2 só tem frases já quantificadas. | Q2: a)–e) são todas da forma (∀…)/(∃…)/(∃\|…). | Apontar para a q. 1 (FME ex. 8, "transforme em proposições"). |
| 7 | menor | `u6_artigo.tex:182` (tabela de gatilhos, linha "nenhum") | O gatilho "nenhum → ~∀~ = ∃" aponta para a **q. 3**, que não tem "nenhum" (trata de "todo homem é mortal" e "alguns alunos são canhotos"). | Negações de "nenhum" estão na Q2 ("nenhum médico é cego") e na Q8 (nefelibata). | Apontar para a q. 2 ou a q. 8. |
| 8 | menor | `u5_partes.tex:189` (Q6) | Conferência (a): a Q6 declara **5-H2** (∀ como "e", ∃ como "ou" num domínio finito), mas todos os itens estão em ℕ ou ℝ e nenhum desmonta o quantificador em conectivos. | Q6 a)–d): domínios infinitos; só treina a ordem (5-E4). | Retirar 5-H2 da Q6 (já é coberto pela Q5 e pelo ex. 5.6b). |
| 9 | menor | `u5_partes.tex:234` (Q12) | 5-E4 (trocar a ordem dos quantificadores) está declarado, mas só é treinado implicitamente: nenhum item pede para comparar ∃M∀x com ∀x∃M. | Resp. 12 só traz as formas ∃∀. | Acrescentar um item: "o que diz (∀x)(∃M)(f(x) ≤ M)? Que funções a satisfazem?" (resposta: todas). Ou retirar 5-E4. |
| 10 | menor | `u6_partes.tex:255` (Q12) | 6-H2 [~(p→q) ⇔ p∧~q] está declarado na prova da irracionalidade de √2, mas o enunciado não é um condicional e a resolução esperada (resp. 12) não nega condicional nenhum. | Resp. 12: supor √2 = a/b irredutível → contradição. | Retirar 6-H2. Ou formular como condicional ("se x² = 2, então x é irracional") e pedir a suposição p ∧ ~q. |
| 11 | menor | `u5_partes.tex:252`, `u6_partes.tex:279` (Síntese, pergunta 1) | A pergunta 1 remete a "(→ Definição)", mas as Unid. 5 e 6 **não têm caixa de Definição**; o significado está nas construções. A aceitação da v3 §2.8 é que a resposta seja localizável. | `grep definicao u5_* u6_*`: nenhuma ocorrência (a Unid. 4 tem). | "(→ construções 5-H1 e 5-H3)" e "(→ construções 6-H1 a 6-H3)". |
| 12 | menor | `u6_artigo.tex:107` | "E é o **quadrado de Aristóteles** em notação moderna" contradiz a linha 39 ("Aristóteles [...] não desenhou nenhum diagrama"). Atribuição posterior posta no autor antigo (conferência d). | Linha 39 × linha 107. | "É a contradição de Aristóteles (o par A–O do quadrado tradicional) em notação moderna". |
| 13 | menor | `u5_artigo.tex:92`; também `u5_partes.tex:114` | Três camadas: "Em 1772, ele [Euler] registrou que a expressão **n²+n+41** dá primos para n=0…39". Euler escreveu outra forma; n²+n+41 é a forma de hoje (deslocada). | Perrin (`perrinEuler`): Euler, em 1772, comentando Jean Bernoulli, escreve "41 − x + xx" e nota que os 40 primeiros termos são primos. O q3 da Unid. 5 já registrava isso. | "Em 1772, ele registrou que 41 − x + x² dá primos nos quarenta primeiros casos; escrita como hoje, n² + n + 41 é primo para n = 0, …, 39." |
| 14 | menor | `u6_artigo.tex:42` | "Os **lógicos medievais** deram nomes de letras [A, E, I, O]" está citado em `sepSquare`, que não diz de onde vêm as letras. | SEP (ed. 2008): só a tabela A/E/I/O, sem a origem. Já a Wikipedia (`squareWiki`) traz a origem: *affirmo*/*nego*. | Citar `squareWiki` aqui ou tirar "medievais". |
| 15 | menor | `u6_artigo.tex:130` | "é um dos formatos mais pedidos nas provas que cobram lógica": afirmação de frequência sem fonte. É a pendência q2 §8.2, que a regra de honestidade do q2 §2.3 trata. O caso 1 (linha 138) faz certo: restringe a "questões da FATEC reunidas para este material". | Nenhum `\src` na frase; o q3 da Unid. 6 não traz contagem. | "...e aparece com frequência nas questões de lógica de vestibular e de concurso reunidas para este material." |
| 16 | menor | `u5_artigo.tex:72–73` ("Os símbolos") | Filtro P5: o parágrafo sobre Peano 1897, Russell e Gentzen 1935 não ajuda a entender quantificadores e repete a tabela de notação da abertura (`abertura.tex:92–93`, mesma fonte). | Os fatos conferem com Miller (ver Fontes na web). | Reduzir a uma linha que remete à tabela da abertura, ou passar para uma Observação. |
| 17 | menor | `u6_partes.tex:94` (comentário do ex. 6.2) | Classifica (e) "todas as vagas [...] **não são** de ensino superior" como a contrária E, sem ressalva. O caso 2 (`u6_artigo.tex:145`) acabou de dizer que "todo aluno não passou" é **ambígua**. | Contradição interna entre o caso 2 e o ex. 6.2. | "(c) é a contrária E; (e), na leitura mais comum, também (a frase é ambígua, ver caso 2)". |
| 18 | menor | `u6_partes.tex:294` (resp. 6) | A negação dada, "o aluno estudou e não passou", omite o "para todo" implícito na afirmação do professor. O ex. 6.4 (comentário) ensina justamente que esse ∀ implícito também se nega. | Afirmação: ∀a (E(a)→P(a)). Negação: ∃a (E(a) ∧ ~P(a)). | "(d); negação: 'algum aluno estudou e não passou'". |
| 19 | menor | `u6_partes.tex:293` (resp. 5h) | A negação de (∃x)(√x < 0) aparece como (∀x≥0)(√x ≥ 0), com o quantificador restrito. Muda a forma que a regra ~∃ ⇔ ∀~ produz, e é essa forma que o item treina. | Regra de 6-H3: ~(∃x)P(x) ⇔ (∀x)~P(x). | "(∀x)(√x ≥ 0) (V: onde √x existe, isto é, para x ≥ 0, ela é ≥ 0)". |
| 20 | menor | `u6_partes.tex:301` (resp. 13); `u5_partes.tex:273` (resp. 12c) | v3 §2.9: Respostas trazem "só o resultado". A resp. 13 traz um passo de justificativa e a 12c, o argumento. | — | Resp. 13: "A valete, B cavaleiro, C valete". Na 12c, basta "M = 1; não tem máximo". |
| 21 | menor | `u6_artigo.tex:144,181–183`; `u6_partes.tex:138` | Notação: a equivalência entre proposições aparece com "=" (~∀ = ∃~; ~(p→q) = p∧~q; ~(a<b) = a≥b), enquanto o capítulo ensina ⇔ (Unid. 4) e usa ⇔ na caixa "Para lembrar" da mesma unidade (`u6_artigo.tex:119`). | Inconsistência entre seções da mesma unidade. | Usar ⇔ fora do código (no código, "=" pode ficar). |
| 22 | menor | `u6_partes.tex:113` (ex. 6.4a) | "um **número** é par se, e somente se, seu quadrado é par": paridade só se aplica a inteiros, e a resolução fala em "inteiro". | Linha 119: "existe um inteiro que…". | "um número inteiro é par…". |
| 23 | menor | `u6_partes.tex:67–79` (ex. 6.1) | O enunciado reconstruído omite o modelo que a prova oferece: a questão começa com "**Considere o exemplo**" (proposição "O cachorro é um animal ou a alface é um vegetal" e sua negação). Isso muda o grau de guia do item. A frase a negar está no PDF do Objetivo, como o comentário diz. | WebFetch do PDF do Objetivo (`fatec2015`): "Considere o exemplo. Assinale a alternativa…"; o exemplo cachorro/alface e a frase de Maria e Júlia aparecem no texto da resolução. Gabarito B confere. | Incluir o exemplo da prova antes do enunciado (fica mais fiel e continua N1). Manter a etiqueta "enunciado reconstruído", porque a frase original está em imagem. |
| 24 | menor | `u6_partes.tex:142–268` (ordem das N2) | Conferência (e): dentro do N2, as múltipla-escolha Q8 e Q9 (as mais guiadas) vêm depois da Q5 (13 itens abertos) e da integradora Q7 (resolução aberta em duas etapas). | Q6, Q8 e Q9 são de alternativas; Q5, Q7, Q10, Q11 e Q12 são abertas. | Reordenar o N2: Q6, Q8, Q9 → Q5, Q10 → Q7 → Q11 → Q12. Atualizar as remissões ("questão 9" no caso 3, "questão 12" em De onde vem, gatilhos, erros). |
| 25 | menor | `matriz.yaml` U6, ex. 6.3 × `u6_partes.tex:97` | Procedência: a matriz diz "autoral + vestibular FATEC 2011, prova 1"; o PDF diz "autoral + adaptado de FATEC 2011" (que é o correto pelo q3: "sem texto literal → [adaptada de…]"). | q3-pesquisa-unid6 §2. | Alinhar a matriz: "autoral + adaptado de FATEC 2011". |
| 26 | menor | PDF p. 79 (ex. 5.5) | O diálogo dos três amigos e as afirmativas I–VI saem num bloco corrido: as quebras do .tex não têm `\par`, e as opções ficam no meio do parágrafo. | Imagem da p. 79. | `\par` entre as falas e as afirmativas em lista (`enumerate`, rótulos I–VI). |
| 27 | menor | PDF p. 81 (Q3c, Q8e), p. 92 e 95 (Q4) | Listas em linha com `\quad` quebram fórmulas no fim da linha: "(∃\|x ∈ / ℕ)(x² = 4)", rótulo "e)" isolado do seu D, "b) / −1 ≤ x < 3". | Imagem da p. 81; pdftotext das p. 92 e 95. | Usar `tasks`/`multicols` ou `enumerate` em linha com `\mbox{…}` em cada item. |
| 28 | menor | PDF p. 82 e 98 (Síntese, perguntas 2–4) | O ponteiro "(→ Onde é usado?)" e "(→ Erros comuns)" se parte em duas linhas ("(→" fica sozinho). | Imagem da p. 82. | `\mbox{(→ Onde é usado?)}` no `\perguntasintese`, ou `\hfill\mbox{…}`. |
| 29 | menor | `fontes.tex:94` (`aristPriorAn`) | A entrada diz "I.23", mas a página indicada se rotula "Part 24 · Page 41". O leitor não encontra "23". | WebFetch: página com "Part 24"; a frase da diagonal está lá. | Acrescentar a numeração de Bekker: "I.23, 41a23–30". |
| 30 | menor | `fontes.tex:16` (`aristInt`) × `abertura.tex:23` | `aristInt` é "cap. 4" (URL pg=4), mas a abertura o cita para "distingue contrárias de contraditórias", que está em *Da Interpretação* 6–7. | Entrada × uso. | Nova entrada para *Da Interpretação* 7 (mesma tradução de Edghill), que também serve à Unid. 6 (A5, passo 1, para `squareWiki`). |
| 31 | menor | `fontes.tex:49,67` (`jevons1870`, `wasonShapiro`) | Sem URL nem DOI. A referência permite achar a obra, mas a lista adota URL nas demais. | — | Acrescentar o DOI (a conferir na editora). |
| 32 | menor | `fontes.tex:28-29,87` (`sepFOL`, `sepBrouwer`) | URLs da versão corrente da SEP (texto mutável), enquanto as outras entradas da SEP apontam para edições arquivadas. A nota de acesso do cabeçalho fixa a versão só para a Wikipédia. | — | Apontar para `plato.stanford.edu/archives/<edição>/entries/...` ou estender a nota de acesso a todas as páginas web. |

**Fora do escopo C (anotado de passagem):** a folha de rosto (`main.tex:16`) ainda diz "Versão 2".

---

## Conferências da v3 (§1b do brief), item a item

**Unidade 5**
- Prefácio: tem a pergunta aberta explícita ("Como dizer algo V ou F sobre x+1=7, sem escolher valor para x?"), e o Fecho a responde (`u5_artigo.tex:94–95`). Tem pré-requisitos e a caixa "O mínimo".
- De onde vem?: responde às três perguntas (dificuldade de Boole → Frege/Peirce → construções 5-H1–H3). A história está separada da reconstrução (caixas de Construção). As três camadas estão bem feitas para Aristóteles, mas não para Euler (#13). P5: Fermat/Euler passa no filtro; "Os símbolos" não passa (#16).
- Onde é usado?: cinco casos com mapa enunciado → estrutura → ferramenta. Cada linha de gatilho aponta para um item; uma aponta errado (#6).
- Erros comuns: os quatro erros têm os 5 passos, contraexemplo concreto e teste de detecção.
- Observações: 5-O1, 5-O2 e 5-O3 passam no teste de pertença.
- (a): 5.1/5-O1 e 5.2/5-O2 (#4), Q6/5-H2 (#8), Q12/5-E4 (#9). Os demais IDs conferem com a resolução.
- (b): N3 (Q11 x³+x=2 por monotonicidade; Q12 máximo × limitada) não estão resolvidos no texto; funções dos níveis coerentes.
- (c): a integradora Q8 precisa do conteúdo da unidade: saber que (∀x∈D) vale se D ⊆ {x : x²>x}. Só a inequação não responde a pergunta.
- (e): ordem das questões aceitável. Ordem dos exemplos violada (#5).
- Síntese: as quatro perguntas estão lá; a pergunta 1 remete a uma seção inexistente (#11).

**Unidade 6**
- Prefácio: tem a pergunta aberta explícita ("O que basta para desmentir uma frase…?"), e o Fecho a responde. Tem pré-requisitos e a caixa "O mínimo".
- De onde vem?: contrário × contraditório (Aristóteles) → quadrado → De Morgan → 6-H2 → 6-H3 (De Morgan generalizado, pela leitura de Peirce) → absurdo. Três camadas bem marcadas no quadrado ("na lógica moderna, ambas V") e na diagonal ("corresponde à prova moderna"), com um deslize (#12). Fonte frágil em Apuleio (#1).
- Onde é usado?: seis casos com mapa; gatilhos com um ponteiro errado (#7).
- Erros comuns: os cinco erros têm os 5 passos, contraexemplo e detecção.
- Observações: 6-O1 e 6-O2 falham no teste de pertença (#2).
- (a): Q9 (#3), Q12 (#10); o resto confere.
- (b): os N3 (Q13 ilha com "todos/exatamente um"; Q14 infinitos primos) não estão resolvidos no texto. A Q14 tem sugestão forte, mas pede a negação de ∀∃ num lugar novo.
- (c): a integradora Q7 precisa da negação estrita → não estrita (6-E5) para incluir 1 e 3. Só a inequação não basta.
- (e): ordem do N2 (#24).

---

## Fontes: chaves, achabilidade e A5

**Chaves:** 86 entradas em `fontes.tex`. Todas as chaves usadas em `\src{}`/`\cite{}` no capítulo (abertura, glossário, u1–u6) existem. Não há entrada nunca citada nem chave duplicada. O `main.log` não tem citação indefinida.

**Achabilidade:** não consegui testar os 83 URLs a partir do contêiner: o proxy de saída recusa CONNECT (403) para esses hosts. Conferi por WebFetch: `miller`, `sepFOL`, `perrinEuler`, `squareWiki`, `sepSquare` (ed. 2008), `fatec2015`, `fatec2019`, `aristPriorAn` (todos abrem e contêm o que é citado, salvo o #1) e `deMorganWiki` (via redirecionamento). Problemas de entrada: #29–#32.

**A5 aplicada às fontes frágeis** (1 = trocar ou complementar pela primária · 2 = a nota de acesso do cabeçalho basta · 3 = remover):

| Fonte frágil | Uso | Ação A5 | Ainda frágil? |
|---|---|---|---|
| `squareWiki` | abertura; U6 (Aristóteles, diagrama) | 1: *Da Interpretação* 7 (Edghill) + `sepSquare`; corrigir Apuleio (#1) | **sim** |
| `deMorganWiki` | abertura; U6 (Ockham; busca; mnemônico) | 1: De Morgan, *Formal Logic* (1847); Ockham, *Summa Logicae* II.32–33. 2 basta para o mnemônico e o exemplo de busca, que não são fatos históricos | **sim** (parte histórica) |
| `corry` | U6 ("atribuído aos pitagóricos") | 2: página acadêmica; afirmação secundária e qualificada ("costuma ser") | não |
| `fatec2015`, `fatec2019`, `fatec2014s2` | U1, U6 | 2: a resolução do Objetivo reproduz a prova (conferido para 2015 e 2019); primária ideal = prova da FATEC/CPS | não |
| `fatec2013` | U1, U4 | 1: prova oficial ou resolução do Objetivo, no lugar da transcrição do Estratégia | **sim** |
| `obmep2010` (wiki Fandom) | U1 | 1: prova oficial OBMEP 2010 | **sim** |
| `obmep2005` (cópia IFES), `obmep2007`, `obmep2009` (host legado `obmep2010.obmep.org.br`, http) | U2, U3 | 1: acervo atual de provas da OBMEP | **sim** |
| `shannon` (Wikipedia) | U1, U2 | 3: `shannonMIT` (primária) já está na lista | resolvível já |
| `philoWiki` | U3 | 3: co-citada com `sepDialectical` e `ls35b` | resolvível já |
| `psyAction` | U3 | 3: resume `wasonShapiro`, que já está na lista | resolvível já |
| `mathpages` | U2 | 3: co-citada com `bobzienComb` | resolvível já |
| `correio`, `migalhas` | U1 | 3 (ou 2): `matos` (acadêmica) sustenta o ponto | resolvível já |
| `futcont` | U1 | 1: *Da Interpretação* 9 + `sepFut` (já na lista) | **sim** em `u1_artigo:57` (citada sozinha) |
| `wasonWiki`, `sussexWason`, `nautilus` | abertura, U3 | 1: Wason (1968), *QJEP* 20(3) + `wasonShapiro`; `nautilus`: 3 | **sim** |
| `ravenWiki` | U3 | 1: Hempel (1945), *Mind* 54 + `fitelson` | **sim** |
| `truthTableWiki` | abertura, U4 | 1: `anellis` (já na lista); Post (1921); *Tractatus* 4.31 | parcialmente |
| `sparkTract`, `wittND` | U4 | 1: *Tractatus* 4.46–4.4661 (trad. Ogden 1922, domínio público) | **sim** |
| `booleAlgWiki`, `maaBoole` | U1, U4 | 1: Boole, *The Laws of Thought* (1854, Gutenberg) | **sim** |
| `shefferWiki`, `shefferStroke` | U4 | 1: Sheffer (1913), *Trans. AMS* 14; Nicod (1917) | **sim** |
| `satWiki` | U4 | 1: o artigo de Cook (STOC 1971); `cook1971` é a página do prêmio, não o artigo | **sim** |
| `smullyan` (Wikipedia) | U1 | 1: Smullyan, *What Is the Name of This Book?* (1978) | **sim** |
| `oupEub` | U1 | 1: Diógenes Laércio II.108 (mesmo site de `dlDouble`); `sepAncient` | **sim** |
| `ls35b` (.docx numa plataforma de curso) | U3 | 1: Sexto Empírico, *Hipotiposes* 2.110–113 (trad. Bury) ou Long & Sedley (1987), 35B, impresso | **sim** (link instável) |
| `liversidge` (LibreTexts, cita entrevista) | U2 | 1: a entrevista original (dados a conferir) | **sim** |
| `fregeColor` (artigo sobre Wittgenstein e Ramsey) | abertura, U2 | 1: Frege, "Der Gedanke" (1918), passagem sobre "e"/"mas"; pertinência fraca | **sim** |
| `plutarchNum` (MathWorld) | abertura, U2 | 2, ou 1: Plutarco, *Conversas à mesa* VIII.9; `bobzienComb` co-citada | não |
| `megarians`, `britIncl`, `britBoole`, `ieeeJevons`, `macJevons`, `educapes` | U1–U2 | 2: obras de referência e repositórios institucionais | não |

---

## Conferido sem problemas
- **Unidade 5, exemplos 5.1–5.6:** tudo confere (5.1 a)–e); 5.2 a)–d); 5.3 a)–c); Fermat 3, 5, 17, 257, 65 537 primos e 2³²+1 = 641·6 700 417; n²+n+41 primo para n = 0…39 e 1681 = 41² em n = 40; relógios com defasagem em (60, 180) s → afirmativa V; 5.6 (i) V, (ii) F, b) V e V).
- **Unidade 5, Q1–Q12:** respostas conferem (Q1 FME ex. 8 a)–h), incluindo d) na leitura impressa √(m²)+9; Q7 a) primeiro contraexemplo n = 41, b) p = 11, 2047 = 23·89; Q8 x²>x ⇔ x<0 ou x>1; Q10 aumento em (2, 4) → (d), e as outras alternativas caem; Q11 raiz única 1, derivada 3x²+1 > 0; Q12 sup g = 1, não atingido).
- **Unidade 6, construções:** as tabelas de 6-H1 e 6-H2 conferem linha a linha; as três formas de ~(p↔q) em 6-O1 são equivalentes; as relações do quadrado conferem por enumeração de modelos, inclusive a vacuidade com S vazio.
- **Unidade 6, exemplos 6.1–6.5 e Q1–Q14:** tudo confere (6.1 (b) única; 6.2 (b); 6.3 F/V, V/F, V/F e x ≤ −3 ∨ x > 2; 6.4 a)–c); 6.5 testemunha (−2, 1) e crescimento em x ≥ 0; Q1 (c), Q2 (a), Q3, Q4, Q5 a)–m), Q6 (d), Q7 [1, 3], Q8 (c), Q9 (e), Q10 a)–c), Q11 x = \|M\|+1, Q13 solução única A valete, B cavaleiro, C valete, Q14 a) negação correta).
- **Matriz:** níveis, integradoras e IDs de todas as questões e exemplos das Unid. 5 e 6 coincidem com o `.tex` (salvo #25). As metas (U5 4/6/2, U6 4/8/2) estão cumpridas. Todo H/U/E obrigatório tem exemplo, e todo U/E tem questão.
- **Procedência:** UF-RS "via FME (ano não informado)" (D9); FME ex. 8, 9 e 10; "adaptada de concurso — …" no formato D-q7-3; FATEC 2019 confere com a prova (texto e alternativas literais); Q9 FATEC 2014/2 com fonte.
- **Fatos conferidos:** Boole xy = x e a classe auxiliar não vazia; Peirce em 1883/1885, cunhou "quantificador", Π/Σ como conjunção/disjunção possivelmente infinitas, independente de Frege (1879); ∃ de Peano 1897 e Russell como operador; ∀ de Gentzen 1935 ("All-Zeichen", modelado no ∃ de Russell); Russell (x) em 1908; Ockham no séc. XIV e De Morgan (1806–1871); a passagem dos *Primeiros Analíticos* sobre a diagonal. Não há anedota sem marca nas Unid. 5 e 6.

## Fontes consultadas na web
- MacTutor, Miller, *Earliest Uses of Symbols of Set Theory and Logic*: https://mathshistory.st-andrews.ac.uk/Miller/mathsym/set/ (∃ Peano 1897 / Russell; ∀ Gentzen 1935; (x) Russell 1908).
- SEP, Ewald, *The Emergence of First-Order Logic*: https://plato.stanford.edu/entries/logic-firstorder-emergence/ (Boole; Peirce 1883/1885, "quantifier", Π/Σ; independência de Frege). O artigo não menciona Mitchell.
- Perrin, *Pourquoi y a-t-il beaucoup de nombres premiers de la forme n²+n+41?*: https://www.imo.universite-paris-saclay.fr/~perrin/journeedu2311/redaction2311e.pdf (Euler 1772, "41 − x + xx") → #13.
- Wikipedia, *Square of opposition*: https://en.wikipedia.org/wiki/Square_of_opposition (exemplos de *Da Interpretação* 7; diagrama atribuído a Boécio; A/E/I/O de *affirmo*/*nego*) → #1, #14.
- SEP, Parsons, *The Traditional Square of Opposition* (ed. 2008): https://plato.stanford.edu/archives/spr2008/entries/square/ (diagrama "already in the second century CE"; Boécio) → #1.
- Wikipedia, *De Morgan's laws* (via https://en.wikipedia.org/wiki/De_Morgan_dual): Ockham no séc. XIV, Buridan, "break the line, change the sign", exemplo de busca.
- Curso Objetivo, resolução FATEC 1º sem./2015: https://curso-objetivo.br/vestibular/resolucao_comentada/fatec/2015/fatec2015.pdf (q. 11: "Considere o exemplo", alternativas, gabarito B) → #23.
- Curso Objetivo, resolução FATEC 1º sem./2019: https://www.curso-objetivo.br/vestibular/resolucao_comentada/fatec/2019/fatec2019.pdf (q. 11 literal; gabarito B).
- Elpenor, *Prior Analytics* (Jenkinson), p. 41: https://www.ellopos.net/elpenor/greek-texts/ancient-greece/aristotle/prior-analytics.asp?pg=41 (frase da diagonal; página rotulada "Part 24") → #29.
- Buscas sem resultado conclusivo para os DOIs de Wason & Shapiro (1971) e Jevons (1870) → #31 fica "a conferir".
