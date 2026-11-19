# Escopo — Cap. II · Conjuntos (FME vol. 1)

Etapa 1 (`kit/etapas/1-escopo.md`). Sai daqui: a divisão em unidades, os IDs (que vão para `matriz.yaml`),
as metas e o plano de pesquisa de cada dossiê. **O usuário aprova este arquivo antes da etapa 2.**

## 1. Material de entrada
PDF entregue pelo usuário em 2026-11-19: `02 - Cap II - Conjuntos.pdf` (35 páginas; não versionado — ver ESTADO).

| páginas do PDF (livro) | conteúdo |
|---|---|
| 1–5, 8–10, 12–13, 16–17 (pp. 18–22, 25–27, 29–30, 33–34) | teoria, itens 19–40 (§ I a XI) |
| 6–7, 10–11, 13–20 (pp. 23–24, 27–28, 30–37) | exercícios 11–61 (resolvidos no livro: 11, 12, 17, 18, 24, 29, 32, 39, 43) |
| 21–22 (pp. 38–39) | Leitura: "Cantor e a teoria dos conjuntos" (H. H. Domingues) |
| 23–25 (pp. 271–273) | respostas dos exercícios do Cap. II (13–61) |
| 25–34 (pp. 314–322) | questões de vestibular 7–47 ("Conjuntos") |
| 35 (p. 404) | respostas das questões de vestibular 7–47 |

- Leitura **visual** das páginas (110 dpi; zoom de 200 dpi nas passagens duvidosas). A camada de texto do
  PDF serviu de índice e de apoio à transcrição; ela perde ∈, ⊂, ∪, ∩, = e traz respostas ocultas de outros
  capítulos (a p. 271 tem, invisíveis, respostas que começam no exercício 10 do Cap. I).
- **Lição desta etapa:** numa leitura em página dupla a 110 dpi, li "torcem *apenas* pelo Palmeiras" na
  vest. 30, e o texto diz "torcem pelo Palmeiras" (o que muda a resposta). Na montagem, transcrever enunciado
  de questão **com zoom de 200 dpi e conferência contra a camada de texto**.

Problemas encontrados no material:

| # | onde | problema | tratamento |
|---|---|---|---|
| M1 | item 29 | título "Conjuntos iguais" repetido (já é o § V, item 25); o 29 é a igualdade por dupla inclusão | U2: construção "igualdade = dupla inclusão" |
| M2 | ex. 13e | "capitais da região Centro-Oeste": o gabarito omite Brasília (DF está na região) | adaptar: "capitais dos **estados** da região Centro-Oeste" — aí o gabarito vale |
| M3 | ex. 14 (gabarito) | B = {0, −10, −20, …} descrito como "múltiplo inteiro e **negativo** de 10" (0 não é negativo); C = {1, 4, 9, …} como "quadrado de um inteiro" (0 = 0² ficaria de fora) | resposta própria: "não positivo"; "quadrado de inteiro positivo" — vira material de E (U1) |
| M4 | ex. 13d | "frações com numerador e denominador entre 0 e 3": {1/1, 1/2, 2/1, 2/2} tem 4 frações, mas só 3 números (1/1 = 2/2) | U1/U2: deixar explícito que o conjunto é de *frações* (objetos), e usar o contraste como exemplo de igualdade |
| M5 | ex. 15 e 16 | universo não declarado: o gabarito (só D unitário) supõe x real; em ℤ, A = {2} seria unitário | U1: é exatamente o erro "esquecer o universo"; enunciado do material declara U |
| M6 | ex. 42b | "Ā − A ∪ B" sem parênteses; o gabarito lê Ā − (A ∪ B) | adaptar com parênteses |
| M7 | ex. 42f (gabarito) | figura pinta B̄; o pedido é B̄ ∩ A = A − B | divergência (§7) — material usa a resposta correta |
| M8 | vest. 36 (gabarito) | gabarito d (42%); o cálculo dá 100 − n(X ∪ Y) = 48% (e) | divergência (§7) |
| M9 | vest. 20, 22, 33 | "A e B" usado no sentido inclusivo (inclui quem está nos três); na 20, a leitura exclusiva dá 62 (alternativa d), não 58 (c) | U6: vira o erro E1 ("A e B" × "só A e B"); enunciado do material deixa a leitura inequívoca |
| M10 | ex. 26 | "círculo" no sentido de disco (região), não de circunferência | nota no enunciado |
| M11 | ex. 47 | "a ⊂ E" é F porque *a* não é conjunto (o FME admite elementos que não são conjuntos) | U2: observação sobre urelementos × teoria em que tudo é conjunto |
| M12 | todas as vestibulares | sem ano (só a banca) | procedência "[BANCA via FME, ano não informado]"; procurar ano só se a função for "aplicação real" |
| M13 | Leitura | atribui a Arquimedes a distinção infinito potencial/atual (é de Aristóteles, *Física* III); data a definição de Dedekind de 1872 (publicada em 1888, *Was sind und was sollen die Zahlen?*) | a Leitura não é reproduzida; serve de pista. Conferir no dossiê (A5) antes de usar qualquer fato dela |
| M14 | lacunas da teoria | o FME usa sem definir no texto: complementar em relação a U (Ā, A^C, X′, ∁A — só em exercícios), n(A ∪ B) e n(A ∪ B ∪ C) (só exercícios 48 e 50), n(𝒫(A)) = 2ⁿ (usado nos ex. 22, 49 e vest. 40, 43, 46), diferença simétrica (ex. 60) | §8, decisão D3 |

