# Revisão independente — Unidade 5 · Contando elementos: dois conjuntos (v1c2-conjuntos)

**Escopo revisado:** `tex/u5_artigo.tex`, `tex/u5_partes.tex`, as entradas da U5 em `tex/fontes.tex`,
`main.pdf` (pp. impressas 57–69 = físicas 61–73; texto por `pdftotext -layout` e imagens a 110 dpi de
cada página), `dossies/u5.md` e o bloco `n: 5` de `matriz.yaml`. Regras: `kit/didatica.md` (v4) e
`kit/referencia/licoes-do-piloto.md`. Decisões locais respeitadas (não apontadas como problema): D2, D3,
D5, D7/D9, D11. Não li `verif/`, `revisoes/` (outros relatórios) nem `ESTADO.md`. O `checar.py` foi
rodado (ele recompila o `main.tex`; as fontes não mudaram): **nenhuma falha e nenhum aviso** para a U5.

Todas as 6 respostas de exemplo e as 21 respostas de questão foram refeitas em Python (força bruta onde
cabia: conjuntos de 1 a 100, divisores de 120, $\mathcal P(A)\cup\mathcal P(B)$ com conjuntos reais
até 6 elementos, os 3 600 estudantes da q. 20 um a um). **Nenhuma divergência de resposta.**

## Achados

