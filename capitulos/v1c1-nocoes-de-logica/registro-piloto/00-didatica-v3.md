# Didática v3 — material de matemática a partir do FME

Data: 2026-11-18 · Origem: conversa de fechamento do piloto (Cap. I), pontos p1–p20 do usuário + evidência do q7 (`q7-revisao.md`).
Substitui a didática v2 (`00-decisoes.md` § "Didática"). Decisões anteriores que continuam valendo estão listadas no §9; as que foram substituídas, no §10.

Legenda de origem: **(u)** formulado pelo usuário · **(u+c)** proposta da conversa que o usuário aceitou ao mandar registrar a v3 · **(q7)** decorre dos achados da revisão.

---

## 1. Princípios

| # | Princípio | Origem |
|---|---|---|
| P1 | **A didática é a base.** Ela muda só por decisão explícita do usuário, com nova versão (v1 → v2 → v3) registrada aqui. (Revisa o p1 "imutável".) | (u) |
| P2 | **Cada quesito é documentado.** | mantido |
| P3 | **O material é autocontido.** | mantido |
| P4 | **Padronizar a arquitetura, não a experiência.** A *função* de cada seção é fixa; extensão, profundidade e forma variam com o conceito. Um conceito historicamente rico pode ter um "De onde vem?" longo; uma técnica algébrica simples, meia página. A sequência é um esqueleto, não uma camisa de força. | (u) p5, p20 |
| P5 | **O objetivo é aprender matemática.** A história é pano de fundo para o desenvolvimento do raciocínio, nunca o produto. | (u) p6 |
| P6 | **Ensinar o processo de fazer matemática**, não só o conteúdo: *compreender* (De onde vem?) → *reconhecer* (Onde é usado?) → *diagnosticar* (Erros comuns) → *executar* (Exemplos, Questões) → *consolidar* (Síntese de domínio). | (u) p20; "consolidar" (u) p19 |
| P7 | **Começar pelo problema, não pela fórmula.** A definição é justificada pela reconstrução do problema que ela resolve. | (u) p1 |
| P8 | **Erro se explica, não se proíbe.** Em vez de "fazer assim é errado", reconstrói-se o raciocínio que leva ao erro e mostra-se onde ele quebra. | (u) p2 |

### A pergunta-filtro (P5)
Feita e refeita durante a construção, para **cada** trecho histórico, curiosidade ou digressão:

> **"Isso melhora a compreensão do conceito que estou ensinando, ou apenas torna o capítulo mais interessante?"**

Se só torna mais interessante: sai, ou vai para Observações (camada opcional, §2.5). Corolário (q7): quanto menos um fato histórico ajuda a entender, menos ele justifica o custo de pesquisá-lo e conferi-lo. No piloto, quase todos os erros sérios do q7 estavam na história; nenhum estava nas respostas.

---

## 2. Arquitetura da unidade

Cada seção é definida pela **pergunta que responde**. O critério de aceitação de cada uma é essa função, não um formato ou um tamanho.

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

### 2.1 Prefácio — *Por que isso merece ser estudado?* (u) p9
- **Função:** responder rápido "por que estamos falando disso?" e **deixar uma pergunta em aberto** que o aluno queira resolver. Ele explica o propósito, prepara o conceito e prende a atenção. Fica fora da narrativa.
  - Modelo: *"Por que a fórmula de Bhaskara tem exatamente essa forma? Ela poderia ter sido escrita de outra maneira?"*
  - No piloto: *"x + 1 = 7 não é verdadeira nem falsa. Como transformá-la numa afirmação sem escolher x?"* (Unid. 5).
- **Contém:** a pergunta aberta, o porquê, os pré-requisitos (w7) e a caixa **"O mínimo que você precisa"** (D-q7-1).
- **Tamanho:** o necessário para criar a pergunta, em geral menos de uma página. Substitui c2 ("≈ 1 página").
- **Aceitação:**
  - Há uma pergunta aberta explícita, e a unidade a responde.
  - Depois do prefácio, o leitor sabe dizer por que o tema importa.

### 2.2 De onde vem? — *Como chegamos a essa ferramenta?* (u) p10, p12
- **Objetivo:** responder três perguntas:
  1. Por que alguém precisou disso?
  2. Como a ideia foi construída?
  3. Como podemos reconstruí-la hoje?