## 2. Inventário do FME — nada pode faltar

### Teoria
| item do FME | conteúdo | unidade | entra como |
|---|---|---|---|
| intro + 19 | noções primitivas (conjunto, elemento, pertinência); ∈, ∉; elemento pode ser conjunto; diagrama de Euler-Venn | U1 | construção (H1) + definição |
| 20 | descrição por enumeração: finita, infinita com reticências, finita grande | U1 | construção (H2) |
| 21 | descrição por propriedade {x \| P(x)} | U1 | construção (H2) |
| 22 | conjunto unitário | U1 | definição (H4) |
| 23 | conjunto vazio (propriedade logicamente falsa) | U1 | construção (H4) |
| 24 | conjunto universo; {x ∈ U \| P(x)}; exemplo da mediatriz (reta, plano, espaço) | U1 | construção (H3) + exemplo |
| 25 | igualdade: ordem e repetição não importam | U2 | construção (H1) |
| 26 | A ≠ B | U2 | definição (H1) |
| 27 | subconjunto, ⊂ (inclui a igualdade) | U2 | construção (H2) |
| 28 | ⊃, ⊄ | U2 | definição (H2) + erro E3 |
| 29 | igualdade por dupla inclusão (ver M1) | U2 | construção (H3) |
| 30 | propriedades da inclusão; prova de ∅ ⊂ A por vacuidade | U2 | construção (H2) |
| 31 | conjunto das partes 𝒫(A) | U2 | construção (H4) |
| 32 | reunião | U3 | construção (H1) |
| 33 | propriedades da reunião (via proposições, remete ao ex. 7 do Cap. I) | U3 | construção (H2) |
| 34 | interseção | U3 | construção (H1) |
| 35 | propriedades da interseção (inclui A ∩ U = A) | U3 | construção (H2) |
| 36 | conjuntos disjuntos | U3 | definição (H4) |
| 37 | absorção e distributivas | U3 | construção (H3) |
| 38 | diferença | U4 | construção (H1) |
| 39 | complementar de B em A, ∁_A B | U4 | construção (H2) |
| 40 | propriedades da complementação (inclui De Morgan relativo a A) | U4 | construção (H3) |
| Leitura | Cantor, infinito potencial/atual, Galileu, Dedekind, enumerabilidade | U1, U2 | pistas para o dossiê (M13); Galileu → 2-O2 |

