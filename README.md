# Skills de Claude Code

Skills que uso a diario con Claude Code. Cada carpeta de `skills/` es una skill independiente.

| Skill | Para qué |
|---|---|
| `api-claude-ahorro` | Gastar pocos tokens al programar contra la API de Anthropic |
| `cerrar-fase` | Commit, PR y merge de una fase de trabajo, seguidos y sin parar |
| `consejo` | Pasar una decisión por 5 asesores con revisión a ciegas y veredicto |
| `elegir-modelo` | Qué modelo y esfuerzo usar en cada tarea y subagente |
| `investigacion-profunda` | Investigar un tema a fondo y dejar fichas ordenadas |
| `mejorar-skills` | Corregir una skill de verdad: buscar la causa, no añadir parches |
| `optimizar-tokens` | Hábitos para gastar menos contexto en Claude Code |
| `orquestar-sonnet` | Repartir trabajo entre subagentes Sonnet con encargos acotados |
| `sanear-skills` | Revisar todas tus skills de una vez: contradicciones, duplicados, texto que sobra |

## Instalar

Copia la carpeta de la skill a `~/.claude/skills/` y reinicia Claude Code.

```bash
git clone <este-repo> && cp -r skills/consejo ~/.claude/skills/
```

Las skills están en español.
