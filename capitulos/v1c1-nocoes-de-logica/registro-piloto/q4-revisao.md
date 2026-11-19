# q3 — Revisão do material coletado · Cap. I — Noções de lógica

Piloto · FME vol. 1, Cap. I · 2026-11-17
Depende de: `00-decisoes.md`, `q1-pesquisa.md`, `q2-estrutura.md`, `matriz.yaml` · Alimenta: q4 (decisões)

O q3 **revisa e relata**: confere o material contra a didática e contra o plano do q2. **Não muda o plano.** As divergências vão numeradas para o q4 decidir (§8). Única alteração feita em arquivo: o *pool* de questões da `matriz.yaml` recebeu as questões encontradas aqui (é material coletado, não plano).

---

## 0. Registro de decisão do usuário
- **e1 confirmada (2026-11-17):** questões de concurso entram com etiqueta própria. `q2-estrutura.md` foi atualizado.

---

## 1. Itens `[a verificar]` — resultado

| Item (origem) | Resultado | O que fica valendo | Fonte |
|---|---|---|---|
| Boole, *Mathematical Analysis of Logic*, 1847 (q1) | **confirmado** | MAL (1847) e *Laws of Thought* (1854); De Morgan, *Formal Logic*, também 1847 | Britannica; SEP *George Boole* |
| ∨ vem do latim *vel* (q1, U2) | **corrigido** | A história do *vel* é a versão de manual e é contestada. Elkind & Zach (2023) rastreiam o ∨ ao trabalho de Whitehead e Russell anterior aos *Principia*: o primeiro ∨ para disjunção está num manuscrito de Russell de 1903. Leibniz usou "v" para *vel* (1679), mas isso ficou desconhecido. Boole usava + para o "ou" **exclusivo** (1847). A SEP tem uma seção chamada "o mito de *vel* e *aut*". | Elkind & Zach, *Review of Symbolic Logic* 16(3), 2023; slides dos autores; SEP *Disjunction* |
| Números de Hiparco (103 049 / 310 952) e Schröder (q1, U2) | **confirmado** | Plutarco atribui a Hiparco 103 049 conjunções "afirmativas" e 310 952 "negativas". Nos anos 1990 se reconheceu que 103 049 é o 10º número de Schröder (Hough, 1994; Stanley, 1997). 310 952 difere só no último dígito da metade da soma do 10º e do 11º, provavelmente erro de cópia antigo. | Encyclopedia.com (*Hipparchus*); Acerbi; MathPages; Bobzien |
| Polinômio de Euler n² + n + 41 (q2, ex. 5.4) | **confirmado** | Euler, 1772: primo para n = 0…39; em n = 40 dá 1681 = 41². Euler escreveu a forma 41 − x + xx (= n² − n + 41, primo para n = 1…40). | Perrin (Paris-Saclay), com a citação de Euler; Mathematical Gazette 2024; MSU/CRC |
| Łukasiewicz 1920 (q1, U1) | **descartado** | Saiu do plano no q2 (`1-O2` passou a ser "é dia" dos estoicos). Fica fora do material. | — |
| Paradoxo de Russell / barbeiro (q1, U5) | **descartado** | Saiu do plano no q2. Fica fora. | — |

**Saldo:** 4 confirmados ou corrigidos com fonte, 2 descartados. Nenhum `[a verificar]` remanescente no plano.

---

## 2. Correções ao q1 (o q1 errou ou ficou incompleto)

| # | O q1 disse | O que a revisão mostrou |
|---|---|---|
| C1 | A transcrição da FATEC 2013 "tem erros de sinal nas alternativas" | **Não são erros.** As alternativas B (y ≠ 4) e C (y ≠ 4 → x ≥ 3) são **distratores deliberados**, confirmados em duas transcrições independentes (Estratégia Vestibulares, Racha Cuca) e compatíveis com o PDF oficial do CPS (cujos símbolos a extração não recupera). Resposta: **E**. |
| C2 | "Escassez de lógica formal em vestibular" | **Parcialmente errado.** A FATEC tem um bloco fixo de "Raciocínio Lógico" na prova, e em vários anos ele traz lógica proposicional (2011, 2013, 2014, 2017, 2019 encontrados). O vestibular raro é o tradicional (FUVEST, Unicamp); o que existe se concentra em FATEC, PUC-GO, IFs e OBMEP. |
| C3 | "As OBMEP V2–V6 vêm sem ano" | Anos localizados (§3). O FME **adaptou** pelo menos uma: na V5, a ordem das alternativas está invertida em relação à prova (na OBMEP, 16 é a alternativa A; no FME, é a e). |
| C4 | Wason: "~10%" | Manter "cerca de 10% ou menos": Wason (1968) relata menos de 10%; Wason & Shapiro (1971), cerca de 4%. |

