# Didática v4 — texto consolidado (normativo)

Material de estudo de matemática a partir dos capítulos do *Fundamentos de Matemática Elementar* (FME).
Este arquivo é a regra. Ele junta a didática v3 (2026-11-18), as decisões do piloto que continuam
valendo, as emendas do R3 (E-R3-1 a E-R3-5) e as regras da v4 (2026-11-20), já incorporadas no lugar
de cada regra. Mudanças de versão: §12.
Histórico completo: `capitulos/v1c1-nocoes-de-logica/registro-piloto/`.

**P1 — a didática muda só por decisão explícita do usuário**, registrada aqui como nova versão
(v4 → v5), com data e motivo, e anotada no §12. Ajustes locais de um capítulo vão para o `ESTADO.md` dele.

---

## 1. Princípios

| # | Princípio |
|---|---|
| P1 | A didática é a base; muda só por decisão do usuário, versionada. |
| P2 | Cada etapa é documentada em arquivo (escopo, dossiê, matriz, revisão, ESTADO). |
| P3 | O material é autocontido: o estudante não precisa do FME para estudar por ele. |
| P4 | **Padronizar a arquitetura, não a experiência.** A função de cada seção é fixa; extensão e forma variam com o conceito. |
| P5 | **O objetivo é aprender matemática.** A história é pano de fundo do raciocínio, nunca o produto. |
| P6 | Ensinar o processo: compreender (De onde vem?) → reconhecer (Onde é usado?) → diagnosticar (Erros) → executar (Exemplos, Questões) → consolidar (Síntese). |
| P7 | Começar pelo problema, não pela fórmula: a definição é justificada pela reconstrução do problema que ela resolve. |
| P8 | Erro se explica, não se proíbe: reconstrói-se o raciocínio que leva a ele e mostra-se onde quebra. |

**Pergunta-filtro (P5)**, para cada trecho histórico, curiosidade ou digressão:
> "Isso melhora a compreensão do conceito, ou apenas torna o capítulo mais interessante?"

Se só torna mais interessante: sai, ou vai para Observações. Quanto menos um fato ajuda a entender,
menos ele justifica o custo de pesquisá-lo e conferi-lo. No piloto, quase todos os erros sérios
estavam na história; nenhum nas respostas.

---

## 2. Arquitetura da unidade

O capítulo é dividido em **unidades**; cada unidade tem as nove seções, nesta ordem:

```
Prefácio ............... Por que isso merece ser estudado?
De onde vem? ........... Por que foi necessário? Como surgiu? Como reconstruímos hoje?
Onde é usado? .......... Onde aparece? Como reconheço a estrutura? Como escolho a ferramenta?
Erros comuns ........... Onde o raciocínio costuma quebrar? Por que o erro parece plausível?
Observações ............ Aprofundamentos, conexões, exceções, curiosidades (camada opcional)
Exemplos ............... Aplicação guiada nos três níveis
Questões ............... Aplicação independente, progressivamente menos guiada
Síntese de domínio ..... O que significa? Como foi construído? Quando usar? Como não errar?
Respostas .............. Verificação rápida
```
Prefácio + De onde vem? + Onde é usado? formam um **artigo destacável**, sem limite de extensão,
sob o filtro P5.

### 2.1 Prefácio — *Por que isso merece ser estudado?*
- Responde rápido "por que estamos falando disso?" e **deixa uma pergunta aberta explícita**, que a
  unidade responde. Fora da narrativa. Em geral menos de uma página.
- Contém: o gancho, a pergunta aberta (em negrito), "Ao final, você será capaz de", os pré-requisitos
  e a caixa **"O mínimo que você precisa"** (em todas as unidades).
- **Aceitação:** há pergunta aberta explícita e a unidade a responde; depois do prefácio, o leitor sabe
  dizer por que o tema importa.

### 2.2 De onde vem? — *Como chegamos a essa ferramenta?*
- Responde: (1) por que alguém precisou disso? (2) como a ideia foi construída? (3) como podemos
  reconstruí-la hoje? Alvo: compreensão antes de memorização, uma rede de significado.
- Narrativa + caixas **Construção** (amarela, com ID H) + **Definição**; fecha com **Para lembrar**
  (1 frase + até 3 passos), que é o gabarito da Síntese de domínio.
