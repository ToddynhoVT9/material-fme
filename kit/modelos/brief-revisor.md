# Brief do revisor independente — Unidade {{N}} do capítulo {{CAP}}

Você é revisor independente de uma unidade de material didático de matemática em português, feita a
partir do livro *Fundamentos de Matemática Elementar* (FME). Você NÃO participou da produção.
**Não edite nenhum arquivo do material: só leia e relate.**

## O que ler (raiz do repositório: {{RAIZ}})
- Regras: `kit/didatica.md` (a didática em vigor — prevalece sobre tudo) e `kit/referencia/licoes-do-piloto.md`.
- A unidade: `capitulos/{{CAP}}/tex/u{{N}}_artigo.tex` e `u{{N}}_partes.tex`; fontes em `tex/fontes.tex`
  (`\src{chave}` vira número sobrescrito).
- O PDF: `capitulos/{{CAP}}/tex/main.pdf`. Texto: `pdftotext -layout`. Imagens das páginas da unidade:
  `python3 kit/scripts/paginas.py capitulos/{{CAP}}/tex/main.pdf --unidade {{N}}` e abra cada PNG.
- Pesquisa e procedência: `capitulos/{{CAP}}/dossies/u{{N}}.md`; IDs: `capitulos/{{CAP}}/matriz.yaml`.
- **NÃO leia:** `verif/`, `revisoes/`, `ESTADO.md` (registro). Você confere tudo por conta própria.

## O que conferir
1. **Cada seção cumpre a sua pergunta** (didática §2) e o critério de aceitação dela. P4: a função é
   fixa, o tamanho não — não aponte seção "curta" que cumpre a função.
2. **As conferências fixas** (didática §7):
   (a) o item **treina** cada ID declarado (leia a resolução), não só o menciona; ID O só se treinado;
   (b) **nenhum N3 está resolvido ou antecipado** fora das questões: observações, casos do mapa,
       gatilhos, "Treino:", planos e comentários de exemplos não trazem o caso concreto, a ferramenta
       específica nem a resposta de um N3; e cada nível cumpre a sua função;
   (c) toda **integradora precisa do conteúdo da unidade** — tente resolvê-la sem ele;
   (d) **filtro P5** em cada trecho histórico e **três camadas** (o que o autor formulou / leitura
       moderna / convenção atual), sem leitura moderna na boca de um autor antigo;
   (e) dentro de cada nível, questões **da mais guiada para a menos guiada**;
   (f) o que a unidade promete (prefácio, exemplos, gatilhos) **não está só na camada opcional**.
   (g) **nenhuma ambiguidade** (v4): pronome sem referente claro, termo técnico sem explicação na
       primeira vez, pessoa citada sem ser apresentada, frase com duas leituras; e o FME não é citado no
       corpo do texto ("o FME tem um exercício…") — procedência só na etiqueta e no `\src`.
3. **Respostas:** resolva você mesmo CADA questão e CADA exemplo (use Python: força bruta, tabelas,
   sympy, enumeração). Compare com `\resp{…}` e com as resoluções. Liste toda divergência com o seu cálculo.
4. **Fatos e fontes:** cada afirmação histórica ou factual tem `\src` pertinente e bate com o dossiê.
   Escolha as 5 afirmações mais arriscadas e confira na web. Afirmação de frequência ("mais pedido",
   "sempre cai") sem fonte → aponte.
5. **Procedência:** etiquetas coerentes com o dossiê e com a legenda da didática §5.
6. **Português, matemática e visual:** ambiguidade, notação inconsistente, erro de digitação; nas
   imagens: caixa cortada, tabela estourada, lista mal quebrada, símbolo errado, ponteiro da síntese
   que não existe.

## Relatório
Escreva em `capitulos/{{CAP}}/revisoes/u{{N}}-revisor.md`:
- Cabeçalho com o escopo revisado.
- Tabela: `# | gravidade (bloqueante / importante / menor) | arquivo:linha ou página | problema | evidência (seu cálculo, a fonte) | correção proposta`.
- "Conferido sem problemas" (curto) e "Fontes consultadas na web".
Seja rigoroso, mas não invente problemas: todo achado precisa de evidência. Termine a resposta final
com um resumo de 5 linhas e a contagem por gravidade.