- **Segundo objetivo:** compreensão antes de memorização. A história pode ajudar a memória, mas não se justifica principalmente por isso. O alvo é uma **rede de significado**: o aluno não decora a² + b² = c² como símbolos arbitrários; lembra que "isso nasceu do problema de relacionar os lados de um triângulo retângulo".
- **Formato:** mantém o atual (narrativa, caixas de Construção, Definição).
- **Origem histórica ≠ reconstrução matemática.** As duas aparecem distintas no texto. A reconstrução matemática se sustenta sozinha.
- **Três camadas (u) p7.** Quando um conceito moderno tem raiz antiga, o texto separa, sem virar filosofia da lógica:
  - *o que o autor efetivamente formulou*;
  - *o que uma leitura moderna reconstrói a partir dele*;
  - *o que é a convenção atual* (por exemplo, da lógica clássica).
  - Caso do piloto: Aristóteles formula a não contradição e o terceiro excluído ("ou se afirma ou se nega"). A **bivalência** V/F é leitura moderna, e a convenção é da lógica clássica. O próprio Aristóteles é lido, no cap. 9 de *Da Interpretação*, como abrindo exceção para frases sobre o futuro.
- **Filtro P5** em cada trecho histórico.
- **Aceitação:**
  - As três perguntas estão respondidas.
  - A definição é justificada por um raciocínio, e não só por um fato histórico.
  - Nenhuma atribuição moderna aparece como se fosse do autor antigo.

### 2.3 Onde é usado? — *Como reconheço uma situação em que essa ferramenta é apropriada?* (u) p11, p12, p18
- **Função:** **reconhecimento de padrões.** O aluno costuma saber aplicar a fórmula depois que alguém diz qual usar; o que falta é responder "estou diante desta questão: o que eu faço?". A seção ensina a *selecionar* a ferramenta.
- **Fronteira com "De onde vem?" (p12):**
  - *De onde vem?* explica a ferramenta, com o pano de fundo.
  - *Onde é usado?* ensina a escolhê-la.
  - Exemplo (distância de ponto a reta):
    - *De onde vem?* constrói a projeção perpendicular e chega à fórmula.
    - *Onde é usado?* mostra problemas em que a informação dada indica que a distância perpendicular é o objeto procurado.
- **Núcleo: o mapa do problema (p18).** É a habilidade entre "reconhecer a ferramenta" e "resolver": **traduzir o enunciado para uma estrutura matemática**. Formato:
  > O enunciado diz: "duas retas paralelas estão separadas por…" → Matematicamente, procure: distância entre retas paralelas → Ferramenta: d = |c₁ − c₂| / √(a² + b²).
  - Dois ou três casos trabalhados nesse formato.
  - Depois, a **tabela de gatilhos** (sinal no enunciado → ferramenta → raciocínio), que passa a ser o resumo do mapa, e não o centro da seção.
- **O que não entra:** aplicações que não ensinam a reconhecer (no piloto, Shannon e circuitos como narrativa) vão para *De onde vem?*, se explicam a origem, ou para *Observações*, se só ampliam.
- **Aceitação:**
  - Há casos de enunciado → estrutura → ferramenta.
  - Cada linha da tabela de gatilhos aponta para pelo menos um exemplo ou questão.

### 2.4 Erros comuns — *Onde o raciocínio costuma quebrar?* (u) p8, p13
- **Função:** modelar o raciocínio errado do estudante; uma pequena investigação, **não uma lista de pegadinhas**. A pergunta central é "por que alguém pensaria dessa maneira?".
- **Roteiro de cada erro:**
  1. **Erro**: o que o aluno escreve.
  2. **Por que parece plausível**: o raciocínio que leva a ele.
  3. **Onde quebra**: um contraexemplo concreto.
  4. **Como detectar**: o teste que o aluno faz *depois* de escrever.
  5. **Como evitar / corrigir**: a regra certa.
  - Mais **Onde aparece**: remissão a exemplos e questões.
- **Modelo:**
  > O aluno nega x > 3 como x < 3. *Parece plausível* porque "o contrário de maior é menor". *Quebra* em x = 3, que não está em nenhuma das duas frases. *Detecta-se* perguntando: algum valor fica de fora da frase e da negação? *Corrige-se* com ~(x > 3) ⇔ x ≤ 3.
