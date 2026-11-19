# Etapa 1 — Escopo (uma vez por capítulo)

**Entrada:** o capítulo do FME (PDF ou imagens: teoria, exercícios, respostas) e as questões de
vestibular do capítulo, entregues pelo usuário.
**Saída:** `capitulos/<slug>/` criado; `escopo.md` preenchido; `matriz.yaml` com unidades, IDs e metas;
`verif/fme.py` conferindo o gabarito do livro; `ESTADO.md` com a próxima ação.
**Portão:** o usuário aprova o escopo antes da etapa 2.

## Passos

1. **Ler o material visualmente.** Renderize as páginas (`pdftoppm -r 110 -png`) e leia as imagens.
   A camada de texto (`pdftotext`) só serve para localizar páginas: ela perde símbolos e pode trazer
   respostas de outros capítulos (no piloto, as respostas 1–67 do volume inteiro estavam ocultas).
   Separe o gabarito do capítulo do resto.

2. **Inventariar.** Uma linha por item de teoria, exemplo do livro, exercício e questão de vestibular
   (`escopo.md` §2). Nada do FME pode faltar no material final; o que ficar fora tem motivo escrito.
   Anote problemas do material (§1): erro de impressão, alternativas fora de ordem, questão sem ano.

3. **Conferir o gabarito do FME por programa** (`verif/fme.py`: força bruta, enumeração, sympy).
   Divergência com o livro → §7 do escopo e pendência para o usuário.

4. **Dividir em unidades** (§3). Critérios: uma pergunta por unidade (ela vira a pergunta aberta do
   prefácio); cada unidade depende só das anteriores; tamanhos comparáveis. Desenhe o mapa de
   pré-requisitos. No piloto, 6 unidades para 17 páginas de teoria.

5. **Criar o esqueleto** com os títulos decididos:
   ```
   python3 kit/scripts/esqueleto.py capitulo capitulos/v<vol>c<n>-<slug> \
       --volume <vol> --numero <n> --titulo "<Título>" --unidades "<U1>" "<U2>" …
   ```
   (Para acrescentar uma unidade depois: `esqueleto.py unidade capitulos/<slug> --n 7 --titulo "…"`.)

6. **Definir os IDs de cada unidade** em `matriz.yaml` (`ids:` com uma descrição curta cada):
   - **H** — cada construção que *De onde vem?* fará (em geral 2–4);
   - **U** — cada contexto de uso que *Onde é usado?* ensinará a reconhecer (3–5);
   - **E** — cada erro comum, já com o raciocínio que leva a ele (3–5);
   - **O** — observações candidatas (0–4; opcionais).
   Escreva também `pergunta:` (a pergunta aberta).

7. **Metas** (`questoes_meta`). Ponto de partida do piloto: N1 4 · N2 5–6 · N3 2 · 1 integradora;
   exemplos: 5–6 por unidade, ≥ 1 por nível.

8. **Plano de pesquisa por unidade** (§6): que marcos históricos investigar (e se passam no P5 *a
   priori*), que tipo de enunciado real procurar, que erros documentar, que problemas buscar.
   É a lista de tarefas de cada dossiê.

9. **Apresentar ao usuário** (portão): tabela de unidades com a pergunta de cada uma, resumo dos IDs,
   metas, pendências (§8). Registre a aprovação e as decisões no `ESTADO.md`. Próxima ação: "Dossiê da U1".

## Pronto quando
- todo item do FME tem destino no inventário;
- cada unidade tem pergunta, IDs H/U/E e metas;
- o gabarito do FME foi conferido por programa;
- o usuário aprovou.

## Armadilhas do piloto
- Confiar na camada de texto do PDF (símbolos perdidos, respostas de outros capítulos).
- Questões de vestibular do FME sem ano: vira pendência de procedência já no escopo, não na montagem.
- Lacunas do livro (no Cap. I, a negação do bicondicional): decidir no escopo se entram e onde.
