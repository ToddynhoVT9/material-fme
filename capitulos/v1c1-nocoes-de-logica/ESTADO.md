# ESTADO — Cap. I · Noções de lógica

> Capítulo-piloto, concluído. Serve de **exemplo de referência** para os capítulos novos.

- volume: 1
- número: 1
- título: Noções de lógica
- criado: 2026-11-17
- didática: v3 (`kit/didatica.md`)
- material de entrada: FME vol. 1, cap. I (teoria, exercícios 1–10, 6 questões de vestibular)

## Próxima ação
Nenhuma. Capítulo concluído (`saida/v1c1-nocoes-de-logica.pdf`, 112 páginas).

## Unidades
| U | título | etapa | revisão | observação |
|---|---|---|---|---|
| 1 | Proposição e negação | pronta | R3 (revisor A) | |
| 2 | Conectivos ∧ e ∨ | pronta | R3 (revisor A) | |
| 3 | Condicional e bicondicional | pronta | R3 (revisor B) | |
| 4 | Tautologia, contradição, implicação e equivalência | pronta | R3 (revisor B) | |
| 5 | Sentenças abertas e quantificadores | pronta | R3 (revisor C) | |
| 6 | Negação de proposições | pronta | R3 (revisor C) | |
<!-- FIM UNIDADES -->

## Portões com o usuário
- [x] Escopo aprovado (2026-11-17)
- [x] Calibração da U1 (2026-11-17, decisões c1–c6)
- [x] PDF final entregue (2026-11-18, v3)

## Decisões do capítulo
| # | data | decisão | origem |
|---|---|---|---|
| A19 | 2026-11-18 | ordem do N3 da U1 mantida (Q11 bifurcação → Q12 autorreferência) | R3 |
| K1 | 2026-11-19 | migração para o formato do kit: rótulos `uN:qM` e `ex:N.M`, respostas com `\resp`; texto do PDF idêntico, página a página | extração da skill |
| K2 | 2026-11-19 | o `checar.py` achou 11 remissões de "Treino:"/gatilhos para itens N3 que o R3 deixou passar (U1, U2, U5, U6); corrigidas para apontar só para N1/N2; na U1, a linha de gatilho "frase que fala de si mesma" saiu (era a ferramenta da Q12, N3) | E-R3-1 |

## Pendências
- Fontes frágeis sob nota de acesso e primárias não localizadas: `revisoes/q7-revisao-v3.md` §6.
- Os rótulos do piloto são numéricos (`u4:q5`), herdados da numeração; em capítulos novos, use rótulos semânticos.

## Registro de sessões
| data | etapa · unidade | o que foi feito | checar.py ao sair |
|---|---|---|---|
| 2026-11-17 | q1–q7 | piloto v2 completo | — |
| 2026-11-18 | R1–R3 | refação na v3 + revisão independente | 0 erros, 0 overfull |
| 2026-11-19 | kit | migração para rótulos/\resp; correções K2 | 0 FALHAS · 11 AVISOS (IDs O e uma procedência) |
