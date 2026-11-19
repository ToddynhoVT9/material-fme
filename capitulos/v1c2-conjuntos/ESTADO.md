# ESTADO — Cap. II · Conjuntos

> Painel do capítulo. **Toda sessão começa lendo este arquivo e termina atualizando-o.**
> O que não está aqui (ou nos arquivos que ele aponta) não existe para a próxima sessão.

- volume: 1
- número: 2
- título: Conjuntos
- criado: 2026-11-19
- didática: v3 (`kit/didatica.md`)
- material de entrada: PDF `02 - Cap II - Conjuntos.pdf` (35 p.: teoria itens 19–40, exercícios 11–61, Leitura, respostas, vestibulares 7–47 e respostas), entregue pelo usuário em 2026-11-19. **Não versionado** (texto do livro; o repositório é público): anexar de novo nas sessões de montagem. Mapa das páginas: `escopo.md` §1.

## Próxima ação
Montagem da U1 (só o dossiê é entrada; o PDF do FME não é necessário: os enunciados do FME usados estão transcritos em `dossies/u1.md` §6).

## Unidades
| U | título | etapa | revisão | observação |
|---|---|---|---|---|
| 1 | Conjunto, elemento e descrição | dossiê pronto | — | `verif/u1.py` 42 OK |
| 2 | Igualdade, inclusão e conjunto das partes | escopo | — | — |
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
