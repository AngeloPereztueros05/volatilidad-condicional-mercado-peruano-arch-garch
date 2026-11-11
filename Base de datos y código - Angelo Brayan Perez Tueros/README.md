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
| SMV | SPBLPGPT | S&P/BVL Peru General | Identificada; cobertura histórica pendiente |
| BCRP | PD38026MD | Índice General Bursátil BVL | Correspondencia con índice SMV pendiente |
| BCRP | PD04638PD | Tipo de cambio interbancario, venta | Identificada |
| BCRP | PD12301MD | Tasa de referencia de política monetaria | Identificada |
| FRED / CBOE | VIXCLS | Índice de volatilidad VIX | Método de descarga pendiente |

**Nota:** las coberturas históricas, los procedimientos definitivos de extracción y las unidades de medida se documentarán después de su verificación.

## 6. Estructura del proyecto

- `codigo/`: scripts de extracción, limpieza y análisis.
- `datos crudos/`: archivos originales descargados de las fuentes.
- `datos procesados/`: base integrada y depurada mediante código.
- `salidas/`: tablas, gráficos y resultados del análisis.

## 7. Orden previsto de ejecución

1. `01_extraccion_api.py`
2. `02_scraping_web.py`
3. `03_limpieza_datos.py`
4. `04_analisis.py`

## 8. Entorno de ejecución

- Lenguaje de programación: Python.
- Versión de Python: 3.14.7.
- Gestor de dependencias: pip.
- Entorno virtual: .venv.
- Dependencias: bibliotecas y versiones especificadas en requirements.txt.
- Sistema operativo de desarrollo: Windows.
- Editor de código: Visual Studio Code.


## 9. Reproducibilidad

Los datos crudos se conservarán sin modificaciones. La base de datos procesada será generada mediante la ejecución secuencial de los scripts del proyecto. Para facilitar la reproducción del procedimiento en otros equipos, se utilizará un entorno virtual de Python y las dependencias estarán registradas en el archivo requirements.txt.

- **Fecha de extracción piloto:** 11/11/2026 (VERIFICAR con la bitácora).
- **Fecha de extracción definitiva:** pendiente.
- **Hash SHA-256 de la base procesada:** pendiente de calcular una vez generada la base de datos.
- **Repositorio GitHub:** https://github.com/AngeloPerezTueros05/volatilidad-condicional-mercado-peruano-arch-garch


## 10. Estado del proyecto

Se completó una prueba piloto de extracción histórica mediante el
endpoint de índices de la SMV para enero de 2017. Se realizaron
22 consultas individuales, todas con HTTP 200 y código de respuesta
SMV 0, identificándose el índice SPBLPGPT en las 22 consultas.

La extracción histórica completa para el periodo 2010–2025,
la integración de las fuentes, la limpieza de datos y el análisis
econométrico permanecen pendientes.