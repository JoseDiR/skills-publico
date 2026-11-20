---
name: api-claude-ahorro
description: Reglas para gastar pocos tokens al programar contra la API de Anthropic (Messages API, SDK anthropic, scripts o apps que llaman a Claude por API con pago por uso) - caché de prompt, Batches, tool_choice, salida corta, esfuerzo y presupuesto de salida. Úsala al escribir o revisar código que llama a la API de Claude, al diseñar un pipeline con Claude por API o cuando pregunte cómo abaratar la API. No aplica a Claude Code ni al CLI `claude` (suscripción), que ya cachean solos.
---

# Ahorro de tokens en la API de Claude

Esta skill dice **qué** hacer. La sintaxis exacta (nombres de parámetros, mínimos de caché, precios, ids de modelo) se mira en la skill `claude-api` antes de escribir código: no se inventa.

## Reglas, por orden de impacto

1. **Caché de prompt.** Lo fijo va primero y no cambia: herramientas → system → documentos de referencia → historial. Se marca con `cache_control` el final del prefijo estable. Leer de caché cuesta una fracción de la entrada normal y baja la latencia del primer token. Cualquier cambio en el prefijo (una fecha en el system, reordenar herramientas, cambiar de modelo o de presupuesto de razonamiento) rompe la caché: lo variable va al final.
2. **Batches para lo que no corre prisa.** Lotes de documentos, clasificación, resúmenes, indexado: Message Batches API (descuento del 50 % según Anthropic, resultados en horas). Interactivo nunca.
3. **Historial corto.** Cada llamada reenvía todo el historial. Se recorta o se resume lo viejo; los resultados de herramienta largos se reducen antes de devolverlos al modelo (solo el error, solo las filas útiles).
4. **Salida corta y estructurada.** La salida cuesta varias veces la entrada. Se fija `max_tokens` ajustado, se pide formato cerrado (JSON con esquema, o solo el diff/bloque a cambiar, nunca el archivo entero) y nada de preámbulos.
5. **Esfuerzo y modelo por tarea.** El razonamiento se cobra como salida. Tareas mecánicas: modelo pequeño y esfuerzo bajo; el modelo grande solo para lo que lo necesita (tabla en la página `modelos-claude-5-5-esfuerzo`).
6. **`tool_choice` forzado** cuando ya se sabe qué herramienta toca: el modelo no gasta tokens decidiendo.
7. **Medir.** Contar tokens antes de enviar (endpoint de conteo) y leer `usage` de cada respuesta (entrada, salida, caché leída y escrita). Sin medir no se sabe si la caché funciona.

## Verificación

- [ ] La segunda llamada con el mismo prefijo muestra tokens leídos de caché en `usage`.
- [ ] Nada dinámico (fecha, id, contador) dentro del prefijo cacheado.
- [ ] Las tareas no interactivas van por Batches o está dicho por qué no.
- [ ] `max_tokens` fijado y formato de salida cerrado.