- **Tamanho (P4):** em erros simples, "onde quebra" e "como detectar" podem ser uma frase só. A função dos cinco passos é obrigatória; os cinco campos visuais, não.
- **Aceitação:** todo erro tem contraexemplo concreto e teste de detecção.

### 2.5 Observações — *coisas que ampliam o conceito sem serem necessárias para utilizá-lo* (u) p14
- **Problema que a v3 resolve:** "elementos que fogem das seções anteriores" vira gaveta de "coisas legais" que cresce sem fim.
- **Identidade:** só entra o que amplia o conceito. Tipos admitidos:
  - curiosidades;
  - generalizações;
  - casos-limite;
  - relações com outras áreas;
  - notas históricas que não cabiam na narrativa;
  - consequências interessantes;
  - exceções;
  - conexões com conceitos futuros.
- **Camada opcional, marcada visualmente.** Quem quer o básico segue sem ela; o curioso aprofunda.
- **Teste de pertença:** quem pula todas as observações perde algo necessário para usar o conceito? Se perde, não é observação: vai para a seção a que pertence.
- **Cobertura (u+c, q7):** IDs **O** saem da cobertura obrigatória de exemplos (emenda à w3). Podem alimentar questões N3 de transferência. No piloto, a obrigação de cobrir O gerou ligações forçadas (4-O2, 5-O1, achados do q7).

### 2.6 Exemplos — *aplicação guiada*
- Resolvidos e comentados, no mínimo um por nível (§3). Juntos, cobrem os IDs obrigatórios (H, U, E).
- Formato mantido: plano → resolução → comentário.
- **Aceitação (q7):** cada ID declarado é **de fato treinado** no item, e não só mencionado. Esse ponto é conferido por leitura no q7, porque o `matriz.py` confere só a presença.

### 2.7 Questões — *aplicação independente, progressivamente menos guiada*
- Cada questão é classificada num nível (§3).
- **Ordem dentro do nível (u+c):** da mais guiada para a menos guiada. Substitui a regra de ordenar pela sequência dos IDs (q2 §2.7) e resolve a pendência B23 do q7.
- **Integradoras (u) p17:** podem envolver outros conteúdos, **desde que o conteúdo da unidade seja estruturalmente necessário para a solução**. Teste: a questão se resolve sem o conteúdo da unidade? Se sim, não serve como questão da unidade. Isso permite construir, aos poucos, problemas mais ricos sem perder o que se avalia.

### 2.8 Síntese de domínio — *teste de domínio conceitual* (u) p19
- **Função:** ponte entre resolver exercícios e consolidar o conceito. É uma caixa, não uma seção inteira.
- **Visual:** caixa **amarela**, a cor da Construção: o estudante faz a própria construção.
- **Contém:**
  - uma lista curta do que o estudante deveria saber agora;
  - as quatro perguntas, respondidas pelo próprio aluno:
    - O que esse conceito significa?
    - Como ele foi construído?
    - Como reconheço quando utilizá-lo?
    - Qual é o erro mais perigoso ao aplicá-lo?
- **Aceitação:** cada pergunta tem resposta localizável numa seção da unidade (significa → definição; construído → De onde vem; reconheço → Onde é usado; erro → Erros comuns).

### 2.9 Respostas — *verificação rápida*
- Mantida: só o resultado final, `[ n. resp ]`. Em demonstrações, uma linha do que a prova deve mostrar (c6). Gabarito verificado por programa (w5).

---

## 3. Níveis por função (u) p15 — substitui w2

| Nível | Função | O aluno… |
|---|---|---|
| **N1 — reconhecimento e aplicação** | A ferramenta está clara. | …sabe qual ferramenta usar e a aplica. |
| **N2 — seleção e combinação** | É preciso perceber qual ferramenta usar, e talvez combinar mais de uma. | …escolhe e encadeia. |
| **N3 — transferência** | A ferramenta aparece numa situação diferente da apresentada na teoria. | …reconhece a estrutura num contexto novo. |

