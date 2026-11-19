# Etapa 4 — Revisão independente (por unidade)

**Entrada:** a unidade montada (etapa 3 pronta).
**Saída:** `revisoes/uN-revisor.md` (relatório do revisor) e `revisoes/uN.md` (o que foi feito com
cada achado); unidade corrigida; `ESTADO.md` com a unidade `pronta` (ou aguardando o usuário).

## Passos

1. **Revisor independente.** Preencha `kit/modelos/brief-revisor.md` ({{CAP}}, {{N}}, {{RAIZ}}) e
   lance um subagente (ferramenta Agent, tipo geral) com esse texto como tarefa. Ele lê a didática,
   a unidade, o PDF e o dossiê; **não** lê `verif/`, `revisoes/` nem o registro do ESTADO. Ele refaz
   todas as respostas e confere na web as 5 afirmações mais arriscadas. Espere o relatório.
   - Sem ferramenta de subagente: faça uma revisão "a frio" — releia só a didática, o PDF e o tex;
     refaça as respostas num script novo, sem abrir `verif/uN.py`; e registre que a revisão não foi
     independente.

2. **Triagem.** Para cada achado: *aplicado* · *decidido (manter), com motivo* · *pendente para o
   usuário*. Achado sem evidência não se aplica por obediência: confira antes.
   Registre em `revisoes/uN.md` (tabela: # · status · o que foi feito).

3. **Corrija** e rode de novo `verif/uN.py`, `checar.py --unidades N` e `paginas.py --unidade N`.
   Renumeração é só mover blocos (rótulos); atualize a ordem na `matriz.yaml`.

4. **Padrões.** Se um achado é um tipo de defeito que tende a se repetir, anote-o no `ESTADO.md`
   (Decisões do capítulo) e confira as outras unidades já prontas. Se parecer geral para todo
   capítulo, proponha ao usuário uma emenda à didática ou às lições do piloto — não altere sozinho.

5. **Calibração (primeira unidade do capítulo):** envie ao usuário o PDF com a U1 (ou a primeira
   unidade pronta), com um resumo do que a revisão encontrou. **Não monte outras unidades até ele
   aprovar.** As decisões dele vão para o `ESTADO.md`; as que valem para todos os capítulos, para a
   didática (P1, com o usuário).

6. `ESTADO.md`: unidade → `pronta`; próxima ação.

## Pronto quando
todos os achados têm status · verificador, checar e folhas limpos depois das correções · na U1,
aprovação do usuário registrada.
