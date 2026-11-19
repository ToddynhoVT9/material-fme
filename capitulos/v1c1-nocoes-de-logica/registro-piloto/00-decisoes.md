# 00 — Decisões do projeto (piloto Cap. I — Noções de lógica, FME vol. 1)

Data: 2026-11-17 · atualizado 2026-11-18

> **Didática em vigor: v3 → [`00-didatica-v3.md`](00-didatica-v3.md).** Abaixo, a didática v2 fica como registro histórico; as decisões desta página que a v3 substituiu estão marcadas com ⟶ v3.

## Base fixa

### Didática v2 (histórico — substituída pela v3 em 2026-11-18)
1. **Prefácio** — propósito + curiosidade; fora da narrativa; prepara o estudante (inclui pré-requisitos — w7).
2. **De onde vem?** — contexto histórico, filosófico, experimentos e ideias; demonstrar e construir matematicamente do zero; quem, por quê, em que contexto. Foco no domínio do significado.
3. **Onde é usado?** — contextos de aplicação; como reconhecer, num exercício, qual ferramenta e qual raciocínio usar.
4. **Erros comuns** — quais, por que acontecem, que raciocínio leva a eles, como evitar.
5. **Observações** — complementos que fogem às seções anteriores.
6. **Exemplos** — resolvidos e comentados em 3 níveis (≥ 1 por nível); juntos cobrem tudo das seções anteriores; prioridade a problemas históricos e de vestibular.
7. **Questões** — série de questões (podem envolver outros assuntos, desde que contenham o assunto), cada uma classificada em um nível.
8. **Respostas** — só a resposta final: `[ 14. (c) ]`, `[ 28. 5√3 ]`.

### Pipeline (versão 2 — w10, 2026-11-17)
- q1 — plano estruturado de pesquisa para cada seção da didática
- q2 — plano de estruturação do material
- q3 — pesquisa: execução do plano de pesquisa (q1) orientada pela estruturação (q2)
- q4 — revisão do material coletado (bate com a didática e com o q2?)
- q5 — decidir o que mudar e onde (material ou plano; nunca a didática)
- q6 — criar o material sobre o resultado de q1–q5
- q7 — revisar seção a seção contra q1–q5; resolver pendências

> Na v1 (q1–q6), a pesquisa era feita dentro do q1. No piloto, os arquivos foram renumerados: `q3-revisao` → `q4-revisao`, `q4-decisoes` → `q5-decisoes`, `q5-producao` → `q6-producao`. A coleta feita no q1 conta como a 1ª rodada do q3.

### Princípios
- p1 — a didática é a base e não muda. ⟶ v3 P1: muda só por decisão explícita do usuário, com nova versão registrada.
- p2 — cada quesito é documentado.
- p3 — o material é autocontido.

## Decisões

| # | Decisão |
|---|---|
| w1 | Capítulo dividido em **unidades**; cada unidade com as 8 seções. |
| w2 ⟶ v3 §3 | **N1** aplicação direta, uma etapa · **N2** várias etapas ou combinação com outro conteúdo · **N3** demonstração, problema histórico ou vestibular de 2ª fase. |
| w3 ⟶ v3 §6 (emendada) | **Matriz de cobertura com IDs** (U contexto de uso, E erro comum, O observação…). Exemplos e questões declaram os IDs que cobrem. ID descoberto → revisão manual. |
| w4 | **Procedência**: `[FUVEST 2018]` só com fonte verificada; senão `[adaptada de …]` ou `[autoral]`. Fatos históricos: *documentado* / *anedota*. Entrada = capítulo separado + questões de vestibular respectivas. |
| w5 | **Gabarito verificado** por resolução independente (sympy / força bruta), registrada no q6. |
| w6 ⟶ v3 §2.3 | "Onde é usado": primeiro um **texto analítico** (quase um estudo) de como o conceito costuma aparecer; depois a **tabela de gatilhos** (sinal no enunciado → ferramenta → raciocínio). |
| w7 | **Pré-requisitos** no prefácio. |
| w8 | **Um arquivo por quesito**; q4 registra decisão + motivo. |
| w9 | q7 (antigo q6) feito por **revisor independente** (subagente que não viu a produção). |
| d1 | Saída **LaTeX → PDF**. |
| w11 | Motor **XeLaTeX** (o LuaLaTeX falhou no ambiente). |
| d2 | **Uma skill orquestradora** (SKILL.md curto + references/ por quesito + scripts + template LaTeX); estado em disco, retomável. |
| ordem | **Piloto no Cap. I** manual e documentado → **skill extraída** do que funcionou. |

