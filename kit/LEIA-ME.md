# kit — ferramentas da skill material-didatico-fme

Versão do kit: **1.0** (2026-11-19) · didática v4 consolidada.

| Arquivo | Para quê | Quando ler |
|---|---|---|
| `didatica.md` | a regra: seções, níveis, procedência, matriz, fontes, forma | sempre que for escrever ou revisar |
| `etapas/1-escopo.md` … `5-fechamento.md` | o passo a passo de cada etapa | ao começar a etapa |
| `referencia/macros.md` | sintaxe dos ambientes LaTeX | na montagem |
| `referencia/licoes-do-piloto.md` | defeitos que mais se repetiram e o que custou caro | no dossiê, na montagem e na revisão |
| `modelos/` | ESTADO, escopo, dossiê, matriz, brief do revisor, verificador, tex | copiados pelo `esqueleto.py` (dossiê e brief: à mão) |
| `scripts/esqueleto.py` | cria capítulo / acrescenta unidade | etapa 1 |
| `scripts/checar.py` | compila e aplica as regras mecânicas | ao fim de toda montagem e correção |
| `scripts/matriz.py` | confere a matriz e o LaTeX contra ela | chamado pelo checar; avulso se quiser |
| `scripts/paginas.py` | folhas de contato do PDF para conferência visual | montagem, revisão, fechamento |
| `tex/estilo.sty` | estilo; cada capítulo recebe uma cópia | — |

## Mudanças no estilo em relação ao piloto
- Questões e exemplos com `\label`; remissões com `\ref`/`\qref`/`\exref`.
- Resposta dentro da questão (`\resp{…}`); `\Respostas` monta a lista na ordem das questões.
- Exemplos com número automático (primeiro argumento `{}`).
- Cabeçalho do capítulo por `\cabecalhocapitulo`; ponteiro da síntese por `\ondever{…}`.
- O Cap. I foi migrado para esse formato e o texto do PDF saiu idêntico, página a página.

## Mudar o kit
Mudança na `didatica.md` só por decisão do usuário (nova versão, com data). Mudança em script ou
estilo: teste no capítulo de referência (`checar.py capitulos/v1c1-nocoes-de-logica` deve continuar
sem FALHAS) e anote aqui a nova versão do kit.