- **Não é fácil / médio / difícil.** Uma demonstração não é N3 por ser demonstração: se repete a técnica do texto, é N1 ou N2; é N3 se a técnica precisa ser levada a um lugar novo.
- **Consequência (q7):** um N3 **não pode estar resolvido no texto** da unidade. No piloto havia dois casos (U3 Q12, U4 Q10).
- As cores por nível se mantêm (c3).

---

## 4. Tipos de problema (u) p16

Vestibular não é necessariamente o melhor material didático: uma questão pode ser ótima para avaliar e ruim para introduzir um conceito. Cada tipo tem uma função:

| Tipo | Função | Onde rende mais |
|---|---|---|
| **Histórico** | Mostrar a origem ou a necessidade. | De onde vem?, exemplos N1–N2, N3 de transferência |
| **Vestibular / olimpíada / concurso** | Mostrar a aplicação real. | Onde é usado? (mapa do problema), exemplos e questões N2–N3 |
| **Autoral** | Construir exatamente a habilidade que se quer ensinar. | Qualquer seção; preferido para N1 e para erros comuns |

- O vestibular deixa de ser o padrão da escolha (antes: "prioridade a problemas históricos e de vestibular"). No piloto, a busca por texto de prova conferido foi um dos maiores custos, e várias questões acabaram como "adaptada de…" mesmo assim.
- As regras de procedência continuam (w4, D-q7-3).

---

## 5. Abertura e glossário do capítulo
- **Abertura geral:** mantida (q2 §3). O "Como usar" passa a descrever a arquitetura v3, os níveis por função, a camada opcional e a síntese.
- **Glossário:** vai para o **fim do capítulo** (u) p4, como consulta. No início, parecia dizer "estude isto antes". Substitui c3 nesse ponto.

---

## 6. Matriz de cobertura (emendas à w3)
- **Obrigatórios:**
  - **H** (construção) e **U** (uso): ao menos 1 exemplo.
  - **E** (erro): ao menos 1 exemplo e 1 questão.
  - **U** também: ao menos 1 questão.
- **Opcional:** **O** (observação), com cobertura livre.
- **Conferência semântica no q7:** o item treina o ID declarado? O `matriz.py` confere só a presença; o q7 achou quatro declarações vazias.

---

## 7. Impacto no pipeline

| Quesito | O que muda |
|---|---|
| q1 (plano de pesquisa) | A pesquisa histórica passa pelo filtro P5 já no plano: pesquisar o que ajuda a entender. Para cada marco, prever as três camadas (§2.2). Para Onde é usado?, pesquisar enunciados reais que alimentem o mapa do problema. |
| q2 (estrutura) | Cada seção é especificada por função e critério de aceitação (§2). Níveis por função. Ordem das questões por grau de guia. Glossário no fim. Síntese de domínio em cada unidade. |
| q3 (pesquisa) | Problemas classificados por tipo (§4). A busca de vestibulares serve à aplicação real, não ao preenchimento. |
| q4 (revisão do coletado) | Aplicar o filtro P5 ao material histórico coletado. Separar o que é narrativa (De onde vem?) do que é observação (camada opcional). |
| q5 (decisões) | Sem mudança de natureza. |
| q6 (produção) | Erros no roteiro de 5 passos. Observações marcadas como opcionais. Síntese de domínio. Integradoras com teste de necessidade. |
| q7 (revisão independente) | O brief ganha cinco conferências: (a) o item treina o ID declarado; (b) N3 não resolvido no texto; (c) integradora necessita do conteúdo da unidade; (d) filtro P5 e três camadas nos trechos históricos; (e) cada seção cumpre sua pergunta. Revisores em paralelo por blocos de unidades (mantido). |

---

## 8. Decididos na abertura da refação (usuário, 2026-11-18)
| # | Decisão |
|---|---|
| A1 | **"Para lembrar" é o gabarito da Síntese de domínio.** A caixa fica onde está, e a síntese remete a ela e às seções. |
| A2 | **Camada opcional das Observações:** selo na caixa + fonte menor. |
| A3 | **Três camadas (§2.2):** em texto corrido. A distinção fica subentendida, mas bem demarcada pela redação ("Aristóteles diz…", "lido hoje…", "a lógica clássica convenciona…"), sem caixa nem rótulo. |
| A4 | **O FME é só a base de conteúdo** (para o processo não perder nem esquecer nada do assunto); não é obra de referência citada por edição. A entrada nas Fontes fica genérica, e a pendência C3 do q7 está encerrada. |
| A5 | **Fontes frágeis:** (1) procurar a fonte primária; (2) se não houver, avaliar se a nota de acesso basta; (3) em último caso, remover a afirmação, se a fonte frágil prejudicar muito o material. |

