---
name: sanear-skills
description: Revisa de una vez todas las skills propias (y los dos CLAUDE.md) para quitar contradicciones, duplicados, reglas viejas y texto que sobra, y dejar cada una más corta. Úsala con «revisa/sanea mis skills», «revisa todas las skills», «contradicciones entre skills», «limpia las skills». Para una sola skill o un error concreto, `mejorar-skills`.
---

# Sanear skills

Revisión global. Cada cambio sigue el método de `mejorar-skills`, que aquí no se repite.

## 1. Inventario y copia

- Lista las skills propias: `~/.claude/skills/*` (no hay skills dentro de los proyectos). Las de terceros
  (higgsfield-*, graphify, archify, prompt-master, plugins) quedan fuera, salvo que sus
  disparadores pisen los de una propia.
- Cuenta las líneas de cada una (`wc -l`).
- `~/.claude` no está en git: copia cada skill a `<scratchpad>/backup-skills/`
  antes de tocar nada.

## 2. Leer entero

Lee cada skill entera, más `~/.claude/CLAUDE.md` y el `CLAUDE.md` del proyecto. Si son muchas, se
reparte la lectura entre subagentes Sonnet `effort: medium` de solo lectura, agrupados por tema
(`orquestar-sonnet`). Cada uno devuelve sus hallazgos con `archivo:línea` y cita literal.

## 3. Qué buscar

- **Contradicciones** entre skills, o entre una skill y un CLAUDE.md. Manda la regla más reciente; la
  vieja se borra y queda en el historial.
- **Duplicados:** una regla vive en un solo sitio y los demás la enlazan.
- **Reglas viejas:** scripts, rutas, marcas o flujos que ya no existen. Antes de afirmarlo, comprueba
  en disco si existen.
- **Texto que sobra:** historias, ejemplos largos, secciones «Correcciones» (pasan al historial).
- **Disparadores que se pisan** entre dos skills.
- Un **objetivo de líneas** por skill.

Comprueba tú cada hallazgo abriendo las líneas citadas; descarta lo que no se sostenga.

## 4. Lista y elección

Entrega una lista numerada agrupada por skill. Cada punto lleva `archivo:línea`, el tipo, el cambio
en una línea y si es seguro o una sospecha. Las dudas sobre qué quiere el usuario de verdad van como
preguntas. Termina con «¿Cuáles aplico?» y **para**: solo se aplica lo que elija.

## 5. Aplicar

- Orden de `mejorar-skills`: corregir > juntar > borrar > añadir. Se reescribe en su sitio; la skill
  queda igual o más corta.
- Una línea por cambio en `~/.claude/skills-historial/<skill>.md` (fecha, qué y por qué).
- Compara las líneas con la copia: ninguna crece sin motivo.
- Informe final breve: los cambios por skill, lo que quedó pendiente y lo que se tocó sin preguntar.
