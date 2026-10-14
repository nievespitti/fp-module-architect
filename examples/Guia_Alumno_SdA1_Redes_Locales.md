# Guía de Trabajo del Alumno · Situación de Aprendizaje 1
## ¿Cómo se comunican los equipos de una red?
**Módulo:** Redes Locales (0225) · 1.º SMR · Curso 2026-2027  
**Duración:** 7-8 semanas (48 horas lectivas)  
**Resultado de Aprendizaje Principal:** RA1 (Estructura de redes locales cableadas)  
**Resultados Complementarios:** RA4 (Configuración inicial IP) y RA6 (Seguridad, orden y profesionalidad)

---

## 1. El Reto
Una pequeña empresa necesita poner en marcha su red local para que 5 puestos fijos, 2 portátiles y 1 impresora de red compartan archivos y salgan a Internet.  
**Tu misión:** Diseñar la red, representarla en plano digital, simularla y configurarla en Cisco Packet Tracer, verificar conectividad y defender técnicamente tu solución.

---

## 2. Política de Trabajo y Uso de Inteligencia Artificial (IA)
- **Permitido:** Usar IA generativa para resolver dudas conceptuales, depurar comandos o pedir explicaciones técnicas sobre protocolos.
- **No permitido:** Entregar archivos o memorias generados íntegramente por IA sin comprensión propia.
- **Control de autoría:** La calificación final de cada bloque incluye comprobaciones prácticas individuales en el aula de informática. *Debes ser capaz de explicar y reproducir cualquier configuración que entregues.*

---

## 3. Bloques de Trabajo y Entregables (Correspondencia con Alexia)

La evaluación de la SdA1 se compone de **6 Evidencias Calificables en Alexia** + **1 Registro de Actitud y Seguridad Profesional (RA6)**.  
> *Puedes consultar los criterios detallados de cada nivel de logro en el [Banco de Rúbricas e Instrumentos de la SdA1](Rubricas_Evaluacion_SdA1_Redes_Locales.md).*

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CALIFICACIÓN SdA1 (100 %)                            │
├────────────────────────────────────────────────────────────────────────┤
│ EV1: Prácticas Packet Tracer (15 %)        -> CE 1.a, 1.c (anticipa 4) │
│ EV2: Diagnóstico y Resolución (15 %)       -> CE 1.a, 1.c (anticipa 5) │
│ EV3: Tipos, Medios y Topologías (10 %)     -> CE 1.b, 1.d, 1.g, 1.h    │
│ EV4: Representación Mapa Físico (10 %)     -> CE 1.e, 1.f              │
│ EV5: Proyecto Final Pequeña Empresa (25 %) -> CE 1.a - 1.h             │
│ EV6: Prueba Práctica Individual (25 %)     -> CE 1.a - 1.h             │
├────────────────────────────────────────────────────────────────────────┤
│ Transversal: Registro Profesional RA6      -> Acumulativo taller/aula  │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Evidencia 1 (EV1) · Prácticas Packet Tracer
* **Peso en Alexia:** 15 %
* **Criterios evaluados:** RA1.a, RA1.c (anticipación RA4)
* **Actividades incluidas:**
  - **Actividad 2:** Mi primera red (`PC0` — `Switch` — `PC1`). Cableado directo, configuración IPv4 estática (`192.168.1.0/24`) y verificación con comando `ping`.
  - **Actividad 5:** Análisis del tráfico TCP/IP en *Simulation Mode*. Inspección de PDUs (capa física, enlace y red) durante el envío de paquetes ICMP/ARP.
* **Entregable:**
  - Archivo `.pkt` funcional en Moodle: `SdA1_EV1_Apellido_Nombre.pkt`.
* **Rúbrica de corrección (0-10):**
  - **10 - 9:** Topología correcta, direccionamiento coherente sin solapamientos, ping bidireccional exitoso y simulación explicada correctamente.
  - **8 - 7:** Red funcional con errores menores en etiquetas o descripción de capas.
  - **6 - 5:** Conectividad parcial conseguida tras corrección guiada.
  - **4 - 0:** Sin conectividad, direccionamiento incorrecto o archivo no entregado.

