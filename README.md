# TPI_Reynoso_Laureano
Trabajo Practico Integrador


# Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) — **Programación 1**
Tecnicatura Universitaria en Programación (UTN) — Modalidad a Distancia

> **Integrante:** **[NOMBRE: Reynoso, Laureano]**

---

## Descripción

Aplicación de consola desarrollada en **Python 3** para gestionar información sobre países.
El sistema lee un conjunto de datos desde un archivo **CSV** y, a través de un menú interactivo,
permite agregar y actualizar países, buscarlos, filtrarlos, ordenarlos y obtener estadísticas.

Cada país se describe con cuatro datos: **nombre**, **población**, **superficie** (en km²) y **continente**.
La información se organiza como una **lista de diccionarios** (cada país es un diccionario) y se
mantiene persistida en el archivo `paises.csv`.

## Funcionalidades

- **Agregar** un país (no se permiten campos vacíos ni países duplicados).
- **Actualizar** la población y la superficie de un país existente.
- **Buscar** un país por nombre (coincidencia parcial o exacta, sin distinguir mayúsculas).
- **Filtrar** por continente, por rango de población o por rango de superficie.
- **Ordenar** por nombre, población o superficie, en orden ascendente o descendente.
- **Estadísticas:** país con mayor y menor población, promedio de población y de superficie,
  y cantidad de países por continente.
- **Listar** todos los países cargados.

Incluye validaciones de entrada y manejo básico de errores (datos inválidos, filas mal formadas
en el CSV, búsquedas sin resultados, etc.).

## Requisitos

- **Python 3.x** (no requiere instalar librerías externas; usa solo módulos de la biblioteca estándar).

## Estructura del proyecto

```
.
├── main.py        # Programa principal (menú y todas las funciones)
├── paises.csv     # Dataset base (20 países de los 5 continentes)
└── README.md      # Este archivo
```

## Cómo ejecutar

1. Clonar el repositorio o descargar los archivos en una misma carpeta:

   ```bash
   git clone [COMPLETAR: URL del repositorio]
   cd [COMPLETAR: nombre de la carpeta]
   ```

2. Ejecutar el programa (asegurate de que `main.py` y `paises.csv` estén en la misma carpeta):

   ```bash
   python main.py
   ```

   > En algunos sistemas el comando es `python3 main.py`.

## Formato del archivo CSV

La primera línea es el encabezado y define las columnas. Cada línea siguiente es un país:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

## Ejemplos de entradas y salidas

### Menú principal

```
==================================================
        GESTIÓN DE DATOS DE PAÍSES
==================================================
 1. Agregar país
 2. Actualizar país (población y superficie)
 3. Buscar país por nombre
 4. Filtrar por continente
 5. Filtrar por rango de población
 6. Filtrar por rango de superficie
 7. Ordenar países
 8. Mostrar estadísticas
 9. Listar todos los países
 0. Salir
==================================================
Elegí una opción:
```

### Agregar un país (opción 1)

```
--- Agregar país ---
Nombre: Islandia
Población: 372520
Superficie (km²): 103000
Continente: Europa
[OK] País 'Islandia' agregado correctamente.
```

### Buscar un país por nombre (opción 3)

```
Elegí una opción: 3
Texto a buscar en el nombre: ina

Nombre                    Población    Superficie km²  Continente
-----------------------------------------------------------------
Argentina                45,376,763         2,780,400     América
China                 1,411,778,724         9,596,961        Asia
Filipinas               109,581,078           300,000        Asia
Dinamarca                 5,792,202            43,094      Europa

Total: 4 país(es).
```

### Filtrar por continente (opción 4)

```
Elegí una opción: 4
Continente: Oceanía

Nombre                    Población    Superficie km²  Continente
-----------------------------------------------------------------
Australia                25,687,041         7,692,024     Oceanía
Nueva Zelanda             5,084,300           268,021     Oceanía
Papúa Nueva Guinea        8,947,024           462,840     Oceanía
Fiyi                        896,445            18,274     Oceanía
Islas Salomón               686,884            28,896     Oceanía
Samoa                       198,414             2,842     Oceanía
Vanuatu                     307,145            12,189     Oceanía

Total: 7 país(es).
```

### Mostrar estadísticas (opción 8)

```
--- Estadísticas ---
País con MAYOR población: China (1,411,778,724 hab.)
País con MENOR población: Samoa (198,414 hab.)
Promedio de población:   83,432,919 hab.
Promedio de superficie:  1,332,748 km²
Cantidad de países por continente:
  - América: 18
  - Asia: 19
  - Europa: 22
  - África: 17
  - Oceanía: 7
```

### Manejo de errores (ejemplo)

```
Población: abc
  > Ingresá un número entero válido (sin signos ni letras).
Población: -5
  > Ingresá un número entero válido (sin signos ni letras).
Población: 372520
```

## Enlaces

- **Video demostrativo:** [COMPLETAR: enlace con permisos públicos de visualización]
- **Documentación (PDF):** [COMPLETAR: enlace al PDF, o indicar que está en la raíz del repositorio]
