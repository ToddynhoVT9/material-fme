# Revisão independente — Unidade 4 (Diferença e complementar) · Cap. II `v1c2-conjuntos`

- **Escopo:** `tex/u4_artigo.tex` (141 linhas), `tex/u4_partes.tex` (417 linhas), entradas de `tex/fontes.tex`
  usadas pela unidade, `dossies/u4.md`, bloco `n: 4` de `matriz.yaml`, PDF `tex/main.pdf` (páginas impressas
  43–55 = páginas 47–59 do PDF; o PDF é posterior aos `.tex`). Regras: `kit/didatica.md` (v4) e
  `kit/referencia/licoes-do-piloto.md`.
- **Não lidos** (conforme o brief): `verif/`, `revisoes/`, `ESTADO.md`.
- **Decisões locais respeitadas** (não apontadas como problema): D2 (bloco "Mais questões de vestibular"),
  D3 (diferença simétrica só como N3), D5 (etiqueta "[BANCA via FME, ano não informado]"), D7/D9.
- **Método:** leitura do LaTeX e das 13 páginas renderizadas (80 e 200 dpi); `checar.py --sem-compilar
  --unidades 4` (sem falhas nem avisos); script próprio em Python (força bruta sobre subconjuntos e análise
  elemento a elemento) para **todos** os exemplos, questões, contraexemplos dos erros e identidades das
  construções; conferência na web das afirmações históricas.

## Achados

