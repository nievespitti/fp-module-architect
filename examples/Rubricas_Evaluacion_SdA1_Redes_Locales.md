# Banco de Rúbricas e Instrumentos de Evaluación
## Situación de Aprendizaje 1: ¿Cómo se comunican los equipos de una red?
**Módulo:** Redes Locales (0225) · 1.º SMR · Curso 2026-2027  
**Resultado de Aprendizaje Principal:** RA1 (Estructura de redes locales)  
**RAs Complementarios:** Anticipación RA4 (Configuración IP) y RA6 (Seguridad y profesionalidad)

---

## 1. Escala de Desempeño Estándar (LOMLOE - 4 Niveles)

| Nivel | Rango Numérico | Denominación | Descriptor General de Desempeño |
|:---:|:---:|---|---|
| **Nivel 4** | **10 - 9** | Excelente / Sobresaliente | Dominio técnico pleno, autonomía total, justificación argumentada con vocabulario profesional y anticipación de problemas. |
| **Nivel 3** | **8 - 7** | Bueno / Notable | Cumple todos los requisitos funcionales con autonomía habitual; imprecisiones menores de rotulación o detalle que no afectan a la red. |
| **Nivel 2** | **6 - 5** | Básico / Suficiente | Red o tarea funcional con ayuda o supervisión docente puntual; cumple los estándares mínimos exigibles para el nivel de 1º SMR. |
| **Nivel 1** | **4 - 0** | Insuficiente | No operativo, errores graves de direccionamiento o concepto, falta de entrega o incapacidad de explicar lo realizado. |

---

## 2. Rúbricas Analíticas por Evidencia (Alexia EV1 a EV6)

### Rúbrica EV1 · Prácticas en Cisco Packet Tracer (Peso en SdA: 15 %)
**Criterios de Evaluación vinculados:** RA1.a, RA1.c (anticipación RA4)  
**Evidencia:** Archivo `.pkt` funcional (Actividades 2 y 5) + comprobación de simulación.

| Indicador | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Topología y cableado físico (CE 1.c)** *(25 %)* | Selección perfecta de dispositivos (PC, Switch) y tipo de cable directo/cruzado adecuado; puertos etiquetados y ordenados. | Topología correcta; cableado adecuado pero falta rotulación de puertos o nombres de equipos por defecto. | Topología operativa pero caótica visualmente o con selección de puertos no optimizada. | Dispositivos mal conectados, cables incorrectos o topología incompleta. |
| **Direccionamiento IPv4 (RA4)** *(35 %)* | IPs estáticas dentro del rango `/24` asignadas sin duplicidades; máscaras exactas; coherencia lógica absoluta. | Direccionamiento operativo y funcional con pequeñas incoherencias no críticas (ej. saltos arbitrarios de rango). | Direccionamiento operativo tras una corrección guiada del profesor en el aula. | Máscaras incompatibles, IPs duplicadas o equipos sin configurar. |
| **Verificación de conectividad (CE 1.a)** *(25 %)* | Comando `ping` 100% exitoso bidireccionalmente; interpreta perfectamente la respuesta (TTL, tiempo, bytes). | `ping` exitoso; comprende el resultado aunque duda en el significado técnico de parámetros secundarios. | `ping` funciona tras varios intentos o reinicio de interfaz; comprensión básica del resultado. | `ping` fallido (100% pérdida de paquetes) o desconoce cómo ejecutarlo. |
| **Inspección de tráfico y simulación (CE 1.a)** *(15 %)* | Describe el flujo exacto de las PDUs en Simulation Mode diferenciando claramente trama Ethernet (capa 2) y paquete IP (capa 3). | Explica el recorrido de la PDU en el switch identificando las capas principales con vocabulario adecuado. | Identifica que el paquete viaja por la red pero confunde las funciones de capa 2 y capa 3. | Incapaz de utilizar el modo simulación o explicar el recorrido del paquete. |

---

### Rúbrica EV2 · Diagnóstico y Resolución de Averías (Peso en SdA: 15 %)
**Criterios de Evaluación vinculados:** RA1.a, RA1.c (anticipación RA5)  
**Evidencia:** Ficha de soporte técnico de averías + archivo `.pkt` reparado (Actividad 3).

