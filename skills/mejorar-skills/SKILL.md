---
name: mejorar-skills
description: Cómo mejorar de verdad una skill, un CLAUDE.md, un prompt o una memoria. Úsala SIEMPRE antes de cambiar cualquiera de ellos porque algo salió mal, porque el usuario te corrigió mientras usabas una skill o porque te pidió «mejora la skill», «optimiza la skill», «apúntalo en la skill» o «que no vuelva a pasar». También con «qué aprendemos de esta sesión». Para revisar todas las skills a la vez, `sanear-skills`. Encuentra la causa del error antes de escribir y, muchas veces, el arreglo es borrar o corregir algo que ya estaba en vez de añadir otra regla.
---

# Mejorar skills de verdad

Por Gonzalo López (@gonzalo_lopezg), idea de Remy Gaskell (@aiwithremy).

Cuando algo falla, lo fácil es añadir una línea a la skill. Luego falla otra cosa y otra línea. Al mes la skill es el
doble de larga, tiene reglas que se contradicen y funciona peor. Esta skill cambia eso: antes de tocar nada, buscas por
qué pasó.

> Antes de añadir, intenta borrar. Casi ningún problema viene de algo que falta: viene de algo que sobra, que está mal o
> que choca con otra cosa.

## Cuándo se usa

- **Siempre que vayas a cambiar una skill o unas instrucciones** por un error, una corrección o un «mejóralo». Te lo pida
  o no: es la forma de hacer ese cambio.
- **Cuando te pidan revisar** («qué aprendemos de esta sesión»): haces los pasos con cada cosa que falló en la sesión y
  entregas una lista numerada (ver «Cómo lo cuentas»).

## 1. Mira lo que pasó de verdad

- La corrección exacta del usuario, con sus palabras, y lo que entregaste justo antes.
- Qué skill estaba cargada y qué decía en ese momento.
- Si la conversación se ha compactado, no te fíes del resumen. En Claude Code la sesión entera sigue en
  `~/.claude/projects/<carpeta del proyecto>/<id de la sesión>.jsonl`: busca ahí el momento con una frase del usuario.
- Tu propia explicación del error es una sospecha, no una prueba.

## 2. Lee entero lo que vas a tocar

La skill completa, y el `CLAUDE.md` o `AGENTS.md` que le afecte. No arregles a partir de un trozo. Busca cuatro cosas:

1. **Una regla que ya lo decía.** Si estaba clara y no se cumplió, el fallo fue de ejecución: no añadas nada. Repetir la
   misma regla en otro sitio no la hace cumplirse.
2. **Una regla que lo provoca.** «Explica todo con detalle» provoca correos largos; «haz los correos cortos» debajo no lo
   arregla, lo enfrenta. Corrige o borra la de arriba.
3. **Dos reglas que chocan.** Manda la más reciente; borra la otra (queda en el historial).
4. **Una regla vieja**, de algo que ya no se hace así. Fuera.

## 3. Encuentra la causa, no el síntoma

Recorre estas preguntas y para en la primera que explique el fallo:

1. ¿Tenías la información que hacía falta?
2. ¿Estaba en el sitio correcto?
3. ¿Se usó la skill que tocaba, o ni se cargó?
4. ¿La instrucción era clara y no chocaba con otra?
5. ¿Falló una herramienta o un script, no la skill?
6. ¿Se siguió la instrucción que había?
7. ¿El usuario quería eso siempre, o solo en este caso?

## 4. Decide si merece una regla

Solo si pasa las cinco:

- **Se va a repetir.**
- **La skill puede evitarlo** (si falló una herramienta, se arregla la herramienta).
- **No está ya escrito** en ese sitio.
- **Es estable**, no un gusto de un día ni algo de una sola pieza.
- **Compensa** lo que alarga la skill.

Si no pasa, no se escribe nada y se dice: «fue puntual, no lo apunto». Muchas veces esa es la respuesta correcta.

## 5. Ponlo en un solo sitio, el más concreto

1. Un dato o una referencia mal → se corrige ese dato.
2. Un script o una herramienta → se arregla el script.
3. Algo de una tarea → la skill de esa tarea.
4. Algo que comparten varias skills → su parte común.
5. Algo de todo el proyecto → el `CLAUDE.md` del proyecto.
6. Algo que vale para cualquier trabajo → el `CLAUDE.md` general. Es el último recurso.

Nunca la misma regla en varios sitios.

## 6. El cambio más pequeño que lo evita

Por orden de preferencia: **corregir** una regla que está mal, **juntar** dos que se solapan, **borrar** la que choca o
sobra y, solo si nada de eso vale, **añadir** una nueva. Nunca una regla por cada ejemplo: tiene que cubrir el tipo de
fallo.

Antes de escribirlo, dos preguntas:

- Si este cambio hubiera estado antes, ¿se habría evitado el fallo? Si no, no es el arreglo.
- ¿Qué otro trabajo puede salir peor con esto? Si algo, acótalo.

## 7. Reescribe, no pegues

- La regla nueva va en su sitio del flujo, donde se lee cuando hace falta, nunca como parche al final ni en un montón de
  «notas».
- Borra lo que el cambio deja mal, viejo o repetido, también los ejemplos que ya no aplican.
- Junta duplicados y aprieta lo que queda, para que la skill se lea como escrita hoy de una vez.
- El caso real que motivó el cambio no va en la skill: va al historial (ver abajo).
- La skill acaba igual de larga o más corta, salvo que lo nuevo de verdad pida más.

## Cómo lo cuentas

- **Si te pidieron el cambio** («apúntalo en la skill»): lo haces así y dices en una línea qué cambiaste **y qué
  quitaste o juntaste**, no solo lo que añadiste.
- **Si el cambio se te ocurre a ti**: lo propones y esperas su sí antes de tocar la skill.
- **En una revisión**: una lista numerada. Por cada punto: qué pasó (con la frase exacta), la causa, qué regla ya
  existía, dónde va el cambio, el cambio en una línea y si es seguro o una sospecha. Al final, lo que **no** merece regla
  y por qué. Luego: «¿Cuáles aplico?». Aplicas solo los números que diga.
- **Historial:** cada cambio aplicado deja una línea en `~/.claude/skills-historial/<skill>.md`
  (`- AAAA-MM-DD · qué cambió · por qué`), lo más reciente arriba.
- Nunca cambies una skill que no has leído entera, y nunca subas la sesión ni sus datos a ningún sitio de fuera.
