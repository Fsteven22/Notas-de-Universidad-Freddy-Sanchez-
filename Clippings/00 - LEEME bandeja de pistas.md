---
dg-publish: false
tags: [clippings, protocolo, colaboracion]
---

# 📥 Bandeja de Pistas (cómo colaborar)

> [!info] ℹ️ Protocolo para quien investiga
> Esta carpeta es la **bandeja de entrada**. Cualquiera con acceso puede dejar pistas; cada agente las convierte en notas formales.
>
> **Acceso necesario:** escritura en la carpeta `Clippings/` (OneSync compartido o pull request a git).

## 📝 Cómo dejar una pista

1. Crea un `.md` aquí con nombre `PISTA - <tema>.md` (ej. `PISTA - tecnicas pomodoro.md`).
2. Usa esta plantilla mínima:

```markdown
# PISTA - <tema>

- **Link:** <url>
- **Para la materia:** <ej. IDIG2012 U1>
- **Destino:** <nota exacta donde se integra>
- **Por qué sirve (1-2 líneas):** <qué aporta que no tenemos>
- **Estado:** #pendiente
```

3. Cambia el tag a `#procesado` cuando se confirme la integración.

## ⚙️ Qué hace cada agente al procesar

1. Lee la pista y el link (web o PDF).
2. Extrae solo lo evaluable y lo cita formal en la nota destino + tarjeta SR si aplica.
3. Marca `#procesado` y **borra la pista** (igual que los `.md` de capturas: referencia temporal), pero solo después de commitear la integración.

## 🔒 Reglas para trabajar en paralelo

> [!warning] ⚠️ El vault y el repo git son compartidos: varias sesiones pueden tocarlo a la vez.
> 1. **Reclamar una pista es un rename atómico**: al tomarla, renómbrala a `PISTA - <tema> [EN-PROCESO <agente>].md`. Si otro agente ve ese nombre, no la toca.
> 2. **Una nota destino = un agente responsable**: la pista declara la nota exacta (`- **Destino:**`). Nadie edita una nota que no reservó.
> 3. **Bitácora por agente**: cada agente escribe solo en `Clippings/LOG-<agente>.md` (qué procesó, qué commiteó). La tabla de estado no se edita entre agentes: el estado se deduce de los nombres de archivo.
> 4. **Borrar después del commit**: la pista se elimina cuando su integración ya está commiteada; si se cae la sesión, la pista sigue en la bandeja y otro agente puede retomarla.
> 5. **Nada de `git add -A` / `git commit -a`**: stagea solo tus paths (`git add <ruta>`), rama propia por agente y nunca toques lo que otro agente dejó sin commitear.

## 🔍 Cuándo investigar fuera del PDF (regla permanente)

> Si el PDF docente no cubre algo evaluable (ejercicio referenciado sin diagrama, caso nombrado sin datos, regla sin ejemplo), se activa este flujo: se definen los temas faltantes → se investigan (~10 links con autor/fecha) → se arman `PISTA` → se integra lo nuevo + cita + se borra la pista. Lo ya cubierto por el PDF no se duplica.

## 📊 Estado actual

El estado se lee por los nombres de archivo de esta carpeta:

| Prefijo | Significado |
|---|---|
| `PISTA - <tema>.md` | pendiente, libre para tomar |
| `PISTA - <tema> [EN-PROCESO <agente>].md` | reservada por un agente |
| `LOG-<agente>.md` | bitácora de un agente |

> [!tip] 📌 Bitácoras abierta
> `LOG-opencode.md` está activo: el agente opencode está tocando
> `Universidad/3er Semestre/**` (links rotos) y
> `Universidad/Herramientas/Mantenimiento/**`. No editar esas rutas sin
> avisar en esa bitácora.
> Revisa `LOG-<agente>.md` antes de arrancar: ahí está qué commiteó cada
> sesión y qué dejó pendiente.

---
**Tags:** #clippings #protocolo #colaboracion
