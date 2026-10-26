#!/usr/bin/env python3
"""Audita referencias numeradas que Obsidian renderiza como checkbox.

Obsidian interpreta cualquier item de lista que empiece con ``[token]`` como
task list, por lo que una referencia APA escrita como ``- [1] Autor...`` se
pinta como un checkbox marcado en vez de como una referencia.

Este script encuentra esos casos en todo el vault, los clasifica y opcionalmente
los corrige (``--fix``) convirtiéndolos en ``- **[1]** Autor...``.

Uso:
    py qa_refs_checkbox.py [RAIZ_VAULT] [-o REPORTE] [--scope SUBCARPETA] [--fix]
"""

import argparse
import re
import sys
from pathlib import Path

LISTA = re.compile(r"^(?P<prefijo>\s*(?:>\s*)*)(?P<marcador>[-*+]\s+)\[(?P<token>[^\]]{0,6})\](?P<resto>\s+.*)?$")
EXCLUIDOS = {".git", "node_modules", "__pycache__", ".obsidian", ".trash"}


def es_excluido(parte: Path) -> bool:
    return any(p.lower() in EXCLUIDOS or p.startswith("_BACKUP") for p in parte.parts)


def clasificar(token: str) -> str:
    if token.isdigit():
        return "referencia"
    if token.strip() == "":
        return "checkbox_pendiente"
    if token in ("x", "X"):
        return "checkbox_marcado"
    if token.startswith("!"):
        return "callout_en_lista"
    return "simbolo"


def auditar(raiz: Path, scope: str | None):
    hallazgos = []
    base = raiz / scope if scope else raiz
    for archivo in sorted(base.rglob("*.md")):
        rel = archivo.relative_to(raiz)
        if es_excluido(rel):
            continue
        try:
            texto = archivo.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for num, linea in enumerate(texto.splitlines(), start=1):
            m = LISTA.match(linea)
            if not m:
                continue
            token = m.group("token")
            tipo = clasificar(token)
            if tipo == "checkbox_pendiente" or tipo == "checkbox_marcado":
                continue
            hallazgos.append(
                {
                    "archivo": str(rel).replace("\\", "/"),
                    "linea": num,
                    "token": token,
                    "tipo": tipo,
                    "texto": linea.strip(),
                    "prefijo": m.group("prefijo"),
                    "marcador": m.group("marcador"),
                    "resto": m.group("resto") or "",
                }
            )
    return hallazgos


def leer_texto(path: Path) -> tuple[str, bool]:
    crudo = path.read_bytes().decode("utf-8")
    return crudo.replace("\r\n", "\n"), "\r\n" in crudo


def escribir_texto(path: Path, texto: str, crlf: bool) -> None:
    eol = "\r\n" if crlf else "\n"
    path.write_bytes((eol.join(texto.split("\n"))).encode("utf-8"))


def corregir(raiz: Path, refs, simbolos) -> int:
    por_archivo = {}
    for h in refs + simbolos:
        por_archivo.setdefault(h["archivo"], []).append(h)
    aplicados = 0
    for rel, items in por_archivo.items():
        destino = raiz / rel
        original, crlf = leer_texto(destino)
        lineas = original.split("\n")
        for h in items:
            i = h["linea"] - 1
            actual = lineas[i]
            if h["tipo"] == "referencia":
                token = f"**[{h['token']}]**"
            else:
                token = f"\\[{h['token']}\\]"
            nuevo = f"{h['prefijo']}{h['marcador']}{token}{h['resto']}"
            if nuevo != actual:
                lineas[i] = nuevo
                aplicados += 1
        escribir_texto(destino, "\n".join(lineas), crlf)
    return aplicados


def main() -> int:
    raiz_default = Path(__file__).resolve().parents[3]
    ap = argparse.ArgumentParser(description="Audita referencias [n] interpretadas como checkbox por Obsidian.")
    ap.add_argument("raiz", nargs="?", default=str(raiz_default), help="Raiz del vault")
    ap.add_argument("-o", "--out", default=None, help="Archivo de reporte UTF-8")
    ap.add_argument("--scope", default=None, help="Auditar solo una subcarpeta")
    ap.add_argument("--fix", action="store_true", help="Corregir referencias numeradas a ** [n] **")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    if not raiz.exists():
        print(f"No existe la raiz: {raiz}", file=sys.stderr)
        return 2

    hallazgos = auditar(raiz, args.scope)
    refs = [h for h in hallazgos if h["tipo"] == "referencia"]
    simbolos = [h for h in hallazgos if h["tipo"] == "simbolo"]
    callouts = [h for h in hallazgos if h["tipo"] == "callout_en_lista"]

    lineas = []
    lineas.append(f"raiz={raiz}")
    lineas.append(f"referencias_como_checkbox={len(refs)}")
    lineas.append(f"simbolos_como_checkbox={len(simbolos)}")
    lineas.append(f"callouts_en_lista={len(callouts)}")
    lineas.append("")
    lineas.append("=== REFERENCIAS NUMERICAS (se renderizan como checkbox) ===")
    for h in refs:
        lineas.append(f"{h['archivo']}:{h['linea']}  [{h['token']}]  {h['texto']}")
    lineas.append("")
    lineas.append("=== SIMBOLOS EN LISTA (tambien se renderizan como checkbox) ===")
    for h in simbolos:
        lineas.append(f"{h['archivo']}:{h['linea']}  [{h['token']}]  {h['texto']}")
    lineas.append("")
    lineas.append("=== CALLOUTS DENTRO DE LISTA (no se corrigen automaticamente) ===")
    for h in callouts:
        lineas.append(f"{h['archivo']}:{h['linea']}  [{h['token']}]  {h['texto']}")

    por_archivo = {}
    for h in refs + simbolos:
        por_archivo.setdefault(h["archivo"], []).append(h)
    lineas.append("")
    lineas.append("=== RESUMEN POR ARCHIVO ===")
    for rel, items in sorted(por_archivo.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lineas.append(f"{len(items):3d}  {rel}")

    reporte = "\n".join(lineas) + "\n"
    if args.out:
        Path(args.out).write_text(reporte, encoding="utf-8")
        print(f"referencias={len(refs)} simbolos={len(simbolos)} callouts={len(callouts)} reporte={args.out}")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(reporte)

    if args.fix:
        aplicados = corregir(raiz, refs, simbolos)
        print(f"corregidos={aplicados}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
