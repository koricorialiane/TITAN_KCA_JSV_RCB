# Anexo de cálculos y trazabilidad

## A.1 Parámetros base utilizados

| cell_radius_km | carrier_frequency_mhz | gsm_timeslot_ms |
| --- | --- | --- |
| 3 | 900 | 0.577 |

## A.2 Desarrollo detallado del escenario A

#### Caso 50 km/h

1. Conversión de velocidad: `v = 50 / 3.6 = 13.8889 m/s`.
2. Desviación Doppler máxima: `f_d = v · f_c / c = 13.8889 · 900e6 / 3e8 = 41.6667 Hz`.
3. Tiempo de coherencia: `T_c ≈ 0.423 / f_d = 0.423 / 41.6667 = 0.010152 s = 10.152 ms`.
4. Comparación con el timeslot GSM: `T_c / T_slot = 10.152 / 0.577 = 17.5945`.
Interpretación: el canal se clasifica como **cuasiestatico**. Por tanto, la ráfaga puede considerarse cuasiestática o estable dentro del timeslot, pero la robustez del enlace sigue dependiendo de codificación, entrelazado y margen de diseño.

Mini conclusión parcial: la movilidad extrema incrementa el Doppler y reduce el tiempo de coherencia; sin embargo, con los parámetros base el canal sigue siendo manejable dentro de una ráfaga GSM.

#### Caso 250 km/h

1. Conversión de velocidad: `v = 250 / 3.6 = 69.4444 m/s`.
2. Desviación Doppler máxima: `f_d = v · f_c / c = 69.4444 · 900e6 / 3e8 = 208.3333 Hz`.
3. Tiempo de coherencia: `T_c ≈ 0.423 / f_d = 0.423 / 208.3333 = 0.00203 s = 2.0304 ms`.
4. Comparación con el timeslot GSM: `T_c / T_slot = 2.0304 / 0.577 = 3.5189`.
Interpretación: el canal se clasifica como **estable_con_margen_reducido**. Por tanto, la ráfaga puede considerarse cuasiestática o estable dentro del timeslot, pero la robustez del enlace sigue dependiendo de codificación, entrelazado y margen de diseño.

Mini conclusión parcial: la movilidad extrema incrementa el Doppler y reduce el tiempo de coherencia; sin embargo, con los parámetros base el canal sigue siendo manejable dentro de una ráfaga GSM.

## A.3 Métricas de fading exportadas

| model | doppler_hz | envelope_min | envelope_max | envelope_std | relative_peak_to_peak | speed_kmh | coherence_time_ms | stability_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rayleigh | 41.6667 | 0.00894961 | 3.32166 | 0.586993 | 3.31271 | 50 | 10.152 | cuasiestatico |
| rician | 41.6667 | 0.734056 | 1.25486 | 0.100871 | 0.5208 | 50 | 10.152 | cuasiestatico |
| rayleigh | 208.333 | 0.145474 | 3.0415 | 0.453328 | 2.89602 | 250 | 2.0304 | estable_con_margen_reducido |
| rician | 208.333 | 0.694197 | 1.2311 | 0.105082 | 0.536901 | 250 | 2.0304 | estable_con_margen_reducido |

## A.4 Planificación celular y asignación de ARFCNs

| scenario | cell | cell_radius_km | cluster_size_N | total_carriers | carriers_per_cell | arfcn_range | arfcn_list | reuse_ratio_D_over_R | reuse_distance_km |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B_campamento_base | A | 1.5 | 4 | 24 | 6 | 1-6 | 1, 2, 3, 4, 5, 6 | 3.4641 | 5.19615 |
| B_campamento_base | B | 1.5 | 4 | 24 | 6 | 7-12 | 7, 8, 9, 10, 11, 12 | 3.4641 | 5.19615 |
| B_campamento_base | C | 1.5 | 4 | 24 | 6 | 13-18 | 13, 14, 15, 16, 17, 18 | 3.4641 | 5.19615 |
| B_campamento_base | D | 1.5 | 4 | 24 | 6 | 19-24 | 19, 20, 21, 22, 23, 24 | 3.4641 | 5.19615 |

| cell | arfcn | carrier_role | frequency_hopping_recommended | power_policy | available_timeslots | engineering_note |
| --- | --- | --- | --- | --- | --- | --- |
| A | 1 | BCCH/CCCH control | False | fixed/stable | 8 | BCCH debe ser detectable y estable para camping, sincronización y control. |
| A | 2 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| A | 3 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| A | 4 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| A | 5 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| A | 6 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| B | 7 | BCCH/CCCH control | False | fixed/stable | 8 | BCCH debe ser detectable y estable para camping, sincronización y control. |
| B | 8 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| B | 9 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| B | 10 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| B | 11 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| B | 12 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| C | 13 | BCCH/CCCH control | False | fixed/stable | 8 | BCCH debe ser detectable y estable para camping, sincronización y control. |
| C | 14 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| C | 15 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| C | 16 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| C | 17 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| C | 18 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| D | 19 | BCCH/CCCH control | False | fixed/stable | 8 | BCCH debe ser detectable y estable para camping, sincronización y control. |
| D | 20 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| D | 21 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| D | 22 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| D | 23 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |
| D | 24 | TCH traffic | True | adaptive if supported | 8 | TCH transporta tráfico; puede beneficiarse de hopping y control de potencia. |

## A.5 Instrumentación y checklist RED

| rbw_hz | rbw_khz | noise_figure_db | noise_floor_dbm | delta_vs_100khz_db | measurement_interpretation |
| --- | --- | --- | --- | --- | --- |
| 100000 | 100 | 6 | -118 | 0 | RBW ancho: medida rápida, más ruido integrado. |
| 10000 | 10 | 6 | -128 | -10 | RBW estrecho: menor ruido integrado, barrido más lento. |
| 1000 | 1 | 6 | -138 | -20 | RBW estrecho: menor ruido integrado, barrido más lento. |

- RBW = 100 kHz: `N = -174 + 10 log10(100000) + 6 = -118 dBm`.
- RBW = 10 kHz: `N = -174 + 10 log10(10000) + 6 = -128 dBm`.
- RBW = 1 kHz: `N = -174 + 10 log10(1000) + 6 = -138 dBm`.

| area | evidence | student_task |
| --- | --- | --- |
| Uso eficiente del espectro | planificación ARFCN, clúster N=4, distancia de reutilización y control de co-canal | Justificar que la asignación espectral reduce interferencias y evita solapamientos. |
| Emisiones no deseadas | medida con analizador de espectro y ajuste de RBW | Explicar cómo se distinguirían señales débiles de ruido instrumental. |
| Estabilidad de canal | Doppler, tiempo de coherencia y comparación con timeslot GSM | Defender si el enlace es viable durante la ráfaga en movilidad. |
| Documentación técnica | tablas, gráficas, hipótesis y trazabilidad de cálculos | Incluir ecuaciones, unidades y discusión ingenieril. |

## A.6 Artefactos generados

- `outputs/escenario_a_movilidad.csv` y `outputs/escenario_a_fading_metricas.csv`.
- `outputs/escenario_b_planificacion.csv` y `outputs/escenario_b_canales_logicos.csv`.
- `outputs/certificacion_rbw.csv` y `outputs/certificacion_red_checklist.csv`.
- Trazas `outputs/traza_*.csv` y figuras PNG en `outputs/figures/`.
