---
name: cerrar-fase
description: Cierra una fase o rama de trabajo sin interrumpir al usuario - commit, push, PR, traer main y resolver conflictos, verificar y fusionar el PR, todo seguido y sin pedir permiso. Úsala SIEMPRE al terminar una fase o rama de `plan-por-fases`, y cuando diga "commit y PR", "haz commit, PR y fusiona", "cierra la rama", "súbelo y mergea" o "lo que queda de commit/PR". Solo para cuando algo la bloquea de verdad.
---

# Cerrar fase

Al acabar cada fase, commit, PR y merge van **solos y sin preguntar**, y se sigue con la siguiente. Es la excepción a
«los commits los hace el usuario» de los CLAUDE.md. **Rama base** = `main`, o la que fije el proyecto: donde abajo pone `main`, léase la base.

## Pasos (seguidos, sin preguntar)

1. **Estado real.** `git status --short`, rama actual y `git rev-list --left-right --count HEAD...origin/main`.
   Si la rama local tiene commits sin subir (p. ej. ingestas del motor en `main`), van en el mismo PR.
2. **Rama.** Si estás en `main` (o la rama base), crea una rama con nombre de la fase.
3. **Commit.** `git add -A` y saca del índice lo que no se versiona: `*.tmp`, `*.lock`, scripts de prueba
   sueltos (`test_*.js` en la raíz), logs, `.env` y cualquier archivo con claves, tokens o cookies (míralo
   antes: si dudas, fuera). Mensaje: qué se hizo, en español, con la línea `Co-Authored-By` de la sesión.
4. **Traer main.** `git fetch` y `git merge origin/main`. Si hay conflictos, ver §Conflictos.
5. **Verificar antes de subir.** Los tests y comprobaciones del proyecto. Un fallo que ya
   estaba en main o que no tiene que ver se apunta, no bloquea.
6. **PR y merge.** `git push -u origin <rama>`, `gh pr create` (cuerpo breve: qué entra, qué no, cómo se
   verificó; termina con la línea de Claude Code), `gh pr merge --merge`. Luego `git switch main` y
   `git pull` en el checkout donde trabaja el usuario, si no tiene cambios sin commitear.
7. **Nota de traspaso y seguir.** Añade al archivo de estado del plan (el que fije el plan; si no
   hay, `docs/<plan>/estado.md` del repo) 3-6 líneas: fase cerrada, PR (enlace), qué quedó fuera o falló
   sin bloquear, y la fase siguiente con lo que necesita saber. Así, si el contexto se compacta solo
   (autocompact), se sigue desde la nota. Luego empieza la fase siguiente sin esperar. `/compact` no se
   puede lanzar desde Claude: solo lo ejecuta el usuario. Al terminar la **última** fase, resumen final y parada.

## Conflictos

- **Generados** (`index.md`, `indice/`, `datos.json`…): no se editan; se regeneran con su script.
- **Registros que solo crecen** (`log.md`, `processed.json`, colas): se juntan los dos lados (JSON: unión
  de claves; log: las dos tandas de entradas, la más reciente arriba).
- **Frontmatter**: `python -I ~/.claude/skills/cerrar-fase/fm_resolver.py <archivos>` resuelve los bloques
  que solo tienen campos (listas = unión, `fecha_actualizacion` = la mayor, resto = main). Acepta CRLF.
- **Texto** (wiki, código): si son pocos, a mano; si son muchos, subagentes Sonnet en `medium` con
  `orquestar-sonnet`, archivos sin solapar, normas escritas en un archivo y un comprobador que dé OK.
- **Borrado en un lado y cambiado en el otro** (UD/DU): se saca el diff del lado que cambió, se lleva lo
  nuevo a la página que sustituye a la borrada y se confirma el borrado.

## Solo se para antes si…

- El push o el merge los rechaza GitHub (permisos, protección de rama, workflow sin scope).
- Un conflicto exige decidir algo de producto o contenido que no se deduce de los dos lados.
- Hay datos sensibles en lo que se iba a subir y no está claro si deben ir.
- Los tests fallan por el cambio de esta fase y no se arreglan en un intento.

En esos casos: dilo en una línea con lo que falta y deja la rama tal cual (sin `reset` ni `--force`).