### Exercícios (51)
| item | conteúdo | unidade | entra como |
|---|---|---|---|
| 11 (resolvido) | elementos de conjuntos dados por propriedade | U1 | exemplo N1 (adaptado) |
| 12 (resolvido) | propriedade característica de conjuntos enumerados | U1 | exemplo N1 (adaptado) |
| 13 | escrever com símbolos (ver M2, M4) | U1 | questão N1 |
| 14 | propriedade dos elementos (ver M3) | U1 | questão N1/N2 |
| 15 | quais são unitários (ver M5) | U1 | questão N2 (universo declarado) |
| 16 | quais são vazios (divisor de zero, divisível por zero) | U1 | questão N2 |
| 17 (resolvido) | escrever e classificar sentenças com ∈, ⊂ | U2 | exemplo N1 |
| 18 (resolvido) | V/F de inclusões, com justificativa | U2 | exemplo N1 |
| 19 | igualdades verdadeiras | U2 | questão N1 |
| 20 | V/F com ∈ e ⊂, chaves aninhadas | U2 | questão N2 |
| 21 | diagrama de D ⊂ C ⊂ B ⊂ A | U2 | questão N1 |
| 22 | 𝒫({a, b, c, d}) | U2 | questão N1 |
| 35 | nº de X com {1, 2} ⊂ X ⊂ {1, 2, 3, 4} | U2 | questão N2 |
| 47 | E = {a, {a}}: ∈ e ⊂ (ver M11) | U2 | questão N2 |
| 23 | reuniões de conjuntos dados | U3 | questão N1 |
| 24 (resolvido) | A ⊂ A ∪ B | U3 | exemplo N1 (prova pelo elemento genérico) |
| 25 | V/F com ∪ para conjuntos quaisquer | U3 | questão N1 |
| 26 | reunião dos discos de raio r que contêm O (ver M10) | U3 | questão N3 (transferência: reunião infinita na geometria) |
| 27 | reunião das paralelas a r em α | U3 | questão N2 |
| 28 | interseções de conjuntos dados | U3 | questão N1 |
| 29 (resolvido) | A ∩ B ⊂ A | U3 | exemplo (com o 24) |
| 30 | V/F com ∩ | U3 | questão N1 |
| 31 | quadriláteros: L ∩ P, R ∩ P, … | U3 | questão N2 integradora (geometria) |
| 32 (resolvido) | X com X ∪ B = A ∪ C e X ∩ B = ∅ | U3 | exemplo N2 |
| 33 | X a partir de três condições | U3 | questão N2 |
| 34 | C a partir de reuniões e interseções | U3 | questão N3 |
| 36 | sombrear A ∩ B ∩ C, A ∩ (B ∪ C)… | U3 | questão N1 |
| 37 | máximo de n((A ∩ B) ∩ C) | U3 | questão N2 |
| 46 | elementos de conjuntos dados por equações com "ou"/"e" | U3 | questão N2 integradora (equações) |
| 61 | diagrama com A ⊄ B, B ⊄ A, C ⊃ A ∪ B, D ⊂ A ∩ B | U3 | questão N2 |
| 38 | diferenças | U4 | questão N1 |
| 39 (resolvido) | A − B ⊂ A | U4 | exemplo N1 |
| 40 | V/F com diferença | U4 | questão N1 |
| 41 | X ⊂ A com A − X = B ∩ C | U4 | questão N2 |
| 42 | sombrear expressões com complementar (ver M6, M7) | U4 | questão N1/N2 |
| 43 (resolvido) | A − B̄ = A ∩ B | U4 | exemplo N2 |
| 44 | V/F com complementar em U | U4 | questão N2 |
| 45 | F̄ com F dado por inequação | U4 | questão N1 integradora (inequação) |
| 53 | simplificar P′ ∪ (P ∩ Q) | U4 | questão N2 |
| 55 | n(A), n(B) a partir de Ā, A ∩ B, A ∪ B | U4 | questão N2 |
| 60 | diferença simétrica: cálculo, provas, diagramas | U4 | questão N3 (operação nova definida no enunciado) |
| 48 | provar n(A ∪ B) = n(A) + n(B) − n(A ∩ B) | U5 | construção H1 + questão N2 (refazer a prova) |
| 49 | n(𝒫(A ∪ B)) com n(A), n(B), n(A ∩ B) | U5 | questão N2 (usa U2) |
| 51 | n(A ∩ B): múltiplos de 3 × divisores de 120 | U5 | questão N2 integradora (divisibilidade) |
| 52 | inglês/francês: 415 alunos | U5 | questão N1 |
| 58 | etnias: brancos, não negros, 50% amarelos | U5 | questão N2 |
| 59 | plano médico por filial (porcentagens de bases diferentes) | U5 | questão N3 |
| 50 | fórmula de n(A ∪ B ∪ C) | U6 | construção H3 + questão N2 |
| 54 | n de regiões com C ⊂ B | U6 | questão N2 |
| 56 | sabão em pó: tabela de 3 marcas | U6 | questão N1 |
| 57 | determinar A, B, C a partir de seis condições | U6 | questão N3 |