| Indicador | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Metodología de diagnóstico (CE 1.a)** *(35 %)* | Aplica un orden lógico riguroso (físico → enlace → red); usa `ping`, `ipconfig` y LEDs de estado de forma sistemática. | Procedimiento de diagnóstico correcto; localiza los fallos con rapidez sin saltarse pasos clave. | Diagnóstico poco sistemático (ensayo y error); localiza las averías tras ayuda o pistas del profesor. | Actúa a ciegas modificando parámetros al azar; no sigue ningún método técnico. |
| **Resolución de incidencias (CE 1.c)** *(40 %)* | Identifica y repara el 100% de las 4 averías inducidas (IP, máscara, interfaz switch down, tipo de cable). | Repara 3 de las 4 averías de forma autónoma y eficaz. | Repara al menos 2 averías esenciales garantizando conectividad básica. | No repara las incidencias o crea averías nuevas durante la manipulación. |
| **Documentación del parte técnico** *(25 %)* | Ficha técnica completada con lenguaje profesional impecable: síntoma observado, causa raíz exacta y solución aplicada. | Ficha completa y clara; descripciones correctas aunque vocabulario técnico coloquial en algún punto. | Ficha técnica incompleta pero comprensible en sus soluciones básicas. | Ficha sin rellenar, ilegible o con causas técnicas inventadas. |

---

### Rúbrica EV3 · Fundamentos: Dispositivos, Tipos, Medios y Topologías (Peso: 10 %)
**Criterios de Evaluación vinculados:** RA1.b, RA1.d, RA1.g, RA1.h  
**Evidencia:** Cuaderno técnico / Cuestionario de aplicación práctica (Actividades 4, 6, 7 y 8).

| Indicador | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Dispositivos y funciones (CE 1.c)** *(25 %)* | Distingue con precisión NIC, Hub, Switch, Router y AP; explica la diferencia entre conmutar (MAC) y enrutar (IP). | Conoce la función de cada dispositivo y su uso en red local sin errores graves de concepto. | Identifica los dispositivos pero duda al explicar la función de router frente a switch. | Confunde dispositivos básicos (ej. cree que un switch y un router hacen lo mismo). |
| **Clasificación por alcance (CE 1.b)** *(25 %)* | Clasifica sin vacilar escenarios reales en PAN, LAN, CAN, MAN y WAN justificando distancias y tecnologías. | Clasifica correctamente la mayoría de escenarios con justificación técnica suficiente. | Identifica LAN y WAN correctamente, con dudas en redes intermedias (CAN/MAN). | No distingue entre red local (LAN) e Internet/red amplia (WAN). |
| **Medios de transmisión (CE 1.d)** *(25 %)* | Compara rigurosamente par trenzado (Cat 6/6A), fibra óptica y Wi-Fi; justifica su elección según coste, ancho de banda e interferencias. | Justifica la elección de medio según distancia y velocidad con criterios técnicos razonables. | Conoce las diferencias básicas de velocidad entre cable y Wi-Fi; justificación superficial. | Desconoce las características de los medios o propone medios inviables en el escenario. |
| **Topologías y tolerancia a fallos (CE 1.g, 1.h)** *(25 %)* | Analiza topologías en estrella, árbol, bus y malla; argumenta alternativas y propone redundancias eficaces ante caída de enlaces. | Reconoce topologías físicas y lógicas y argumenta ventajas de la estrella sobre el bus. | Identifica la topología en estrella; justificación de ventajas e inconvenientes muy elemental. | Confunde topologías o es incapaz de proponer una estructura alternativa ante un fallo. |

---

### Rúbrica EV4 · Representación del Mapa Físico de la Red (Peso: 10 %)
**Criterios de Evaluación vinculados:** RA1.e, RA1.f  
**Evidencia:** Plano digitalizado de la red (Draw.io / Excalidraw / PDF) (Actividad 9).

| Indicador | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Simbología y normalización (CE 1.f)** *(30 %)* | Utiliza simbología estándar de telecomunicaciones (racks, rosetas RJ-45, canalizaciones, switches); leyenda clara y ordenada. | Simbología comprensible y coherente en todo el plano; leyenda completa con elementos identificables. | Simbología no normalizada pero comprensible; leyenda incompleta. | Plano sin leyenda, iconos arbitrarios o incomprensibles para un instalador. |
| **Interpretación y distribución espacial (CE 1.e)** *(40 %)* | Ubicación óptima del rack, tomas de usuario (rosetas) y canalizaciones respetando distancias reales y estética arquitectónica. | Distribución lógica y realista de equipos y tomas en cada departamento o estancia. | Distribución funcional con fallos de trazado (canalizaciones atravesando zonas no permitidas). | Distribución irreal, tomas en lugares inaccesibles o ausencia de trazado físico. |
| **Diferenciación mapa físico vs. lógico (CE 1.e)** *(30 %)* | Distingue nítidamente el mapa físico (canalizaciones, armarios, tomas) del mapa lógico (redes IP, nombres de host). | Plano centrado en lo físico con referencias lógicas bien integradas sin sobrecargar el dibujo. | Mezcla elementos físicos y lógicos en un único dibujo generando cierta confusión visual. | No distingue un esquema lógico de un plano de planta de instalación física. |

