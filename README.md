# material-fme

Repositório de trabalho da skill **material-didatico-fme**: transforma capítulos do *Fundamentos de
Matemática Elementar* (FME) em material de estudo na didática v3, em LaTeX → PDF.

```
material-fme/
├── kit/                       ferramentas da skill (não editar por capítulo)
│   ├── didatica.md            a didática em vigor (normativa)
│   ├── etapas/                1-escopo · 2-dossie · 3-montagem · 4-revisao · 5-fechamento
│   ├── referencia/            macros.md (LaTeX) · licoes-do-piloto.md
│   ├── modelos/               ESTADO, escopo, dossiê, matriz, brief do revisor, verificador, tex/
│   ├── scripts/               esqueleto.py · checar.py · matriz.py · paginas.py · texparse.py
│   └── tex/estilo.sty         estilo (copiado para cada capítulo na criação)
└── capitulos/
    └── v1c1-nocoes-de-logica/ o piloto (Cap. I, vol. 1) — exemplo de referência
```

## Como se usa
- Cada capítulo vive em `capitulos/v<vol>c<n>-<slug>/`, com um **`ESTADO.md`** que diz em que etapa
  está cada unidade e qual é a próxima ação.
- Trabalhe **uma etapa de uma unidade por sessão** (ex.: "dossiê da U3"). A sessão começa lendo o
  `ESTADO.md` e termina atualizando-o.
- Entre sessões, o repositório precisa persistir. O jeito mais simples é um repositório no GitHub:
  a sessão clona, trabalha e dá *commit/push* no fim. Também funciona uma pasta no computador
  (app desktop) ou um zip anexado a cada sessão e baixado no fim.

## Dependências
XeLaTeX (TeX Live com `tcolorbox`, `circuitikz`, `babel` + `\babelprovide{brazilian}`), Poppler
(`pdftoppm`, `pdftotext`, `pdfinfo`), Python 3 com `pyyaml` e `Pillow` (`sympy` opcional).

## Conferências rápidas
```
python3 kit/scripts/checar.py capitulos/<cap>            # compila + regras automáticas
python3 kit/scripts/matriz.py capitulos/<cap>/matriz.yaml --tex capitulos/<cap>/tex
python3 kit/scripts/paginas.py capitulos/<cap>/tex/main.pdf --unidade 2
python3 capitulos/<cap>/verif/u2.py
```
