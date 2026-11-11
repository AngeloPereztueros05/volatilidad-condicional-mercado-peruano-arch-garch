# Nombres y apellidos: Angelo Brayan Perez Tueros
# Código de matrícula: 2023200389L
# Tema y número del temario: Tema (68) Volatilidad condicional del mercado peruano: modelos ARCH/GARCH
# Fecha de elaboración: 2026-11-11

from pathlib import Path
from datetime import datetime, timedelta
import time
import requests

# CONSTANTES DEL PROYECTO
CODIGO_MATRICULA = "2023200389L"

FECHA_INICIO_PILOTO = "2017-01-01"
FECHA_FIN_PILOTO = "2017-01-31"

CODIGO_INDICE = "SPBLPGPT"
NOMBRE_INDICE = "S&P/BVL Peru General"

URL_BASE = (
    "https://mvnet.smv.gob.pe/"
    "SMV.OData.Api/api/valores/Indices"
)

PAUSA_SOLICITUDES = 1
TIEMPO_ESPERA = 60

USER_AGENT = (
    "ProyectoAcademicoFinanzasI/1.0 "
    "(investigacion educativa)"
)

DIRECTORIO_BASE = Path(__file__).resolve().parent.parent
DIRECTORIO_CRUDO = DIRECTORIO_BASE / "datos crudos"
ARCHIVO_BITACORA = DIRECTORIO_BASE / "log ejecucion.txt"


def preparar_directorios():
    """Crea la carpeta de datos crudos si no existe."""
    DIRECTORIO_CRUDO.mkdir(parents=True, exist_ok=True)


def convertir_fecha(fecha):
    """Convierte una fecha al formato requerido por la API."""
    return datetime.strptime(fecha, "%d/%m/%Y")

def generar_fechas_piloto():
    """Genera los días de lunes a viernes del periodo piloto."""
    fecha_inicio = datetime.strptime(
        FECHA_INICIO_PILOTO, "%Y-%m-%d"
    )
    fecha_fin = datetime.strptime(
        FECHA_FIN_PILOTO, "%Y-%m-%d"
    )

    fechas = []
    fecha_actual = fecha_inicio

    while fecha_actual <= fecha_fin:
        if fecha_actual.weekday() < 5:
            fechas.append(
                fecha_actual.strftime("%d/%m/%Y")
            )

        fecha_actual += timedelta(days=1)

    return fechas

def generar_nombre_archivo(fecha):
    """Genera un nombre único para conservar la respuesta original."""
    fecha_nombre = convertir_fecha(fecha).strftime("%Y%m%d")
    marca_tiempo = datetime.now().strftime("%H%M%S_%f")

    nombre = (
        f"datos_crudos_smv_indices_{fecha_nombre}_"
        f"{CODIGO_MATRICULA}_{marca_tiempo}.json"
    )

    return DIRECTORIO_CRUDO / nombre


def registrar_bitacora(datos):
    """Registra el resultado de cada consulta."""
    try:
        with ARCHIVO_BITACORA.open("a", encoding="utf-8") as archivo:
            archivo.write("\n\nREGISTRO DE EXTRACCIÓN SMV\n")
            archivo.write("==========================\n")
            archivo.write(f"Fecha y hora: {datos['fecha_hora']}\n")
            archivo.write(f"Fecha consultada: {datos['fecha_consultada']}\n")
            archivo.write(f"Endpoint: {datos['url']}\n")
            archivo.write(f"Código HTTP: {datos['http']}\n")
            archivo.write(f"Código SMV: {datos['codigo_smv']}\n")
            archivo.write(f"Estado: {datos['estado']}\n")
            archivo.write(f"Índice encontrado: {datos['indice']}\n")
            archivo.write(f"Observaciones: {datos['observaciones']}\n")

        return True

    except OSError as error:
        print(f"Error al escribir la bitácora: {error}")
        return False


