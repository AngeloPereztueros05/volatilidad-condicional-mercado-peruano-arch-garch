# Diccionario de variables

## 1. Identificación

- **Estudiante:** Angelo Brayan Perez Tueros
- **Matrícula:** 2023200389L
- **Tema:** 68. Volatilidad condicional del mercado peruano: modelos ARCH/GARCH.
- **Periodo de estudio:** 2010-01-01 al 2025-12-31.

## 2. Variables principales

| Nombre de variable | Identificador | Definición | Unidad | Frecuencia | Fuente | URL o endpoint | Estado de verificación |
|---|---|---|---|---|---|---|---|
| Índice bursátil peruano | SPBLPGPT | S&P/BVL Peru General. Valor de cierre identificado en la API de índices. | Puntos de índice | Diaria | SMV | https://mvnet.smv.gob.pe/SMV.OData.Api/api/valores/Indices?sFechaIndice=DD/MM/YYYY | Parcial |
| Índice bursátil BCRP | PD38026MD | Índice General Bursátil BVL. | VERIFICAR | Diaria, por verificar | BCRP | https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD38026MD/json/2010-1-1/2025-12-31/esp | Parcial |
| Tipo de cambio | PD04638PD | Tipo de cambio interbancario, venta. | Soles por dólar estadounidense | Diaria | BCRP | https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04638PD/json/2010-1-1/2025-12-31/esp | Parcial |
| Tasa de referencia | PD12301MD | Tasa de referencia de la política monetaria. | Porcentaje | Diaria | BCRP | https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD12301MD/json/2010-1-1/2025-12-31/esp | Parcial |
| Índice VIX | VIXCLS | Índice de volatilidad VIX. | Puntos del índice | Diaria | FRED / CBOE | https://fred.stlouisfed.org/series/VIXCLS | Pendiente |

**Nota:** El estado «Parcial» indica que la serie ha sido identificada, pero aún requiere verificar aspectos como su cobertura histórica, unidades o integración. El estado «Pendiente» indica que todavía no se ha confirmado el procedimiento de descarga y tratamiento de la variable.

## 3. Variables derivadas

| Variable | Definición | Método de cálculo | Estado |
|---|---|---|---|
| Rendimiento diario | Variación logarítmica del índice bursátil | 100 × [ln(Pt) − ln(Pt-1)] | Pendiente |
| Volatilidad condicional | Varianza condicional estimada del rendimiento | Modelos ARCH/GARCH | Pendiente |
| Volatilidad condicional (desviación estándar) | Raíz cuadrada de la varianza condicional | √ht | Pendiente |

## 4. Identificación de campos de la API de índices SMV

| Campo | Significado |
|---|---|
| Fecha | Fecha de consulta del índice |
| Tipo | Nemónico del índice |
| Indice | Denominación del índice |
| Anterior | Cierre del índice en la fecha anterior |
| Ultimo | Cierre del índice en la fecha consultada |
| Variacion | Variación porcentual |
| Apertura | Valor de apertura |
| Maxima | Valor máximo |
| Minima | Valor mínimo |

El índice objetivo identificado es `SPBLPGPT`, correspondiente a S&P/BVL Peru General. En la prueba piloto de enero de 2017, el índice fue identificado en las 22 consultas individuales realizadas, todas con HTTP 200 y código de respuesta SMV 0.

**Nota metodológica:** La identificación del índice `SPBLPGPT` no implica que su cobertura histórica diaria para todo el periodo 2010–2025 esté confirmada. Antes de utilizarlo en el análisis econométrico, se verificará la disponibilidad de observaciones, la continuidad de las fechas y la correspondencia con la serie `PD38026MD` del BCRP. Las diferencias entre ambas fuentes se documentarán sin asumir que representan series idénticas.

## 5. Consideraciones de tratamiento

1. No modificar los archivos crudos descargados de las fuentes.
2. Verificar las fechas disponibles antes de integrar las series.
3. No completar automáticamente los valores faltantes sin justificación metodológica.
4. Considerar que la tasa de referencia del BCRP puede permanecer constante entre decisiones de política monetaria.
5. Considerar las diferencias entre los calendarios bursátiles de Perú y Estados Unidos.
6. Para integrar las series de distinta procedencia, se utilizará una fecha común como clave temporal. Se documentarán las fechas sin observación y las diferencias entre calendarios de negociación, sin completar automáticamente los valores faltantes.
7. Verificar la correspondencia histórica entre el índice SMV y la serie bursátil del BCRP.

## 6. Pendientes de verificación

- Cobertura histórica 2010–2025 del índice `SPBLPGPT`.
- Método de extracción histórica de la API de índices SMV.
- Correspondencia entre `SPBLPGPT` y `PD38026MD`.
- Unidades y frecuencia definitivas de las series BCRP.
- Método de descarga programática de `VIXCLS`.
- Tratamiento de fechas no coincidentes y observaciones faltantes.

**Nota:** las variables y definiciones se documentan según la información identificada hasta el momento. Los elementos no confirmados permanecen señalados como pendientes.