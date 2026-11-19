# Lições do piloto (Cap. I, nov/2026)

O que deu errado ou custou caro no piloto, para não repetir. Fonte: as revisões q7 (v2) e R3 (v3),
107 achados no R3, nenhum erro de resposta. Os defeitos estavam na didática, na história e na forma.

## Defeitos que mais se repetiram (procure-os ativamente)
| Padrão | Exemplo do piloto | Regra |
|---|---|---|
| **N3 antecipado fora das questões** | observação já dizia que "esta frase tem cinco palavras" é verdadeira (resolvia a Q12 de autorreferência); caso 5 da U4 trazia "bebês, crocodilos", o mesmo cenário do exemplo N3 | didática §2.3, §2.5, §3; `checar.py` pega "Treino:" e gatilhos |
| **ID declarado e não treinado** | exemplos declarando observações (4-O1, 5-O1) que só citavam; 4-H3 declarado num exemplo que não fazia a tabela | §2.6; revisão (a) |
| **Leitura moderna na boca do autor antigo** | "o 'ou' de Boole era o exclusivo dos estoicos"; Eubulides com formulação moderna; "Apuleio e Boécio organizaram o quadrado" | §2.2, três camadas |
| **Frequência sem fonte** | "um dos formatos mais pedidos"; "a FATEC tem um bloco fixo de raciocínio lógico" | §8 |
| **Fonte pouco pertinente** | a página citada não dizia o que o texto afirmava (IEEE sobre Jevons; Venn e os "círculos eulerianos") | conferir a passagem, não só o tema |
| **Integradora que não precisa da unidade** | inequação do 2º grau "sem resolver nenhuma inequação" — resolvia-se sem lógica | §2.7: tente resolver sem a unidade |
| **Nível pelo tamanho, não pela função** | "verifique pela tabela" classificado N2 (é N1: a ferramenta está dada) | §3 |
| **Ordem por guia invertida** | N2 que entrega a ferramenta inteira depois de N2 abertos | §2.7 |
| **Prometido só na camada opcional** | a negação do ↔ e a notação da barra só em observações, mas usadas no exemplo 6.4 | §2.5 (E-R3-3) |
| **Ponteiro da síntese para seção inexistente** | "(→ Definição)" numa unidade sem caixa de definição | §2.8; `checar.py` |
| **Lista em linha quebrando mal** | alternativas com `\mbox` + `\hspace` | §10; `checar.py` |

## O que custou caro
- **Mudar a didática no meio** obrigou a refazer o capítulo inteiro (R1–R3). Hoje ela está estável;
  mudanças só com o usuário, e preferencialmente entre capítulos.
- **Renumerar à mão**: cada reordenação de questões exigia atualizar remissões, respostas, matriz e
  verificador; num desses passos, dois arquivos foram apagados por um erro de script. Resolvido com
  rótulos e `\resp` (o capítulo-modelo foi migrado; o texto do PDF saiu idêntico).
- **Conferir texto de prova** (vestibular, olimpíada) foi um dos maiores custos e muitas questões
  acabaram "adaptadas" mesmo assim. Use prova quando a função for mostrar a aplicação real.
- **História profunda que virou observação ou saiu.** O filtro P5 vem antes da pesquisa, não depois.
- **Revisão só no fim**: o mesmo defeito em seis unidades. Revisão por unidade e calibração na U1.
- **Contexto da sessão**: um capítulo inteiro não coube numa sessão. Uma sessão por etapa de unidade,
  com o estado no `ESTADO.md`.

## O que funcionou (manter)
- Verificador por programa para toda resposta calculável: zero erros de resposta em 225 checagens.
- Revisor independente que refaz as respostas e confere a web sem ver a produção.
- Matriz de IDs ligando texto, exemplos e questões.
- Os casos do mapa do problema e o roteiro de cinco passos dos erros.
