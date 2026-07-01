"""ESTRUCTURA DE DATOS PRINCIPAL
-----------------------------
- Cada país se representa con un DICCIONARIO:
      {"nombre": str, "poblacion": int, "superficie": int, "continente": str}
- La colección completa de países es una LISTA de esos diccionarios.

Idea general: el CSV es la "base de datos" en disco. Al iniciar, el programa
carga los datos en memoria (una lista). Cada vez que se agrega o actualiza un
país, se vuelve a guardar el CSV para que los cambios queden persistidos.
"""
import csv
import os
CARPETA = os.path.dirname(os.path.abspath(__file__))  # carpeta donde está este .py
ARCHIVO_CSV = os.path.join(CARPETA, "paises.csv")      # carpeta + nombre del archivo


# ==========================================================================
# LECTURA Y ESCRITURA DE CSV
# ==========================================================================

def cargar_paises(nombre_archivo):
    """Lee el archivo CSV y devuelve una lista de diccionarios.

    - Si el archivo no existe, avisa y devuelve una lista vacía.
    - Si una fila tiene un formato inválido (texto donde se espera un número,
      columnas faltantes o campos vacíos), la ignora e informa cuál fue.
    """
    paises = []

    if not os.path.exists(nombre_archivo):
        print(f"[Aviso] no se encontró '{nombre_archivo}' se inicia con una lista vacia.")
        return (paises)
    try:
        with open (nombre_archivo,"r",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            #start=2 por que en la fila 1 esta el encabezado.
            for numero_fila,fila in enumerate (lector, start=2):
                try:
                    pais = {
                        "nombre": fila['nombre'].strip(),
                        "poblacion": int(fila['poblacion']),
                        "superficie": int(fila['superficie']),
                        "continente":  fila['continente'].strip(),
                    }
                        #No se permite campos de texto vacios.
                    if pais["nombre"]== "" or pais["continente"] == "":
                        print(f"[Aviso] fila {numero_fila} ignorada contiene campos vacios.")
                        continue
                    paises.append(pais)
                except(ValueError,KeyError,AttributeError):
                    # ValueError: población/superficie no es un número.
                    # KeyError: falta una columna esperada.
                    print(f"[Aviso] Fila {numero_fila} ignorada: formato invalido.")
        print(f"Se cargaron {len(paises)} paises desde '{nombre_archivo}'. " )
    except OSError:
        print(f"[ERROR] No se pudo abrir el archivo '{nombre_archivo}'.")

    return paises

def guardar_paises(nombre_archivo,paises):
    """
    Guarda la lista completa de paises en el CSV (sobreescribe el contenido).
    Devuelve true si pudo guardar, False si hubo un error de escritura.
    """
    try:
        with open(nombre_archivo,"w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre","poblacion","superficie","continente"]
            escritor = csv.DictWriter (archivo,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except OSError:
        print(f"[Error] no se pudo guardar en '{nombre_archivo}' .")
        return False
#================================================================================================
#FUNCIONES DE VALIDACION DE ENTRADA
#================================================================================================   

def leer_texto_no_vacio(mensaje):
    """Pide un texto al usuario y repeti hasta que NO este vació"""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("El valor no puede quedar vacio intente de nuevo")
    
def leer_entero_positivo(mensaje):
    """Pide un numero >= 0 y repite hasta que la entrada sea valida"""
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            return int(entrada)
    
        print("Ingrese un numero entero valido(sin signos, sin letras)")

def leer_rango(etiqueta):
    """Pide un numero minimo y uno maximo asegurando que el minimo <= máximo"""
    while True:
        minimo = leer_entero_positivo(f"{etiqueta} minimo: ")
        maximo = leer_entero_positivo(f"{etiqueta} maximo: ")
        if minimo <= maximo:
            return minimo, maximo
        print("El mínimo no puede ser mayor que el máximo.Intente de nuevo")

def normalizar(texto):
    """Pasa a minusculas y saca las tildes, para comparar sin importar acentos."""
    texto = texto.lower()
    texto = texto.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return texto


#===========================================================================================================
#=======ALTA Y ACTUALIZACIÓN=============
#===========================================================================================================

def existe_pais(paises,nombre):
    """Devuelve True ya existe un pais con ese nombre(Ignora Mayusculas)"""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False
    
def agregar_pais(paises):
    """Solicita los datos de un pais nuevo y lo agrega a la lista,
    No se permiten campos vacios ni paises duplicados.
    """
    print("\n----AGREGAR PAÍS----")
    nombre = leer_texto_no_vacio("Nombre: ")

    if existe_pais(paises, nombre):
        print(f"Error el pais {nombre} ya existe.No se agrego")
        return
    
    poblacion = leer_entero_positivo("Poblacion: ")
    superficie = leer_entero_positivo("Superficie (km²): ")
    continente = leer_texto_no_vacio("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)
    guardar_paises(ARCHIVO_CSV, paises)
    print(f"[ok] pais '{nombre}' agregado correctamente")

def actualizar_pais(paises):
    """Busca un pais por nombre y busca su actualizacion y su superficie"""
    print("\n----ACTUALIZAR PAÍS----")
    if not paises:
        print("No hay paises cargados.")
        return
    nombre = leer_texto_no_vacio("Nombre de pais a actualizar: ")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Datos actuales -> Población: {pais['poblacion']:,} | "
                  f"Superficie: {pais['superficie']:,} km²")
            pais["poblacion"] = leer_entero_positivo("Nueva población: ")
            pais["superficie"] = leer_entero_positivo("Ingrese la superficie (km²): ")
            guardar_paises(ARCHIVO_CSV,paises)
            print(f"[ok] '{pais['nombre']}' actualizado correctamente")
            return
    
    print(f"[Error] no se encontro el pais '{nombre}'.")

#============================================================================================================
#===================BUSQUEDA==============================
#============================================================================================================

def buscar_paises(paises,texto):
    """Devuelve la lista de paises cuyo nombre tienen 'texto'
    La coincidencia es parcial y no distingue mayúsculas de minúsculas.
    (Si se escribe el nombre completo, también funciona como búsqueda exacta.)
    """
    texto = texto.lower()
    encontrados = []
    for pais in paises:
        if texto in pais["nombre"].lower():
            encontrados.append(pais)
    return encontrados
    

#============================================================================================================
#FILTROS
#============================================================================================================

def filtrar_por_continente(paises, continente):
    """Devuelve los paises de un continente dado (ignora Mayusculas)."""
    continente = normalizar(continente)
    resultado = []
    for pais in paises:
        if normalizar(pais["continente"]) == continente:
            resultado.append(pais)
    return resultado

def filtrar_por_rango_poblacion(paises,minimo,maximo):
    """Devuelve paises cuya población esta entre minimos y maximos (inclusive)"""
    resultado = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)
    return resultado

def filtrar_por_rango_superficie(paises,minimo,maximo):
    """Devuelve paises cuyo rango esta entre minimo y maximo (inclusive)"""
    resultado = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)
    return resultado