---

### Rúbrica EV5 · Proyecto Final: Red de Pequeña Empresa (Peso: 25 %)
**Criterios de Evaluación vinculados:** RA1.a a RA1.h (Integrador global)  
**Evidencia:** Memoria técnica resumida + Plano integrado + Archivo `.pkt` funcional (Actividad 10).

| Criterio | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Diseño y dimensionamiento (CE 1.c, 1.d, 1.g)** *(25 %)* | Propuesta técnica impecable para la pyme (puestos fijos, Wi-Fi, impresora); previsión de crecimiento futuro y costes razonados. | Diseño completo que cubre todos los puestos solicitados con equipamiento adecuado. | Red suficiente para operar en el momento actual, sin previsión de ampliación. | Faltan puestos de trabajo, equipamiento insuficiente o sobredimensionado sin criterio. |
| **Simulación Packet Tracer (CE 1.a, 1.c, RA4)** *(35 %)* | Archivo `.pkt` 100% operativo; etiquetas informativas; direccionamiento IP riguroso; pruebas de ping exitosas entre todos los nodos. | Maqueta `.pkt` funcional en todos sus departamentos; pruebas exitosas con errores cosméticos de etiquetado. | Maqueta operativa en la mayoría de equipos; requiere ajustes menores en puerta de enlace o DNS. | Red no operativa en Packet Tracer; fallos de direccionamiento masivos o enlaces en rojo. |
| **Integración con plano físico (CE 1.e, 1.f)** *(20 %)* | Correspondencia matemática exacta entre los equipos del archivo `.pkt` y los símbolos y canalizaciones del plano arquitectónico. | Coherencia clara entre plano y simulación, con discrepancias menores de numeración de tomas. | Plano y maqueta guardan relación general pero difieren en la cantidad de puestos o ubicaciones. | El plano y la simulación representan dos redes distintas sin conexión. |
| **Memoria técnica y defensa (CE 1.h)** *(20 %)* | Memoria ejecutiva limpia (máximo 4 págs); tabla BOM de materiales detallada; argumentación técnica sólida ante preguntas del profesor. | Memoria técnica bien estructurada con tabla de direccionamiento y listado de dispositivos correcto. | Memoria técnica básica con carencias de formato o justificaciones técnicas muy breves. | Memoria incompleta, copiada literalmente o incapaz de defender las decisiones técnicas tomadas. |

---

### Rúbrica EV6 · Prueba Práctica Individual de Demostración (Peso: 25 %)
**Criterios de Evaluación vinculados:** RA1.a a RA1.h (Garantía de autoría)  
**Evidencia:** Prueba práctica individual en aula (55 min) en Packet Tracer + preguntas de control (Actividad 11).

| Dimensión | Nivel 4: Excelente (10 - 9) | Nivel 3: Bueno (8 - 7) | Nivel 2: Suficiente (6 - 5) | Nivel 1: Insuficiente (4 - 0) |
|---|---|---|---|---|
| **Montaje y conexión autónoma** *(30 %)* | Conecta la topología de examen en menos de 15 minutos sin consultar apuntes ni dudar en interfaces. | Monta la topología correctamente en tiempo adecuado con autonomía habitual. | Completa el montaje apurando el tiempo límite fijado para la prueba. | No logra montar la topología solicitada en el tiempo asignado. |
| **Configuración y conectividad IP** *(40 %)* | Configura direcciones, máscaras y puertas de enlace sin un solo fallo; verifica conectividad con `ping` al primer intento. | Direccionamiento correcto; resuelve con rapidez algún error tipográfico cometido durante la prueba. | Consigue conectividad parcial o tras subsanar errores evidentes señalados en la pauta. | Sin conectividad; configuraciones erróneas que impiden la comunicación en la red. |
| **Resolución de reto / avería inducida** *(15 %)* | Localiza y repara la avería sorpresa del examen en menos de 5 minutos explicando el porqué. | Localiza y subsana el problema de forma autónoma con procedimiento correcto. | Corrige la incidencia con lentitud o tras varios intentos infructuosos. | No detecta el fallo inducido en el escenario de examen. |
| **Defensa oral y preguntas de control** *(15 %)* | Responde con soltura y precisión profesional a las 2 preguntas formuladas por el profesor sobre el flujo de paquetes. | Responde correctamente con conceptos claros demostrando autoría indudable de su trabajo. | Respuesta titubeante o incompleta, pero demuestra que comprende lo que ha hecho. | Incapaz de responder o contradice las configuraciones presentes en su propio examen. |

