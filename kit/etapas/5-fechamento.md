# Etapa 5 — Fechamento (uma vez por capítulo)

**Entrada:** todas as unidades `pronta` no `ESTADO.md`.
**Saída:** `tex/abertura.tex`, `tex/glossario.tex` e `tex/fontes.tex` finais; conferência entre
unidades; `saida/<slug>.pdf`; entrega ao usuário.

## Passos

1. **Abertura** (`kit/didatica.md` §9; modelo pronto: `capitulos/v1c1-nocoes-de-logica/tex/abertura.tex`):
   - *Por que este capítulo*: 2–4 parágrafos, sem frequência sem fonte.
   - *Linha do tempo*: só marcos contados em alguma unidade (narrativa ou observação), com `\src` e a
     unidade. Tire dos dossiês (§2.2, veredito P5 "narrativa" ou "observação").
   - *Mapa das unidades*: diagrama TikZ de pré-requisitos (do escopo) e a tabela "a pergunta que a
     unidade responde" — **igual** à pergunta aberta de cada prefácio — e "o que você leva dela".
   - *Tabela de notação*: símbolo, leitura, quem introduziu, quando, unidade — só com fonte.
   - *Como usar*: o texto do modelo; ajuste só o que for específico do capítulo.

2. **Glossário:** termos novos de cada dossiê (cabeçalho) + símbolos; uma linha cada, com a unidade.

3. **Fontes:** `checar.py` lista órfãs e faltantes; elimine duplicatas; confira o formato.

4. **Coerência entre unidades** (leitura): notação igual em todas; o que uma unidade diz que "volta na
   Unidade X" volta mesmo; pré-requisitos do prefácio batem com o mapa; termos batem com o glossário;
   nenhuma unidade contradiz outra. Opcional: um subagente revisor só para isso.

5. **Conferência final:** todos os `verif/uN.py` sem falhas; `checar.py capitulos/<slug>` sem FALHAS;
   `paginas.py` na abertura, glossário, fontes e em amostras de cada unidade.

6. **Entrega:** copie `tex/main.pdf` para `saida/<slug>.pdf`, envie ao usuário com um resumo curto
   (páginas, unidades, checagens, pendências que ficaram) e marque o portão no `ESTADO.md`.
