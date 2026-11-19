# Macros e ambientes do `estilo.sty` (kit)

Motor: **XeLaTeX** (o `checar.py` compila). Unicode direto no fonte (ã, ç, —, «»); símbolos lógicos em
modo matemático (`$\wedge$`, `$\vee$`, `${\nao}p$`).

## Estrutura da unidade
| Comando | Uso |
|---|---|
| `\section{Título}` | abre a unidade ("Unidade N  Título"; zera questões e exemplos) |
| `\Prefacio` `\DeOndeVem` `\OndeEUsado` `\ErrosComuns` `\Observacoes` `\Exemplos` `\Questoes` `\Respostas` | títulos das seções, nesta ordem. `\Respostas` já imprime as respostas guardadas pelas `\resp` |
| `\subsubsection{…}` | subtítulos dentro de uma seção |

## Prefácio e artigo
| Ambiente / macro | Uso |
|---|---|
| `prefacio` | corpo do prefácio (sem quadro) |
| `\gancho{texto}` | frase de abertura em destaque |
| `minimo` | caixa "O mínimo que você precisa" |
| `\begin{construcao}[título]{N-H1}` | construção amarela com ID |
| `\begin{definicao}[nome]` | definição formal |
| `\begin{paralembrar}\label{lembrar-uN}` | fecha o *De onde vem?*: 1 frase + ≤ 3 passos |
| `\begin{caso}{1 · nome}{N-U1}` … `\end{caso}` | caso do mapa do problema |
| `\mapa{o enunciado diz}{procure}{ferramenta}` | as três linhas do mapa (dentro de `caso`) |
| `\reconhecer` | rótulo "Como reconhecer." |
| `\begin{gatilhos}` linhas `sinal & ferramenta & raciocínio & N-U1 · q.~\ref{uN:nome}\\` `\end{gatilhos}` | tabela de gatilhos; separe linhas com `\\\fino` e termine a última com `\\` |
| `\begin{tabelaverdade}{ccc}` … | tabela com `\toprule`; linhas com `\\\fino` |
| `\begin{citacao}` | citação longa |
| `\src{chave}` | número da fonte (sobrescrito) → `\bibitem{chave}` em `fontes.tex` |
| `\anedota` | marca de história não verificável |

## Erros e observações
| Ambiente / macro | Uso |
|---|---|
| `\begin{erro}{título}{N-E1}` | caixa de erro |
| `\campo{O erro.}` `\campo{Por que parece plausível.}` `\campo{Onde quebra.}` `\campo{Como detectar.}` `\campo{Como corrigir.}` `\campo{Onde aparece.}` | os campos do roteiro |
| `\begin{obs}{N-O1}` | observação (selo "aprofundamento opcional" e letra menor automáticos) |

## Exemplos e questões
| Ambiente / macro | Uso |
|---|---|
| `\begin{exemplo}{}{nível}{procedência}{IDs}` + `\label{ex:uN:nome}` | exemplo; `{}` = número automático N.k; nível 1/2/3 dá a cor |
| `\plano` `\resolucao` `\comentario` | partes do exemplo |
| `\begin{questao}{nível}{procedência}{IDs}\label{uN:nome}` | questão (número automático por unidade) |
| `\begin{questao}[integradora]{…}{…}{…}` | questão integradora (selo) |
| `\resp{texto}` | resposta final da questão, escrita dentro dela; sai na seção Respostas |
| `\resposta{S}{texto}` | linha manual nas Respostas (ex.: a da síntese) |
| `\ref{rótulo}` `\qref{u2:nome}` → "questão 7" · `\exref{ex:u2:nome}` → "exemplo 2.3" | remissões (nunca número digitado) |
| `\nivel{2}` `\integradora` `\cobre{N-U1}` `\fonte{…}` | selos avulsos |

Listas de itens e alternativas: `\begin{enumerate}[label=\alph*)]` ou `[label=(\alph*)]`, dentro de
`\begin{multicols}{2}` (ou 3) quando os itens são curtos.

## Síntese
```latex
\begin{sintese}
\textbf{Ao fim desta unidade, você deveria saber:}
\begin{itemize}[leftmargin=1.4em,itemsep=1pt] \item … \end{itemize}
\smallskip\noindent\textbf{Responda com suas palavras, sem consultar.} Depois, confira com a caixa
\emph{Para lembrar} (p.~\pageref{lembrar-uN}) e com a seção indicada.
\begin{enumerate}[label=\arabic*.,leftmargin=1.4em]
  \perguntasintese{O que significa …? \ondever{construção N-H1}}
  \perguntasintese{Como … foi construído? \ondever{De onde vem?}}
  \perguntasintese{Como você reconhece …? \ondever{Onde é usado?}}
  \perguntasintese{Qual é o erro mais perigoso …? \ondever{Erros comuns}}
\end{enumerate}
\end{sintese}
```

## Capítulo
| Arquivo | Conteúdo |
|---|---|
| `main.tex` | `\renewcommand{\cabecalhocapitulo}{Cap.~II — Título}`; folha de rosto; `\input` de abertura, unidades, glossário, fontes |
| `glossario.tex` | `\begin{glossario}` `\item[Termo] significado \hfill\emph{Unid.~2}` |
| `fontes.tex` | `thebibliography`; uma `\bibitem{chave}` por fonte citada |
