"""Entrenador de pitch personal (Comunicación S3).

Uso:
    py pitch_trainer.py guion.txt        # analiza + ensayo con cronometro por bloques
    py pitch_trainer.py --modelo         # muestra el pitch modelo y lo ensaya

Ventana objetivo: 105-120 s (1:45 a 2:00). Ritmo español neutro: ~2.2 palabras/s.
Bloques S3: Quien soy (20s) / Que hago (40s) / Prueba (30s) / Cierre (20s).
"""
import pathlib
import sys
import time

BLOQUES = [
    ("Quien soy", 20, "nombre, carrera, semestre, identidad en 1 frase"),
    ("Que hago y que se", 40, "stack, cursos, que sabes hacer hoy"),
    ("Prueba", 30, "1 logro con dato: proyecto, nota, taller, repo"),
    ("Cierre y aporte", 20, "que aportas al equipo/empresa + frase final"),
]
MIN_T, MAX_T = 105, 120
RITMO = 2.2  # palabras por segundo

MODELO = """Soy Freddy Sanchez, estudiante de tercer semestre de Ingenieria de Software en la ESPOL.
Mi identidad profesional es clara: soy el desarrollador que documenta lo que construye,
cumple las fechas que promete y explica sin rodeos lo que hizo y por que lo hizo asi.
Hoy manejo Python y Java, diseno de bases de datos relacionales desde el modelo
entidad-relacion hasta las tablas, y publico mis apuntes de cada materia en un sitio web
que mantengo yo mismo con Obsidian, Git y despliegue continuo.
Como prueba de lo que digo, mis notas de Bases de Datos incluyen mas de cuarenta diagramas
verificados uno por uno y casos completos resueltos como Tiny College, con entidades,
claves y cardinalidades justificadas. En Comunicacion, prepare este pitch con estructura
medida por bloques y ensayado con cronometro, y mantengo un sistema de repaso espaciado
con tarjetas diarias para no olvidar lo aprendido. Ademas, convierto el material de cada clase,
incluso fotos del pizarron, en documentos ordenados que mis companeros tambien pueden usar.
Si trabajo con ustedes, aporto codigo trazable, actas claras despues de cada reunion
y comunicacion directa cuando algo se atrasa, con la causa y el plan, no con excusas.
Busco un equipo donde la exigencia sea mutua: yo llego preparado a cada entrega,
y espero lo mismo de quienes trabajan conmigo. Esa es mi propuesta: constancia verificable. Gracias."""


def analizar(texto):
    palabras = len(texto.split())
    estimado = palabras / RITMO
    print(f"Palabras: {palabras} | Tiempo estimado: {estimado:.0f}s", end=" ")
    if estimado < MIN_T - 5:
        print(f"(CORTO: faltan ~{int((MIN_T - estimado) * RITMO)} palabras)")
    elif estimado > MAX_T + 5:
        print(f"(LARGO: sobran ~{int((estimado - MAX_T) * RITMO)} palabras)")
    else:
        print("(EN RANGO 1:45-2:00, ±5s de tolerancia)")
    return palabras


def ensayar():
    print("\nEnsayo: pulsa Enter al EMPEZAR y al TERMINAR cada bloque.\n")
    total = 0.0
    reporte = []
    for nombre, objetivo, pista in BLOQUES:
        input(f"[{nombre} | objetivo {objetivo}s | {pista}] EMPEZAR...")
        ini = time.perf_counter()
        input(f"[{nombre}] TERMINAR...")
        dt = time.perf_counter() - ini
        total += dt
        marca = "OK" if abs(dt - objetivo) <= 7 else ("CORTO" if dt < objetivo else "LARGO")
        reporte.append((nombre, objetivo, dt, marca))
        print(f"  -> {dt:.0f}s vs {objetivo}s: {marca}\n")
    print(f"TOTAL: {total:.0f}s", end=" ")
    if total < MIN_T - 5:
        print("(CORTO: agrega prueba o detalle)")
    elif total > MAX_T + 5:
        print("(LARGO: recorta adjetivos y repeticiones)")
    else:
        print("(EN RANGO: listo para presentar)")
    print("\nDetalle por bloque:")
    for nombre, objetivo, dt, marca in reporte:
        print(f"  {nombre}: {dt:.0f}s / {objetivo}s {marca}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--modelo":
        print(MODELO)
        print()
        analizar(MODELO)
        ensayar()
    elif len(sys.argv) > 1:
        texto = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
        analizar(texto)
        ensayar()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
