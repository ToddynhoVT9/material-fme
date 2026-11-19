# q3 — Pesquisa da Unidade 3 (Condicional e bicondicional)

Pipeline v2 (w10), padrão c1. Etiquetas: `[documentado]`, `[relato]` (autor antigo), `[anedota]`, `[fraco — fora do texto]`.

## 1. História

### 1.1 A escola dialética: Diodoro e Fílon
- Diodoro Crono e Fílon, o Lógico, são os dois membros mais conhecidos da "escola dialética" (fim do séc. IV – meados do séc. III a.C.); Fílon estudou com Diodoro. `[documentado]` — SEP, *Dialectical School*.
- Fílon foi amigo de Zenão de Cítio (fundador do estoicismo), segundo Diógenes Laércio; Crisipo escreveu duas obras em resposta a livros de Fílon. `[documentado]` — Wikipedia, *Philo the Dialectician* (cita DL).
- SEP: Fílon introduziu uma versão da implicação material; Diodoro, uma precursora da implicação estrita. `[documentado]`

### 1.2 Os quatro critérios (Sexto Empírico, *Hipotiposes Pirrônicas* 2.110–113)
- Fílon: condicional correto é o que não tem antecedente verdadeiro e consequente falso; exemplo: quando é dia e eu converso, "se é dia, eu converso" é correto. `[relato de Sexto]` — LS 35B (tradução Long & Sedley).
- Diodoro: o que nem podia nem pode ter antecedente verdadeiro e consequente falso. `[relato]`
- "Coesão": correto quando o contraditório do consequente conflita com o antecedente. `[relato]` (atribuído em geral aos estoicos; Sexto não dá nome)
- "Inclusão": o consequente está contido potencialmente no antecedente; nesse critério, "se é dia, é dia" seria falso. `[relato]`
- Os quatro aparecem em ordem crescente de força lógica. `[documentado]` — *History and Philosophy of Logic*, artigo sobre o 4º condicional de Sexto (resumo).
- Sexto (*Adv. Math.* 8) diz que, para Fílon, um condicional pode ser verdadeiro de três modos e falso de um. `[relato]` — Wikipedia, *Philo the Dialectician*.

### 1.3 Os corvos de Calímaco
- Epigrama de Calímaco (fr. 393 Pfeiffer) sobre Diodoro: os corvos nos telhados perguntam "o que se segue de quê?", alusão às disputas helenísticas sobre a verdade dos condicionais. Sexto comenta o epigrama em *M.* 1.309–12. `[documentado]` — M. J. White, "What worried the crows?", *Classical Quarterly*.

### 1.4 Implicação material e suas críticas
- *Principia Mathematica* (1910) usa a "implicação material" de Russell para o "se… então". A partir de 1912, C. I. Lewis objetou: com ela, uma proposição falsa implica qualquer proposição. `[documentado]` — C. I. Lewis (Wikipedia); Open Logic Project (pt), *Paradoxes of the material conditional*; artigo em *Organon F* (2019) sobre o centenário do *Survey of Symbolic Logic*.
- Lewis propôs a "implicação estrita" e a axiomatizou no *Survey of Symbolic Logic* (1918), primeiro sistema formal de lógica modal. `[documentado]` — *Organon F* (2019).
- Lewis não chamava os resultados de "paradoxos"; dizia que eram "um tanto surpreendentes", "suspeitos ao senso comum". `[documentado]` — Shieh, cap. em *Pragmatism in Transition* (Springer).

### 1.5 Símbolos e "iff"
- → Hilbert (1922); ↔ A. Becker (1933); ⇒ e ⇔ Bourbaki (1954). `[documentado]` — Miller (MacTutor).
- "iff": impresso pela primeira vez em *General Topology* de J. L. Kelley (1955); invenção atribuída a Paul Halmos, que disse tê-la inventado mas duvidar de ter sido o primeiro. `[documentado]` — Wikipedia, *If and only if*.

### 1.6 Wason (1966/1968)
- Tarefa de seleção, criada em 1966 (Wason 1966, 1968). No estudo de Wason, menos de 10% acertaram. `[documentado]` — Wikipedia, *Wason selection task*.
- Wason & Shapiro (1971): ~4% escolhem a resposta logicamente correta na versão abstrata; ~45% escolhem "A e 4". `[documentado]` — Psychology in Action (resumo de Wason & Shapiro 1971); artigo original (*QJEP* 23, 63–71).
- Griggs & Cox (1982/1983): com a regra de idade para beber cerveja, a maioria acerta. `[documentado]` — material de aula da Univ. de Sussex.
- Cosmides (1989): hipótese do "contrato social" / detecção de trapaceiros; a explicação é disputada (Sperber & Girotto). `[documentado]` — Nautilus; Sperber & Girotto (CORE).

### 1.7 Os corvos de Hempel (contrapositiva)
- Hempel (1945): "todos os corvos são pretos" equivale a "tudo o que não é preto não é corvo"; se observar exemplos confirma, então uma maçã verde confirmaria que os corvos são pretos. `[documentado]` — Wikipedia, *Raven paradox*; Fitelson (2006), *Philosophy Compass*.
- Vira a nova observação **3-O3**, que liga os corvos de Calímaco aos de Hempel (coincidência temática, não histórica).

## 2. Uso
- Teoremas: hipótese → tese; recíproca de um teorema nem sempre vale; definições escritas com "se" querem dizer "se, e somente se".
- Provas: OBMEP 2007 (bolo de César), Simulado OBMEP 2017 N3 q14 (Ari, Bruna, Carlos), OBMEP 2011 (Tia Geralda); concursos: "sabe-se que a afirmação… é falsa".
- Computação: o `if` das linguagens é controle de fluxo, não conectivo; a igualdade de booleanos (`==`) é o ↔; XNOR.

## 3. Questões e transcrições
- **FME ex. 4–6** transcritos da página renderizada (p. 9). Respostas recalculadas no script.
- **OBMEP 2007, 1ª fase, N2 q8 (bolo de César)** — texto do FME = prova (q4); gabarito (d).
- **Ari, Bruna e Carlos** — FME V4 = Simulado OBMEP 2017 N3 q14 (q4); o FME imprime as alternativas fora de ordem (a, b, c, e, d) — reordenadas; gabarito (a).
- **Tia Geralda** — Simulado OBMEP 2017 N2 q12 (= OBMEP 2011). O texto integral não pôde ser copiado; a questão entra **reescrita** com etiqueta `[adaptada de OBMEP 2011]`.
- **VUNESP/TJ-SP ("Se Ana é gerente…")**: ano não localizado nesta rodada → **sai do banco** (w4); substituída por autoral no mesmo formato.

## 4. Fontes novas
sepDialectical · philoWiki · ls35b · hplFourth · whiteCrows · lewisWiki · openlogicPar · organonF · shieh · iffWiki · wasonWiki · psyAction · wasonShapiro · sussexWason · nautilus · sperber · ravenWiki · fitelson · obmep2007 · simulado2017