## Material de entrada (validado com o Cap. I)
- Leitura **visual** das páginas (a extração de texto perde ∧, ∨, ~, ≠, ∈) — passo zero do q1.
- Ingestão **filtra o gabarito** (cobre o volume inteiro).
- Questões de cada unidade: exercícios internos do FME + vestibulares pesquisados/verificados + autorais.
- **Cap. I em 6 unidades**: (1) Proposição e negação · (2) Conectivos ∧ e ∨ · (3) Condicional e bicondicional · (4) Tautologia, contradição, implicação e equivalência · (5) Sentenças abertas e quantificadores · (6) Negação de proposições.

## Pendências do q2 — resolvidas (2026-11-17)
- Há **abertura geral do capítulo** além do prefácio de cada unidade.
- Numeração de questões e respostas **reinicia em cada unidade**.

## Calibração da Unidade 1 (usuário, 2026-11-17)
| # | Decisão |
|---|---|
| c1 | **Prefácio + "De onde vem?" + "Onde é usado?" devem funcionar como um artigo destacável** sobre o assunto: tempo e espaço para a história, a filosofia, os experimentos e a construção. **Sem limite de extensão**; a extensão varia por unidade. As **Observações** também crescem: continuam menores que as outras seções, mas não minúsculas. |
| c2 ⟶ v3 §2.1 | **Prefácio ≈ 1 página**, papel de resumo: gancho, por que importa, o percurso, pré-requisitos. Continua "introdução rápida", fora da narrativa. |
| c3 | Visual: prefácio **sem quadro** (fundo branco); "O mínimo" mantém a cor; **construção amarela**; definição, erros e observações mantêm as cores; **exemplos coloridos por nível** (N1 verde, N2 azul-escuro, N3 roxo); tabelas com **filetes finos entre as linhas**, mantendo os grossos; **glossário no início do capítulo** (⟶ v3 §5: glossário no fim). |
| c4 | Distribuição de dificuldade aprovada. |
| c5 | Trocar `[doc]` por **número da fonte** (`[n]`, ligado à lista de fontes). |
| c6 | Em questão de demonstração, a resposta traz **uma linha dizendo o que a prova precisa mostrar**. |

## Emendas do q7 (2026-11-18) — ver `q7-revisao.md` §3
| # | Decisão |
|---|---|
| D-q7-1 | Caixa "O mínimo que você precisa" em **todas** as unidades (emenda ao q2 §2.1 / D4). |
| D-q7-2 | "Para lembrar" = 1 frase + ≤ 3 passos (aplicado nas 6 unidades). |
| D-q7-3 | Etiquetas: `[adaptada de concurso — BANCA/ÓRGÃO ANO]`, `[FME, exercício n]`, `[adaptado do FME, item n]`, `[histórico]`, `[… — via FME]`; a legenda da abertura é a referência (substitui o formato literal do e1). |
| q7 | Revisão por **3 revisores independentes em paralelo** (por blocos de unidades), cada um refazendo todas as respostas sem ver as conferências da produção. |

## Emendas do R3 (2026-11-18) — ver `00-didatica-v3.md` §12 e `q7-revisao-v3.md`
| # | Decisão |
|---|---|
| E-R3-1 | Conferência fixa: observações, casos, gatilhos e "Treino:" não antecipam nem resolvem N3; "Treino:" e gatilhos apontam só para N1/N2. |
| E-R3-2 | IDs O fora do `\cobre` quando o item só os menciona. |
| E-R3-3 | O que a unidade promete não fica só na camada opcional. |
| E-R3-4 | Síntese aponta para seção existente; listas em `enumerate`/`multicols`; renumeração sincroniza remissões, matriz e verificador. |
| E-R3-5 | Primária ao lado da fonte frágil; nota de acesso para toda a web; nada de frequência sem fonte. |
| A19 | Ordem do N3 da U1 mantida (Q11 bifurcação → Q12 autorreferência). |
