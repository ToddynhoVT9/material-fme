# ESTADO — Cap. II · Conjuntos

> Painel do capítulo. **Toda sessão começa lendo este arquivo e termina atualizando-o.**
> O que não está aqui (ou nos arquivos que ele aponta) não existe para a próxima sessão.

- volume: 1
- número: 2
- título: Conjuntos
- criado: 2026-11-19
- didática: v4 (desde 2026-11-20; a U1 já atende) (`kit/didatica.md`)
- material de entrada: PDF `02 - Cap II - Conjuntos.pdf` (35 p.: teoria itens 19–40, exercícios 11–61, Leitura, respostas, vestibulares 7–47 e respostas), entregue pelo usuário em 2026-11-19. **Não versionado** (texto do livro; o repositório é público): anexar de novo nas sessões de montagem. Mapa das páginas: `escopo.md` §1.

## Próxima ação
Dossiê da U3 (Reunião e interseção). Seguir a didática v4 e D7 (estendida: nem a construção resolve sentença de questão N2).

## Unidades
| U | título | etapa | revisão | observação |
|---|---|---|---|---|
| 1 | Conjunto, elemento e descrição | calibrada (pronta) | R1 (revisor independente): 0 · 6 · 19, todos tratados | `verif/u1.py` 47 OK; checar 0/0 |
| 2 | Igualdade, inclusão e conjunto das partes | pronta | R1 (revisor independente): 0 · 4 · 17, todos tratados | `verif/u2.py` 23 OK; checar 0/0 |
| 3 | Reunião e interseção | escopo | — | — |
| 4 | Diferença e complementar | escopo | — | — |
| 5 | Contando elementos: dois conjuntos | escopo | — | — |
| 6 | Três conjuntos e as regiões do diagrama | escopo | — | — |
<!-- FIM UNIDADES -->

Etapas de uma unidade: `escopo` → `dossiê` → `montagem` → `revisão` → `pronta`.
Fechamento do capítulo (depois de todas `pronta`): abertura, glossário, fontes, conferência entre unidades, PDF final.

## Portões com o usuário
- [x] Escopo aprovado (2026-11-19, D1–D5)
- [ ] Calibração: U1 pronta e aprovada pelo usuário, antes de montar as demais
- [ ] PDF final entregue — etapa 5

## Decisões do capítulo
| # | data | decisão | origem |
|---|---|---|---|
| C1 | 2026-11-19 | transcrever enunciado de questão com zoom de 200 dpi e conferir contra a camada de texto (a leitura em página dupla a 110 dpi errou a vest. 30) | escopo §1 |
| C2 | 2026-11-19 | o PDF do FME e a camada de texto não entram no repositório (público); só referências a páginas | escopo §1 |
| D1 | 2026-11-19 | seis unidades (U5 dois conjuntos, U6 três conjuntos) | usuário |
| D2 | 2026-11-19 | Questões seguem as metas (escolhidas pela função, cobrindo todos os U/E); o resto do FME vai para um bloco **"Mais questões de vestibular"** no fim da seção Questões, ordenado por nível, sem meta, com respostas (vale para qualquer unidade em que o FME passe da meta). Decisão local; a didática não muda | usuário |
| D3 | 2026-11-19 | lacunas do FME como construção: complementar em U (4-H2), n(A ∪ B) (5-H1), n(A ∪ B ∪ C) (6-H3), n(𝒫(A)) = 2ⁿ (2-H4); diferença simétrica só como questão N3 da U4, definida no enunciado | usuário |
| D4 | 2026-11-19 | resposta correta nas divergências; questões com problema de redação (13e, 14, 42b) em versão adaptada, etiqueta "[adaptado do FME, exercício n]" | usuário |
| D6 | 2026-11-19 | usar a notação {expressão \| condição} (ex.: {2ⁿ \| n ∈ ℕ}), apresentada em 1-H2 | usuário |
| D7 | 2026-11-19 | erro, caso do mapa ou prefácio **não** usam o mesmo caso concreto (equação, lista, conjunto) de uma questão N2 — senão a questão vira cópia (achado 5 da revisão da U1) | revisão U1 |
| D8 | 2026-11-20 | **calibração da U1** (usuário): tom, *Onde é usado?* e dificuldade das questões aprovados. Regras daqui em diante: (a) não citar o FME no corpo do texto ("o FME tem um exercício…", "aparece assim no FME"): a procedência fica só na etiqueta e no `\src`; (b) "Como reconhecer" descreve o sinal no enunciado, não onde a questão aparece; (c) reler cada parágrafo do artigo procurando ambiguidade (referente de pronome, termo sem explicação, frase que admite duas leituras); (d) o prefácio fala do capítulo, não do volume. **(a)–(c) promovidas à didática v4** (2026-11-20) | usuário |
| D9 | 2026-11-20 | D7 estendida: a **construção** (De onde vem?) também não usa o mesmo caso concreto de uma sentença de questão N2 (achado 5 da revisão da U2) | revisão U2 |
| D5 | 2026-11-19 | vestibulares do FME com etiqueta "[BANCA via FME, ano não informado]", sem procurar o ano | usuário |

