# Volatilidad condicional del mercado peruano: modelos ARCH/GARCH

## 1. Identificación del proyecto

- **Estudiante:** Angelo Brayan Perez Tueros
- **Código de matrícula:** 2023200389L
- **Curso:** Finanzas I
- **Unidad:** II
- **Tema:** 68. Volatilidad condicional del mercado peruano: modelos ARCH/GARCH.

## 2. Pregunta de investigación

¿En qué medida los modelos de la familia ARCH/GARCH capturan la volatilidad condicional del rendimiento diario del índice bursátil peruano durante 2010–2025, y cómo se relacionan con ella el VIX, el tipo de cambio sol/dólar y la tasa de referencia del BCRP?

## 3. Objetivo general

Modelar la volatilidad condicional del rendimiento diario del índice bursátil peruano y evaluar el papel de factores externos, mediante una base de datos propia construida con API y descarga programática.

## 4. Periodo de estudio

- **Fecha de inicio:** 2010-01-01.
- **Fecha de corte:** 2025-12-31.
- **Frecuencia objetivo:** diaria.

## 5. Fuentes de datos candidatas

| Institución | Serie o identificador | Variable | Estado |
|---|---|---|---|
| SMV | SPBVGPT | S&P/BVL Peru General | Identificada; cobertura histórica pendiente |
| BCRP | PD38026MD | Índice General Bursátil BVL | Correspondencia con índice SMV pendiente |
| BCRP | PD04638PD | Tipo de cambio interbancario, venta | Identificada |
| BCRP | PD12301MD | Tasa de referencia de política monetaria | Identificada |
| FRED / CBOE | VIXCLS | Índice de volatilidad VIX | Método de descarga pendiente |

**Nota:** las coberturas históricas, los procedimientos definitivos de extracción y las unidades de medida se documentarán después de su verificación.

## 6. Estructura del proyecto

- `codigo/`: scripts de extracción, limpieza y análisis.
- `datos_crudos/`: archivos originales descargados de las fuentes.
- `datos_procesados/`: base integrada y depurada mediante código.
- `salidas/`: tablas, gráficos y resultados del análisis.

## 7. Orden previsto de ejecución

1. `01_extraccion_api.py`
2. `02_scraping_web.py`
3. `03_limpieza_datos.py`
4. `04_analisis.py`

## 8. Entorno de ejecución

- Lenguaje: Python.
- Versión de Python: PENDIENTE DE DEFINIR.
- Dependencias: se especificarán en `requirements.txt`.
- Sistema operativo utilizado: Windows.

## 9. Reproducibilidad

Los datos crudos se conservarán sin modificaciones. La base procesada será generada mediante los scripts del proyecto.

- Fecha de extracción: PENDIENTE.
- Hash SHA-256 de la base procesada: PENDIENTE.
- Repositorio GitHub: PENDIENTE.

## 10. Estado del proyecto

Actualmente se encuentra en la fase de validación de fuentes y preparación de la estructura de archivos. La extracción automatizada y el análisis econométrico aún no se han iniciado.