---
name: orquestar-sonnet
description: Cómo Opus reparte trabajo en subagentes Sonnet (medium) con encargos bien acotados, los lanza con una plantilla fija, verifica lo que vuelve y redacta una respuesta única. Úsala SIEMPRE antes de llamar a `Agent` con `model: "sonnet"` y cuando haya que «repartir», «delegar», «lanzar subagentes», «paralelizar» o «dividir en tareas». Qué modelo usar: `elegir-modelo`.
---

# Orquestar subagentes Sonnet

Opus piensa, reparte y responde; Sonnet ejecuta encargos cerrados. Un subagente arranca **en
frío**: no ha visto la conversación, no sabe por qué existe su tarea ni dónde termina. Todo lo
que necesita tiene que ir en el encargo, y todo lo que devuelve tiene que poder comprobarse.
Si el encargo es vago, Sonnet rellena los huecos con suposiciones y se sale del ámbito.

Qué modelo y esfuerzo usa cada parte: skill `elegir-modelo`. Esta skill empieza cuando ya se
ha decidido delegar.

## §1. Roles

| Rol | Hace | No hace |
|---|---|---|
| **Opus (coordinador)** | Entiende la petición, parte el trabajo, escribe los encargos, verifica y redacta la respuesta final | Delegar el criterio: qué es correcto, qué se descarta y cómo se resuelve una contradicción lo decide él |
| **Sonnet (ejecutor)** | Cumple un encargo dentro de su ámbito y devuelve el informe fijo | Ampliar el alcance, arreglar «de paso» lo que ve, decidir por el usuario |

**Por defecto trabaja el agente principal; se delega solo si compensa** (trabajo grande,
paralelo e independiente), porque cada subagente arranca en frío y gasta muchos tokens. No
delegues una tarea pequeña (unas pocas llamadas) ni una que dependa de lo hablado en el chat.

## §2. Partir el trabajo

Un encargo está bien acotado si cumple los cuatro rasgos:

1. **Resultado claro y límites:** una frase con el resultado concreto, más lo que queda fuera.
2. **«Hecho» medible:** un comando y su salida esperada, un test que pasa o una lista de
   fuentes con URL. «Que funcione bien» no vale: no se puede comprobar.
3. **Pocas dependencias:** el encargo avanza sin esperar a otro encargo, a ti ni a un sistema
   externo. Si depende de otro, va en serie y recibe el resultado del anterior en su contexto.
4. **Tamaño justo:** un subagente lo acaba de una vez y su resultado se revisa de un vistazo.
   Orientación: hasta ~5 archivos en código, o una pregunta con sus subpreguntas en investigación.
   Si es más grande, se parte en dos.

**Reglas de reparto:**
- **Código en paralelo:** dos encargos nunca tocan el mismo archivo; si se solapan, van en serie.
- **Carpeta:** los encargos de solo lectura y los de archivos separados comparten la carpeta.
  Worktree solo si los archivos pueden cruzarse, o para agentes y sesiones independientes.
- **Investigación:** un encargo por pregunta. Las preguntas no se solapan; si dos encargos
  pueden acabar buscando lo mismo, se fusionan.
- **Lo que solo Opus puede hacer** (decidir el diseño, elegir entre opciones, la síntesis
  final) no se reparte.

## §3. Enseñar el reparto y esperar

Antes de lanzar nada, enseña el reparto y **para hasta que el usuario dé su visto bueno**: debe
poder corregirlo antes de que cueste tokens. **Excepción:** dentro de un plan ya aprobado
(`plan-por-fases`, después de la Fase 0) no se para: se enseña la tabla en una línea y se lanza.

```
| # | Encargo (resultado) | Ámbito | Fuera de alcance | Hecho cuando | Orden |
|---|---|---|---|---|---|
| 1 | … | archivos / pregunta | … | comando → salida / fuentes | paralelo |
| 2 | … | … | … | … | tras 1 |
```

Añade debajo una línea por cada cosa que hará Opus mismo (verificar, sintetizar, lo que no se
delega).

## §4. Plantilla del encargo

Rellena todos los campos y escribe el prompt para alguien listo que no sabe nada del proyecto.
Nada de «como hablamos» ni «lo de antes»: el subagente no lo ha visto.

