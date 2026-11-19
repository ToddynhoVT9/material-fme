# Etapa 2 — Dossiê (por unidade)

**Entrada:** `escopo.md` (a unidade: pergunta, itens do FME, plano de pesquisa) e os IDs em `matriz.yaml`.
**Saída:** `dossies/uN.md` completo (modelo: `kit/modelos/dossie.md`); checagens das respostas do
banco em `verif/uN.py`; ajustes de IDs na `matriz.yaml`.
**O dossiê é a única entrada da montagem.** Tudo o que o texto afirmar como fato, toda procedência e
toda fonte saem dele. A montagem não pesquisa.

## Passos

1. Copie o modelo: `cp kit/modelos/dossie.md capitulos/<slug>/dossies/uN.md` e preencha o cabeçalho.

2. **Prefácio (§1):** um gancho concreto que crie a pergunta aberta da unidade.

3. **História (§2.2) — com o filtro P5 primeiro.** Para cada marco do plano, antes de pesquisar fundo,
   pergunte: ele ajuda a entender a ferramenta? Classifique já: *narrativa*, *observação* ou *fora*.
   Pesquise com profundidade proporcional ao valor: narrativa precisa de fonte boa; observação, de uma
   fonte; "fora" não se pesquisa.
   - Preencha as **três camadas**: o que o autor formulou (com a passagem) · a leitura moderna · a
     convenção atual. Se não souber o que o autor disse de fato, o marco não entra como fala do autor.
   - Fontes, em ordem de preferência: obra original (Perseus, Gutenberg, archive.org, edição crítica)
     → enciclopédia acadêmica (Stanford Encyclopedia of Philosophy, MacTutor) e artigos com DOI →
     Wikipédia e afins (**frágil**: aplique A5 — procurar a primária e citá-la ao lado).
   - Anote a passagem que sustenta a afirmação (paráfrase curta, página ou seção).

4. **Reconstrução (§2.3):** para cada H, os passos que chegam à ferramenta por raciocínio.

5. **Onde é usado (§3):** 2–4 casos de mapa do problema, cada um com um enunciado real e sua
   procedência. Gatilhos genéricos (nunca o caso concreto de um N3).

6. **Erros (§4):** os cinco passos de cada E, com contraexemplo concreto.

7. **Observações (§5):** só o que passa no teste de pertença (dispensável para usar o conceito).

8. **Banco de problemas (§6).** Fontes: exercícios do FME da unidade, vestibulares do FME, provas
   encontradas, problemas históricos e autorais. Para cada um: tipo, **nível pela função** (N3 só se a
   situação for nova em relação ao que o texto vai ensinar), IDs que treina, procedência e status.
   - Texto de prova só vira `[PROVA ANO, q.~n]` se conferido na prova (PDF oficial ou resolução que
     reproduz o enunciado). Senão: `[adaptada de …]`. Conferir prova é caro: faça só quando a função
     do item for mostrar a aplicação real; para treino, prefira autoral.
   - **Confira a resposta de cada problema por programa** em `verif/uN.py` (nomes provisórios; a
     montagem troca pelos rótulos finais). Gabarito oficial divergente → pendência.
   - Cubra as metas da matriz com folga (2–3 a mais), para a montagem escolher.

9. **Fontes (§7):** entradas já no formato do `\bibitem`, com chave, status e data de conferência.

10. Atualize `matriz.yaml` (IDs ajustados) e o `ESTADO.md` (próxima ação: "Montagem da UN").

## Pronto quando
- todo H, U e E tem material (construção, caso ou erro) no dossiê;
- o banco cobre as metas, com respostas conferidas por programa;
- todo fato tem fonte com status, e toda fonte frágil passou por A5;
- pendências para o usuário estão listadas (§8), sem bloquear o resto.

## Armadilhas do piloto
- Atribuir leitura moderna a autor antigo ("o 'ou' de Boole era o exclusivo dos estoicos";
  "Eubulides propôs…" com forma moderna).
- Afirmações de frequência sem fonte ("um dos formatos mais pedidos", "a FATEC tem um bloco fixo").
- Wikipédia, Fandom, blogs e transcrições como única fonte; datas de prova "via" sites não oficiais.
- Fontes pouco pertinentes: a página citada não diz o que o texto afirma (conferir a passagem!).
- Gastar a pesquisa em curiosidade que depois vira observação ou sai.