---

## 3. Procedência das questões do FME (regularizada)

| FME | Procedência apurada | Status | Observação |
|---|---|---|---|
| V1 | UF-RS (o FME não dá ano) | **ano não localizado** | discursiva ("justifique") |
| V2 | **OBMEP 2010, 1ª fase** (N2 q18 / N3 q11; também no N1) | confirmado em várias fontes secundárias concordantes | tamanduás e preguiças |
| V3 | **OBMEP 2009, 1ª fase, N3 q4** (também N1 q11) | **fonte primária** (PDF da prova no site da OBMEP) | uma base secundária diz 2008; a prova diz 2009. Alternativas do FME = as da prova |
| V4 | **Simulado OBMEP 2017, N3, q14** (questão reaproveitada; o ano original não foi localizado) | **fonte primária** (obmep.org.br, com solução: Ari, água) | gabarito confere com o FME (a) |
| V5 | **OBMEP 2005, 1ª fase, N3 q20** (e N2) | fonte secundária concordante (Olimpédia) + cópia da prova sem acesso (robots) | **o FME inverteu a ordem das alternativas** |
| V6 | **OBMEP 2007, 1ª fase, N2 q8** (e N3) | **fonte primária** (PDF da prova, OBMEP 2007) | gabarito D confere |

---

## 4. Questões externas novas

Respostas **verificadas por script** (`scripts/verif_vest_cap1.py`, bloco q3).

| Questão | Tipo | Unid. | Nível | IDs | Resposta | Verificação | Status do texto |
|---|---|---|---|---|---|---|---|
| FATEC 1º sem/2013, q13 — contrapositiva de "se x < 3, então y = −4" | vestibular | 3/4 | N1 | 3-U4, 3-E2 | **E** (se y ≠ −4, então x ≥ 3) | script: só E é equivalente | texto completo em 2 fontes concordantes; PDF oficial com símbolos ilegíveis |
| FATEC 1º sem/2019, q11 — negar "todas as vagas deste vestibular são de ensino superior" | vestibular | 6 | N1 | 6-U2, 6-E1 | **B** (existem vagas que não são…) | lógica (∃¬) | alternativas em 2 fontes; enunciado-base resumido |
| FATEC 2017 — negar "nenhum nefelibata é pragmático" | vestibular | 6 | N2 | 6-U2, 6-H4 | **C** (algum nefelibata é pragmático) | lógica (¬∀¬ = ∃) | **resumido** (qconcursos não fornece literal) |
| FATEC 1º sem/2014 — negar "Maria não faz Polímeros ou Júlia faz Silvicultura" | vestibular | 6 | N1 | 6-U1, 6-E2 | **B** (Maria faz Polímeros e Júlia não faz Silvicultura) | script: ¬(¬M ∨ J) ≡ M ∧ ¬J | **resumido** |
| FATEC 2011, prova 1 — negar −3 < x ≤ 2 | vestibular · **integradora** (inequações) | 6 | N2 | 6-U1, 6-E5 | **A** (x ≤ −3 ou x > 2) | script (malha de x) | **resumido** |
| PUC-GO 2010 — "nenhum vegetariano é carnívoro; todo felino é carnívoro" | vestibular | 4 | N2 | 4-U5 | **A** (nenhum felino é vegetariano) | script (modelos de 3 indivíduos) | **resumido** |
| OBMEP 2011, 1ª fase — Tia Geralda e os biscoitos (está no Simulado OBMEP 2017 N2 q12) | olimpíada | 3 | N3 | 3-U2, 3-U3 | **Eduardo** | script: culpado único = E | **texto primário** (simulado OBMEP) |
| CESPE/CEBRASPE 2023 — [(P → Q) ∧ P] → Q é tautologia? | concurso | 4 | N1 | 4-H1, 4-U1 | **tautologia** | script | resumido |
| VUNESP 2013 — contraditória de "todo homem é mortal" | concurso | 6 | N1 | 6-U2, 6-H4 | "algum homem não é mortal" | lógica | resumido |