| # | gravidade | arquivo:linha ou página | problema | evidência (seu cálculo, a fonte) | correção proposta |
|---|---|---|---|---|---|
| 1 | importante | `u4_partes.tex:218–220` (questão 6); `u4_artigo.tex:118` (caso 2, "Treino"); `u4_artigo.tex:138` (gatilho 2); p. 46 e 51 | A questão 6 (FME 53) declara **4-H3**, e o caso 2 e a linha de gatilho "complementar de ∪ ou de ∩ → De Morgan" mandam treinar nela. Mas $P'\cup(P\cap Q)$ não tem complementar de reunião nem de interseção, e a própria resolução usa a **distributiva** e $P'\cup P=U$ (propriedade 4-H2 (4)), sem De Morgan e sem $A-B=A\cap\overline B$. Conferência (a): o ID declarado não é treinado. E o gatilho manda o estudante a um item que não tem o sinal da linha. | Resposta: "Pela distributiva, $P'\cup(P\cap Q)=(P'\cup P)\cap(P'\cup Q)=U\cap(P'\cup Q)$". Conferi a identidade por força bruta (todos os pares de subconjuntos de um universo de 4 elementos): correta, mas o caminho natural não passa por H3. | Trocar o `\cobre` da questão 6 para `4-H2, 4-U2` (e a matriz). No caso 2 e no gatilho 2, apontar o treino para `\qref{u4:ita42}` (questão 9, N2), cujo item III, $B^C\cup C^C=(B\cap C)^C$, é exatamente o sinal da linha. A questão 6 pode continuar no "Treino" do caso 2 como simplificação. |
| 2 | importante | `u4_partes.tex:223` (questão 7, `\cobre`); `u4_partes.tex:22` (4-E2, "Onde aparece") | A questão 7 (FME 44) declara **4-E2** (De Morgan errado), e o erro 4-E2 remete a ela. Nenhum dos quatro itens tem complementar de reunião ou de interseção: (a) é a identidade da diferença simétrica, (b) a inversão da inclusão pelo complementar, (c) e (d) $A-B$ contra $\complement A$ e $\complement B$. Quem comete o erro 4-E2 acerta a questão 7 do mesmo jeito. | Leitura dos itens: nenhum envolve $\overline{A\cap B}$ nem $\overline{A\cup B}$. A cobertura de 4-E2 continua garantida pela questão 9 (item III; quem "distribui" marca III como falsa) e pela 14 (item III). | Tirar `4-E2` do `\cobre` da questão 7 (e da matriz) e trocar o "Onde aparece" do 4-E2 por "exemplo 4.5; \qref{u4:ita42}". Se quiser uma segunda remissão, use a questão 14 (`u4:ufpi38`) e acrescente 4-E2 ao `\cobre` dela e à matriz. A questão 7 continua treinando 4-H2 e 4-H3 (itens c e d usam $A-B=A\cap\overline B\subset\overline B$). |
| 3 | importante | `u4_partes.tex:57` (ex. 4.1, `\cobre`), `:158` (questão 1, `\cobre`); `u4_artigo.tex:111` (caso 1, "Treino"), `:137` (gatilho 1); p. 45, 46, 48, 51 | **4-U1** ("traduzir 'exceto', 'não', 'fora de'") não é treinado em nenhuma questão. A questão 1 (FME 38) e o exemplo 4.1 são cálculo simbólico, sem nenhuma palavra de exclusão, mas declaram 4-U1, e o gatilho "'exceto', 'que não' → q. 1" aponta para um item sem esse sinal. Só o exemplo 4.7 (turma) treina de fato a tradução. O prefácio ("traduzir 'exceto', 'não' e 'fora de' em operações") e a síntese prometem essa habilidade. A didática (§6) exige que todo U tenha ≥ 1 questão. | Os enunciados da questão 1 ("determine $A-B$, $B-A$, …") e do exemplo 4.1 ("Calcule: …") não trazem nenhuma das palavras do caso 1. Nenhuma outra questão N1/N2 da unidade tem enunciado verbal de exclusão (a 17, com "disjuntos de $B$", é N3). | Incluir uma questão N1 ou N2 autoral com enunciado verbal ("exceto", "que não", "nem … nem"), num contexto diferente do exemplo 4.7, e apontar o caso 1 e o gatilho 1 para ela. Tirar 4-U1 do `\cobre` do exemplo 4.1 e da questão 1, ou manter só no exemplo 4.7. A mesma questão pode resolver o achado 4 (ver abaixo). |
| 4 | importante | `u4_partes.tex:158` (questão 1, `\cobre` 4-E4); `u4_partes.tex:40` (4-E4, "Onde aparece") | A única questão que declara **4-E4** é a 1, e ela não põe o estudante diante do erro. O item (e), $A-(B\cap C)$, com conjuntos dados, se resolve calculando antes $B\cap C$; ninguém precisa distribuir a diferença. Não há item com $A-(B\cup C)$, e nada pede para comparar com $(A-B)\cup(A-C)$. Conferência (a), e a exigência do §6 (todo E com ≥ 1 questão) fica cumprida só no papel. | Cálculo: $B\cap C=\{d,e,g\}$, $A-\{d,e,g\}=\{a,b,c\}$ (caminho direto). Só quem decidisse distribuir cairia no erro dual, $(A-B)\cap(A-C)=\{a,b\}\cap\{a,c\}=\{a\}$. O exemplo 4.7 (c) treina o 4-E4 porque pede a comparação ("Compare com …"). A questão 13 (N3) também envolve o 4-E4, mas não pode ser remissão de erro. | Opção 1: a questão nova do achado 3 pede "quem não está nem em … nem em …" e a comparação com $(X-Y)\cup(X-Z)$. Ela treina 4-U1 e 4-E4 juntos e passa a ser o "Onde aparece" do 4-E4. Opção 2: acrescentar à questão 1 o item "compare (e) com $(A-B)\cap(A-C)$ e com $(A-B)\cup(A-C)$" e trocar a etiqueta para "[adaptado do FME, exercício 38]". |
| 5 | menor | `u4_artigo.tex:51`; p. 44 | "nas décadas de 1840": 1846 e 1847 são da mesma década. | A primeira formulação é de 1846 (artigo lido em 9/11/1846 na Cambridge Philosophical Society), e *Formal Logic* é de 1847 (Open Book Publishers, cap. 2; Britannica). | "na década de 1840" ou "em 1846–1847". |
| 6 | menor | `u4_artigo.tex:51`; p. 44 | Três camadas: o texto põe *universo do discurso*, em itálico, como termo de De Morgan ("esgotassem o *universo do discurso*"). De Morgan escreveu "universe of a proposition, or of a name". O nome "universe of discourse" aparece em Boole (*Laws of Thought*, 1854). Britannica e encPhil usam a expressão moderna para descrever a ideia, o que sustenta a ideia, não o rótulo. | Open Book Publishers, *De Morgan and Logic*, cap. 2: "universe of a proposition, or of a name" (p. 380 do artigo de 1846). Wikipedia, "Domain of discourse": "The phrase universe of discourse was used by George Boole in Laws of Thought (1854)". | "… de modo que $X$ e $x$, juntos, esgotassem o 'universo' daquilo de que se fala — hoje chamado *universo do discurso* —". Assim o rótulo fica na camada moderna. |
| 7 | menor | `u4_artigo.tex:51`; p. 44 | Ambiguidade (g): "A convenção atual é a mesma" — a mesma que quê? (o referente é a ideia de De Morgan, duas frases antes). | Leitura. | "A convenção atual mantém essa exigência: antes de falar em complementar, fixe o universo." |
| 8 | menor | `u4_artigo.tex:20`; p. 43 | Os pré-requisitos e "O mínimo" omitem a Unidade 2, mas a unidade a usa: "Elemento genérico (Unidade 2)" (ex. 4.2), $B\subset A$ (4-H2), $n(\mathcal P(\cdot))$ e $2^n$ (questões 10, 16 e 17). | `u4_partes.tex:79` remete à Unidade 2. $\mathcal P$ e $n(X)$ são definidos em `u2_artigo.tex:97–115`. | Pré-requisitos: "Unidades 1 a 3 (universo; inclusão e conjunto das partes; reunião, interseção e regiões)". Se couber, um item em "O mínimo": "$B\subset A$: todo elemento de $B$ está em $A$; $\mathcal P(A)$ tem $2^n$ elementos (Unidade 2)". |
| 9 | menor | `u4_partes.tex:303` (resp. 12); p. 55 | Frase tautológica na resposta: "Se $x\in A$, então $x\in A$, mas $x$ não está em $A-B$ nem em $B-A$". | A ideia certa: $x\in A\cap B$ está no lado direito ($A$), mas não no esquerdo. Conferi por força bruta (universo de 4 elementos) que não há $A,B\neq\varnothing$ com $(A-B)\cup(B-A)=A$. | "Se $x\in A$, então $x\in A\cap B$: está em $A$, mas não está em $A-B$ nem em $B-A$, isto é, não está no lado esquerdo — contradição." |
| 10 | menor | `abertura.tex:57` × respostas da U4 (`u4_partes.tex:220, 256, 270, 303, 317, 380, 394`) | A abertura promete "As respostas trazem só o resultado final […] Nas questões de demonstração, a resposta diz, em uma linha, o que a prova deve mostrar" (didática §2.9). Várias respostas trazem a justificativa, e a 12 traz a prova inteira (3 linhas). O mesmo padrão já aparece na U3 (p. ex., resposta "27. Cada elemento de …"), então parece convenção do capítulo. | Comparação direta dos textos. | Decidir no capítulo: ou enxugar (resp. 12: "Não existem: a prova deve mostrar que $B\neq\varnothing$ leva a contradição"), ou registrar no `ESTADO.md` que respostas de múltipla escolha e de "analise" trazem a justificativa em uma ou duas linhas. |
| 11 | menor | `u4_artigo.tex:129–131` × `:140`; p. 46 | Caso 4 e gatilho 4 divergem na ferramenta: o caso diz "decidir região a região ou elemento a elemento, como na Unidade 3" (sem ID); o gatilho diz "4-H1, 4-H2". | Leitura. | No caso 4, "Ferramenta: 4-H1 (4) e 4-H2 — traduzir cada dado para uma região (ou elemento a elemento)", alinhado ao gatilho. |
| 12 | menor | `u4_artigo.tex:114–133`; p. 46 | Os casos 2 e 4 não têm enunciado real com procedência (didática §2.3: os casos vêm "com 'Como reconhecer' e um enunciado real com procedência"). O dossiê tirou os candidatos por D7 (eram N2 da unidade). O critério de aceitação do §2.3 não exige o enunciado, e a U3 tem caso no mesmo padrão. | `dossies/u4.md:95–97` ("sinal genérico"). | Opcional: usar um enunciado de prova que não esteja na unidade (ou só o comando, como no caso 3). Ou deixar como está, com a decisão registrada. |
| 13 | menor | `u4_partes.tex:368` (questão 16); p. 54 | Ambiguidade (g): "dupla ordenada" não é definida no capítulo (par ordenado é assunto posterior). O texto é da prova e tem de ficar. | `grep` em `tex/`: o termo só aparece aqui. | Uma nota curta depois do enunciado: "(dupla ordenada: o par $(n(A),n(B))$, com a ordem importando)". |
| 14 | menor | p. 46 (caso 2, linha "O enunciado diz"; tabela de gatilhos, linha 2); p. 52 (questão 11 e, 1º diagrama) | Visual: no caso 2, "e −" fica sozinho na linha seguinte, e a barra $\overline{\phantom{A}}$ sai flutuando, sem letra. Na tabela de gatilhos, "∩" fica sozinho na 2ª linha da célula. Na questão 11 (e), os rótulos $A$ e $B$ do 1º diagrama encostam no traço dos círculos. | Imagens das páginas a 200 dpi. | Caso 2: "expressões com barra ($\overline{A}$), expoente $^{C}$, apóstrofo ($A'$) ou 'complementar de', combinadas com $\cup$, $\cap$ e $-$". Gatilho: "complementar de reunião ou de interseção". Questão 11: afastar os nós, p. ex. `(-2.0,1.3)` e `(2.0,1.3)`. |