---

## 3. Instrumento de Autoevaluación del Alumnado (Metaaprendizaje LOMLOE)

*Instrucciones para el alumno:* Rellena esta ficha al finalizar la SdA1 antes de la entrega del proyecto final. Valora tu nivel de 1 a 4 y añade una reflexión honesta.

| Indicador de Autoevaluación | 1 (En inicio) | 2 (En proceso) | 3 (Conseguido) | 4 (Dominado) | ¿Cómo lo demuestro? (Evidencia propia) |
|---|:---:|:---:|:---:|:---:|---|
| Sé explicar qué le ocurre a un paquete de datos desde que sale de un PC hasta que llega a otro. | | | | | |
| Configuro direcciones IPv4 y máscaras de red en Packet Tracer sin cometer errores de solapamiento. | | | | | |
| Si una red no responde al `ping`, sé qué comandos usar para encontrar el fallo de forma ordenada. | | | | | |
| Sé justificar cuándo conviene instalar fibra óptica, cable de cobre Cat 6 o red Wi-Fi en una empresa. | | | | | |
| He utilizado la Inteligencia Artificial para entender conceptos difíciles y no solo para copiar respuestas. | | | | | |
| He mantenido mi puesto de trabajo del aula ordenado y he cuidado el material informático. | | | | | |

*Reflexión personal del alumno (máximo 4 líneas):*  
*¿Cuál ha sido la mayor dificultad técnica que has superado en esta SdA y qué harías diferente en el próximo proyecto?*  
`__________________________________________________________________________________________________`

---

## 4. Instrumento de Coevaluación entre Pares (Revisión de Proyecto Pyme)

*Instrucciones:* Cada alumno/pareja revisa el proyecto de otro compañero antes de la entrega definitiva y completa esta rúbrica de revisión técnica entre iguales.

**Proyecto evaluado de:** `____________________________________`  
**Evaluador:** `_______________________________________________`

| Aspecto Técnico Auditado | Sí (2 pts) | Parcial (1 pt) | No (0 pts) | Observaciones de mejora constructiva |
|---|:---:|:---:|:---:|---|
| **1. Conectividad:** Al abrir su archivo `.pkt`, ¿hacen `ping` todos los equipos entre sí? | | | | |
| **2. Direccionamiento:** ¿Tiene una tabla clara con IPs, máscaras y puertas de enlace? | | | | |
| **3. Plano:** ¿El plano digital coincide exactamente con los equipos que hay en Packet Tracer? | | | | |
| **4. Justificación:** ¿La memoria explica por qué eligió esa topología y ese tipo de cable? | | | | |
| **5. Presentación:** ¿La documentación está ordenada, sin faltas y con aspecto profesional? | | | | |
| **PUNTUACIÓN TOTAL COEVALUACIÓN (sobre 10):** | | | | |

---

## 5. Lista de Control Observacional: Registro Transversal RA6 (Seguridad y Taller)

*Registro continuo del profesor en aula de informática (acumulativo para la SdA4):*

| Criterio Observable | Indicador de Desempeño Profesional | Cumple (1) | Mejorable (0,5) | No cumple (0) |
|---|---|:---:|:---:|:---:|
| **Orden del puesto (6.h)** | Teclado, ratón y cables recogidos al finalizar la sesión lectiva. | | | |
| **Ergonomía (6.e)** | Altura de pantalla adecuada, postura corporal correcta frente al monitor. | | | |
| **Cuidado del hardware (6.b)** | Manipulación cuidadosa de conectores RJ-45, cables y botones de encendido. | | | |
| **Uso responsable (6.b)** | Cierre de sesión correcto en el sistema operativo y apagado ordenado del PC. | | | |
| **Convivencia y seguridad (6.e)** | Respeta las instrucciones del laboratorio; no consume alimentos ni bebidas en el aula. | | | |