# ==========================================================================
# ORDENAMIENTOS
# ==========================================================================


def ordenar_paises(paises, clave, descendente=False):
    """Devuelve una NUEVA lista ordenada por la clave indicada.

    clave: "nombre", "poblacion" o "superficie".
    descendente: False = de menor a mayor / A-Z, True = al revés.
    """
    #para texto ordenamos en minúscula para no separar  mayúsculas de minúsculas.
    return sorted(paises, key=lambda p: p[clave].lower() if clave == "nombre" else p[clave], reverse=descendente)

# ==========================================================================
# ESTADÍSTICAS
# ==========================================================================

def pais_con_mayor_poblacion(paises):
    """Devuelve el pais con mayor población (o none si la lista está vacía)"""
    if not paises:
        return None
    mayor = paises[0]
    for pais in paises[1:]:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
    return mayor

def pais_con_menor_poblacion(paises):
    """Devuelve el pais con menor población o (None si la lista esta vacia)"""
    if not paises:
        return None
    menor = paises[0]
    for pais in paises[1:]:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
    return menor
    
def promedio_poblacion(paises):
    """Calcula el promedio de poblacion de todos los paises"""
    if not paises:
        return 0
    total = 0
    for pais in paises:
        total += pais["poblacion"]
    return total / len(paises)

def promedio_superficie(paises):
    """Calcula el promedio de superficie de todos los paises"""
    if not paises:
        return 0
    total = 0
    for pais in paises:
        total += pais["superficie"]
    return total / len(paises)