## Conferido sem problemas

- **Respostas (item 3 do brief):** todas conferem com o meu cálculo. Exemplos 4.1–4.8, contraexemplos
  de 4-E1 a 4-E4, exemplos de 4-H1 (2)–(3) e 4-H2 (1), identidades de 4-H3 (3) e as questões 1–17. Unicidade
  verificada nas questões 5, 8 e 10 e no exemplo 4.6 (uma só solução). Questão 13: análise elemento a
  elemento dos 16 padrões de pertinência a $X,Y,Z,W$, para $0\le e\le 11$; o conjunto é $\{1,3,7,8\}$ (c),
  e nenhum elemento fora de $1..8$ entra. Questão 16: só $n(B)-n(A)=7$ é forçado; a soma não tem cota, e
  há vários pares (a). Questão 17: $\sum_{k\le6}\binom8k=247=2^8-9$ (a). Python: `set('abracadabra') -
  set('alacazam')` = `{'r','d','b'}` (caso 1).
- **(b) Nenhum N3 antecipado:** os treinos dos casos, os gatilhos e os "Onde aparece" dos erros apontam só
  para N1 e N2 (`checar.py` sem avisos). A diferença simétrica (questão 11) não aparece no texto. A
  identidade $(A-B)\cup(B-A)=(A\cup B)-(A\cap B)$ só aparece em questões (7a, 15-III). A H1 (4) dá só a
  ferramenta geral ("só $A$", "só $B$"). O exemplo 4.8 (N3) trata $A-B=B-A$, outro caso, não a questão 12.
  "Disjunto ⇔ contido em $A-B$" (questão 17) não é antecipado.