### Questões de vestibular (41: 7–47, todas sem ano — M12)
| item | banca | conteúdo | unidade | entra como |
|---|---|---|---|---|
| 7 | U.E. Londrina-PR | rejeição a dois partidos | U5 | questão N1 |
| 8 | FEI-SP | inglês/francês por sexo (bases diferentes) | U5 | questão N2 |
| 9 | UFF-RJ | caixas reprovadas nos dois testes | U5 | questão N1 |
| 10 | ESPM-SP | porcentagens → total de funcionários | U5 | questão N2 |
| 11 | PUC-PR | biotecnologia/proteção: afirmativas I–IV | U5 | questão N1 |
| 12 | UFF-RJ | espécies dentro/fora da Mata Atlântica | U5 | questão N2 |
| 13 | UF-CE | português/matemática | U5 | questão N1 |
| 14 | UE-CE | azul/amarelo | U5 | questão N1 |
| 15 | FEI-SP | aparelhos A e B | U5 | questão N1 |
| 16 | PUC-MG | conta própria/carteira assinada | U5 | questão N1 |
| 17 | UF-RN | espanhol/inglês | U5 | questão N1 |
| 18 | UF São Carlos-SP | fumantes por sexo (bases diferentes) | U5 | questão N2 |
| 21 | UF-RN | 3º ano ou não estudam francês | U5 | questão N2 |
| 32 | PUC-MG | frações de uma partição | U5 | questão N2 |
| 41 | ITA-SP | n(𝒫(A) ∪ 𝒫(B)) + 1 = n(𝒫(A ∪ B)) | U5 | questão N3 (usa U2) |
| 19 | UF-PE | duas modalidades por aluno, restrições | U6 | questão N3 |
| 20 | U.E. Londrina-PR | cardápio do RU (ver M9) | U6 | questão N2 |
| 22 | Udesc-SC | leitura: revistas/livros/jornais | U6 | questão N2 |
| 23 | FEI-SP | produtos A, B, C | U6 | questão N1 |
| 24 | UF-PA | três disciplinas, ninguém fora | U6 | questão N1 |
| 25 | U.E. Londrina-PR | três novelas | U6 | questão N1 |
| 26 | UF-PA | Paysandu, Remo, Vasco (A ∩ B = ∅) | U6 | questão N2 |
| 27 | UF-PI | Cotas, Bolsas, Enem | U6 | questão N2 |
| 28 | UF-ES | serviços básicos ("exatamente um") | U6 | questão N3 |
| 29 | UF-PE | anúncios em C, D, F (0-0 a 4-4) | U6 | questão N2 |
| 30 | UF-ES | máximo de torcedores do Palmeiras | U6 | questão N3 |
| 31 | UF-PE | exatamente duas / as três / nenhuma | U6 | questão N2 |
| 33 | U.F. Uberlândia-MG | piscinas por período | U6 | questão N2 |
| 34 | UF-PE | Matemática, Física, Química | U6 | questão N2 |
| 35 | Unicamp-SP | eleição no clube + probabilidade | U6 | questão N3 integradora (probabilidade) |
| 36 | FGV-SP | marcas X, Y, Z (ver M8) | U6 | questão N2 |
| 37 | UF-MG | "pelo menos" (mínimo da interseção tripla) | U6 | questão N3 |
| 38 | UF-PI | A ∩ B = ∅ ⇒ ?; De Morgan com ∈ | U3 | questão N2 |
| 39 | ITA-SP | (A − B) ∪ (B − A) = A com A, B ≠ ∅ | U4 | questão N3 |
| 40 | ITA-SP | subconjuntos de A disjuntos de B com ≤ 6 elementos | U4 | questão N3 (resolve-se sem binomial: 2⁸ − 8 − 1) |
| 42 | ITA-SP | três igualdades com complementar | U4 | questão N2 |
| 43 | ITA-SP | n(𝒫(A ∩ B)) a partir de diferenças | U4 | questão N2 |
| 44 | ITA-SP | negação de x ∈ A ∩ B, distributiva, A △ B | U4 | questão N2 |
| 46 | ITA-SP | n({C : C ⊂ B − A}) = 128 | U4 | questão N2 |
| 47 | ITA-SP | quatro conjuntos ⊂ ℕ, expressão com ∪, ∩, − | U4 | questão N3 |
| 45 | ITA-SP | maior cadeia em 𝒫(U) | U2 | questão N3 |

Contagem por unidade (itens do FME que viram questão): U1 4 · U2 7 · U3 14 · U4 16 · U5 21 · U6 21 — total 83
(42 exercícios não resolvidos + 41 vestibulares; os 9 resolvidos viram exemplos).
**U5 e U6 passam muito das metas** (≈ 12 questões) por causa do banco de vestibular — ver §8, D2.

## 3. Divisão em unidades
| U | título | pergunta aberta (prefácio) | itens do FME | exercícios FME | vestibulares FME | pré-requisitos |
|---|---|---|---|---|---|---|
| 1 | Conjunto, elemento e descrição | Como descrever um conjunto de modo que ninguém possa discordar sobre quem está dentro e quem está fora? | 19–24 | 11–16 | — | Cap. I (sentença aberta, quantificadores) |
| 2 | Igualdade, inclusão e conjunto das partes | Quando dois conjuntos são o mesmo — e qual a diferença entre *ser elemento* e *ser parte*? | 25–31 | 17–22, 35, 47 | 45 | U1; Cap. I (condicional, bicondicional) |
| 3 | Reunião e interseção | Como o "ou" e o "e" da lógica viram operações entre conjuntos? | 32–37 | 23–34, 36, 37, 46, 61 | 38 | U1, U2; Cap. I (∧, ∨, propriedades) |
| 4 | Diferença e complementar | Como descrever o que fica de fora — e por que "fora" sempre depende de onde estamos? | 38–40 (+ complementar em U, lacuna M14) | 38–45, 53, 55, 60 | 39, 40, 42, 43, 44, 46, 47 | U3; Cap. I (negação, De Morgan) |
| 5 | Contando elementos: dois conjuntos | Como contar quem está em pelo menos um de dois grupos sem contar ninguém duas vezes? | (lacuna M14: ex. 48) | 48, 49, 51, 52, 58, 59 | 7–18, 21, 32, 41 | U3, U4 (U2 para 𝒫) |
| 6 | Três conjuntos e as regiões do diagrama | Com três grupos, como organizar a contagem para não se perder nas sobreposições? | (lacuna M14: ex. 50) | 50, 54, 56, 57 | 19, 20, 22–31, 33–37 | U5 |