| # | gravidade | arquivo:linha ou página | problema | evidência (seu cálculo, a fonte) | correção proposta |
|---|---|---|---|---|---|
| 1 | bloqueante | `u5_artigo.tex:131` (caso 3 do mapa, p. 60) | O caso 3 traz como sinal “da matriz” e “da filial”, que é o contexto concreto da **q. 12 (N3, FME 59)** — a única questão com matriz e filiais —, e lhe atribui a ferramenta específica (5-H3 (4): converter em contagens; tabela). É a antecipação de N3 proibida pela §2.3 (E-R3-1): o aluno chega à q. 12 já com o contexto e a ferramenta nomeados. O dossiê (§3, caso 3) diz “sinal genérico” e só se preocupou com as N2 (vest. 8 e 18); a q. 12 escapou. O `checar.py` não pega porque não há remissão por rótulo. | q. 12: “A firma tem a matriz na capital … filial de Santos … filial de Campinas”; caso 3: ““da matriz” e “da filial”” → “5-H3 (4): converter em contagens; tabela de dupla entrada”. | Trocar “da matriz” e “da filial” por um par neutro que não esteja em nenhum N3 (p. ex. “da turma A” e “da turma B”, “de cada loja”). Vale reavaliar se a q. 12 continua sendo transferência: com três grupos, a conta é a mesma média ponderada da q. 10 (N2). |
| 2 | importante | `u5_artigo.tex:92` (5-H3 (4), p. 59) | A construção usa “20\% de um grupo de $H$ pessoas e 15\% de um grupo de $M$ pessoas” → $0{,}20H+0{,}15M$. São os números e a divisão (H = homens, M = mulheres) da **q. 10 (N2, UFSCar)**: “20\% dos homens e 15\% das mulheres … fumam”. Isso fere D7/D9 (a construção não usa o caso concreto de uma N2) e entrega a equação da q. 10 ($0{,}20h+0{,}15(1-h)=0{,}18$). O próprio dossiê evitou esse par no erro 5-E4 (“D7: vest. 18 usa 20\%/15\%”), mas não na H3. | Dossiê §2.3 H3 (4) e §4 E4; q. 10 em `u5_partes.tex:227`. | Trocar porcentagens e letras: p. ex. “Se 30\% de um grupo de $P$ pessoas e 25\% de um grupo de $Q$ pessoas …, são $0{,}30P+0{,}25Q$”. |
| 3 | importante | `u5_partes.tex:166–173` (q. 5, p. 65) | A **integradora** q. 5 resolve-se sem o conteúdo da unidade (conferência (c)). (a) é a interseção (U3). Para responder (a), o aluno já lista os 16 divisores de 120 e marca os 8 múltiplos de 3; (b) se lê direto da lista (os 8 restantes), sem 5-H1/5-H2. O acréscimo (b) foi feito para “treinar” 5-H2, mas a contagem de “só $B$” não é necessária. | $B=\{1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120\}$; $B-A=\{1,2,4,5,8,10,20,40\}$: 8, por leitura direta. | Substituir (b) por uma pergunta em que a fórmula seja necessária e a listagem, cara. P. ex.: “Quantos números de 1 a 120 são divisores de 120 ou múltiplos de 3?” → $16+40-8=48$ (conferido por força bruta). Resposta: “b) $16+40-8=48$”. |
| 4 | importante | `u5_partes.tex:265–345` (bloco “Mais questões de vestibular”, pp. 66–68) | Dentro do N1 do bloco, a ordem é a do FME (vest. 9, 13, 14, 15, 16, 17), não da mais guiada para a menos guiada (conferência (e); D2: “a ordenação vale dentro do bloco”). A q. 14 (UFF, caixas de leite) é a **menos** guiada: é preciso traduzir “aprovadas nos dois testes” como “fora da reunião das reprovações”. Mesmo assim, vem em primeiro lugar. Já as q. 17, 18 e 19 aplicam a fórmula direto e vêm por último. | q. 19: $14+8-3$ (uma conta). q. 17 e 18: fórmula e depois o complemento. q. 15: complemento e depois isolar. q. 16: isolar $n(B)$, com a expressão ambígua “gostam igualmente”. q. 14: tradução de “aprovadas nos dois” e depois isolar. | Reordenar o N1 do bloco: ufrn17 → fei15 → pucmg16 → ufce13 → uece14 → uff9 (os rótulos mantêm as remissões). |
| 5 | importante | `u5_partes.tex:65` e `:73` (ex. 5.2 e 5.3, pp. 62–63) | Os níveis dos exemplos não batem com a função (§3; lição “nível pelo tamanho”). **Ex. 5.3** (N2): os dados já são as regiões, e o plano diz isso. É só somar regiões, com a ferramenta clara: N1. Ele é mais simples que a q. 3 (N1), que exige calcular as regiões. **Ex. 5.2** (N2) tem estrutura idêntica à das q. 4 e 15, ambas N1 (total, $n(A)$, $n(B)$, nenhum → interseção). Um mesmo tipo de item aparece com dois níveis. | Ex. 5.2: 60, 35, 20, 15 nenhum → 10. q. 4: 1 000, 600, 500, 200 nenhum → 300. q. 15: 1 150, 654, 564, 176 nenhum → 244. Ex. 5.3: $40+10$; $40+25+10+15$. | Ex. 5.3 → N1 e colocá-lo logo depois do 5.1. Para o 5.2, uniformizar: ou ele vira N1, ou as q. 4 e 15 viram N2. A preferência é o exemplo virar N1, porque o mapa (caso 2) já entrega a ferramenta. Ainda sobram N2 (5.4, 5.5), então a cobertura continua cumprida. |
| 6 | menor | `u5_artigo.tex:20` (prefácio, p. 57) | “para uma das questões, Unidade 2 (número de subconjuntos)”: são duas questões que usam $2^n$, a q. 11 ($2^6$) e a q. 13 ($2^a+2^b=2^{a+b}$). | q. 11 e q. 13 (as duas marcadas integradoras por 2ⁿ, dossiê §8). | “para duas das questões”. |
| 7 | menor | `u5_partes.tex:19` (5-E2, onde quebra, p. 61) | “Quem toma os 25 por “só natação” conta $25+15+5=45$”. Para chegar a 45, é preciso ler **também** os 15 como “só corrida”. Quem lesse só os 25 como “só natação” contaria $25+15=40$. A frase tem duas leituras (conferência (g)). | 25 só natação + 15 inclusivo → 40; 25 só + 15 só + 5 → 45. | “Quem toma os 25 e os 15 por “só natação” e “só corrida” conta …”. |
| 8 | menor | `u5_partes.tex:10–11` (5-E1, p. 61) | O teste de detecção (“A soma passou do total?”) não se aplica ao próprio contraexemplo, que não dá o total da turma. Ele também falha quando a soma não passa do total (q. 2: $221+163=384<415$). | E1, onde quebra: “Numa turma, 30 … 20 … 8”, sem total. | Dar um total ao contraexemplo (p. ex. “numa turma de 45 alunos”, $50>45$) e completar o teste: “… ou: o enunciado informa quantos estão nos dois? Então esse número tem de ser descontado.” |
| 9 | menor | `u5_artigo.tex:124` (caso 2, p. 60) | “três dos números (total, cada grupo, os dois, nenhum) e a pergunta pelo outro”. A H3 (2) fala em **cinco** números ($N$, $n(A)$, $n(B)$, $n(A\cap B)$, nenhum), e todos os itens do caso dão quatro e pedem o quinto. “Três” só vale se “cada grupo” contar como um. Fica ambíguo (g) e destoa da H3. | Ex. 5.2 e q. 4: quatro dados → um pedido. | “todos os números menos um (total, cada grupo, os dois, nenhum) e a pergunta pelo que falta”. |
| 10 | menor | `u5_artigo.tex:134` e `:141` (caso 3 e gatilho, p. 60) | “O sinal é a expressão “dos” ou “das” depois da porcentagem” não discrimina: “60\% dos funcionários” (q. 7) e “70\% dos domicílios” (ex. 5.5) também têm “dos”, e ali a base é uma só. O sinal real é que os “dos” apontam para **grupos diferentes**. | q. 7, ex. 5.5: mesma base, mesmo sinal. | “O sinal são porcentagens referidas a grupos diferentes (“dos homens”, “das mulheres”) …”. No gatilho: “porcentagens de grupos diferentes”. |
| 11 | menor | `u5_artigo.tex:82` e `:103` (5-H2 (4) e Para lembrar, passo 1, p. 59) | “comece pela interseção” é dado como regra geral. Nos itens do caso 2 (ex. 5.2, 5.5; q. 4, 7, 15), a interseção é a incógnita, e o plano do próprio ex. 5.2 começa pelo “nenhum”. O Para lembrar é o gabarito da síntese e não deve contradizer um exemplo. | Ex. 5.2, plano: “Primeiro, achar $n(C\cup G)$ pelos que não têm nenhum”. | “comece pela interseção; se ela é o que falta, ache-a primeiro pela fórmula (5-H3 (2))”. |
| 12 | menor | `u5_artigo.tex:36` (Por que alguém precisou disso, p. 57) | Afirmação de frequência sem fonte (§8): “Os números que se divulgam costumam ser os de cada característica separada”. | — | Tirar a frequência: “Quando se divulgam só os números de cada característica, a pergunta que interessa…”. |
| 13 | menor | pp. 63–65 e 67–68 (PDF) | Quebras de página ruins. (i) O enunciado da q. 3 termina no pé da p. 64 (“Está(ão) correta(s)…”, com meia página em branco), e as alternativas ficam no topo da p. 65. (ii) O mesmo ocorre na q. 19: enunciado na p. 67, alternativas na p. 68. (iii) A caixa do ex. 5.5 quebra deixando só “7 500.” no topo da p. 64. | Imagens das pp. 63, 64, 65, 67 e 68. | Na montagem final, manter as alternativas junto do enunciado (p. ex. `\needspace` ou `\begin{samepage}` em volta do enunciado e das `multicols`) e evitar a quebra da caixa do ex. 5.5 na última linha. |

