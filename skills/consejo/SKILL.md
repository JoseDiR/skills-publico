---
name: consejo
description: Pasa una decisión con algo en juego por un consejo de 5 asesores (abogado del diablo, primeros principios, ambicioso, el de fuera y ejecutor) que responden por separado, se revisan a ciegas y acaban en un veredicto con un primer paso. Basada en LLM Council de Ole Lehmann (método Karpathy). Úsala con «pásalo por el consejo», «pregúntale al consejo», «consejo esto», «¿hago X o Y?», «no me decido entre…», «¿estoy loco si…?». NO para preguntas con una sola respuesta, escribir o resumir.
---

# Consejo

Para decisiones donde equivocarse sale caro (precio, qué vídeo grabar, contratar o automatizar, qué propuesta priorizar). Evita que Claude dé la razón por defecto. Gasta 10 subagentes: no lo uses para lo trivial; si la pregunta no tiene alternativas reales, contesta normal y dilo.

## Pasos

1. **Contexto (≤30 s).** Lee lo que afecte a la decisión: `~/.claude/projects/*/memory/MEMORY.md` y las memorias que encajen (perfil, plan de 90 días, proyectos), el CLAUDE.md del proyecto y lo que el usuario haya citado. Si la pregunta es vaga, **una** sola pregunta.
2. **Enmarca** en un texto neutro, sin opinar: la decisión, el contexto (fase, público, cifras, restricciones) y qué está en juego.
3. **5 asesores en paralelo** (subagentes `general-purpose`, `model: sonnet`, `effort: medium`, en un solo mensaje). Cada uno recibe su ángulo + el texto enmarcado y responde en 150-300 palabras, sin matizar ni equilibrar, en español:
   - **Abogado del diablo**: el fallo que lo hunde.
   - **Primeros principios**: qué se quiere resolver de verdad; a veces «la pregunta está mal».
   - **Ambicioso**: la oportunidad mayor que se escapa.
   - **El de fuera**: sin contexto del usuario; ve lo obvio y la jerga que nadie entiende.
   - **Ejecutor**: qué se hace el lunes por la mañana; el camino más rápido.
4. **Revisión a ciegas** (5 subagentes, `model: haiku`, `effort: low`, en paralelo). Baraja las respuestas como A-E (orden aleatorio). Cada revisor, en ≤200 palabras: la más sólida y por qué, la del mayor punto ciego y qué se les escapó a todos.
5. **Presidente** (tú, sin subagente): con las respuestas ya con nombre y las 5 revisiones, escribe en el chat:

```
## Veredicto del consejo: {tema}
### En qué coinciden
### En qué chocan        (los dos lados, sin suavizar)
### Puntos ciegos        (lo que salió solo en la revisión)
### Recomendación        (una respuesta clara; puede ir contra la mayoría si el que discrepa razona mejor)
### Lo primero que haces (una sola cosa)
```

6. Sin archivos salvo que lo pida; si lo pide, `output/consultas/consejo-AAAA-MM-DD-tema.md` del proyecto.
