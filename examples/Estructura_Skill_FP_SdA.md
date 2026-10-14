# Arquitectura de la Skill: `fp-sda-creator` (Diseñador de SdAs y Evaluación Alexia)

Este documento define la estructura y el flujo de trabajo para crear una **Skill reutilizable** que permita configurar cualquier módulo o asignatura de Formación Profesional (Grados Básico, Medio y Superior) según el modelo curricular LOMLOE y la integración con el cuaderno de Alexia.

---

## 1. Definición y Metadatos de la Skill

* **Nombre sugerido:** `fp-sda-creator`
* **Ubicación destino (Workspace o Global):** `.agents/skills/fp-sda-creator/SKILL.md`
* **Propósito:** Generar la documentación didáctica completa de una Situación de Aprendizaje (SdA) a partir del currículo oficial del módulo: programación docente, guía del alumno con entregables claros y matriz de configuración para Alexia.

---

## 2. Parámetros de Entrada Requeridos por la Skill

Para configurar cualquier asignatura/módulo, la skill solicita o lee:
1. **Datos del Módulo:** Título del ciclo (CFGM/CFGS), código y nombre del módulo, curso (1º o 2º) y horas anuales/semanales.
2. **Marco Curricular:** Resultado(s) de Aprendizaje (RA) a trabajar y lista oficial de Criterios de Evaluación (CE) asociados.
3. **Contexto del Alumnado y Reto:** Entorno profesional simulado o problema real que motiva el aprendizaje.
4. **Herramientas de Taller / Software:** Software técnico (p. ej. Packet Tracer, VS Code, Wireshark, máquinas virtuales, etc.) o instrumental de laboratorio.

---

## 3. Salidas Estandarizadas que Produce la Skill

Para cada SdA, la skill genera automáticamente 3 artefactos sincronizados:

### A. Documento Pedagógico (Docente / Inspección)
* Ficha de la SdA (Contexto, temporalización, RAs principales y complementarios).
* Secuenciación de actividades basada en ciclos activos (PPI: Contexto → Experiencia → Reflexión → Acción → Evaluación).
* Medidas DUA (Diseño Universal para el Aprendizaje).
* Marco de uso pedagógico de Inteligencia Artificial (dónde se permite, cómo se verifica).

### B. Guía de Trabajo del Alumno (`Guia_Alumno_SdA.md`)
* Lenguaje directo, motivador y sin jerga burocrática excesiva.
* Desglose claro de retos, entregas y plazos.
* Rúbricas e indicadores de logro visibles de antemano ("Qué tengo que entregar", "Cómo se evalúa").
* Transparencia en los criterios de autoría (pruebas individuales sin conexión).

### C. Matriz de Configuración del Cuaderno de Alexia (`Mapeo_Alexia_SdA.md`)
* Lista de columnas evaluables en Alexia con sus nombres y códigos.
* Asignación porcentual de pesos por evidencia (evitando atomización excesiva; idealmente entre 4 y 6 columnas por SdA).
* Matriz de trazabilidad biunívoca: ningún CE del Real Decreto queda sin evaluar ni huérfano.
* Fórmula matemática lista para introducir en Alexia.
* Registro observacional para criterios transversales (actitud, seguridad, PRL).

---

## 4. Patrón de Evidencias Recomendado para FP Técnica

La skill adopta el estándar validado en Redes Locales:

| Tipo de Evidencia | Peso Típico | Finalidad Pedagógica | Instrumento |
|---|:---:|---|---|
| **EV1: Práctica Guiada / Simulación** | 10 - 15 % | Adquisición inicial de destrezas técnicas | Lista de cotejo / Archivo técnico |
| **EV2: Diagnóstico / Resolución Incidencias** | 10 - 15 % | Capacidad analítica y resolución de problemas | Rúbrica de diagnóstico |
| **EV3: Fundamentos Teórico-Prácticos** | 10 % | Asimilación de conceptos y terminología | Cuestionario aplicado / Fichas |
| **EV4: Representación / Esquema / Diseño** | 10 % | Capacidad de abstracción y documentación | Rúbrica de plano / memoria |
| **EV5: Proyecto Integrador / Reto Final** | 25 - 30 % | Aplicación global en escenario profesional | Rúbrica de proyecto |
| **EV6: Prueba Práctica Individual de Aula** | 25 - 30 % | Garantía de autoría y dominio individual | Prueba técnica en vivo |
| **Transversal: Registro Observacional** | Acumulativo | Hábitos profesionales, seguridad y orden | Lista de control de aula |

---

## 5. Próximo Paso para Instalar la Skill
Cuando se valide el funcionamiento completo de esta SdA1, la skill puede compilarse directamente en `.agents/skills/fp-sda-creator/SKILL.md` para ser ejecutada ante cualquier nuevo módulo (Sistemas Operativos, Seguridad Informática, Servicios en Red, etc.).
