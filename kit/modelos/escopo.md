# Escopo — Cap. {{CAP_ROMANO}} · {{TITULO_CAPITULO}} (FME vol. {{VOLUME}})

Etapa 1 (`kit/etapas/1-escopo.md`). Sai daqui: a divisão em unidades, os IDs (que vão para `matriz.yaml`),
as metas e o plano de pesquisa de cada dossiê. **O usuário aprova este arquivo antes da etapa 2.**

## 1. Material de entrada
| páginas (livro) | conteúdo |
|---|---|
| | teoria (itens/numeração do livro) |
| | exercícios |
| | respostas dos exercícios |
| | questões de vestibular do capítulo |
| | respostas das questões de vestibular |

- Leitura **visual** das páginas (a camada de texto perde símbolos e pode conter respostas de outros capítulos).
- Problemas encontrados no material (erros de impressão, alternativas fora de ordem, questões sem ano):

| # | onde | problema | tratamento |
|---|---|---|---|

## 2. Inventário do FME — nada pode faltar
Cada item de teoria, exemplo do livro, exercício e questão de vestibular do capítulo tem uma linha.

| item do FME | conteúdo | unidade | entra como |
|---|---|---|---|
| | | | (construção / definição / exemplo / questão / observação / fora — com motivo) |

## 3. Divisão em unidades
| U | título | pergunta aberta (prefácio) | itens do FME | exercícios FME | vestibulares FME | pré-requisitos |
|---|---|---|---|---|---|---|

Critérios: uma pergunta por unidade; a unidade precisa das anteriores e não das posteriores;
tamanho comparável (P4: a função é fixa, o tamanho não). Mapa de pré-requisitos (para a abertura):

```
U1 → U2 → …
```

## 4. IDs por unidade (rascunho — a versão oficial fica em `matriz.yaml`)
### U1 — [título]
- H1: [construção de De onde vem?]
- U1: [contexto de uso / gatilho]
- E1: [erro comum, com o raciocínio que leva a ele]
- O1: [observação candidata — opcional]

## 5. Metas por unidade
| U | N1 | N2 | N3 | integradoras | exemplos (≥ 1 por nível) |
|---|---|---|---|---|---|

## 6. Plano de pesquisa (o que cada dossiê precisa achar)
### U1
- História (passa no filtro P5?): [marcos a investigar, com as três camadas previstas]
- Onde é usado: [que tipo de enunciado real procurar; provas, olimpíadas, concursos, aplicações]
- Erros: [onde o raciocínio quebra; fontes didáticas se houver]
- Problemas: [históricos? de prova? autorais para N1 e erros?]

## 7. Gabarito do FME conferido
Script: `verif/fme.py` (força bruta / sympy). Divergências com o gabarito do livro:

| item | resultado |
|---|---|

## 8. Para o usuário decidir
- 
