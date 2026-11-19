#!/usr/bin/env python3
"""Matriz de cobertura: confere a matriz.yaml e, com --tex, o LaTeX contra ela.

Uso:
  python3 kit/scripts/matriz.py capitulos/<cap>/matriz.yaml [--tex capitulos/<cap>/tex] [--unidades 1,2]

Regras (didática v3 §6):
  R1  todo ID H/U/E da unidade tem >= 1 exemplo (O é opcional)          -> FALHA
  R2  a unidade tem exemplo N1, N2 e N3                                    -> FALHA
  R3  todo U e E tem >= 1 questão                                          -> PENDÊNCIA
  R4  nº de questões por nível >= meta                                     -> PENDÊNCIA
  R5  nenhum item cita ID inexistente                                      -> FALHA
  R6  nº de integradoras >= meta                                           -> PENDÊNCIA
Com --tex:
  T1  cada item da matriz existe no LaTeX com os mesmos IDs e o mesmo nível
      (casados por `rotulo`; sem rótulo, exemplos por `id` e questões pelo conjunto de IDs)
  T2  todo ID da unidade aparece em algum lugar do LaTeX
  T3  item no LaTeX que não está na matriz
Saída: código 1 se houver FALHA.
"""
import sys, os, yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import texparse as tp


def pref(n, ids):
    return {i if "-" in str(i) else f"{n}-{i}" for i in ids}


def main(path, texdir=None, unid=None):
    m = yaml.safe_load(open(path, encoding="utf-8"))
    falhas, pend = [], []
    cap = tp.capitulo(texdir) if texdir else {}
    for u in (m.get("unidades") or []):
        n = u["n"]
        if unid and n not in unid:
            continue
        ids = set(u["ids"])
        ex = u.get("exemplos") or []
        q = u.get("questoes_pool") or []
        for item in ex + q:
            for i in item.get("cobre", []):
                if i not in ids:
                    falhas.append(f"R5 U{n}: {item.get('rotulo') or item.get('id') or item.get('ref')} cita ID inexistente {i}")
        cob_ex = {i for e in ex for i in e.get("cobre", [])}
        for i in sorted(i for i in ids - cob_ex if i[0] in "HUE"):
            falhas.append(f"R1 U{n}: {n}-{i} sem exemplo")
        for lv in (1, 2, 3):
            if lv not in {e["nivel"] for e in ex}:
                falhas.append(f"R2 U{n}: sem exemplo N{lv}")
        cob_q = {i for x in q for i in x.get("cobre", [])}
        for i in sorted(i for i in ids if i[0] in "UE" and i not in cob_q):
            pend.append(f"R3 U{n}: {n}-{i} ainda sem questão")
        meta = u.get("questoes_meta") or {}
        for lv in (1, 2, 3):
            tem = sum(1 for x in q if x["nivel"] == lv)
            if tem < meta.get(f"N{lv}", 0):
                pend.append(f"R4 U{n}: N{lv} {tem}/{meta[f'N{lv}']}")
        integ = sum(1 for x in q if x.get("integradora"))
        if integ < meta.get("integradoras", 0):
            pend.append(f"R6 U{n}: integradoras {integ}/{meta['integradoras']}")
        print(f"Unidade {n} — {u['titulo']}: {len(ids)} IDs · exemplos N1–N3 = "
              f"{[sum(1 for e in ex if e['nivel'] == k) for k in (1, 2, 3)]} · questões N1–N3 = "
              f"{[sum(1 for x in q if x['nivel'] == k) for k in (1, 2, 3)]} "
              f"(meta {[meta.get(f'N{k}', 0) for k in (1, 2, 3)]}) · integradoras {integ}")

        if not texdir:
            continue
        if n not in cap:
            falhas.append(f"T1 U{n}: unidade sem arquivos uN_*.tex em {texdir}")
            continue
        itens = cap[n]["itens"]
        tex_ex = [i for i in itens if i["tipo"] == "exemplo"]
        tex_q = [i for i in itens if i["tipo"] == "questao"]
        usados = set()
        for kind, lista_m, lista_t in (("exemplo", ex, tex_ex), ("questão", q, tex_q)):
            por_rot = {i["rotulo"]: i for i in lista_t if i["rotulo"]}
            restantes = list(lista_t)
            for item in lista_m:
                alvo = None
                if item.get("rotulo"):
                    alvo = por_rot.get(item["rotulo"])
                    if alvo is None:
                        falhas.append(f"T1 U{n}: {kind} {item['rotulo']} da matriz não existe no LaTeX")
                        continue
                elif kind == "exemplo" and item.get("id") is not None:
                    alvo = next((i for i in lista_t if i["n"] == str(item["id"])), None)
                    if alvo is None:
                        falhas.append(f"T1 U{n}: exemplo {item['id']} da matriz não existe no LaTeX")
                        continue
                else:
                    esperado = pref(n, item.get("cobre", []))
                    alvo = next((i for i in restantes if set(i["ids"]) == esperado and id(i) not in usados), None)
                    if alvo is None:
                        falhas.append(f"T1 U{n}: {kind} '{item.get('ref', '?')}' sem correspondente no LaTeX (IDs {sorted(esperado)})")
                        continue
                usados.add(id(alvo))
                esperado = pref(n, item.get("cobre", []))
                nome = item.get("rotulo") or item.get("id") or item.get("ref")
                if set(alvo["ids"]) != esperado:
                    falhas.append(f"T1 U{n}: {kind} {nome}: LaTeX declara {sorted(alvo['ids'])} ≠ matriz {sorted(esperado)}")
                if alvo["nivel"] != item["nivel"]:
                    falhas.append(f"T1 U{n}: {kind} {nome}: nível N{alvo['nivel']} no LaTeX ≠ N{item['nivel']} na matriz")
            for i in lista_t:
                if id(i) not in usados:
                    falhas.append(f"T3 U{n}: {kind} {i['rotulo'] or i['n']} está no LaTeX e não na matriz")
        vistos = set(tp.outros_ids(cap[n]["texto"]))
        for i in itens:
            vistos |= set(i["ids"])
        for i in sorted(pref(n, ids) - vistos):
            falhas.append(f"T2 U{n}: {i} não aparece no LaTeX")

    print("\nFALHAS:" if falhas else "\nFALHAS: nenhuma")
    for f in falhas:
        print("  -", f)
    print("\nPENDÊNCIAS:" if pend else "\nPENDÊNCIAS: nenhuma")
    for p in pend:
        print("  -", p)
    return 1 if falhas else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    tex = a[a.index("--tex") + 1] if "--tex" in a else None
    uni = {int(x) for x in a[a.index("--unidades") + 1].split(",")} if "--unidades" in a else None
    sys.exit(main(a[0], tex, uni))
