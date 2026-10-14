---
name: fp-module-architect
description: Construye la documentación completa y auditable de un módulo de FP (programación didáctica, situaciones de aprendizaje con sus 7 documentos, tabla maestra, cuaderno Excel sesión a sesión, FEOE, informe de validación) para cualquier módulo, ciclo, número de RA y centro. Úsala cuando la docente pida programar un módulo de FP, crear SdA, tabla maestra, temporalización o preparar una inspección educativa.
---

# fp-module-architect

Pipeline con fuente única `module.json`. El texto oficial y las cifras salen de scripts; el modelo solo redacta lo pedagógico. El informe de auditoría lo genera `validate.py`, nunca el redactor.

Scripts en `scripts/` (Python). Plantillas en `templates/`. Modelos reales de calidad en `examples/` (Redes Locales SdA1): leerlos antes de redactar cualquier documento.

## Reglas que no se saltan
1. Nunca decir "completo" ni "listo para inspección" sin ejecutar `validate.py` y leer su informe. Adjuntar el resultado literal.
2. Los CE se copian del PDF oficial con `extract_official_ce.py`. Nunca de memoria ni reformulados.
3. Una SdA por vez: redactar, `render.py`, `validate.py`, corregir, y solo entonces la siguiente. No generar varias en bloque ni delegar redacción larga a un modelo pequeño.
4. Nada de datos inventados: alumnado NEAE, fechas, festivos, pesos no confirmados. Lo no confirmado se pregunta o queda marcado `[[REDACTAR: ...]]` (el validador lo rechaza).
5. Tratar a la docente con "ustedes", sin infantilizar.

## Fases (cada una termina con una puerta)
**0. Recogida de datos (preguntar, no suponer).** Plataforma del aula virtual del centro (Moodle propio, EVAGD...) y plataforma de seguimiento de la FEOE (pueden ser distintas). Módulo y código, curso, centro, año, horas nominales (de la norma de la comunidad correcta), PDF oficial del currículo de esa comunidad, horario semanal por franjas y duración de cada sesión, calendario oficial del ciclo (inicio, evaluaciones, vacaciones, fin de clases del módulo, FEOE, proyecto intermodular), días no lectivos y de libre disposición del centro, actos oficiales, qué RA son transversales y en qué evaluación se evalúa cada RA. Si horario o calendario vienen en PDF, convertir a imagen con PyMuPDF y leerla (el texto sale desordenado).
Puerta: lista de datos confirmados por la docente.

**1. CE oficiales.** `python scripts/extract_official_ce.py <pdf> --out <carpeta>/ra_oficiales.json`. Comprobar nº de RA y CE contra el PDF.

**2. module.json.** `python scripts/init_module.py <carpeta> --nombre ... --codigo ... --curso ... --centro ... --anio ... --horas N --docente ...`. Rellenar horario, calendario, `evaluaciones` por RA y `transversal`. Esquema en `references/module_schema.md`.

**3. Horas reales.** `validate.py` calcula horario × calendario − no lectivos. Si hay déficit frente a las horas nominales, avisar con cifras y dejar que la docente decida el reparto. No inventar horas.

**4. Estructura de SdA y pesos (decide la docente).** Proponer: RA principal y complementarios de cada SdA, horas, fechas, evidencias EV1-EV6 con pesos (suman 100; EV5 proyecto 25-30; EV6 individual presencial sin internet 25-30), peso de cada RA (suman 100) y de cada CE dentro del RA (suman 100). Todos los RA deben darse antes de FEOE o fin de clases. Registrar en module.json solo lo confirmado.

**4b. FEOE dual.** Si las horas de aula son menores que las nominales, el resto se dualiza: `dual` en module.json con CE y horas por CE, evidencia genérica de empresa (diario EVAGD, valoración del tutor, tutorías) y alternativa obligatoria en el centro por si la empresa no cubre el CE. Aula + dual = horas nominales.

**5. Tabla maestra.** Rellenar en module.json "evalua", "evidencia" e "instrumento" por CE y ejecutar `python scripts/build_tabla_maestra.py <carpeta>` (xlsx + md).

**6. Por cada SdA (bucle).** `python scripts/new_sda.py <carpeta> <n>` crea los 7 documentos. Redactar cada `[[REDACTAR: ...]]` imitando `examples/` en profundidad (guía ≥5 KB, rúbricas ≥6 KB con indicadores y 4 niveles, examen con escenario nuevo, etc.). Luego `python scripts/render.py <carpeta>` y `python scripts/validate.py <carpeta>`. Corregir hasta que esa SdA no tenga errores.

**7. Cuaderno Excel.** Rellenar `sesiones` de cada SdA (una entrada por sesión real, con plan, CE y evidencia) y ejecutar `python scripts/build_cuaderno.py <carpeta>`. Debe haber cero filas PENDIENTE. El mismo script añade las hojas de gestión (Alumnado, Asistencia, Actitud, FEOE seguimiento y Calificaciones con fórmulas que calculan CE, RA y módulo con los pesos de module.json; parámetro `grupo.alumnos`). Probar las fórmulas con la librería `formulas` antes de entregar.

**8. Programación didáctica.** Partir de `templates/programacion.md`; incluir horas reales frente a nominales, tabla de SdA, pesos, recuperación, DUA y FEOE. `render.py` y `md_to_docx.py`. Ficha FEOE (`templates/feoe_ficha_seguimiento.md`) y Memoria si aplica.

**9. Cierre.** `python scripts/validate.py <carpeta>` genera `Informe_Validacion.md`. Entregarlo tal cual, con sus errores si los hay.

Guía de calidad de redacción: `references/guia_redaccion.md`.