- **D7/D9:** nenhum erro, caso, construção ou prefácio usa o caso concreto de uma questão N2. O contraexemplo
  de 4-E2 ($U=\{1..4\}$) é distinto do exemplo 4.5. 4-H3 (3) é enunciada em geral.
- **(c) Integradoras:** 4 (complementar em $E$), 16 ($B-A$ com $A\subset B$) e 17 ($\complement_A B$) não se
  resolvem sem a unidade.
- **(e) Ordem dentro do nível:** sequência principal N1 1→4, N2 5→10, N3 11→13; no bloco D2, N2 14→16, N3 17.
  Integradoras no fim do nível. Bate com o dossiê.
- **(f) Camada opcional:** O1 (notações $\complement_U A$, $A\setminus B$) e O2 (Ockham) não guardam nada
  usado fora delas. As notações usadas nas questões ($X'$, $\complement A$, $B^C$) estão em 4-H2 (2) ou são
  definidas no enunciado.
- **(g)** De Morgan e Ockham são apresentados antes de citados. O FME não é citado no corpo do texto: só em
  etiquetas e `\src`. O comando do caso 3 vem entre aspas, com `\src{fme}`.
- **Síntese:** os ponteiros (construção 4-H2, construção 4-H3, Onde é usado?, Erros comuns) existem. "Para
  lembrar" está na p. 45, como indicado.
- **Enunciados:** todos os enunciados do LaTeX batem com as transcrições do dossiê (§6, notas). Procedências
  coerentes com o dossiê e com o §5 (FME, adaptado do FME 42, "[ITA/UF-PI via FME, ano não informado]"). O
  exemplo 4.1 é autoral; a tabela do dossiê ainda diz "adaptado", mas a nota de ajuste do próprio dossiê
  explica a troca.
- **Matriz:** os rótulos, os níveis e as integradoras batem com o LaTeX. A sequência principal (4/6/3)
  supera a meta (4/5/2), como na U3.
- **Fatos:** `\src` presentes e pertinentes (ver abaixo). O filtro P5 passa: a história de De Morgan explica
  por que o complementar exige universo e por que $\cap$ e $\cup$ trocam, e Ockham fica na observação.
- **Visual:** nenhuma caixa cortada, tabela estourada ou lista com `\mbox`. Os diagramas do exemplo 4.3
  sombreiam as regiões certas.

## Fontes consultadas na web

1. Encyclopaedia Britannica, "History of logic: Boole and De Morgan" — confirma: De Morgan "did introduce
   the enormously influential notion of a possibly arbitrary and stipulated 'universe of discourse'"; "a
   lowercase letter represented its complement relative to the universe of discourse"; *Formal Logic* em 1847.
   https://www.britannica.com/topic/history-of-logic/Boole-and-De-Morgan
2. "Modern Logic: The Boolean Period: De Morgan", *Encyclopedia of Philosophy* (Encyclopedia.com) — confirma:
   "a term X and its 'contrary' x between them exhaust the 'universe of discourse'"; registra também que De
   Morgan "did not, in fact, invent" as leis (coerente com 4-O2).
   https://encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/modern-logic-boolean-period-de-morgan
3. S. Burris, *notes1.pdf* (Waterloo) — confirma a citação "The contrary of PQ is p,q; that of P,Q is pq"
   ([4], p. 118). Está no Prelúdio e no cap. 3 (De Morgan), onde se explica que justaposição = interseção e
   vírgula = reunião. https://www.math.uwaterloo.ca/~snburris/htdocs/LOGIC/LOGICIANS/notes1.pdf
4. Encyclopaedia Britannica, "Augustus De Morgan" — confirma "Known verbally by William of Ockham in the 14th
   century" e "expressed mathematically by De Morgan" (4-O2); "English mathematician and logician".
   https://www.britannica.com/biography/Augustus-De-Morgan
5. Open Book Publishers, *De Morgan and Logic*, cap. 2 — datação: universo e contrários introduzidos no artigo
   lido em 9/11/1846 (Trans. Cambridge Phil. Soc. 8); termo de De Morgan: "universe of a proposition, or of a
   name". https://books.openbookpublishers.com/10.11647/obp.0408/ch2.xhtml
6. Wikipedia, "Domain of discourse" (versão de nov/2026) — "The phrase universe of discourse was used by
   George Boole in Laws of Thought (1854)". https://en.wikipedia.org/wiki/Domain_of_discourse
7. Python Tutorial §5.4 — a página não pôde ser aberta nesta sessão (domínio fora da lista permitida). O
   resultado `{'r','d','b'}` foi conferido executando o código.

## Contagem

- bloqueante: 0
- importante: 4 (achados 1–4)
- menor: 10 (achados 5–14)
