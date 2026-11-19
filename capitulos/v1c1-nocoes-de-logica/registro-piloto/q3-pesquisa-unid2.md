# q3 — Pesquisa da Unidade 2 (Conectivos ∧ e ∨)

Pipeline v2 (w10). Rodada única de pesquisa profunda para a unidade, já no padrão c1 (artigo destacável, sem limite de extensão).
Etiquetas: `[documentado]` = fonte consultada nesta rodada ou na rodada 1; `[relato]` = fato transmitido por autor antigo (Sexto, Plutarco), cuja veracidade não se pode checar; `[anedota]` = história ilustrativa.

## 1. História

### 1.1 Antes dos estoicos
- Teofrasto (c. 371–c. 286 a.C.), sucessor de Aristóteles, foi o primeiro de quem se sabe que examinou a sério proposições compostas ("p ou q", "se p então q"); a investigação sistemática só veio com os estoicos. `[documentado]` — Britannica, *Ancient logic: Theophrastus*.

### 1.2 Estoicos: conjunção, disjunção e os indemonstráveis
- Conectivos estoicos são verofuncionais: o valor da composta depende só do valor das partes. `[documentado]` — Bobzien (*Stoic Logic*, rodada 1); apcz.umk.pl (rodada anterior da Unid. 2).
- Conjunção verdadeira ⇔ todas as partes verdadeiras. A disjunção estoica padrão (*diezeugmenon*) é **exclusiva**: exatamente uma parte verdadeira (Cícero, *Topica*). `[documentado]` — Bobzien; Britannica.
- Os estoicos conheciam também a disjunção **inclusiva** ("verdadeira se ao menos uma parte for verdadeira"), mas ela era pouco usada. `[documentado]` — Britannica, *inclusive disjunction*.
- Galeno (séc. II d.C.) teria distinguido três usos do "ou" na *Introdução à dialética* (Malatesta, citado num blog). `[fraco — não entra no texto]`.
- Os cinco indemonstráveis (Sexto, *Adv. Math.* 8.223; Diógenes Laércio 7.79–81). 3º: "não ambos o 1º e o 2º; o 1º; logo, não o 2º". 4º: "ou o 1º ou o 2º; o 1º; logo, não o 2º". 5º: "ou o 1º ou o 2º; não o 1º; logo, o 2º". `[documentado]` — Project Euclid (NDJFL); Bobzien.
- **O cão de Crisipo**: diante de uma encruzilhada tripla, o cão fareja dois caminhos e segue pelo terceiro sem farejar; Crisipo teria dito que o animal usa o 5º indemonstrável. `[relato de Sexto Empírico]` — Aberdein, "Logic for dogs" (PhilArchive ABELFD).

### 1.3 Crisipo × Hiparco: contar compostas (2-O1)
- Plutarco (*Quaest. conv.* VIII.9; *De Stoic. rep.* 29): Crisipo disse que, com dez assertíveis, formam-se mais de um milhão de conjunções; Hiparco "refutou", com 103 049 do lado afirmativo e 310 952 do negativo. `[relato]` — MathWorld, *Plutarch numbers*; tradução de Goodwin (Perseids).
- 1994: David Hough nota que 103 049 é o 10º número de Schröder "pequeno" (número de parentetizações de 10 letras); publicado por Stanley (1997). Habsieger, Kazarian e Lando (1998): (s₁₀+s₁₁)/2 = 310 954, a 2 unidades do segundo número. `[documentado]` — MathWorld; MathPages.
- Bobzien (*Oxford Studies in Ancient Philosophy* 40, 2011) argumenta que, dentro da lógica estoica, Crisipo tinha razão. `[documentado]` — título e resumo do artigo.
- Uso didático: contraste entre "contar linhas da tabela" (2ⁿ) e "contar fórmulas" (explode muito mais rápido).

### 1.4 Boole, Jevons, Peirce
- Boole: produto xy = "e" (interseção de classes); soma x + y só faz sentido para classes **disjuntas** (leitura exclusiva). `[documentado]` — arXiv 1710.01542; Peirce (1870) citado em lista de discussão.
- Jevons (*Pure Logic*, 1864) critica a preferência de Boole pelo "ou" exclusivo e adota a soma **inclusiva**; Peirce, nos anos 1860, propõe o mesmo. Praticamente todos os lógicos posteriores seguem a leitura inclusiva. `[documentado]` — IEEE Computer Society, *Jevons*; Britannica, *Boole and De Morgan*; Couturat (*Algebra of Logic*, Project Euclid).
- Boole escreveu um manuscrito de resposta às críticas de Jevons (c. 1863) e não adotou a leitura inclusiva. `[documentado]` — Waszek (2025).
- Piano lógico de Jevons: construído em 1869 por um relojoeiro de Salford; apresentado à Royal Society em 1870 (*Phil. Trans.* 160, 497–518); está no Museu de História da Ciência de Oxford; mostra as 16 combinações de 4 termos. `[documentado]` — historyofinformation.com; MacTutor *Jevons*; computerhistory.org.

