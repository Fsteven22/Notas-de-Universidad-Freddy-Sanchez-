---
dg-publish: false
---

# 🧪 Catálogo de errores del vault

> [!info] Nota espejo
> Esta nota contiene **ejemplos intencionalmente rotos**: los fixers de `Mantenimiento/` la excluyen (coinciden por nombre de archivo). No la corrijas a mano.

## Test: fences con línea blanca dentro de callouts

> [!info] Cómo leer el test
> Cada variante tiene un callout con un code fence adentro. Si el callout se "rompe" (el título sale como texto plano o el bloque se sale de la caja), esa variante es la culpable. Dime cuáles A/B/C/D se ven mal.

## Variante A — línea blanca `> ` (con espacio) dentro del fence

> [!example] TEST A
> **Solución:**
> ```
> linea uno
> 
> linea tres
> ```
> Marcador A1: si lees esto dentro del callout, A está bien.

## Variante B — línea blanca `>` (sin espacio) dentro del fence

> [!example] TEST B
> **Solución:**
> ```
> linea uno
>
> linea tres
> ```
> Marcador B1: si lees esto dentro del callout, B está bien.

## Variante C — blanco del fence fuera problema: `>   ` tres espacios como separador de callout (fuera del fence)

> [!example] TEST C
> **Solución:**
> ```
> linea uno
> linea dos
> ```
>   
> Marcador C1: si lees esto dentro del callout, C está bien.

## Variante D — control: fence sin líneas blancas

> [!example] TEST D
> **Solución:**
> ```
> linea uno
> linea dos
> linea tres
> ```
> Marcador D1: si lees esto dentro del callout, D está bien.

Estos son los tipos de errores que puedes encontrarte: 

1: Callouts solapados: El primero consume a todos y los que vienen despues se colocan como texto

>[!note] Estudios de trabajo 
>Un estudio dice que ""
>[!success] El problema resuelto
>El problema tiene una solucion que dice ""

Solucion: Usar un espacio en blanco para separarlos: 

>[!note] Estudios de trabajo 
>Un estudio dice que ""

>[!success] El problema resuelto
>El problema tiene una solucion que dice ""

2: Callouts con sus > separados por espacios: rompen el callout y el contenido se dispersa

>[!note] EL flujo de trabajo: 

>El trabajo es parte de la vida cotidiana

>Y la vida cotidiana es parte del trabajo 

Solucion: Quitar los espacios o rellenarlos con > segun corresponda

>[!note] EL flujo de trabajo: 
>El trabajo es parte de la vida cotidiana
>Y la vida cotidiana es parte del trabajo 

>[!note] EL flujo de trabajo: 
>
>El trabajo es parte de la vida cotidiana
>
>Y la vida cotidiana es parte del trabajo 

3: Callouts de preguntas con success dentro: Un callout que debe estar dentro de otro 

>[!question] Ejercicios resueltos
>1 - Como funciona la electricidad? 
>[!success]- Respuesta
>La electricidad funciona de manera..

Solucion: Colocarle un > adicional desde que empieza la pregunta hasta cuando termina

>[!question] Ejercicios resueltos
>1 - Como funciona la electricidad? 
>
>>[!success]- Respuesta
>>La electricidad funciona de manera..

4: Links que no llevan a un archivo real que exista
Solucion: crear el archivo, eliminar el link o redireccionarlo con el archivo que exista

5: contenido matematico que no tiene los $

p(x) = x^2 + 2x + 2 

Solucion: colocarle los signos de dolar en ambos lados

$p(x) = x^2 + 2x + 2$

6: contenido matematico importante como formulas que no tienen los dobles $

Formula: F = m.a

Solucion: colocarle los dobles $

Formula de la fuerza:
$$F = m.a$$
7: Contenido que está fuera de callouts: Todo contenido, tabla, formula o numero que esté fuera de un callout es considerado error 

| nombre | pais    |
| ------ | ------- |
| steven | ecuador |
Solucion: Crear un callout para los elementos 

>[!notes] Informacion del creador 
>
> 
> |Nombre     | Pais    |
> | --- | --- |
> |Steven     | Ecuador   |
> 
> 