**Contagem:** 1 bloqueante · 4 importantes · 8 menores.

## Conferido sem problemas
- **Respostas:** todas corretas, 6 exemplos e 21 questões, incluindo as letras: 3 d, 4 d, 6 d, 7 b,
  9 c, 10 e, 13 a, 14 a, 15 c, 16 a, 17 b, 18 a, 19 b, 20 d, 21 b. Também conferi os números do
  gancho (mínimo de 10 nos dois) e dos erros: E1 42, E2 45/35, E3 5/10, E4 120 = 15\%. As resoluções e
  os `\resp` são coerentes com D11 (a q. 1 traz só a linha do que a prova deve mostrar).
- **Transcrições × dossiê:** as q. 3, 4, 6, 7, 8, 9, 10, 11, 12 e 13 batem com os textos integrais do
  dossiê. Na q. 3, o parêntese que o dossiê abrevia com “(…)” aparece por extenso. As q. 14–21
  batem com os resumos (os números conferem).
- **Seções:** o prefácio tem pergunta aberta explícita, respondida por H1–H3. *De onde vem?* responde
  às três perguntas, e a reconstrução se sustenta por raciocínio. O mapa tem três casos enunciado →
  estrutura → ferramenta, e “Como reconhecer” descreve sinais do enunciado (v4). Os erros
  seguem o roteiro de cinco passos com contraexemplo concreto. As observações são opcionais e não
  guardam nada prometido (o prometido está em H1–H3).