Por que seis e não cinco: a teoria do FME cabe em quatro unidades (U1–U4), mas o banco de vestibular é quase
todo de contagem (32 de 41 questões); U5 (dois conjuntos: fórmula e tabela 2×2) e U6 (três conjuntos:
oito regiões, "exatamente/pelo menos", máximos e mínimos) têm perguntas diferentes e o tamanho do banco pede
a divisão. Mapa de pré-requisitos (para a abertura):

```
Cap. I ─┐
        U1 → U2 → U3 → U4 → U5 → U6
                └──────────────↗ (𝒫(A) e 2ⁿ, usados em U5)
```

## 4. IDs por unidade (rascunho — a versão oficial fica em `matriz.yaml`)
### U1 — Conjunto, elemento e descrição
- H1: noções primitivas e pertinência — um conjunto fica determinado por quem pertence (∈, ∉); um conjunto pode ser elemento de outro
- H2: as duas descrições — enumeração (finita; reticências com lei visível) e propriedade {x | P(x)}; passar de uma a outra
- H3: o universo — {x ∈ U | P(x)}; a resposta depende de U (mediatriz em reta/plano/espaço; equação em ℤ ou ℝ); por que a propriedade sozinha não basta
- H4: vazio e unitário — propriedade logicamente falsa dá ∅; ∅ ≠ {0} ≠ {∅}
- U1: traduzir descrição verbal ↔ notação (listar elementos; achar propriedade característica)
- U2: conjunto-solução de equação/inequação como {x ∈ U | P(x)} — fixar U antes de resolver
- U3: classificar um conjunto (vazio, unitário, finito, infinito) a partir da descrição
- E1: esquecer o universo — resolver em ℝ quando era ℤ (ou o contrário) — raciocínio: "a equação é a mesma"
- E2: reticências sem lei clara ({2, 4, …} pode ser pares ou potências de 2) — raciocínio: "o padrão é óbvio"
- E3: confundir vazio com {0} ou {∅}; achar {x | 0·x = 0} vazio — raciocínio: "tem um zero, então é nada"
- E4: aceitar descrição sem critério de pertinência ("os números grandes") — raciocínio: "todo mundo entende"
- O1: paradoxo do barbeiro (versão popular do de Russell) — se o de Russell não estiver em H3
- O2: compreensão de conjuntos em programação ({x for x in U if P(x)}: o universo é obrigatório)

### U2 — Igualdade, inclusão e conjunto das partes
- H1: igualdade pela pertinência — ordem e repetição não importam; A ≠ B quando há testemunha
- H2: inclusão como implicação (x ∈ A ⇒ x ∈ B); ⊂ do FME admite igualdade; ∅ ⊂ A por vacuidade (Cap. I); ⊃, ⊄
- H3: igualdade por dupla inclusão — o método de prova
- H4: conjunto das partes e n(𝒫(A)) = 2ⁿ (cada elemento: entra ou não entra) — lacuna M14
- U1: decidir ∈ ou ⊂ em sentenças V/F (chaves aninhadas)
- U2: provar inclusão ou igualdade pelo elemento genérico
- U3: contar subconjuntos com restrição ({1, 2} ⊂ X ⊂ {1, 2, 3, 4}; 𝒫 de 𝒫)
- E1: trocar ∈ por ⊂ ({a} ∈ {a, b}) — raciocínio: "{a} está em {a, b}"
- E2: inverter ∅: "∅ ∈ A sempre" / "∅ ⊂ A só se A tiver ∅" — raciocínio: "o vazio está em todo lugar"
- E3: negar A ⊂ B como B ⊂ A (⊄ não é ⊃) — raciocínio: "se não está contido, contém"
- E4: provar igualdade com uma inclusão só, ou com exemplos — raciocínio: "verifiquei e deu"
- E5: contar 𝒫(A) esquecendo ∅ ou o próprio A — raciocínio: "parte é pedaço menor"
- O1: notação ⊆ / ⊊ em outros livros (o ⊂ do FME admite igualdade)
- O2: Galileu e a parte "tão grande quanto o todo" (subconjunto próprio infinito) — pista da Leitura
- O3: urelementos: no FME, *a* não é conjunto ("a ⊂ E" é F); na teoria usual, tudo é conjunto (M11)