### 1.5 Frege: "e" e "mas"
- *Begriffsschrift* (1879): "e" e "mas" têm o mesmo conteúdo conceitual e diferem só no "colorido" (*Färbung*). `[documentado]` — core.ac.uk 237398527; Bussière-Caraes (PhilArchive BUSCWC).

### 1.6 Venn (1880)
- "On the Diagrammatic and Mechanical Representation of Propositions and Reasonings", *Philosophical Magazine*, jul. 1880. Venn chamava seus desenhos de "círculos eulerianos"; o termo "diagrama de Venn" aparece com C. I. Lewis (1918). `[documentado]` — Ruskey & Weston, *Venn Diagram Survey* (EJC); DOI 10.1080/14786448008626877.

### 1.7 Shannon (1937)
- Dissertação de mestrado no MIT, assinada em 10/8/1937, publicada nas *Trans. AIEE* em 1938. Série ↔ "e"; paralelo ↔ "ou". `[documentado]` — MIT DSpace; LibreTexts (cita entrevista de Shannon a Liversidge, 1993).
- Shannon usou a convenção oposta à de hoje: trabalhava com "obstrução" (*hindrance*), com 1 = circuito aberto, e por isso escrevia + para a ligação **em série**. A convenção atual (1 = fechado; série = produto; paralelo = soma) veio depois. `[documentado]` — Springer (*Exploring the Early Digital*); Springer (*Key Topics*); texto da dissertação ("let the symbol + be defined to mean the series connection").

### 1.8 Símbolos
- ∨: origem nos trabalhos de Whitehead e Russell **anteriores** aos *Principia* (c. 1903); Peano usava ∪ e nunca ∨; a etimologia "∨ = *vel*" é mito. A adoção por Hilbert (*Grundzüge*, 1928) garantiu a difusão. `[documentado]` — Elkind & Zach, *Review of Symbolic Logic* 16(3), 2023.
- ∧: Heyting (1930); os *Principia* usavam o ponto (p.q). `[documentado]` — Miller (rodada 1).

## 2. Uso

- Intervalos e inequações: "−3 < x ≤ 2" é conjunção; "x ≤ 3" é a disjunção "x < 3 ou x = 3" (é o 2º exemplo do próprio FME, item 4).
- Produto nulo: ab = 0 ⇔ a = 0 ∨ b = 0 (disjunção inclusiva: ambos podem ser zero).
- Conjuntos (Cap. II): A ∩ B = {x | x ∈ A ∧ x ∈ B}; A ∪ B = {x | x ∈ A ∨ x ∈ B}.
- Provas: FME ex. 3 (classificar compostas); OBMEP 2009 (restrições simultâneas); OBMEP 2005 ("apenas uma é verdadeira").
- Computação: `and`/`&&`, `or`/`||`; avaliação de curto-circuito; portas AND/OR; operadores de busca.
- Língua: "mas", "porém", "contudo" = conjunção com contraste (Frege); "nem… nem…" = ~p ∧ ~q; "ou" do garçom costuma ser exclusivo; "Pedro e Paulo carregaram o piano" não é conjunção de proposições (predicado coletivo) → nova observação 2-O4.

## 3. Questões e transcrições (feitas a partir das páginas renderizadas, w4)

- **FME, exercício 3** (p. 6): a) 3 > 1 e 4 > 2; b) 3 > 1 ou 3 = 1; c) 2 | 4 ou 2 | (4 + 1); d) 3(5 + 2) = 3·5 + 3·2 e 3 | 7; e) 1/2 < 3/4 ou 5 | 11; f) (−1)⁶ = −1 e 2⁵ < (−2)⁷; g) √16 = 6 ou mdc(4, 7) = 2. Respostas do FME: V, V, V, F, V, F, F (confere com script).
- **OBMEP 2009, 1ª fase, N3 q4** (= FME V3): texto do FME = texto da prova (q4). Resposta (c).
- **OBMEP 2005, 1ª fase, N3 q20** (= FME V5): **texto original obtido** (PDF da prova, cópia no site do IFES). Alternativas na prova: A) 16, B) 13, C) 11, D) 5, E) 1. Resposta **(A)**. O FME inverte a ordem (16 vira "e"). Fonte: st.ifes.edu.br, prova_nivel3.

## 4. Fontes novas (chaves para `fontes.tex`)
theophrastus · britIncl · euclidStoic · aberdein · plutarchNum · mathpages · bobzienComb · arxivBoole · ieeeJevons · britBoole · historyInfo · fregeColor · venn · shannonMIT · shannonConv · elkindZach · obmep2005 · obmep2009