- **N3:** ex. 5.6 é transferência legítima; nada no texto toca a q. 13 (ITA). O1 e O2 não antecipam
  nem a q. 12 nem a q. 13, e a O2 não dá a fórmula para três conjuntos. A exceção é o caso 3
  (achado 1).
- **Integradoras:** as q. 11 e 13 precisam de 5-H1 (sem a fórmula não se chega a $n(A\cup B)=6$ nem a
  $2^a+2^b-1$). A exceção é a q. 5 (achado 3).
- **IDs:** cada ID declarado é treinado na resolução, inclusive E1 no ex. 5.1 e na q. 2 e E2 nas q. 3
  e 6. Nenhum ID O foi declarado.
- **Três camadas e P5:** a passagem de Yule separa o que ele formulou (atributos, letras gregas,
  classes últimas, sentido inclusivo) da leitura moderna (“Lidas hoje…”) e da convenção atual.
  O texto não põe $\cap$, $\cup$ nem $n(A)$ na boca de Yule, e a passagem explica 5-H1, 5-H2 e o erro
  5-E2. A oração sobre Pearson só dá o nome da tabela. Passa no filtro por pouco, como terminologia
  útil, e não é um problema.
- **Procedência:** as etiquetas seguem a §5 e D5. O FME não é citado no corpo; o único `\src{fme}` está
  no caso 1, como permitido.
- **D7/D9:** prefácio, erros, H1 e casos do mapa não usam o caso concreto de nenhuma N2. A exceção é a
  H3 (4) (achado 2).
- **Síntese:** os quatro ponteiros (construção 5-H1, construção 5-H2, Onde é usado?, Erros comuns)
  apontam para caixas e seções existentes. A “p. 59” do Para lembrar está certa.
- **Fontes:** a numeração no PDF está certa ([25] Yule, [26] Miller, [27] Pearson, [28] eomIE,
  [29] eomIEprob), e cada `\src` é pertinente à passagem.
- **Matriz:** o `matriz.py` e o `checar.py` não acusam nada. As metas (N1 4, integradoras 1) parecem
  mínimos: a sequência tem 5 N1 e 3 integradoras.

## Fontes consultadas na web
1. Yule, 8.ª ed. (EconBiz/ZBW): a ficha da obra confirma “8. ed. rev”, Londres, Griffin, 1927
   (https://digi.econbiz.de/viewer/fullscreen/1751730271/11). As páginas de texto confirmam as
   passagens citadas. A p. 32 traz “termed the ultimate classes … it is never necessary to
   enumerate more than the ultimate frequencies. All the others can be obtained from these by simple
   addition”. A p. 34 (§19) traz “used in an inclusive sense … with or without others”.
   (https://digi.econbiz.de/viewer/fulltext/1751730271/32/ e …/34/)
2. Edições ao longo da primeira metade do século XX: as resenhas da Cambridge (Mathematical Gazette;
   J. Inst. Actuaries) registram a 14.ª ed., com Kendall, de 1950. Isso confirma “várias
   edições na primeira metade do século XX”.
3. Miller, *Earliest Known Uses … (C)*, MacTutor: “CONTINGENCY TABLE was introduced by Karl
   Pearson in 1904, in "On the Theory of Contingency…", Drapers' Company Research Memoirs, Biometric
   Series I” (https://mathshistory.st-andrews.ac.uk/Miller/mathword/c/). Confirma o nome e a data.
4. Encyclopedia of Mathematics, “Inclusion-exclusion formula”: traz
   $P(A_1\cup\dots\cup A_n)=S_1-S_2+\dots$, de que o caso de dois eventos é particular. Pertinente à
   5-O1 (https://encyclopediaofmath.org/wiki/Inclusion-exclusion_formula).
5. Encyclopedia of Mathematics, “Inclusion-and-exclusion principle”: as correções alternadas
   (inclui, exclui) valem para qualquer número finito de propriedades. Pertinente à 5-O2
   (https://encyclopediaofmath.org/wiki/Inclusion-and-exclusion_principle).