### U3 — Reunião e interseção
- H1: reunião como "ou" inclusivo e interseção como "e" — das definições por pertinência aos conectivos do Cap. I
- H2: propriedades herdadas da lógica (idempotente, comutativa, associativa, elemento neutro ∅ e U)
- H3: absorção e distributivas (pela lógica e pelas regiões)
- H4: disjuntos; diagrama de dois conjuntos com 4 regiões
- U1: calcular ∪ e ∩ de conjuntos dados (listas, figuras, intervalos, classes de quadriláteros)
- U2: "ou"/"e" numa condição → reunião/interseção de conjuntos-solução
- U3: descobrir um conjunto desconhecido por condições de ∪ e ∩ (elemento a elemento)
- U4: V/F de propriedades para conjuntos quaisquer — provar ou dar contraexemplo
- E1: tratar ∪ como soma (repetir elementos; "contar A ∩ B duas vezes") — ponte para U5
- E2: A ∩ B = ∅ ⇒ A = ∅ ou B = ∅ — raciocínio: "como no produto de números"
- E3: distribuir pela metade: A ∪ (B ∩ C) = (A ∪ B) ∩ C — raciocínio: "como a·(b + c)"
- E4: ler "ou" como exclusivo (tirar A ∩ B da reunião) — raciocínio: "ou um ou outro"
- O1: dualidade (trocar ∪ ↔ ∩ e ∅ ↔ U leva propriedade verdadeira em propriedade verdadeira)
- O2: reunião e interseção de infinitos conjuntos (discos, retas — geometria)

### U4 — Diferença e complementar
- H1: diferença A − B (x ∈ A e x ∉ B); não comutativa
- H2: complementar de B em A (só se B ⊂ A) e complementar em U — Ā, A^C, A′, ∁A (lacuna M14)
- H3: leis de De Morgan como a negação do "e"/"ou" do Cap. I; A − B = A ∩ B̄
- U1: traduzir "exceto", "não", "fora de" em diferença/complementar
- U2: simplificar expressões com complementar (De Morgan, A − B̄ = A ∩ B)
- U3: sombrear no diagrama expressões com − e complementar
- U4: reconstruir conjuntos a partir de diferenças e complementares (elemento a elemento)
- E1: comutar a diferença (A − B = B − A) — raciocínio: "é a mesma 'distância'"
- E2: De Morgan errado: (A ∩ B)ᶜ = Aᶜ ∩ Bᶜ — raciocínio: "o complementar distribui"
- E3: complementar sem universo (ou ∁_A B com B ⊄ A) — raciocínio: "o de fora é óbvio"
- E4: A − (B ∪ C) = (A − B) ∪ (A − C) — raciocínio: "a diferença distribui como a interseção… ou como a reunião?"
- O1: notações do complementar e diferença (A \ B; Bᶜ; ∁)
- O2: complemento em computação (NOT, máscaras de bits) — candidato; só se ajudar

### U5 — Contando elementos: dois conjuntos
- H1: n(A ∪ B) = n(A) + n(B) − n(A ∩ B) por contagem dupla (lacuna M14; ex. 48)
- H2: contar por regiões disjuntas: só A, só B, ambos, nenhum; total = soma das quatro (tabela 2×2)
- H3: o complemento na contagem: nenhum = total − n(A ∪ B); porcentagem como contagem sobre 100
- U1: pesquisa com dois atributos (sim/não) → quatro regiões
- U2: identificar o dado que falta (total, interseção, "nenhum") e isolá-lo na fórmula
- U3: subgrupos com bases diferentes (porcentagem dos homens × das mulheres) → tabela de dupla entrada
- E1: somar n(A) + n(B) sem descontar a interseção
- E2: tomar "estudam inglês" por "só inglês"
- E3: esquecer quem não está em nenhum (ou supor que todos estão em algum)
- E4: somar porcentagens de bases diferentes (20% dos homens + 15% das mulheres ≠ 35%)
- O1: contar por correspondência (Cantor, Galileu) — pista da Leitura
- O2: inclusão–exclusão para n conjuntos (conexão futura)

### U6 — Três conjuntos e as regiões do diagrama
- H1: três conjuntos, oito regiões (Venn) — o diagrama como tabela de todas as combinações
- H2: preencher de dentro para fora (três → só dois → só um → nenhum)
- H3: n(A ∪ B ∪ C) e as contagens "exatamente k" e "pelo menos k" (soma das n = 1·e₁ + 2·e₂ + 3·e₃)
- U1: pesquisa com três atributos e dados das interseções
- U2: dados indiretos ("não optaram por", "exatamente dois") → equações nas regiões
- U3: máximo e mínimo (o que os dados obrigam: "pelo menos 35%")
- U4: regiões com elementos em vez de números (achar A, B, C pelas condições)
- E1: tomar "A e B" por "só A e B" (ou o contrário) — M9
- E2: esquecer de somar de volta n(A ∩ B ∩ C) na fórmula
- E3: preencher de fora para dentro (subtrair os pares do total de cada conjunto sem descontar os três)
- E4: confundir "exatamente dois" com "pelo menos dois"
- O1: círculos de Euler × diagrama de Venn (Euler mostra só as relações que existem)
- O2: Venn para quatro ou mais conjuntos (com círculos não dá)

