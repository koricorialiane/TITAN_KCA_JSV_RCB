# Guía de uso docente

## Objetivo

Este código transforma el reto en una práctica reproducible. No se limita a calcular resultados: obliga al alumno a interpretar la relación entre capa física, canal radio, planificación celular e instrumentación.

## Actividades propuestas

### Actividad 1 — Movilidad y Doppler

El alumno debe ejecutar el escenario A y responder:

- ¿Cuál es el Doppler máximo a 50 km/h y 250 km/h?
- ¿Cómo cambia el tiempo de coherencia?
- ¿Es razonable considerar el canal estable durante un timeslot GSM?
- ¿Qué implicaciones tiene para codificación, entrelazado y robustez del enlace?

### Actividad 2 — Rayleigh frente a Rician

El alumno debe comparar la envolvente normalizada del canal bajo:

- Rayleigh: entorno sin componente dominante de línea de vista.
- Rician: entorno con componente dominante, por ejemplo visión parcial del valle o celda elevada.

### Actividad 3 — Planificación de frecuencias

El alumno debe justificar:

- por qué 24 portadoras con N=4 dan 6 portadoras por celda;
- cómo se reparte BCCH y TCH;
- por qué BCCH no suele saltar en frecuencia y se mantiene estable;
- qué significa D/R = sqrt(3N).

### Actividad 4 — Instrumentación RED/RBW

El alumno debe analizar el suelo de ruido para RBW de 100 kHz, 10 kHz y 1 kHz.

Debe explicar que reducir RBW no aumenta la potencia real de la señal: reduce el ruido integrado por el instrumento, mejora la visibilidad de señales débiles y aumenta el tiempo de barrido.

## Entregables recomendados

- Tabla Doppler/coherencia.
- Gráfica de coherencia frente al timeslot.
- Gráfica de fading Rayleigh/Rician.
- Tabla de ARFCNs y canales lógicos.
- Tabla y gráfica de suelo de ruido.
- Discusión integrada de resultados.

## Artefactos que ya genera el proyecto

- `outputs/informe_resultados.md`: borrador largo del artículo técnico con introducción, estado del arte, metodología, resultados, discusión y referencias.
- `outputs/anexo_calculos.md`: anexo de cálculo paso a paso para justificar unidades, hipótesis y fórmulas.
- `outputs/guion_defensa.md`: esquema breve para presentación oral o defensa.
- `outputs/figures/*.png`: figuras listas para insertar en el PDF final.

## Cómo usar el repositorio con la rúbrica

### Formato y estructura

- Utiliza `outputs/informe_resultados.md` como columna vertebral del trabajo.
- Convierte el Markdown a PDF desde el editor que use el grupo o el docente.
- Mantén portada, índice y anexos como capas externas al informe generado.

### Rigor teórico

- Conserva los apartados de FDMA/TDMA, canales lógicos, fading y RED.
- Añade citas bibliográficas formales si el docente exige un estilo IEEE o APA más estricto.

### Precisión matemática

- Usa `outputs/anexo_calculos.md` para revisar conversiones y resultados antes de cerrar la versión final.
- No cambies unidades a mitad del desarrollo sin dejar la equivalencia escrita.

### Análisis y conclusiones

- Cierra cada sección del informe con una mini conclusión parcial.
- En la discusión final conecta siempre movilidad, reutilización y medida instrumental.

## Recomendación de flujo de trabajo

1. Ejecutar `python -m protocolo_titan.main`.
2. Revisar `outputs/informe_resultados.md` y `outputs/anexo_calculos.md`.
3. Ajustar texto, referencias y estilo visual según la asignatura.
4. Exportar el documento final a PDF.
5. Ensayar la exposición con `outputs/guion_defensa.md`.