- **Origem histórica ≠ reconstrução matemática.** As duas aparecem distintas; a reconstrução se
  sustenta sozinha, por raciocínio, nunca por autoridade ("aplicamos a regra porque X disse").
- **Três camadas**, em texto corrido, demarcadas pela redação, sem caixa nem rótulo: *o que o autor
  formulou* ("Aristóteles diz…") / *o que uma leitura moderna reconstrói* ("lido hoje…") / *a convenção
  atual* ("a lógica clássica convenciona…"). Nunca pôr a leitura moderna na boca do autor antigo.
- **Aceitação:** as três perguntas respondidas; definição justificada por raciocínio; nenhuma
  atribuição moderna como se fosse do autor antigo; todo fato com fonte.

### 2.3 Onde é usado? — *Como reconheço quando usar a ferramenta?*
- Função: **reconhecimento de padrões** — ensinar a *escolher* a ferramenta. *De onde vem?* explica a
  ferramenta; *Onde é usado?* ensina a reconhecer quando ela serve.
- Núcleo: o **mapa do problema** — 2 a 4 casos no formato *o enunciado diz → procure (estrutura
  matemática) → ferramenta*, com "Como reconhecer" e um enunciado real com procedência. Depois, a
  **tabela de gatilhos** (sinal → ferramenta → raciocínio → ID · treino) como resumo.
- Aplicação que não ensina a reconhecer vai para *De onde vem?* (se explica a origem) ou Observações.
- **Nada aqui antecipa um N3** (E-R3-1): casos, "Treino:" e gatilhos não trazem o caso concreto, a
  ferramenta específica nem a resposta de um item N3; "Treino:" e a coluna "ID · treino" apontam só
  para exemplos e questões **N1/N2**. O sinal do gatilho é genérico ("premissas encadeáveis", não
  "bebês, crocodilos").
- **"Como reconhecer" descreve o sinal no enunciado** — palavras, estrutura ou contexto que indicam a
  ferramenta —, não onde a questão aparece nem de que livro ela vem (v4).
- **Aceitação:** há casos enunciado → estrutura → ferramenta; cada linha de gatilho aponta para ≥ 1
  item N1/N2.

### 2.4 Erros comuns — *Onde o raciocínio costuma quebrar?*
- Uma pequena investigação, não uma lista de pegadinhas: "por que alguém pensaria assim?".
- Roteiro de cada erro: (1) **o erro**; (2) **por que parece plausível**; (3) **onde quebra** —
  contraexemplo concreto; (4) **como detectar** — teste feito *depois* de escrever; (5) **como
  corrigir**; + **onde aparece** (remissões por rótulo).
- Em erros simples, (3) e (4) podem ser uma frase; a função dos cinco passos é obrigatória.
- **Aceitação:** todo erro tem contraexemplo concreto e teste de detecção.

### 2.5 Observações — *amplia o conceito sem ser necessária para usá-lo*
- Tipos admitidos: curiosidade, generalização, caso-limite, relação com outras áreas, nota histórica
  que não cabia na narrativa, consequência interessante, exceção, conexão com conceito futuro.
- **Camada opcional**: caixa cinza com selo "aprofundamento opcional" e letra menor.
- **Teste de pertença:** quem pula *todas* as observações perde algo necessário para usar o conceito?
  Se sim, não é observação. Em particular, **o que a unidade promete** (prefácio, exemplos, gatilhos)
  vem em *De onde vem?* ou *Onde é usado?*; a observação guarda só a ampliação (E-R3-3).
- Uma observação não resolve nem antecipa um N3 (E-R3-1).

### 2.6 Exemplos — *aplicação guiada*
- Resolvidos e comentados, **≥ 1 por nível**; juntos cobrem todo ID **H, U e E**.
- Formato: Plano → Resolução → Comentário.
- **Cada ID declarado é treinado**, não só mencionado. IDs O só entram no `\cobre` se o item treina a
  observação (E-R3-2); a simples remissão ("veja 2-O3") fica sem declaração.

### 2.7 Questões — *aplicação independente, progressivamente menos guiada*
- Cada questão tem nível (§3). **Dentro do nível, da mais guiada para a menos guiada.**
- **Integradora** (outro assunto junto) só se o conteúdo da unidade for **estruturalmente necessário**:
  tente resolvê-la sem ele; se der, não serve.
