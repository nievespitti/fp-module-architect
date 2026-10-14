# Configuración del Cuaderno de Alexia · SdA1: Redes Locales
**Módulo:** Redes Locales (0225) · 1.º SMR (2026-2027)  
**SdA1:** ¿Cómo se comunican los equipos de una red?  
**Peso de la SdA en el módulo:** 15 % (corresponde al 100 % del RA1)

---

## 1. Columnas a crear en el Cuaderno del Profesor (Alexia)

Se configuran **6 columnas evaluables directas** asociadas a la SdA1, todas en escala numérica de **0 a 10** (con 2 decimales):

| Código Alexia | Nombre de la Columna / Evidencia | Criterios de Evaluación Oficiales Asociados | Instrumento Docente | Peso en SdA1 (RA1) | Peso Total en Módulo (0225) |
|---|---|---|---|:---:|:---:|
| **S1_EV1** | Prácticas Packet Tracer (Intro + Simulación) | **1.a** (70%), **1.c** (30%) *(Anticipa RA4)* | Lista de cotejo / Archivo .pkt | **15 %** | 2,25 % |
| **S1_EV2** | Diagnóstico y Resolución de Errores | **1.a** (50%), **1.c** (50%) *(Anticipa RA5)* | Rúbrica de diagnóstico + .pkt | **15 %** | 2,25 % |
| **S1_EV3** | Fundamentos: Tipos, Medios y Topologías | **1.b** (25%), **1.d** (25%), **1.g** (25%), **1.h** (25%) | Cuestionario aplicado / Fichas | **10 %** | 1,50 % |
| **S1_EV4** | Representación del Mapa Físico | **1.e** (50%), **1.f** (50%) | Rúbrica de plano digital (Draw.io/PDF) | **10 %** | 1,50 % |
| **S1_EV5** | Proyecto Final: Red Pequeña Empresa | **1.a** a **1.h** (Global integrador) | Rúbrica de proyecto (Memoria + PKT + Plano) | **25 %** | 3,75 % |
| **S1_EV6** | Prueba Práctica Individual de Aula | **1.a** a **1.h** (Demostración de autoría) | Prueba práctica individual en aula | **25 %** | 3,75 % |
| **TOTAL** | **Calificación Final SdA1 / RA1** | **RA1 completo (1.a - 1.h)** | **Media ponderada de EV1 a EV6** | **100 %** | **15,00 %** |

---

## 2. Relación de Criterios de Evaluación (RD 1691/2007) y Cobertura

Esta configuración garantiza que **ningún criterio de evaluación del RA1 quede sin evaluar**:

| Criterio | Descripción operativa | Dónde se evalúa (Evidencias) | Cobertura en Alexia |
|:---:|---|---|:---:|
| **1.a** | Principios de funcionamiento de redes locales | EV1 (Packet Tracer), EV2 (Diagnóstico), EV5 (Proyecto), EV6 (Prueba) | Cuádruple |
| **1.b** | Tipos de redes (PAN, LAN, CAN, MAN, WAN) | EV3 (Actividades), EV5 (Proyecto), EV6 (Prueba) | Triple |
| **1.c** | Elementos de red y su función (Switch, Router, AP, NIC) | EV1 (Packet Tracer), EV2 (Diagnóstico), EV5 (Proyecto), EV6 (Prueba) | Cuádruple |
| **1.d** | Medios de transmisión (cobre, fibra, inalámbrico) | EV3 (Fichas técnicas), EV5 (Proyecto), EV6 (Prueba) | Triple |
| **1.e** | Reconocimiento e interpretación del mapa físico | EV4 (Plano), EV5 (Proyecto), EV6 (Prueba) | Triple |
| **1.f** | Aplicaciones informáticas para representar el mapa físico | EV4 (Draw.io/Excalidraw), EV5 (Plano integrado del proyecto) | Doble |
| **1.g** | Topologías de red físicas y lógicas | EV3 (Topologías), EV5 (Proyecto), EV6 (Prueba) | Triple |
| **1.h** | Estructuras alternativas y justificación técnica | EV3 (Caso práctico), EV5 (Memoria técnica), EV6 (Defensa) | Triple |

---

## 3. Registro Observacional Transversal (Columna Auxiliar RA6)

En Alexia se puede crear opcionalmente una columna de tipo formativo/cualitativo o registro diario:
* **Código:** `OBS_RA6_T1`
* **Nombre:** Observación Aula / Taller (PRL y Profesionalidad)
* **Tipo:** Lista de control (Apto / En proceso) o valoración 1-10.
* **Ítems registrados:**
  1. Orden y limpieza en el puesto informático.
  2. Apagado correcto de equipos y ordenación del cableado de red.
  3. Cuidado y uso responsable del hardware de red.
  4. Respeto a las normas de seguridad del laboratorio.
* **Destino:** Se acumula para la evaluación formal de la SdA4 (RA6).

---

## 4. Fórmula de Cálculo en Alexia para la Nota de la SdA1

```text
Nota_SdA1 = (S1_EV1 * 0.15) + (S1_EV2 * 0.15) + (S1_EV3 * 0.10) + (S1_EV4 * 0.10) + (S1_EV5 * 0.25) + (S1_EV6 * 0.25)
```
*(Todas las notas intermedias y la final se expresan en escala 0 a 10 con dos decimales).*

---

## 5. Parámetros de Recuperación en Alexia

Si un alumno realiza la segunda oportunidad de alguna evidencia o la prueba de recuperación general de la SdA:
- **Columna opcional de recuperación:** `S1_REC_RA1` (Tipo: Numérica 0-10).
- **Fórmula con recuperación activa:**
  ```text
  Nota_Final_RA1 = MAX(Nota_SdA1; S1_REC_RA1)
  ```
- **Trazabilidad docente:** Si se actualiza directamente sobre la columna original (ej. `S1_EV6`), se anota en el campo *Observaciones del alumno* la fecha de la prueba de recuperación y la calificación previa para mantener el histórico. Consulte [`Protocolo_Recuperacion_SdA1_Redes_Locales.md`](Protocolo_Recuperacion_SdA1_Redes_Locales.md).

