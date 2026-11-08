# Diccionario de variables

## 1. Identificación

- **Estudiante:** Angelo Brayan Perez Tueros
- **Matrícula:** 2023200389L
- **Tema:** 68. Volatilidad condicional del mercado peruano: modelos ARCH/GARCH.
- **Periodo de estudio:** 2010-01-01 al 2025-12-31.

## 2. Variables principales

| Nombre de variable | Identificador | Definición | Unidad | Frecuencia | Fuente |
|---|---|---|---|---|---|
| Índice bursátil peruano | SPBVGPT | S&P/BVL Peru General. Valor de cierre identificado en la API de índices. | Puntos de índice | Diaria, por verificar para toda la cobertura | SMV |
| Índice bursátil BCRP | PD38026MD | Índice General Bursátil BVL. | Por verificar | Diaria, por verificar | BCRP |
| Tipo de cambio | PD04638PD | Tipo de cambio interbancario, venta. | Soles por dólar estadounidense, según denominación de la serie | Diaria | BCRP |
| Tasa de referencia | PD12301MD | Tasa de referencia de la política monetaria. | Porcentaje, por verificar | Diaria | BCRP |
| Índice VIX | VIXCLS | Índice de volatilidad VIX. | Puntos del índice | Diaria | FRED / CBOE |

## 3. Variables derivadas

| Variable | Definición | Método de cálculo | Estado |
|---|---|---|---|
| Rendimiento diario | Variación logarítmica del índice bursátil | 100 × [ln(Pt) − ln(Pt-1)] | Pendiente |
| Volatilidad condicional | Varianza condicional estimada del rendimiento | Modelos ARCH/GARCH | Pendiente |
| Volatilidad condicional (desviación estándar) | Raíz cuadrada de la varianza condicional | √ht | Pendiente |

## 4. Identificación de campos de la API SMV

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

El índice objetivo identificado es `SPBVGPT`, correspondiente a S&P/BVL Peru General.

## 5. Consideraciones de tratamiento

1. No modificar los archivos crudos descargados de las fuentes.
2. Verificar las fechas disponibles antes de integrar las series.
3. No completar automáticamente los valores faltantes sin justificación metodológica.
4. Considerar que la tasa de referencia del BCRP puede permanecer constante entre decisiones de política monetaria.
5. Considerar las diferencias entre los calendarios bursátiles de Perú y Estados Unidos.
6. Verificar la correspondencia histórica entre el índice SMV y la serie bursátil del BCRP.

## 6. Pendientes de verificación

- Cobertura histórica 2010–2025 del índice `SPBVGPT`.
- Método de consulta por rangos de fechas de la API de índices SMV.
- Correspondencia entre `SPBVGPT` y `PD38026MD`.
- Unidades y frecuencia definitivas de las series BCRP.
- Método de descarga programática de `VIXCLS`.
- Tratamiento definitivo de fechas no coincidentes y observaciones faltantes.

**Nota:** las variables y definiciones se documentan según la información identificada hasta el momento. Los elementos no confirmados permanecen señalados como pendientes.