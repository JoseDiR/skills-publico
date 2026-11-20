---
name: optimizar-tokens
description: Estándar de ahorro de tokens en Claude Code. Un hook de UserPromptSubmit recuerda su resumen en cada mensaje; se carga entera al empezar una tarea grande. Clasifica la petición y limita lo que se lee, se ejecuta y se escribe. Modelo y esfuerzo: `elegir-modelo`.
---

# Optimizar tokens

Versión completa de las reglas de ahorro de tokens.

| Petición | Cómo se trabaja |
|---|---|
| Pregunta directa | Sin herramientas si ya se sabe; si no, la consulta mínima |
| Cambio acotado | Solo los archivos implicados, sin explorar alrededor |
| Tarea grande | Plan primero, `elegir-modelo` y delegar solo si compensa (`orquestar-sonnet`) |

## Leer menos
- Grep o Glob antes que Read; Read con `offset`/`limit` si se sabe qué parte hace falta.
- Navegador: `get_page_text`/`read_page` antes que capturas; capturas con `scale` 0,5–0,7.

## Ejecutar menos
- Llamadas independientes en paralelo o en lote (`browser_batch`).
- No repetir una prueba cara si una barata demuestra lo mismo; esperar con notificación, no sondeando.

## Contexto largo
- Sesión nueva para temas no relacionados. `/compact` solo se propone: lo lanza el usuario.

## Medir
En operaciones caras (benchmarks, `claude -p`, ingestas) anotar los tokens y decir si el
ahorro se notó. Si un cambio no ahorra, se dice y se quita.