---

## 9. Continuam valendo
- w1: capítulo em unidades.
- w4: procedência, com o formato de D-q7-3.
- w5: gabarito verificado.
- w7: pré-requisitos no prefácio.
- w8: um arquivo por quesito.
- w9: revisor independente.
- d1, w11: XeLaTeX → PDF.
- d2: skill orquestradora.
- Ordem do projeto: piloto → skill.
- c1: o artigo destacável sem limite de extensão continua, agora **sob o filtro P5**.
- c3, menos o glossário: cores, filetes, exemplos coloridos por nível.
- c5: fontes numeradas.
- c6: resposta de demonstração.
- D-q7-1: "O mínimo" em todas as unidades.
- D-q7-3: etiquetas.

## 10. Substituídas pela v3

| Antes | Agora |
|---|---|
| Didática v2 (8 seções, `00-decisoes.md`) | §2 (9 seções, com a Síntese de domínio) |
| p1 "a didática é imutável" | P1: muda só por decisão do usuário, versionada |
| w2 níveis por dificuldade / tipo | §3 níveis por função |
| w3 "todo ID tem exemplo" | §6: O opcional; conferência semântica |
| w6 "Onde é usado" = texto analítico + tabela | §2.3: mapa do problema + tabela de gatilhos |
| c2 prefácio ≈ 1 página | §2.1: o necessário para criar a pergunta |
| c3 glossário no início | §5: glossário no fim |
| Exemplos: "prioridade a histórico e vestibular" | §4: tipo de problema por função |
| q2 §2.7 ordem por ID | §2.7: ordem por grau de guia |

---

## 11. Próximos passos (ordem decidida pelo usuário, 2026-11-18)
1. ✅ Registrar a v3 (este arquivo).
2. ✅ Refazer o Cap. I na v3 em três partes (`q8-refacao-v3.md`): **(R1)** o que pede pouco esforço → **(R2)** o que pede muito esforço → **(R3)** q7 do Cap. I v3 e correções (`q7-revisao-v3.md`).
3. Só então extrair a skill, com o Cap. I v3 como exemplo de referência.

---

## 12. Emendas do R3 (q7 do Cap. I v3, 2026-11-18)
| # | Emenda |
|---|---|
| E-R3-1 | **Conferência fixa (f) no q6 e no q7: nada fora das questões antecipa um N3.** Observações, casos do mapa, linhas de gatilho, "Treino:", planos e comentários de exemplos não podem trazer o caso concreto, a ferramenta específica ou a resposta de um item N3. "Treino:" e a coluna "ID · treino" dos gatilhos apontam só para exemplos e questões N1/N2. O sinal do gatilho é descrito sem o caso concreto (não "bebês, crocodilos", mas "premissas encadeáveis"). Foi o padrão mais repetido do R3, em todas as unidades. |
| E-R3-2 | **IDs O não entram no `\cobre` de um item que só os menciona.** A remissão ("veja 4-O2") pode ficar, sem declaração. Vale para exemplos e questões. |
| E-R3-3 | **O que a unidade promete fica fora da camada opcional.** Se o prefácio, um exemplo ou um gatilho usa algo (a negação do ↔, a notação da barra), isso vem em *De onde vem?* ou em *Onde é usado?*; a observação guarda só a ampliação. |
| E-R3-4 | **Ponteiros e leiaute.** A síntese remete a uma seção que existe na unidade (sem caixa de Definição → "construção X-Hn"). Itens e alternativas em `enumerate` (com `multicols` quando curtos), nunca `\mbox` + `\hspace` em linha. Ao renumerar questões, atualizar remissões, matriz e verificador no mesmo passo. |
| E-R3-5 | **Fontes:** fonte secundária frágil ganha a obra original ao lado sempre que localizada; a nota de acesso vale para todas as páginas da web; não há afirmação de frequência ("mais pedido", "bloco fixo") sem fonte que a sustente. |
