---
name: elegir-modelo
description: Úsala al empezar una tarea, al cambiar de fase (diseño → código → pruebas), antes de lanzar un subagente o cuando algo se atasca. Decide qué modelo y qué esfuerzo usa cada parte y cada subagente (Opus, Sonnet o Haiku) y cuándo subir o bajar.
---

# Elegir modelo

## §1. La regla

**El modelo más barato que haga bien la tarea.** Se sube de modelo solo con evidencia de que
el actual no llega (fallos repetidos, un plan que no se sostiene), nunca "por si acaso".

## §2. Tarea → modelo y esfuerzo

| Rol | Modelo · esfuerzo | Para qué |
|---|---|---|
| **Planificar y decidir** (la sesión) | Opus · high (medium si el plan es sencillo) | Planes y arquitectura, comparar opciones, decisiones difíciles de deshacer, depurar donde Sonnet ya se atascó, revisar un diseño |
| **Ejecutar lo decidido** | Sonnet · medium | Programar desde un plan aprobado, refactorizar, tests y benchmarks, documentación, ediciones en varios archivos, **redactar páginas de wiki** desde la fuente |
| **Rastrear** | Haiku · low | Buscar y explorar código (`Explore` con `model: "haiku"`, que si no usa el del padre), resumir logs, clasificar, comprobaciones con criterio fijo |

Ejemplo canónico: **Opus** planifica → **Sonnet** ejecuta con un encargo bien acotado
(`orquestar-sonnet`) → se vuelve a **Opus** solo si Sonnet se atasca.

## §3. Momentos de cambio

- **Plan aprobado** → la ejecución va a subagentes Sonnet (§4).
- **Sonnet falla 2 veces en el mismo error**, o el plan deja de valer → Opus solo para ese
  punto; resuelto, se vuelve a Sonnet.
- **Subir (en este orden):** 1) más esfuerzo (Sonnet high), 2) Opus, 3) Fable, solo proponerlo
  (~2x de coste). Señales de atasco: se salta archivos, no ejecuta los tests, abandona a medias,
  repite el error, entrega sin cumplir el «hecho».
- `max` solo para problemas duros sin supervisión, y probado antes (sobrepiensa).

## §4. Cómo se aplica

- **Delegar:** `Agent` con `model` (solo alias) y **siempre `effort`**: un subagente no hereda
  el esfuerzo de la sesión. Encargo, reparto y verificación: `orquestar-sonnet`, que también
  decide cuándo no compensa delegar.
- **Cambiar el modelo o el esfuerzo de la sesión** reprocesa todo el contexto a precio
  completo: mejor delegar (caché propia). Si hace falta, se propone en una línea; lo cambia el
  usuario (selector de la app o `/model`), nunca Claude.
- El ajuste global es `effortLevel` en `~/.claude/settings.json`; no se cambia sin preguntar.

## §5. Evidencia

- Haiku no respeta topes escritos en el prompt: los límites van en el código.
- Haiku de verificador gastaba 12.000 tokens razonando; con `MAX_THINKING_TOKENS=0`, unos 5.000.
en su código.
