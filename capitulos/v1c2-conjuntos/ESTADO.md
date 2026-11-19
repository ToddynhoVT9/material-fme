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
**Aguardando o usuário aprovar o escopo** (`escopo.md` §8: D1–D5). Depois: dossiê da U1.

## Unidades
| U | título | etapa | revisão | observação |
|---|---|---|---|---|
| 1 | Conjunto, elemento e descrição | escopo | — | — |
| 2 | Igualdade, inclusão e conjunto das partes | escopo | — | — |
| 3 | Reunião e interseção | escopo | — | — |
| 4 | Diferença e complementar | escopo | — | — |
| 5 | Contando elementos: dois conjuntos | escopo | — | — |
| 6 | Três conjuntos e as regiões do diagrama | escopo | — | — |
<!-- FIM UNIDADES -->

Etapas de uma unidade: `escopo` → `dossiê` → `montagem` → `revisão` → `pronta`.
Fechamento do capítulo (depois de todas `pronta`): abertura, glossário, fontes, conferência entre unidades, PDF final.

## Portões com o usuário
- [ ] Escopo aprovado (unidades, IDs, metas) — etapa 1
- [ ] Calibração: U1 pronta e aprovada pelo usuário, antes de montar as demais
- [ ] PDF final entregue — etapa 5

## Decisões do capítulo
| # | data | decisão | origem |
|---|---|---|---|
| C1 | 2026-11-19 | transcrever enunciado de questão com zoom de 200 dpi e conferir contra a camada de texto (a leitura em página dupla a 110 dpi errou a vest. 30) | escopo §1 |
| C2 | 2026-11-19 | o PDF do FME e a camada de texto não entram no repositório (público); só referências a páginas | escopo §1 |

Decisões locais deste capítulo. Mudança na **didática** só com o usuário, como nova versão em `kit/didatica.md`.

## Pendências
- Portão do escopo: D1 (seis unidades), D2 (excesso de vestibulares em U5/U6), D3 (lacunas do FME como construção), D4 (divergências do gabarito), D5 (vestibulares sem ano) — `escopo.md` §8.
- Divergências do gabarito do FME (`verif/fme.py`): ex. 13e, 14B/C (redação), 42f, vest. 36 — `escopo.md` §7.
- Leitura do FME com atribuições a conferir antes de qualquer uso (Arquimedes × Aristóteles; Dedekind 1872 × 1888) — `escopo.md` M13.

## Registro de sessões
| data | etapa · unidade | o que foi feito | checar.py ao sair |
|---|---|---|---|
| 2026-11-19 | 1 · escopo | esqueleto (6 unidades); leitura visual das 35 p.; inventário (22 itens de teoria, 51 exercícios, 41 vestibulares); `verif/fme.py` (98 conferências, 0 falhas, 5 divergências); IDs e metas na matriz | compila (26 p.); só FALHAS de cobertura da matriz, esperadas antes da montagem |