- Em demonstração, a resposta diz em uma linha *o que a prova deve mostrar*.

### 2.8 Síntese de domínio — *teste de domínio conceitual*
- Caixa amarela, antes das Respostas: lista curta do que o estudante deveria saber + as quatro
  perguntas, cada uma com ponteiro para onde está a resposta: O que significa? (→ definição ou
  construção) · Como foi construído? (→ De onde vem?) · Como reconheço quando usar? (→ Onde é usado?)
  · Qual o erro mais perigoso? (→ Erros comuns). O "Para lembrar" é o gabarito.
- **Aceitação:** cada ponteiro aponta para uma seção ou caixa que **existe** na unidade (sem caixa de
  Definição → "construção X-Hn").

### 2.9 Respostas — *verificação rápida*
- Só o resultado final, `[ n. resp ]`; demonstração com a linha do que a prova deve mostrar.
- Toda resposta calculável é **conferida por programa**, separado da redação (`verif/uN.py`).

---

## 3. Níveis por função

| Nível | Função | O aluno… |
|---|---|---|
| **N1 — reconhecimento e aplicação** | A ferramenta está clara. | sabe qual usar e a aplica. |
| **N2 — seleção e combinação** | É preciso perceber qual ferramenta usar, talvez combinar. | escolhe e encadeia. |
| **N3 — transferência** | A ferramenta aparece numa situação diferente da apresentada. | reconhece a estrutura num contexto novo. |

- Não é fácil/médio/difícil: uma demonstração que repete a técnica do texto é N1 ou N2.
- **Um N3 nunca está resolvido nem antecipado no texto da unidade** (§2.3, §2.5).
- Item que entrega a ferramenta inteira no enunciado é N1, mesmo que seja longo.
- Cores: N1 verde, N2 azul-escuro, N3 roxo.

---

## 4. Tipos de problema

| Tipo | Função | Onde rende mais |
|---|---|---|
| **Histórico** | mostrar a origem ou a necessidade | De onde vem?, exemplos N1–N2, N3 de transferência |
| **Prova** (vestibular, olimpíada, concurso) | mostrar a aplicação real | Onde é usado?, exemplos e questões N2–N3 |
| **Autoral** | construir exatamente a habilidade | qualquer seção; preferido para N1 e para erros |

O vestibular não é o padrão de escolha: é ótimo para avaliar, nem sempre para ensinar. Conferir o
texto de uma prova é caro — só vale quando a função do item é mostrar a aplicação real.

---

## 5. Procedência (etiquetas no cabeçalho de exemplos e questões)