## 5. Metas por unidade
Ponto de partida do piloto (N1 4 · N2 5–6 · N3 2 · 1 integradora; 5–6 exemplos, ≥ 1 por nível).
As metas são **mínimos**; o número final segue o que o FME traz (§2) e a decisão D2.

| U | N1 | N2 | N3 | integradoras | exemplos (≥ 1 por nível) | itens do FME já alocados (N1/N2/N3) |
|---|---|---|---|---|---|---|
| 1 | 4 | 5 | 2 | 1 | 5–6 | 2/2/0 (+ 2 exemplos) |
| 2 | 4 | 5 | 2 | 1 | 5–6 | 3/3/1 (+ 2 exemplos) |
| 3 | 4 | 5 | 2 | 1 | 5–6 | 5/7/2 (+ 3 exemplos) |
| 4 | 4 | 5 | 2 | 1 | 5–6 | 3/9/4 (+ 2 exemplos) |
| 5 | 4 | 6 | 2 | 1 | 6 | 9/10/2 |
| 6 | 4 | 6 | 2 | 1 | 6 | 4/11/6 |

## 6. Plano de pesquisa (o que cada dossiê precisa achar)
Filtro P5 aplicado *a priori*: só entra na pesquisa histórica o que explica uma escolha da definição ou
um erro comum. Toda data e atribuição com fonte; A5 para fontes frágeis.

### U1
- História (passa no P5): por que "conjunto" virou noção primitiva. Cantor (conjuntos de pontos, década de
  1870) como origem do tema; compreensão irrestrita em Frege → carta de Russell (1902) → separação de
  Zermelo (1908), que obriga a escrever {x ∈ U | P(x)}. Três camadas: o que Frege/Zermelo formularam ×
  leitura moderna (axioma da separação) × convenção escolar (universo explícito). Fontes: SEP "The Early
  Development of Set Theory" (Ferreirós), van Heijenoort (*From Frege to Gödel*), Zermelo 1908.
  Conferir M13 (Aristóteles × Arquimedes; Dedekind 1872 × 1888) se algo da Leitura for usado.
- Onde é usado: conjunto-solução (provas de vestibular/ENEM que pedem "o conjunto solução em ℤ/ℝ");
  compreensão de conjuntos em Python como aplicação real com procedência (documentação oficial).
- Erros: universo esquecido (ex. 15), reticências ambíguas; ∅ × {0}. Fontes didáticas se houver.
- Problemas: autorais para N1 e erros; histórico: o barbeiro/Russell como N3 de transferência? (cuidar para
  não antecipar na observação).

### U2
- História (passa no P5): Peano (1889) separa "é elemento de" (ε, de *est*) de "está contido"; Frege
  insiste na diferença entre subsunção (∈) e subordinação (⊂) — explica o erro E1. Fonte: Cajori,
  *A History of Mathematical Notations*; Peano, *Arithmetices principia* (1889). O símbolo ∅ (Weil, Bourbaki)
  **não passa** no P5 → no máximo observação, sem pesquisa extra.
- Onde é usado: sentenças V/F com ∈/⊂ (vestibulares); contagem de subconjuntos (combinações de opcionais,
  "monte seu pedido") como aplicação de 2ⁿ.
- Erros: ∈ × ⊂, ∅; negação da inclusão (liga ao Cap. I, negação do condicional).
- Problemas: ITA 45 (cadeias) como N3; autorais para 2ⁿ.

### U3
- História (passa no P5): Boole (1847, 1854) — classes, xy para a parte comum e x + y só para classes sem
  parte comum; Jevons (1864) torna a soma inclusiva. Explica por que ∪ não é soma (E1, ponte para U5).
  **Atenção (lição do piloto):** não pôr a leitura moderna na boca de Boole; citar a passagem primária
  (*Laws of Thought*, cap. II–IV, Gutenberg). Venn só se a U6 não usar.
- Onde é usado: buscas booleanas (AND/OR), filtros de planilha; conjunto-solução de sistemas (∩) e de
  "ou" (∪). Enunciados reais: vestibulares do FME (38), ENEM se houver.
- Erros: E2 (A ∩ B = ∅), E3 (distributiva pela metade).
- Problemas: ex. 26/27 (geometria), 31 (quadriláteros), 34 (elemento a elemento).