**Identificadas, mas sem texto obtido** (candidatas para o q5, se o texto aparecer):
- FATEC 2019 (q1266043, asserções I/II verdadeira/falsa) — unid. 1/2
- IFF 2017, vestibular 2º sem. — unid. 1/2
- FUNDATEC/SEBRAE-SP 2019, vestibular ("assinale a alternativa que apresenta uma proposição") — unid. 1
- Simulado OBMEP 2017 N3 q4 (cinco amigas, uma diz a verdade) — unid. 1 (só a solução foi lida; gabarito D)

---

## 5. Afirmação de frequência ("negação é o mais cobrado")

- **Evidência:**
  - Das 5 questões de lógica proposicional da FATEC encontradas (2011–2019), **4 são de negação**.
  - Materiais de preparação para concursos citam a negação de "todo/nenhum" como tema recorrente; isso é opinião editorial, não estatística.
  - A OBMEP traz ao menos uma questão de lógica por prova desde 2007, segundo uma dissertação (EduCAPES; fonte secundária).
- **Reformulação para o material:** "Nas provas que cobram lógica formal — em especial a FATEC e concursos — **pedir a negação** de uma frase é um dos formatos mais comuns; na amostra reunida para este material, foi o mais frequente." Sem números gerais.

---

## 6. Conformidade — didática × plano (q2)

| Seção da didática | Exigência da didática | Como o q2 atende | Situação |
|---|---|---|---|
| Prefácio | propósito + curiosidade; **fora da narrativa**; prepara | caixa de abertura; proibido definir/resolver; pré-requisitos (w7) | ✓ |
| De onde vem? | contexto histórico/filosófico, experimentos; **construir do zero**; quem, por quê, contexto; **objetivo: facilitar a memorização** pelo significado | roteiro histórico + construções H + notação + fecho | ⚠ a memorização não está operacionalizada → **D3** |
| Onde é usado? | contextos; **como identificar** num exercício a ferramenta e o raciocínio | texto analítico + tabela de gatilhos | ✓ (frequência reformulada, §5) |
| Erros comuns | quais, por quê, que raciocínio leva, como evitar | 4 campos fixos | ✓ |
| Observações | complementos | itens O | ✓ (+ proposta **D5**) |
| Exemplos | 3 níveis, ≥ 1 por nível; juntos cobrem tudo; **priorizar históricos e vestibulares** | matriz R1/R2 passam | ⚠ **18 de 32 exemplos são autorais** e 2 são de concurso, embora já haja vestibular equivalente → **D1** |
| Questões | série classificada em níveis; **podem envolver outros assuntos** | metas por nível | ⚠ o plano não prevê questões integradoras → **D2** |
| Respostas | só a resposta, formato `[ 14. (c) ]` | formatos definidos | ✓ |
| p3 autocontido | estudante encontra tudo ali | pré-requisitos no prefácio | ⚠ a Unid. 5/6 usa universo, ∈ e intervalos (o Cap. II, Conjuntos, vem *depois*); os exercícios do FME usam mdc, mmc, divisibilidade, potências e raízes → **D4** |

---

## 7. Conformidade — material coletado × plano (q2/matriz)

| Unidade | Base histórica | Questões reais (pool) | Exemplos com fonte real | Situação |
|---|---|---|---|---|
| 1 | Aristóteles, estoicos, Peano/Heyting | 4/10 (FME 1, 2; OBMEP 2010) | 1 (1.1 FME) + 1 histórico | ⚠ pouca questão externa |
| 2 | Crisipo, estoicos, Boole/Jevons, **Hiparco ✓**, ∨ corrigido | 2/10 | 1 FME + 1 OBMEP + Shannon | ⚠ maior déficit relativo |
| 3 | Fílon/Diodoro/corvos, Wason | 7/12 | 1 FME + 1 OBMEP + Wason | ✓ |
| 4 | Tractatus, tabelas, Boole, Carroll | 3/10 | Carroll | ⚠ |
| 5 | Frege/Peirce, Peano/Gentzen, **Euler ✓** | 1/10 | 1 FME + UF-RS + Euler | ⚠ maior déficit absoluto |
| 6 | quadrado das oposições, De Morgan/Ockham | 6/12 (FATEC ×4) | 2 de concurso (substituíveis) | ✓ material farto |

