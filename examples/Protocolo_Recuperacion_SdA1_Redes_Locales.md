# Protocolo de Recuperación y Segunda Oportunidad
## Situación de Aprendizaje 1 (RA1) · Redes Locales (0225)
**Ciclo:** 1.º SMR · Curso 2026-2027  
**Marco Normativo:** LOMLOE / Real Decreto 1691/2007 (Anexo I) · Evaluación Formativa y Continua  
**Principio Clave:** *Recuperación selectiva por Criterios de Evaluación (CE) y evidencias no adquiridas; el alumnado nunca repite tareas ya superadas.*

---

## 1. Principios Pedagógicos y Normativos

1. **Evaluación Continua y Formativa:** La evaluación no busca clasificar, sino asegurar que el alumnado alcanza la competencia profesional exigida en el perfil técnico de SMR.
2. **Conservación de Calificaciones Positivas:** Si un alumno ha superado una o varias evidencias (ej. plano digital o prácticas de Packet Tracer), esas calificaciones se mantienen intactas. Solo se recuperan las evidencias o criterios calificados con nota inferior a 5,00.
3. **Calificación de la Recuperación:**
   - En cumplimiento del principio de aprendizaje competencial, la calificación obtenida en la recuperación sustituye a la calificación inicial en la ponderación de Alexia, reconociendo el dominio alcanzado por el alumno (sin penalizaciones artificiales de "máximo 5" que desmotiven la excelencia técnica).
   - En el cuaderno del profesor queda registrado el histórico (nota inicial, fecha de recuperación y nota definitiva).

---

## 2. Mapa de Recuperación por Evidencia (SdA1)

Para cada una de las 6 evidencias evaluables de la SdA1 se define un itinerario específico de segunda oportunidad:

| Evidencia Inicial | Criterios Oficiales | Motivo de No Superación Típico | Mecanismo de Recuperación (Segunda Oportunidad) | Formato y Plazo |
|---|:---:|---|---|---|
| **S1_EV1: Packet Tracer** (15 %) | **1.a, 1.c** | Red no operativa, solapamiento IP, comando ping fallido. | **Reto Alternativo PKT:** Se entrega una nueva topología equivalente para cablear y direccionar en Packet Tracer, verificando conectividad en presencia del docente. | Archivo `.pkt` + comprobación en aula (plazo: 5 días lectivos tras publicación de nota). |
| **S1_EV2: Diagnóstico** (15 %) | **1.a, 1.c** | No identifica causa raíz del fallo o no repara la red. | **Ficha de Reparación Guiada:** Se asigna un archivo con 3 errores provocados distintos (IP, máscara, interfaz switch down). El alumno documenta síntoma, causa y solución. | Ficha técnica + `.pkt` reparado. |
| **S1_EV3: Fundamentos** (10 %) | **1.b, 1.d, 1.g, 1.h** | Errores conceptuales en medios de transmisión o topologías. | **Cuestionario Práctico de Aplicación:** Prueba técnica breve o entrega corregida de las fichas de dispositivos y medios con defensa oral rápida de 3 preguntas. | Cuestionario en Moodle o ficha corregida. |
| **S1_EV4: Plano Digital** (10 %) | **1.e, 1.f** | Falta de simbología, trazado incoherente o escala errónea. | **Corrección y Reentrega del Plano:** El docente entrega la lista de no conformidades. El alumno subsana los errores en Draw.io / Excalidraw y reentrega en PDF. | Reentrega en Moodle (máximo 1 semana tras feedback). |
| **S1_EV5: Proyecto Pyme** (25 %) | **1.a - 1.h** | Memoria incompleta, falta de justificación técnica o simulación defectuosa. | **Defensa y Subsanación del Proyecto:** Se permite completar los apartados deficientes de la memoria y corregir la maqueta en Packet Tracer, realizando una breve defensa técnica ante el profesor. | Entrega de anexo corregido + defensa de 5 minutos en tutoría. |
| **S1_EV6: Prueba Práctica Individual** (25 %) | **1.a - 1.h** | Falta de autonomía en el aula o no supera el reto presencial. | **Convocatoria Práctica Individual Extraordinaria:** Nueva prueba práctica individual de 55 minutos en aula de ordenadores con un escenario técnico diferente. | Sesión presencial de aula fijada en calendario. |

---

## 3. Calendario y Ventanas de Recuperación

Se establecen **3 momentos temporales** para ejercer el derecho a la recuperación:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   VENTANAS DE RECUPERACIÓN (SdA1)                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Ventana Inmediata (Nivel SdA):                                      │
│    • Sesión 29 (19/11/2026): Cierre de SdA1 y recuperación rápida de   │
│      evidencias prácticas y reentregas de proyectos.                   │
│                                                                        │
│ 2. Ventana Trimestral (Cierre 1.ª Evaluación):                         │
│    • Sesión 42 (22/12/2026): Sesión de cierre previo a Navidad para    │
│      alumnos con criterios pendientes de SdA1 antes de actas.          │
│                                                                        │
│ 3. Ventana Final Ordinaria (Mayo - Junio 2027):                        │
│    • Sesiones 85-88 (20 al 27 de mayo de 2027): Talleres intensivos   │
│      de aula para recuperar CEs pendientes del RA1.                    │
│    • Sesión 93 (03/06/2027): Examen práctico ordinario de recuperación.│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Gestión del Registro en Alexia

Para no destruir la trazabilidad del proceso ni el histórico inicial de notas, el profesorado procederá según dos opciones técnicas admitidas en Alexia:

### Opción A (Recomendada): Columna de Recuperación Específica
1. En la subcarpeta de la SdA1 se crea la columna: `S1_REC_RA1` (Tipo: Numérica 0-10).
2. Se introduce la nota obtenida en el proceso de recuperación.
3. La fórmula de cálculo de la nota final del RA1 se parametriza como:
   $$\text{Nota\_Final\_RA1} = \max(\text{Nota\_Ordinaria\_SdA1}, \text{Nota\_Recuperacion})$$

### Opción B: Actualización de la Evidencia con Trazabilidad Documental
1. Se actualiza la nota en la columna original de la evidencia recuperada (ej. `S1_EV6`).
2. En el campo **Observaciones / Diario del Alumno** de Alexia se deja constancia escrita:
   > *"Nota inicial: 3,5 (17/11/2026). Recuperado mediante prueba individual alternativa el 19/11/2026 con calificación: 7,0."*

---

## 5. Compromiso del Alumno y Plan de Trabajo Autónomo

El alumno que suspenda una evidencia adquiere los siguientes compromisos:
1. **Asistencia a la sesión de retroalimentación (feedback):** Analizar con el profesor la rúbrica donde constan los fallos cometidos.
2. **Uso ético de IA como apoyo:** Puede utilizar herramientas de IA para solicitar explicaciones adicionales o ejercicios de práctica guiada, pero debe ser consciente de que la prueba de recuperación será presencial e individual.
3. **Plazos:** Toda entrega fuera del plazo pactado sin justificación médica o de fuerza mayor supondrá la pérdida de la oportunidad inmediata, postergándose la recuperación al final del trimestre.