---

### Evidencia 2 (EV2) · Diagnóstico y Resolución de Errores de Red
* **Peso en Alexia:** 15 %
* **Criterios evaluados:** RA1.a, RA1.c (anticipación RA5)
* **Actividades incluidas:**
  - **Actividad 3:** Resolución del reto *"¿Por qué no funciona?"*. Se entrega una topología en Packet Tracer con 4 fallos provocados (IPs en rangos distintos, máscara incorrecta, puerto switch en estado *down*, tipo de cable erróneo).
* **Entregable:**
  - Ficha técnica de diagnóstico completada indicando: síntoma observado, herramienta usada (`ping`, `ipconfig`, LEDs), causa raíz y solución aplicada.
  - Archivo `.pkt` reparado.
* **Rúbrica de corrección (0-10):**
  - **10 - 9:** Identifica y repara el 100 % de las incidencias justificando la causa técnica con vocabulario profesional.
  - **8 - 7:** Repara al menos 3 incidencias con justificación técnica válida.
  - **6 - 5:** Repara incidencias por ensayo y error sin explicar claramente la causa raíz.
  - **4 - 0:** Incidencias no resueltas o falta de diagnóstico sistemático.

---

### Evidencia 3 (EV3) · Fundamentos: Dispositivos, Tipos, Medios y Topologías
* **Peso en Alexia:** 10 %
* **Criterios evaluados:** RA1.b, RA1.d, RA1.g, RA1.h
* **Actividades incluidas:**
  - **Actividad 4:** Matriz de dispositivos: NIC, hub vs. switch, router, punto de acceso (AP). Función, capa de trabajo y caso de uso.
  - **Actividad 6:** Clasificación de redes según alcance (PAN, LAN, CAN, MAN, WAN).
  - **Actividad 7:** Ficha de medios de transmisión: par trenzado (Cat 6/6A UTP/FTP), fibra óptica (monomodo/multimodo) y Wi-Fi (2.4/5 GHz).
  - **Actividad 8:** Comparativa de topologías físicas y lógicas (estrella, árbol, bus, malla). Justificación de tolerancia a fallos.
* **Entregable:**
  - Cuaderno técnico digital / Cuestionario de aplicación práctica en Moodle.
* **Criterio de calificación (0-10):**
  - Calificación ponderada de las fichas y del cuestionario técnico aplicado.

---

### Evidencia 4 (EV4) · Representación y Plano Digital de la Red
* **Peso en Alexia:** 10 %
* **Criterios evaluados:** RA1.e, RA1.f
* **Actividades incluidas:**
  - **Actividad 9:** Diseño del mapa físico y lógico de una oficina usando software de diagramación digital (Draw.io, Excalidraw o Packet Tracer).
* **Entregable:**
  - Documento PDF/PNG con el plano del centro/oficina que incluya:
    - Ubicación del armario rack y tomas de usuario (RJ-45).
    - Trazado de canalizaciones.
    - Leyenda y simbología estándar de telecomunicaciones.
* **Rúbrica de corrección (0-10):**
  - **10 - 9:** Simbología normalizada, escalas y ubicaciones lógicas, distinción nítida entre mapa físico y lógico, diseño pulcro y legible.
  - **8 - 7:** Plano comprensible con leyenda completa pero fallos menores en rotulación o trazado.
  - **6 - 5:** Esquema básico con deficiencias de escala o simbología no estándar.
  - **4 - 0:** Plano incompleto, confuso o sin datos de infraestructura física.

---

### Evidencia 5 (EV5) · Proyecto Final: Red de Pequeña Empresa
* **Peso en Alexia:** 25 %
* **Criterios evaluados:** RA1.a, RA1.b, RA1.c, RA1.d, RA1.e, RA1.f, RA1.g, RA1.h
* **Actividades incluidas:**
  - **Actividad 10:** Integración global de los conocimientos adquiridos. El alumno recibe los requerimientos de una pyme (departamentos, número de puestos, conexión a Internet, impresora compartida y zona Wi-Fi para clientes).