Pool total: **23/64** (era 15). Um item usado como exemplo sai do pool (e4).

---

## 8. Divergências para o q4 decidir

Cada item traz o que mudar (material ou plano) e uma recomendação. Nenhum toca a didática.

| # | Divergência | Opções | Recomendação |
|---|---|---|---|
| **D1** | Exemplos majoritariamente autorais; 6.1 e 6.2 de concurso, embora haja vestibular (a regra e1 manda preferir vestibular) | (a) substituir onde houver material real; (b) manter | **(a), mudando o plano:** 6.1 → FATEC 2014/1 (negar ∨); 6.2 → FATEC 2019/1 (negar "todas"); 4.2 → FATEC 2013/1 (contrapositiva, mantendo ~p ∨ q no comentário); 6.3 incorpora FATEC 2011 (−3 < x ≤ 2) como segundo item. O concurso sai dos exemplos. |
| **D2** | A didática permite questões que envolvem outros assuntos; o plano não prevê | (a) meta de ≥ 1 integradora por unidade; (b) não exigir | **(a), mudando o plano:** FATEC 2011 (inequações), OBMEP 2005 (intervalos) e autorais com divisibilidade/potências. |
| **D3** | "De onde vem" deve facilitar a memorização pelo significado; a spec não diz como | (a) acrescentar um fecho "**Para lembrar**": a ideia em 1 frase + a construção em ≤ 3 passos; (b) deixar implícito | **(a), mudando a spec** do §2.2 do q2 (a didática não muda; só fica explícito como cumpri-la). |
| **D4** | p3: a Unid. 5/6 depende de noções de conjunto (o Cap. II vem depois); os exercícios usam mdc, mmc etc. | (a) caixa "O mínimo que você precisa" no prefácio das Unid. 1 e 5; (b) só remeter ao Cap. II | **(a)**: a remissão sozinha quebra o p3. |
| **D5** | O mito do *vel* × *aut* enriquece a Unid. 2 e corrige um erro comum de livros | (a) novo ID `2-O3`, coberto no comentário do exemplo 2.2; (b) só ajustar a frase de "de onde vem" | **(a)** |
| **D6** | O FME adaptou a OBMEP V5 (alternativas invertidas) | (a) usar o texto original da prova; (b) o do FME | **(a)**, com a etiqueta `[OBMEP 2005]` e uma nota "o FME traz versão adaptada". |
| **D7** | 4 questões FATEC/PUC-GO só têm texto resumido (qconcursos não fornece literal) | (a) obter o texto da prova oficial (o CPS publica as provas da FATEC) no q5; se falhar, `[adaptada de FATEC 2014]` com redação reconstruída e resposta verificada; (b) descartar | **(a)** |
| **D8** | `6-E2` está definido como "manter o **e**"; a FATEC 2014 testa manter o **ou** | (a) generalizar para "manter o conectivo ao negar (∧ ou ∨)"; (b) criar um E novo | **(a)** |
| **D9** | V1 (UF-RS) sem ano | (a) etiqueta `[UF-RS — via FME]`; (b) trocar por outra | **(a)**: a fonte é o próprio livro-base. |
| **D10** | Unid. 5 com 1/10 questões reais e nenhum vestibular externo | (a) completar com autorais + FME ex. 8 subdividido; (b) nova busca no q5 | **(a)** e uma busca rápida no q5, sem bloquear. |
| **D11** | Unid. 2 com 2/10 questões reais | idem | idem |
| **D12** | Gancho da Unid. 3 ("menos de 1 em 10") | usar a formulação C4 | — (ajuste de redação) |

---

