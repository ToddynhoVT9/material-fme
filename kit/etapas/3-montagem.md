# Etapa 3 — Montagem (por unidade)

**Entrada:** `dossies/uN.md`, a unidade na `matriz.yaml`, `kit/didatica.md` §2–§3 e §10,
`kit/referencia/macros.md`. Referência de tom e de forma: uma unidade pronta do Cap. I
(`capitulos/v1c1-nocoes-de-logica/tex/u3_*.tex` é um bom modelo).
**Saída:** `tex/uN_artigo.tex` e `tex/uN_partes.tex`; itens na `matriz.yaml`; `verif/uN.py` sem
falhas; entradas novas em `tex/fontes.tex`; `checar.py --unidades N` sem FALHAS; páginas conferidas.

## Passos

1. **Planeje os itens antes de escrever.** A partir do banco do dossiê, escolha exemplos (≥ 1 por
   nível, cobrindo todo H/U/E) e questões (metas por nível). Dê a cada item um **rótulo** semântico
   (`u2:intervalo`, `ex:u2:circuito`) e escreva-os já na `matriz.yaml` (`rotulo`, `nivel`, `fonte`,
   `cobre`, `integradora`). Ordene as questões de cada nível da mais guiada para a menos guiada.
   Para cada N3, escreva em uma linha *o que é novo* em relação ao texto — e não ponha isso no texto.

2. **Escreva `uN_artigo.tex`** (Prefácio, De onde vem?, Para lembrar, Onde é usado?) a partir do
   modelo que o esqueleto criou. Em partes, se for longo: prefácio + De onde vem?, depois Onde é usado?.
   - Fatos só do dossiê, cada um com `\src{chave}`; três camadas na redação; filtro P5.
   - Casos e gatilhos apontam só para itens N1/N2 (`\exref`, `\qref`, `q.~\ref{…}`).

3. **Escreva `uN_partes.tex`** (Erros, Observações, Exemplos, Questões, Síntese, Respostas).
   - Questão: `\begin{questao}{nível}{procedência}{IDs}\label{uN:nome}` … `\resp{resultado}` … `\end{questao}`.
   - Exemplo: `\begin{exemplo}{}{nível}{procedência}{IDs}` + `\label{ex:uN:nome}` + Plano/Resolução/Comentário.
   - Remissões **só por rótulo**; nada de "questão 7" digitado.
   - IDs declarados = o que o item treina de fato; O só se treinado.
   - Síntese: ponteiros com `\ondever{…}` para seções/caixas que existem.

4. **Verificador** `verif/uN.py`: um `chk("rótulo", cálculo, valor impresso)` por resposta calculável
   (exemplos e questões), recalculado sem copiar o texto. Rode até "0 falha(s)".

5. **Fontes:** copie do dossiê para `tex/fontes.tex` as entradas citadas na unidade (sem duplicar chave).

6. **Compile e confira:** `python3 kit/scripts/checar.py capitulos/<slug> --unidades N`.
   Zero FALHAS. Cada AVISO é lido: corrigido ou justificado (remissão numérica que é procedência,
   ID O realmente treinado…).

7. **Confira o visual:** `python3 kit/scripts/paginas.py capitulos/<slug>/tex/main.pdf --unidade N`
   e abra cada folha. Procure: caixa cortada, tabela estourada, lista mal quebrada, página quase vazia
   antes de caixa inquebrável, símbolo errado.

8. **Autoconferência** antes da revisão — as seis conferências da didática §7, item por item:
   (a) treina o ID? (b) algum N3 antecipado em observação, caso, gatilho, plano ou comentário?
   (c) integradora resolve-se sem a unidade? (d) P5 e três camadas? (e) ordem por guia? (f) o
   prometido está fora da camada opcional?

9. `ESTADO.md`: etapa da unidade → `revisão`; registro da sessão com o resultado do `checar.py`.

## Pronto quando
`verif/uN.py` sem falhas · `checar.py --unidades N` sem FALHAS · avisos resolvidos ou justificados ·
folhas conferidas · autoconferência feita.

## Armadilhas do piloto
- Observação, gatilho ou "Treino:" entregando o N3 — o defeito mais repetido (achado em todas as unidades).
- Exemplo declarando ID O que ele só cita.
- Integradora que se resolve sem o conteúdo da unidade (o "sem resolver a inequação" não salva).
- Ponteiro da síntese para "Definição" numa unidade sem caixa de definição.
- Alternativas em linha com `\mbox` + `\hspace` (quebram mal no PDF).