def consultar_fecha(fecha):
    """Consulta una fecha, conserva el JSON y busca el índice objetivo."""
    fecha_hora = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    resultado = {
        "fecha_hora": fecha_hora,
        "fecha_consultada": fecha,
        "url": URL_BASE,
        "http": "Sin respuesta",
        "codigo_smv": "Sin respuesta",
        "estado": "ERROR",
        "indice": "No encontrado",
        "observaciones": "",
    }

    parametros = {"sFechaIndice": fecha}
    encabezados = {"User-Agent": USER_AGENT}

    try:
        respuesta = requests.get(
            URL_BASE,
            params=parametros,
            headers=encabezados,
            timeout=TIEMPO_ESPERA,
        )

        resultado["url"] = respuesta.url
        resultado["http"] = respuesta.status_code

        respuesta.raise_for_status()

        datos_json = respuesta.json()

        if not isinstance(datos_json, dict):
            raise ValueError("La respuesta no tiene estructura JSON válida.")

        # Conservar la respuesta original sin modificarla.
        ruta_archivo = generar_nombre_archivo(fecha)
        ruta_archivo.write_bytes(respuesta.content)

        resultado["codigo_smv"] = datos_json.get(
            "ResponseCode", "No informado"
        )

        registros = datos_json.get("Resultado")

        if str(resultado["codigo_smv"]) != "0":
            resultado["estado"] = "ERROR"
            resultado["observaciones"] = (
                f"Respuesta SMV no exitosa: "
                f"{datos_json.get('Message', 'Sin mensaje')}"
            )

        elif registros is None:
            resultado["estado"] = "SIN_DATOS"
            resultado["observaciones"] = (
                f"Resultado nulo. Código SMV: "
                f"{resultado['codigo_smv']}. "
                f"Mensaje: {datos_json.get('Message', 'No informado')}"
            )

        elif not isinstance(registros, list):
            raise ValueError(
                "El campo Resultado no contiene una lista."
            )

        elif not registros:
            resultado["estado"] = "SIN_DATOS"
            resultado["observaciones"] = (
                "La consulta fue válida, pero no devolvió registros."
            )

        else:
            if not all(
                isinstance(registro, dict) for registro in registros
            ):
                raise ValueError(
                    "Se encontró un registro con estructura inválida."
                )

            indices = [
                registro
                for registro in registros
                if registro.get("Tipo") == CODIGO_INDICE
            ]

            if indices:
                resultado["estado"] = "EXITO"
                resultado["indice"] = CODIGO_INDICE

                for indice in indices:
                    print(
                        f"  Índice: {indice.get('Indice')} | "
                        f"Último valor: {indice.get('ultimo')}"
                    )

                resultado["observaciones"] = (
                    f"Se encontraron {len(indices)} registros "
                    f"del índice objetivo."
                )

            else:
                resultado["estado"] = "SIN_INDICE"
                resultado["observaciones"] = (
                    "La respuesta contiene registros, pero no aparece "
                    f"el índice {CODIGO_INDICE}."
                )

        resultado["observaciones"] += (
            f" Archivo original: {ruta_archivo.name}"
        )

    except requests.RequestException as error:
        if getattr(error, "response", None) is not None:
            resultado["http"] = error.response.status_code

        resultado["observaciones"] = str(error)
        print(f"Error de conexión: {error}")

    except (ValueError, TypeError, KeyError, OSError) as error:
        resultado["observaciones"] = str(error)
        print(f"Error al procesar la respuesta: {error}")

    registrar_bitacora(resultado)

    print(
        f"Fecha: {fecha} | HTTP: {resultado['http']} | "
        f"Estado: {resultado['estado']}"
    )

    return resultado


def main():
    """Ejecuta la prueba piloto de enero de 2017."""
    preparar_directorios()
    fechas_piloto = generar_fechas_piloto()

    print("=" * 60)
    print("PRUEBA PILOTO DE EXTRACCIÓN HISTÓRICA - API SMV")
    print("=" * 60)
    print(f"Matrícula: {CODIGO_MATRICULA}")
    print(f"Índice objetivo: {CODIGO_INDICE}")
    print(f"Periodo: {FECHA_INICIO_PILOTO} al {FECHA_FIN_PILOTO}")
    print(f"Fechas candidatas: {len(fechas_piloto)}")

    resultados = []

    for posicion, fecha in enumerate(fechas_piloto):
        print(
            f"\nConsulta {posicion + 1} "
            f"de {len(fechas_piloto)}"
        )
        resultados.append(consultar_fecha(fecha))

        if posicion < len(fechas_piloto) - 1:
            time.sleep(PAUSA_SOLICITUDES)

    exitosas = sum(
        resultado["estado"] == "EXITO"
        for resultado in resultados
    )

    sin_datos = sum(
        resultado["estado"] == "SIN_DATOS"
        for resultado in resultados
    )

    sin_indice = sum(
        resultado["estado"] == "SIN_INDICE"
        for resultado in resultados
    )

    errores = sum(
        resultado["estado"] == "ERROR"
        for resultado in resultados
    )

    print("\n" + "=" * 60)
    print("RESUMEN DE LA PRUEBA PILOTO")
    print("=" * 60)
    print(f"Consultas realizadas: {len(resultados)}")
    print(f"Índice encontrado: {exitosas}")
    print(f"Fechas sin datos: {sin_datos}")
    print(f"Fechas sin índice objetivo: {sin_indice}")
    print(f"Errores: {errores}")
    print(f"Bitácora: {ARCHIVO_BITACORA}")


if __name__ == "__main__":
    main()