def cantidad_por_continente(paises):
    """Devuelve un diccionario {continente: cantidad de países}."""
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo



# ==========================================================================
# PRESENTACIÓN EN PANTALLA
# ==========================================================================

def mostrar_paises(paises):
    """Muestra los paises recibidos en forma de tabla ordenada."""
    if not paises:
        print("No hay paises que mostrar")
        return
    
    print()
    print(f"{"nombre":<20}{"poblacion":<20}{"superficie km²":<20}{"continente":<12}")
    print("-"*65)
    for pais in paises:
        print(f"{pais["nombre"]:<20}{pais["poblacion"]:<20}{pais["superficie"]:<20}{pais["continente"]:<12}")
    print(f"\n Total: {len(paises)} paises. ")  



# ==========================================================================
# OPCIONES DEL MENÚ (cada una arma su flujo y llama a las funciones de arriba)
# ==========================================================================

def opcion_buscar(paises):
    texto = leer_texto_no_vacio("Texto a buscar en el nombre: ")
    resultados = buscar_paises (paises,texto)
    if resultados:
        mostrar_paises(resultados)
    else:
        print(f"No se encontaron países que contengan '{texto}'.")

def opcion_filtrar_continente(paises):
    continente = leer_texto_no_vacio("continente: ")
    resultados = filtrar_por_continente(paises,continente)
    if resultados:
        mostrar_paises(resultados)
    else:
        print(f"No hay paises del continente '{continente}'")

def opcion_filtrar_poblacion(paises):
    minimo,maximo = leer_rango("poblacion")
    resultados = filtrar_por_rango_poblacion(paises,minimo,maximo)
    if resultados:
        mostrar_paises(resultados)
    else:
        print("No hay países en ese rango de población")

def opcion_filtrar_superficie(paises):
    minimo,maximo = leer_rango("superficie")
    resultados = filtrar_por_rango_superficie(paises,minimo,maximo)
    if resultados:
        mostrar_paises(resultados)
    else:
        print("No hay paises en ese rango de superficie.")
    
def opcion_ordenar(paises):
    if not paises:
        print("No hay paises cargados")
        return 

    print("\n ordenar por:")
    print(" 1. nombre")
    print(" 2. poblacion")
    print(" 3. superficie")

    criterio = input("Opcion: ").strip()

    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio not in claves:
        print("[Error] opcion de ordenamiento inválida")
        return
    
    print("Orden")
    print(" 1. Ascendente (menor a mayor / A-Z)")
    print(" 2. Descendente (mayor a menor / Z-A) ")
    sentido = input("Opcion: ").strip()
    if sentido not in ("1", "2"):
        print("[ERROR] Opción de orden inválida")
        return
    descendente = (sentido == "2")
    ordenados = ordenar_paises(paises,claves[criterio],descendente)
    mostrar_paises(ordenados)

def opcion_estadisticas(paises):
    if not paises:
        print("No hay paises cargados para calcular estadísticas")
        return
    mayor = pais_con_mayor_poblacion(paises)
    menor = pais_con_menor_poblacion(paises)
    print("\n ---Estadísticas----")
    print(f"País con MAYOR poblaión: {mayor["nombre"]} ({mayor["poblacion"]:,}hab.)")
    print(f"País con MENOR poblaión: {menor["nombre"]} ({menor["poblacion"]:,}hab.)")
    print(f"Promedio de Población: {promedio_poblacion(paises):,.0f} hab.")
    print(f"Promedio de Superficie: {promedio_superficie(paises):,.0f} km².")
    print("Cantidad de países por Continente")
    for continente , cantidad in cantidad_por_continente(paises).items():
        print(f"- {continente}: {cantidad}")
# ==========================================================================
# --------------------------MENU PRINCIPAL----------------------------------
# ==========================================================================

def mostrar_menu():
    print("\n" + "=" * 50)
    print("        GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 50)
    print(" 1. Agregar país")
    print(" 2. Actualizar país (población y superficie)")
    print(" 3. Buscar país por nombre")
    print(" 4. Filtrar por continente")
    print(" 5. Filtrar por rango de población")
    print(" 6. Filtrar por rango de superficie")
    print(" 7. Ordenar países")
    print(" 8. Mostrar estadísticas")
    print(" 9. Listar todos los países")
    print(" 0. Salir")
    print("=" * 50)
