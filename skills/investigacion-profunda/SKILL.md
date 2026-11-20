---
name: investigacion-profunda
description: Investiga a fondo un tema (cualquier disciplina) y lo convierte en una monografía de 0 a experto - taxonomía de conceptos, búsqueda de fuentes primarias por concepto, una ficha por concepto en dos niveles (conceptual y técnico) e índice con ruta de aprendizaje. Úsala con «investiga a fondo X», «monografía de X», «de 0 a experto en X», «deep research de X».
---

# Investigación profunda

Convierte un tema en una enciclopedia técnica: una ficha por concepto y un índice que lleva de
0 a experto.

## Normas

- **Buscar antes de escribir:** por cada ficha, 3-5 búsquedas de fuentes primarias (papers,
  normas, documentación oficial, repos). Lo que no se encuentra se dice, no se rellena.
- **Dos niveles por ficha:** conceptual y técnico. Sin un tercero de proveedores salvo que el
  tema trate de ellos.
- **Fórmulas en LaTeX** (`$…$`, `$$…$$`) con cada variable definida; **un diagrama Mermaid** por
  ficha (texto de nodos con paréntesis, entre comillas).
- **Sin cifras inventadas:** cuota de mercado, adopción o rendimiento, solo con fuente citada.
- **Almacenamiento:** guarda las fichas en una carpeta propia del tema, con un `README.md` como índice.

## Fases

1. **Taxonomía:** categorías (fundamentos, métodos, arquitecturas, herramientas, casos) y
   conceptos atómicos sin solapes, en carpetas numeradas (`01_…`, `02_…`).
2. **Búsqueda por concepto:** formulación o estándar formal (RFC, paper, ISO); herramientas que
   usa el sector; fallos y límites reales (post-mortems, debates técnicos).
3. **Ficha** con esta plantilla:

````markdown
# [Nombre del Concepto en Español / Término Internacional]

## 1. Nivel Conceptual (Agnóstico)

### 1.1 Definición Analógica e Intuitiva
[Explicación clara y memorable basada en una analogía del mundo real, comprensible en 2 minutos para alguien sin conocimientos previos en el área.]

### 1.2 Principios de Diseño y Mecánica Interna
[Fundamento teórico y principios de funcionamiento: qué problema fundamental resuelve, cuál es su ciclo de operación y qué dinámica interna gobierna su comportamiento.]

### 1.3 Diagrama de Flujo Lógico
```mermaid
flowchart TD
    [Diagrama Mermaid claro y sin errores de sintaxis que ilustre el flujo o arquitectura del concepto]
```

### 1.4 Características y Capacidades Nucleares
- **[Capacidad 1]:** [Explicación técnica concisa]
- **[Capacidad 2]:** [Explicación técnica concisa]
- **[Capacidad 3]:** [Explicación técnica concisa]

### 1.5 Dónde es Altamente Eficiente (Trabajos Objetivo)
- **[Caso de Uso 1]:** [Descripción de cuándo y por qué supera a alternativas tradicionales]
- **[Caso de Uso 2]:** [Descripción de entorno óptimo]
- **[Caso de Uso 3]:** [Descripción de entorno óptimo]

### 1.6 Antipatrones y Dónde NO es Óptimo
- **[Antipatrón 1]:** [Riesgo de fallo, coste innecesario o mala práctica]
- **[Antipatrón 2]:** [Situaciones donde existen alternativas mucho más simples y eficientes]

---

## 2. Nivel Técnico y Formal (Aplicación en el Sector)

### 2.1 Marco Teórico y Fórmulas Matemáticas
[Ecuaciones rectoras, modelos formales y leyes físicas/matemáticas en LaTeX]:
$$[Ecuación principal en bloque]$$
- Definición formal de cada variable ($x, y, \theta, \dots$).
- Supuestos matemáticos y condiciones de contorno.

### 2.2 Herramientas, Librerías y Software Dominantes en el Sector
- **[Herramienta Líder A]:** [Qué es y por qué es el estándar, con la fuente que lo respalda]
- **[Herramienta Líder B]:** [Alternativa moderna o de código abierto]
- **[Estándar / Formato de Intercambio]:** [Formatos de archivo, protocolos o especificaciones estándar del sector]

### 2.3 Implementación Práctica / Configuración de Producción
```[lenguaje-relevante]
# Snippet de código real, script ejecutable, configuración de producción o especificación formal
# que demuestre cómo se materializa el concepto en la práctica sin código 'de juguete'.
```

### 2.4 Patrones Habituales y Arquitecturas de Integración en la Industria
[Cómo los profesionales y la comunidad ensamblan este concepto junto con otras piezas del ecosistema en proyectos reales. Discusión de arquitecturas de referencia y compromisos técnicos (trade-offs).]

### 2.5 Referencias Técnicas y Fuentes Canónicas
- [Autor / Organización] ([Año]): *[Título de la obra / Paper / Estándar]*. [Editorial o Conferencia].
- [Enlace oficial a documentación técnica o repositorio de referencia].
````

4. **Índice `README.md`:** introducción, mapa de la taxonomía, fichas por categoría con enlace
   relativo y resumen de una línea, y ruta de aprendizaje (fundacional → implementación →
   maestría).

**Hecho cuando:** ninguna sección de la plantilla vacía, Mermaid y KaTeX válidos, código
realista, 0 enlaces rotos en el índice, todo en español.