Decisões locais deste capítulo. Mudança na **didática** só com o usuário, como nova versão em `kit/didatica.md`.

## Pendências
- Divergências do gabarito do FME (`verif/fme.py`): ex. 13e, 14B/C (redação), 42f, vest. 36 — `escopo.md` §7.
- Leitura do FME com atribuições a conferir antes de qualquer uso (Arquimedes × Aristóteles; Dedekind 1872 × 1888) — `escopo.md` M13.

## Registro de sessões
| data | etapa · unidade | o que foi feito | checar.py ao sair |
|---|---|---|---|
| 2026-11-19 | 1 · escopo | esqueleto (6 unidades); leitura visual das 35 p.; inventário (22 itens de teoria, 51 exercícios, 41 vestibulares); `verif/fme.py` (98 conferências, 0 falhas, 5 divergências); IDs e metas na matriz | compila (26 p.); só FALHAS de cobertura da matriz, esperadas antes da montagem |
| 2026-11-19 | 2 · U1 | escopo aprovado (D1–D5); dossiê da U1: história M1–M4 (SEP: Ferreirós, Irvine & Deutsch, Hallett), mapa com 4 casos, E1–E4, banco X1–X6 / P1–P14; O1/O2 trocados na matriz | `verif/u1.py` 42 OK, 0 falha; checar.py não rodado (nada de LaTeX mudou) |
| 2026-11-19 | 3 · U1 | montagem: artigo (4 construções, 2 definições, 4 casos, 6 gatilhos), 4 erros, 2 obs., 6 exemplos (N1 2 · N2 3 · N3 1), 14 questões (N1 5 · N2 6 · N3 3; 2 integradoras); 7 fontes novas; autoconferência §7 feita (u1:parametro deixou de ser integradora: resolve-se só com o discriminante) | 0 FALHAS · 0 AVISOS (37 p.); folhas conferidas |
| 2026-11-19 | 4 · U1 | revisão independente (0 bloqueante, 6 importantes, 19 menores); todos aplicados ou decididos (`revisoes/u1.md`); PDF de calibração em `saida/` | 0 FALHAS · 0 AVISOS; verif 47 OK |
| 2026-11-20 | calibração · U1 + didática v4 + 2 · U2 | ajustes da calibração (D8); didática v4 registrada no kit; dossiê da U2: história M1–M3 (Zermelo/extensionalidade, Peano/ε, Frege/cair sob × subordinação; SEP, MacTutor, Park 2018), O2 Galileu, mapa com 3 casos, E1–E5, banco X1–X6 / P1–P14; M15 (vest. 45 com alternativa repetida) | U1: 0/0, verif 47 OK; `verif/u2.py` 20 OK |
| 2026-11-20 | 3 · U2 | montagem: artigo (4 construções, 2 definições, 3 casos, 4 gatilhos; Zermelo, Peano, Frege em três camadas), 5 erros, 3 obs., 6 exemplos (N1 2 · N2 3 · N3 1), 14 questões (N1 4 · N2 7 · N3 3; 1 integradora); 7 fontes novas; autoconferência (a)–(g) feita | 0 FALHAS · 0 AVISOS (U1+U2, 47 p.); folhas conferidas |
| 2026-11-20 | 4 · U2 | revisão independente (0 bloqueante, 4 importantes, 17 menores); todos tratados (`revisoes/u2.md`): exemplo N3 trocado, Q1 e Q7 reescritas, ordem do N2 refeita | 0 FALHAS · 0 AVISOS; verif U2 23 OK |