```
## Contexto
<Por qué existe esta tarea, en 1-3 frases. Lo que ya se sabe (rutas, hallazgos, decisiones)
para que no lo vuelva a descubrir.>

## Resultado
<Una frase: el resultado concreto.>

## Ámbito
- Puedes tocar o consultar: <rutas exactas / la pregunta y sus subpreguntas>
- Herramientas: <las que necesita; p. ej. «solo lectura y tests» o «búsqueda web»>

## Fuera de alcance
- <Mejoras relacionadas que se dejan para luego>
- No toques archivos fuera del ámbito, no hagas commits ni instales dependencias.
- Si ves algo que conviene cambiar fuera del ámbito, anótalo en «Fuera de alcance detectado»
  y no lo arregles.

## Normas
<Las del proyecto que apliquen: idioma, convenciones, estilo.> Escribe todo en español.
No explores más allá del contexto y las rutas dadas. Si no lo encuentras, di «no encontrado»: no
lo inventes. Cambio mínimo: sin abstracciones ni código defensivo que no se pidan. Salidas
cortas: tests y logs recortados.

## Hecho cuando
- <Criterio comprobable 1: comando → salida esperada / test que pasa>
- <Criterio comprobable 2>

## Si te bloqueas
Para y devuelve «Estado: bloqueado» con lo que falta. No improvises fuera del ámbito para
desbloquearte.

## Devuelve (≤250 palabras, esta plantilla exacta)
Estado: hecho | parcial | bloqueado
Cambios / Hallazgos: <archivo — qué cambió> | <afirmación — fuente (URL, fecha)>
Pruebas del «hecho»: <comando → resultado literal, recortado>
Fuera de alcance detectado: <o «nada»>
Dudas: <o «ninguna»>
```

**«Hecho cuando» según el tipo:**

| Tipo | Criterio típico |
|---|---|
| Código | Test o comando concreto con su salida esperada; `git diff --stat` solo con archivos del ámbito; sin errores nuevos de lint o tipos |
| Investigación | N fuentes primarias (documentación oficial, paper, repo) con URL y fecha; cada afirmación lleva su fuente; lo no encontrado se dice como «no encontrado», no se rellena |

## §5. Lanzar

- `Agent` con `model: "sonnet"` y `effort: "medium"` explícito (`high` solo si un encargo se
  atasca; un subagente no hereda el esfuerzo). Varios en `high` a la vez agotan el límite de 5 h.
  `description` de 3-5 palabras.
- Los encargos paralelos van **en el mismo mensaje**; los de serie, cuando vuelve el anterior,
  con su resultado añadido al «Contexto».
- Avisa en una línea: cuántos encargos lanzaste, con qué modelo y cuáles esperan turno.

## §6. Verificar lo que vuelve

El informe del subagente es una afirmación, no una prueba. Por cada encargo:

- **Código:** ejecuta tú el comando de «hecho» y mira `git diff --stat`: ¿solo cambian archivos
  del ámbito? Lee el diff de lo que importa.
- **Investigación:** abre al menos la fuente de cada afirmación que vaya a sostener la respuesta
  final. Una afirmación sin fuente o con una fuente que no dice eso se descarta.
- **Si no cumple:** un solo reintento con la corrección concreta («el test X falla con Y;
  corrige Z sin tocar W»), por `SendMessage` al mismo subagente para que conserve su contexto.
- **Si vuelve a fallar:** lo hace Opus o se avisa al usuario (señal de atasco de
  `elegir-modelo`). No hay tercer intento a ciegas.

## §7. Respuesta final

Una sola respuesta, redactada por Opus, con dos partes:

1. **La respuesta** a lo que pidió el usuario: integrada y coherente. Si hay contradicciones
   entre encargos, se resuelven con lo verificado y se dice cómo.
2. **Informe por subagente:**

```
| # | Encargo | Estado | Verificado | Pendiente / fuera de alcance |
|---|---|---|---|---|
| 1 | … | hecho | test X pasa (lo ejecuté) | … |
```

Lo que cada subagente apuntó en «Fuera de alcance detectado» se recoge aquí; no se arregla
sin preguntar.