## 9. Estado para o q4
- Matriz: **sem falhas** (R1/R2/R5); pendências R3/R4 = déficit de questões, esperado.
- Banco: 23/64; ~41 a completar (autorais, mais o que D7 e D10 trouxerem).
- Scripts: `verif_vest_cap1.py` estendido com 6 verificações novas, todas conferem.

---

## 10. Fontes novas desta revisão
- Elkind, L. D. C.; Zach, R. *The Genealogy of '∨'*. Review of Symbolic Logic 16(3), 2023: https://philarchive.org/archive/ELKTGO · slides: https://sambuz.com/doc/the-genealogy-of-ppt-presentation-1088927
- SEP, *Disjunction* (seção "The Myth of Vel and Aut"): https://plato.stanford.edu/archives/fall2008/entries/disjunction/
- Britannica, *Boole and De Morgan*: https://www.britannica.com/topic/history-of-logic/Boole-and-De-Morgan
- SEP, *George Boole*: https://plato.stanford.edu/archives/spr2021/entries/boole/
- Encyclopedia.com, *Hipparchus*: https://www.encyclopedia.com/science/dictionaries-thesauruses-pictures-and-press-releases/hipparchus-0
- MathPages, *Hipparchus on Compound Statements*: https://mathpages.com/home/kmath397/kmath397.htm
- Wikipedia, *Schröder–Hipparchus number*: https://en.wikipedia.org/wiki/Schr%C3%B6der%E2%80%93Hipparchus_number
- D. Perrin, sobre Euler (1772): https://www.imo.universite-paris-saclay.fr/~perrin/journeedu2311/redaction2311e.pdf
- Heffernan, Lord & MacHale, *Euler's prime-producing polynomial revisited* (Math. Gazette 2024): https://www.tandfonline.com/doi/pdf/10.1017/mag.2024.11
- OBMEP 2009, prova 1ª fase N3: http://obmep2010.obmep.org.br/provas_static/export/sites/default/provas/provas2009/1_fase/prova_1fase_n3_final.pdf
- OBMEP 2007, prova 1ª fase N2: http://obmep2010.obmep.org.br/provas_static/export/sites/default/provas/provas2007/2007/1_fase/N2_curvas_final_imp_2507.pdf
- Simulado OBMEP 2017 N3 (soluções): https://www.obmep.org.br/docs/sim-2017-N3-solucoes.pdf
- Simulado OBMEP 2017 N2: https://www.obmep.org.br/docs/sim-2017-N2.pdf
- Olimpédia — Banco de questões, Raciocínio Lógico N2/N3: https://olimpedia.fandom.com/pt-br/wiki/Banco_de_Quest%C3%B5es_-_Racioc%C3%ADnio_L%C3%B3gico_-_N%C3%ADvel_3
- Estuda.com — OBMEP 2010 N2 / OBMEP 2009 N3: https://enem.estuda.com/questoes/?acao=imprimir&resolver=723211 · https://app.estuda.com/questoes/?id=82236
- FATEC 1º sem/2013 — prova oficial (CPS): https://bkpsitecpsnew.blob.core.windows.net/uploadsitecps/sites/1/2021/09/prova-vestibular-1s-2013.pdf
- Estratégia Vestibulares — FATEC 2013: https://vestibulares.estrategia.com/public/questoes/Logica-tem-que36f11d49c9/
- Racha Cuca — FATEC raciocínio lógico: https://rachacuca.com.br/educacao/vestibular/tags/raciocinio-logico/
- Estratégia Vestibulares — FATEC 2019: https://vestibulares.estrategia.com/public/questoes/Sa-proposicoes483bc1fe45/
- Educacional Plenus — FATEC 2019: https://educacionalplenus.com.br/fatec-vestibular-2019-prova-de-raciocinio-logico/
- Qconcursos — vestibular, negação/De Morgan: https://www.qconcursos.com/questoes-de-vestibular/disciplinas/matematica-raciocinio-logico/negacao-leis-de-morgan-negativa-de-uma-proposicao-composta/questoes
- Estratégia Concursos — negação de todo/algum/nenhum: https://www.estrategiaconcursos.com.br/blog/raciocinio-logico-negacao-de-todo-e-nenhum-4/