### U4
- História (passa no P5): De Morgan (1846–1847) e o "universo" de uma proposição — o complementar só faz
  sentido relativo a um universo (explica E3); as leis que levam seu nome, na forma de nomes contrários.
  Três camadas. Fontes: De Morgan, *Formal Logic* (1847) e "On the Syllogism I" (1846); MacTutor (A5).
- Onde é usado: "exceto"/"não" em filtros e buscas; contar pelo complemento (prepara U5).
- Erros: E1–E4; documentar com contraexemplos autorais.
- Problemas: ITA 39, 40, 42–44, 46, 47; ex. 60 (diferença simétrica) como N3.

### U5
- História: **filtro P5 provavelmente reprova** a história da inclusão–exclusão (de Moivre, Sylvester): não
  explica nada que a contagem dupla não explique. De onde vem? será reconstrução (a pesquisa com dois
  grupos). Galileu/Cantor (contar por correspondência) só como O1, com fonte primária (Galileu, *Duas novas
  ciências*, 1638) — conferir se vale o custo.
- Onde é usado: pesquisas de opinião e censos com perguntas de "sim/não"; questões de raciocínio lógico de
  concurso (adaptadas, sem afirmação de frequência). Vestibulares do FME (15 questões).
- Erros: E1–E4 (E4 a partir de vest. 8, 18 e ex. 59).
- Problemas: banco do FME (D2); autorais para N1 e erros.

### U6
- História (passa no P5): Venn (1880, "On the diagrammatic and mechanical representation…") desenha os três
  círculos com **todas** as oito regiões, possíveis ou não; os círculos de Euler (*Lettres à une princesse
  d'Allemagne*, 1768) mostram só as relações existentes. Explica por que se desenham as oito regiões e se
  preenche de dentro para fora. Três camadas: Venn (regiões como classes possíveis, sombra para vazias) ×
  leitura moderna (regiões com contagens) × convenção escolar. **Lição do piloto:** a fonte precisa dizer o
  que o texto afirma (o caso "Venn e os círculos eulerianos").
- Onde é usado: pesquisas com três perguntas; problemas de "pelo menos" (mínimos garantidos).
- Erros: E1 (M9: leitura inclusiva × exclusiva), E2–E4.
- Problemas: banco do FME (D2); autorais para N1 e erros.

## 7. Gabarito do FME conferido
Script: `verif/fme.py` (força bruta em subconjuntos de universos pequenos, enumeração por elemento,
sistemas nas regiões, frações exatas). Resultado: **98 conferências, 0 falhas de programa, 5 divergências
com o livro**.

| item | resultado |
|---|---|
| ex. 13e | gabarito omite Brasília (DF, Centro-Oeste) — redação; adaptar para "estados" (M2) |
| ex. 14B, 14C | descrições do gabarito excluem/incluem 0 indevidamente — redação (M3) |
| ex. 42f | gabarito pinta B̄; o certo é A − B (só a "lua" de A fora de B) (M7) |
| vest. 36 | gabarito d (42%); o certo é e (48%) (M8) |
| vest. 20 | gabarito c (58) confere na leitura inclusiva; a exclusiva daria d (62) (M9) |
| demais | conferem (exercícios 11–61; vestibulares 7–47) |

## 8. Para o usuário decidir
- **D1 — divisão em seis unidades** (§3), com a contagem separada em dois conjuntos (U5) e três (U6).
- **D2 — o excesso do banco de vestibular em U5 e U6** (21 e 21 itens do FME, contra metas de ≈ 12):
  - (a) tudo nas Questões, na ordem por nível e grau de guia — seção longa;
  - (b) **recomendado:** Questões com as metas (escolhidas pela função, cobrindo todos os U/E) e um bloco
    **"Mais questões de vestibular"** no fim da seção, ordenado por nível, sem meta, com respostas — nada do
    FME fica de fora e a sequência principal continua curta. É decisão local do capítulo (ESTADO), não
    muda a didática;
  - (c) deixar parte de fora (contraria "nada do FME pode faltar").
- **D3 — lacunas do FME (M14)** entram como construção: complementar em relação a U (U4-H2), n(A ∪ B)
  (U5-H1), n(A ∪ B ∪ C) (U6-H3), n(𝒫(A)) = 2ⁿ (U2-H4). Diferença simétrica só como questão N3 (U4), com a
  definição no enunciado. Recomendo assim.
- **D4 — divergências** (§7): o material usa a resposta correta; nas questões "via FME" com problema de
  redação (13e, 14, 42b), a versão adaptada vai com etiqueta "[adaptado do FME, exercício n]".
- **D5 — vestibulares sem ano**: "[BANCA via FME, ano não informado]", sem caçar o ano (custo alto, pouco
  ganho), salvo quando a função da questão for mostrar a aplicação real.
