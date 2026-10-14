# Prueba Práctica Individual de Demostración (EV6)
## Situación de Aprendizaje 1: ¿Cómo se comunican los equipos de una red?
**Módulo:** Redes Locales (0225) · 1.º SMR · Curso 2026-2027  
**Criterios de Evaluación evaluados:** RA1.a, RA1.b, RA1.c, RA1.d, RA1.e, RA1.f, RA1.g, RA1.h (Garantía de Autoría y Dominio Técnico)  
**Peso en la calificación de la SdA1:** 25 % (Columna Alexia: `S1_EV6`)  
**Duración:** 55 minutos · **Condiciones:** Individual, aula de ordenadores, sin acceso a Internet, sin apuntes.

---

## 1. Datos del Alumno y Control de Convocatoria
- **Apellidos y Nombre:** `____________________________________________________________`
- **Puesto informático nº:** `______` · **Fecha:** `17/11/2026` · **Grupo:** `[ ] A  [ ] B`
- **Archivo entregado en local/pendrive:** `EV6_Apellido_Nombre.pkt`

---

## 2. Escenario Técnico: "Conexión de la Nueva Sucursal Norte"
Una empresa de servicios informáticos abre una pequeña sucursal con dos departamentos: **Atención al Cliente** y **Administración**. Debes poner en marcha la red de área local en Cisco Packet Tracer desde cero, interconectar los equipos, asignar direccionamiento estático y resolver un fallo de conectividad introducido por el instalador previo.

### Topología Requerida:
```
 [ PC-Atencion1 ] ──┐
                    ├── [ Switch-Central (2960) ] ── [ Server-Datos ]
 [ PC-Atencion2 ] ──┘         │
                              └── [ PC-Admin ]
```

---

## 3. Tareas a Realizar (Puntuación sobre 10 puntos)

### Tarea 1: Despliegue Físico y Topología (2,5 puntos) · *CE 1.c, 1.g*
1. Añade en Packet Tracer:
   - 1 Switch Cisco Catalyst 2960 (`Switch-Central`).
   - 2 PCs para Atención (`PC-Atencion1` y `PC-Atencion2`).
   - 1 PC para Administración (`PC-Admin`).
   - 1 Servidor (`Server-Datos`).
2. Conecta cada dispositivo al switch utilizando cable directo de cobre (`Copper Straight-Through`) en los puertos `FastEthernet0/1` a `FastEthernet0/4`.
3. Todos los enlaces físicos deben mostrar LED verde de enlace operativo (`Link Up`).

### Tarea 2: Plan de Direccionamiento IPv4 (3,5 puntos) · *CE 1.a, RA4*
Configura manualmente las interfaces de red según la siguiente tabla (Red: `192.168.10.0/24`):

| Dispositivo | Interfaz | Dirección IP | Máscara de Subred | Puerta de Enlace (Gateway) |
|---|---|---|---|---|
| `PC-Atencion1` | FastEthernet0 | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` |
| `PC-Atencion2` | FastEthernet0 | `192.168.10.12` | `255.255.255.0` | `192.168.10.1` |
| `PC-Admin` | FastEthernet0 | `192.168.10.20` | `255.255.255.0` | `192.168.10.1` |
| `Server-Datos` | FastEthernet0 | `192.168.10.100`| `255.255.255.0` | `192.168.10.1` |

*Comprobación:* Abre la consola de comandos (`Command Prompt`) de `PC-Atencion1` y ejecuta `ping 192.168.10.100`. El resultado debe ser 100% exitoso (0% de pérdida).

### Tarea 3: Resolución de la Avería Inducida (2,0 puntos) · *CE 1.a, 1.c*
El profesor cargará un archivo o modificará un parámetro en tu red simulando una incidencia real (ej. puerto en `shutdown`, máscara de subred incoherente o cable cruzado en lugar de directo).
- **Describe el síntoma detectado:** `________________________________________________`
- **Comando o herramienta utilizada para diagnosticar:** `___________________________`
- **Causa raíz del problema:** `____________________________________________________`
- **Solución aplicada:** `__________________________________________________________`

### Tarea 4: Defensa Técnica Individual (2,0 puntos) · *CE 1.a, 1.b, 1.d, 1.h*
El profesor se acercará a tu puesto durante la prueba y te formulará **2 preguntas técnicas breves** de control de autoría:
1. *Pregunta 1 (Capa de enlace vs. Red):* Al enviar un ping de `PC-Atencion1` a `Server-Datos`, ¿qué dispositivo de la red examina la dirección MAC y cuál examinaría la IP si saliéramos a Internet?
   - *Respuesta del alumno:* `______________________________________________________`
2. *Pregunta 2 (Medio y topología):* ¿Por qué esta red utiliza topología en estrella física y qué pasaría con `PC-Admin` si se corta el cable de `PC-Atencion1`?
   - *Respuesta del alumno:* `______________________________________________________`

---

## 4. Hoja de Calificación Rápida Docente (Escala 0 a 10)

| Criterio Evaluado | Puntos Máximos | Puntos Obtenidos | Observaciones |
|---|:---:|:---:|---|
| **1. Montaje físico y puertos correctos** | 2,5 | | |
| **2. Configuración IP y verificación ping** | 3,5 | | |
| **3. Diagnóstico y resolución de avería** | 2,0 | | |
| **4. Defensa oral y control de autoría** | 2,0 | | |
| **CALIFICACIÓN FINAL (EV6):** | **10,0** | | |

*Firma del Alumno:* `________________________` · *Firma del Docente:* `________________________`
