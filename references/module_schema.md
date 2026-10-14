# module.json (fuente única)

```
modulo: {nombre, codigo, curso, centro, anio, horas_nominales}
docente: "..."
horario: [{dia: "Lunes", inicio: "12:10", fin: "13:02", horas: 1}, ...]      # una entrada por sesión semanal
calendario:
  inicio_clases, fin_clases_modulo, fin_curso (ISO yyyy-mm-dd)
  evaluaciones: [{n:1, nombre, fecha}, ...]
  no_lectivos: [{fecha, motivo}]
  periodos_sin_clase: [{inicio, fin, motivo}]     # Navidad, Semana Santa, proyecto intermodular
  hitos: [{fecha, nombre, tipo: EVALUACION|ENTREGA|FESTIVO|FEOE, descripcion}]
  feoe: {inicio, fin, tutorias, tutorias_fechas: [ISO,...]}   # opcional; si hay tutorias_fechas se usan exactamente esas fechas (p. ej. lunes cada 15 días)
dual: {horas, ces: [{ce: "3.d", horas, evidencia_empresa, alternativa_centro}]}   # horas de FEOE dualizadas; aula + dual = nominales
ras: [{n, titulo, peso_ra, transversal: bool, evaluaciones: [1,2],
       ces: [{id, texto (oficial literal), peso (en el RA, suma 100), evalua, evidencia, instrumento}]}]
sdas: [{n, titulo, ra_principal, ras_complementarios: [..], horas, inicio, fin, evaluaciones: [1],
        evidencias: [{id: "EV1", nombre, peso, tipo?: "examen_individual", ces: ["1.a", "1.b"]}],
        sesiones: [{plan, ce?, evidencia?}, ...]}]   # una por sesión real de la SdA, en orden
```

Reglas: Σ peso_ra = 100; Σ peso CE por RA = 100; Σ peso evidencias por SdA = 100; cada CE en ≥1 evidencia; cada SdA con una evidencia tipo examen_individual; ninguna SdA cruza FEOE ni su evaluación.
Un RA transversal aparece en varias SdA (como complementario) y se evalúa en varias evaluaciones.
