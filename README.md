# fp-module-architect

Skill para asistentes de IA con soporte de *skills* (probada con Claude Code) que construye la documentación **completa y auditable de un módulo de Formación Profesional**: programación didáctica, situaciones de aprendizaje (SdA) con sus documentos, tabla maestra, cuaderno del profesor sesión a sesión, **seguimiento de la FEOE** (formación en empresa) y memoria final, más un **validador** que genera el informe de auditoría.

Es la skill hermana de [`programacion-architect`](https://github.com/nievespitti/programacion-architect), que cubre ESO y ámbitos de Diversificación y comparte el mismo enfoque: **trazabilidad en lugar de volumen**.

## Cómo funciona

Todo parte de una **fuente única**, `module.json`. El texto oficial y las cifras salen de scripts; el asistente solo redacta lo pedagógico; y el informe de auditoría lo genera `validate.py`, nunca el redactor.

1. **Datos:** módulo, horas, horario, calendario del ciclo, FEOE, plataformas.
2. **Criterios oficiales:** `extract_official_ce.py` copia literalmente los resultados de aprendizaje (RA) y criterios de evaluación (CE) del PDF oficial.
3. **Horas reales:** horario × calendario − días no lectivos. Si faltan horas respecto a las nominales, se **dualizan en la FEOE** (por CE, con evidencia de empresa y alternativa obligatoria en el centro).
4. **SdA:** una a una, con evidencias y pesos que suman 100.
5. **Cuaderno y tabla maestra** en hojas de cálculo, con las hojas de gestión (alumnado, asistencia, actitud, **seguimiento de la FEOE**, calificaciones con fórmulas).
6. **Cierre:** `validate.py` comprueba pesos, cobertura de CE, horas, carpetas, documentos y FEOE, y emite `Informe_Validacion.md` con resultado APTO o NO APTO.

## Qué incluye

| Carpeta | Contenido |
|---|---|
| `SKILL.md` | Instrucciones de la skill: reglas y fases 0 a 9 |
| `scripts/` | Herramientas en Python (ver abajo) |
| `templates/` | Plantillas de programación, guía del alumnado, rúbricas, medidas DUA, protocolo de recuperación, examen, mapeo para Alexia, **ficha de seguimiento de la FEOE** y memoria final |
| `references/` | Esquema de `module.json` y guía de redacción |
| `examples/` | Documentos de una SdA de un módulo real de Sistemas Microinformáticos y Redes (modelo de calidad) y un `module.json` **ficticio** que pasa por los scripts |

### Scripts

| Script | Qué hace |
|---|---|
| `extract_official_ce.py` | Extrae RA y CE literales de un PDF oficial |
| `init_module.py` | Crea `module.json` con pesos iguales a partir de los RA oficiales |
| `new_sda.py` | Crea los documentos de una SdA |
| `render.py` | Rellena las plantillas con datos de `module.json` |
| `build_tabla_maestra.py` | Tabla maestra (xlsx y md) de RA, CE, evidencias e instrumentos |
| `build_cuaderno.py` y `cuaderno_extra.py` | Cuaderno del profesor y hojas de gestión (incluye seguimiento de la FEOE) |
| `md_to_docx.py` | Convierte los borradores en Markdown a Word |
| `validate.py` | Valida todo y genera el informe de auditoría |

## Qué hay que instalar

- **Python 3.10 o superior** (probado con 3.13).
- Dependencias: `pip install -r requirements.txt` (`python-docx`, `openpyxl`, `pymupdf`).
- Opcional: `pdftotext` (poppler) para leer mejor algunos PDF.
- Un asistente con soporte de skills. En **Claude Code**, la carpeta va en `~/.claude/skills/` (en Windows, `%USERPROFILE%\.claude\skills\`).

```bash
git clone https://github.com/nievespitti/fp-module-architect.git ~/.claude/skills/fp-module-architect
pip install -r ~/.claude/skills/fp-module-architect/requirements.txt
```

## Cómo se usa

Pide al asistente que prepare tu módulo («usa fp-module-architect para programar el módulo…»). Te pedirá el PDF oficial del currículo de tu comunidad, el horario, el calendario y la plataforma del aula virtual y de la FEOE. No inventa datos: lo que no sabe lo pregunta o lo deja marcado `[[REDACTAR: ...]]`, y el validador lo rechaza.

Para ver el flujo con datos ficticios:

```bash
cd examples/modulo-ejemplo
python ../../scripts/build_tabla_maestra.py .
python ../../scripts/build_cuaderno.py .
python ../../scripts/validate.py .
```

El último comando dará **NO APTO** a propósito: al ejemplo le faltan las carpetas de SdA y la programación, y el informe lo señala.

Las entregas para docentes y centros deben ir en **ODT, PDF o Word**, no en Markdown.

## FEOE

- **Dualización:** si las horas de aula no llegan a las nominales, `module.json` declara `dual` con horas por CE, evidencia de empresa y alternativa en el centro. El validador comprueba que aula + FEOE dual = horas nominales.
- **Calendario:** el periodo de FEOE y las fechas de tutoría se registran en `calendario.feoe`; ninguna SdA puede invadirlo.
- **Seguimiento:** el cuaderno incluye la hoja de seguimiento de la FEOE y `templates/feoe_ficha_seguimiento.md` es la ficha de seguimiento (diseñada para el diario del alumnado en EVAGD).

## Alcance y límites

- **Probada con módulos de SMR en Canarias.** El extractor reconoce dos formatos de PDF oficial (fichas autonómicas y BOE/BOC); otros formatos pueden requerir ajustes. Comprueba siempre a mano el número de RA y CE contra el PDF.
- **Convenciones de la autora, no normas.** Las reglas del validador sobre las evidencias (EV1 a EV6, peso del examen individual entre 20 y 35 %, proyecto entre 25 y 30 %…) son criterios de trabajo ajustables, no requisitos de ninguna Consejería. Confírmalas con tu centro.
- **Plataformas.** Hay plantillas pensadas para Alexia y EVAGD; si tu centro usa otras, adapta los documentos.
- **No es asesoramiento normativo.** Contrasta con la normativa de tu comunidad. «APTO» significa que los documentos cumplen las comprobaciones de esta herramienta, no que una inspección los dé por buenos.
- **Pendiente:** unificarla con `programacion-architect` como un perfil más.

## Datos personales

No subas al repositorio datos del alumnado, de empresas colaboradoras ni documentos internos de un centro. El `.gitignore` excluye `proyectos/` y los archivos `*_con_nombres.*`. Los ejemplos de este repositorio son material de modelo; la memoria final de ejemplo lleva cifras **inventadas** y está rotulada como ficticia.

## Contribuir

Se agradecen perfiles de otras comunidades, extractores para otros formatos de PDF y plantillas para otras plataformas. Abre una incidencia o un *pull request*; no incluyas datos reales de alumnado ni de centros.

## Licencia

[MIT](LICENSE).