- `[FUVEST 2019, 1ª fase, q.~12]` — prova real, **só com o texto conferido na prova**;
- `[… via FME]` — questão real com texto tirado do FME (sem ano: "ano não informado" ou identificado por outra fonte);
- `[FME, exercício n]` · `[adaptado do FME, item n]`;
- `[adaptada de concurso — BANCA/ÓRGÃO ANO]` ou `[adaptada de …]` — original não conferido na íntegra; reescrita, resposta conferida;
- `[histórico]` — problema ou experimento contado na unidade;
- `[autoral]` (pode dizer "estrutura de…").
Fatos históricos: documentados, com `\src`; histórias não verificáveis levam `\anedota`.
- **O FME não é citado no corpo do texto** ("o FME tem um exercício que…", "o comando aparece assim no
  FME"): a procedência fica só na etiqueta e no `\src` (v4). Uma pergunta do FME pode ser usada no
  texto; o que não se faz é apresentá-la como "do FME".

---

## 6. Matriz de cobertura

- IDs por unidade: **H** construção (De onde vem?), **U** contexto de uso, **E** erro comum, **O** observação.
- Obrigatórios: todo H e U com ≥ 1 exemplo; todo E com ≥ 1 exemplo e ≥ 1 questão; todo U com ≥ 1 questão;
  cada unidade com exemplo N1, N2 e N3. O é opcional.
- `matriz.yaml` casa cada item com o LaTeX pelo **rótulo** e confere IDs e nível (`kit/scripts/matriz.py`).
  Ela confere presença; se o item **treina** o ID, só a leitura confere (revisão, conferência a).

---

## 7. Conferências fixas (montagem e revisão)

(a) o item treina cada ID declarado · (b) nenhum N3 resolvido ou antecipado fora das questões; cada
nível cumpre a função · (c) integradora precisa do conteúdo da unidade · (d) filtro P5 e três camadas
· (e) ordem por grau de guia dentro do nível · (f) o prometido não está só na camada opcional
· (g) **nenhuma ambiguidade** (v4): todo pronome tem referente claro ("o sistema dele" → "de quem?"),
todo termo técnico é explicado na primeira vez que aparece, toda pessoa é apresentada antes de ser
citada, e nenhuma frase admite duas leituras; o prefácio e o artigo falam do assunto da unidade e do
capítulo, sem promessas sobre "o volume".
O `checar.py` automatiza parte de (b) (remissões de "Treino:" e gatilhos para N3) e os ponteiros da
síntese; o resto é leitura.

---

## 8. Fontes

- Toda afirmação factual tem `\src{chave}` → entrada numerada em *Fontes*.
- **Fonte frágil (A5):** (1) procurar a primária e citá-la ao lado; (2) se não houver, avaliar se a nota
  de acesso basta; (3) em último caso, remover a afirmação, se a fonte frágil prejudicar o material.
- A nota de acesso (data de acesso; vale a versão dessa data) cobre **todas** as páginas da web.
- **Nenhuma afirmação de frequência** ("mais pedido", "sempre cai", "bloco fixo") sem fonte que a sustente.
- O FME é só a base de conteúdo; entra nas Fontes de forma genérica.

---

## 9. Abertura e glossário do capítulo

- **Abertura** (escrita por último): por que este capítulo; linha do tempo só com marcos contados nas
  unidades; mapa das unidades (pré-requisitos + "a pergunta que a unidade responde", igual à pergunta
  aberta de cada prefácio); tabela de notação com fonte; "Como usar este material" (texto padrão do modelo).
- **Glossário** no **fim** do capítulo, como consulta: termo, significado em uma linha, unidade.

---

## 10. Forma (LaTeX e visual)

- XeLaTeX + `kit/tex/estilo.sty` (copiado para cada capítulo). Ambientes e macros: `kit/referencia/macros.md`.
- Prefácio sem quadro; construção e síntese amarelas; definição, "O mínimo" e mapa em azul; erros em
  vermelho; observações cinza com selo; exemplos coloridos por nível; tabelas com filetes finos entre linhas.
- Numeração de questões reinicia em cada unidade; exemplos numerados "unidade.ordem" automaticamente.
- **Rótulos, nunca números digitados:** questões `\label{uN:nome}`, exemplos `\label{ex:uN:nome}`;
  remissões com `\ref`, `\qref`, `\exref`. Resposta dentro da questão com `\resp{…}`; a lista de
  respostas se monta sozinha. Reordenar = mover o bloco.
- Listas de itens e alternativas em `enumerate` (com `multicols` quando curtos), nunca `\mbox` + `\hspace`.
- Fontes como números sobrescritos `[n]`.

---

## 11. Material de entrada

- Entrada = o capítulo do FME separado (teoria, exercícios, respostas) + as questões de vestibular do capítulo.
- **Leitura visual das páginas é a autoridade**; a camada de texto do PDF só serve de índice (perde ∧, ∨,
  ~, ≠, ∈ e pode trazer respostas de outros capítulos).
- O gabarito do FME é conferido por programa antes de ser usado.

---

## 12. Histórico de versões

| versão | data | motivo | o que mudou |
|---|---|---|---|
| v3 | 2026-11-18 | lições do piloto (Cap. I) | texto consolidado; emendas E-R3-1 a E-R3-5 |
| v4 | 2026-11-20 | calibração da U1 do Cap. II (decisão do usuário) | §2.3: "Como reconhecer" descreve o sinal no enunciado · §5: o FME não é citado no corpo do texto · §7: conferência (g), nenhuma ambiguidade |

Unidades prontas afetadas pela v4: Cap. I (todas as unidades; não revistas — revisar só se o usuário pedir);
Cap. II, U1 (já ajustada na calibração).