* **Entregables obligatorios:**
  1. **Memoria técnica resumida (máximo 4 páginas):**
     - Justificación de la topología elegida y medios de transmisión seleccionados.
     - Listado de equipamiento (BOM - Bill of Materials): modelo/tipo de switches, router, AP, tomas y cableado.
     - Tabla de direccionamiento IP (dispositivo, interfaz, IP, máscara, puerta de enlace).
  2. **Plano de red digitalizado (EV4 integrado).**
  3. **Maqueta funcional en Packet Tracer (`.pkt`):**
     - Todos los equipos configurados y operativos.
     - Pruebas de conectividad demostradas (capturas o tabla de pings).
* **Rúbrica de corrección del proyecto (0-10):**
  - **Memoria y justificación técnica (30 %):** Razona adecuadamente las decisiones tomadas en base a costes, rendimiento y escalabilidad.
  - **Simulación en Packet Tracer (40 %):** Estructura organizada, etiquetas claras, conectividad 100 % verificada en todos los departamentos.
  - **Plano y documentación física (20 %):** Correspondencia exacta entre la simulación y el plano arquitectónico.
  - **Calidad de presentación y formato (10 %):** Ortografía, pulcritud y estructura formal de documento técnico.

---

### Evidencia 6 (EV6) · Prueba Práctica Individual de Demostración
* **Peso en Alexia:** 25 %
* **Criterios evaluados:** RA1.a a RA1.h (verificación individual de dominio)
* **Actividades incluidas:**
  - **Actividad 11:** Prueba práctica individual en el aula de ordenadores sin conexión a Internet y sin apuntes (1 sesión de 55 minutos).
  - El alumno recibe un escenario nuevo en Packet Tracer y debe:
    1. Interconectar 3 redes locales mediante switch/router.
    2. Asignar direccionamiento IP correcto según el enunciado.
    3. Resolver 1 fallo de configuración inducido en el escenario.
    4. Responder por escrito/oralmente a 2 preguntas técnicas del profesor sobre el flujo de paquetes o la función de los dispositivos.
* **Calificación (0-10):**
  - Corrección directa del archivo `.pkt` generado durante la prueba y de las preguntas técnicas de justificación.

---

## 4. Registro Transversal RA6 (Desempeño Profesional y Seguridad)
Durante todas las sesiones de la SdA1 se registrará la conducta técnica en el taller/aula:
* Orden y limpieza del puesto de trabajo (cables recogidos, equipos apagados al terminar).
* Postura ergonómica frente al ordenador.
* Cuidado del material informático y herramientas de red.
* Cumplimiento estricto de las normas de convivencia y seguridad del aula.
*(Estas notas parciales alimentarán la calificación de la SdA4 específica de Prevención de Riesgos Laborales).*

---

## 5. Protocolo de Recuperación y Segunda Oportunidad
Si no superas alguna evidencia (nota inferior a 5,00), tienes derecho a una **segunda oportunidad selectiva**:
- **No repites lo que ya tienes aprobado:** Solo recuperas la evidencia o criterios no alcanzados.
- **Evidencias prácticas (EV1 a EV5):** Dispondrás de un plazo de 5 días lectivos para subsanar errores en Packet Tracer, corregir planos o reentregar el proyecto con feedback docente.
- **Prueba individual (EV6):** Se convocará una nueva prueba práctica individual presencial en la sesión 29 (19 de noviembre de 2026).
- **Conserva tu esfuerzo:** La nota obtenida en la recuperación sustituirá a la calificación anterior en Alexia. Consulta el documento completo: [`Protocolo_Recuperacion_SdA1_Redes_Locales.md`](Protocolo_Recuperacion_SdA1_Redes_Locales.md).

