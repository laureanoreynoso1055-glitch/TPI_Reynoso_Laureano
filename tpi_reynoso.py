from funciones_tpi import *
def main():
    """Punto de entrada: carga los datos del CSV y muestra el menú."""
    paises = cargar_paises(ARCHIVO_CSV)   # ← acá se carga el CSV, una sola vez al arrancar

#=============================================================================================================
#============MENU PRINCIPAL===============
#=============================================================================================================

    while True:
        
        mostrar_menu()
            
        opcion = input("Elegí una opción: ").strip()
            
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            opcion_buscar(paises)
        elif opcion == "4":
            opcion_filtrar_continente(paises)
        elif opcion == "5":
            opcion_filtrar_poblacion(paises)
        elif opcion == "6":
            opcion_filtrar_superficie(paises)
        elif opcion == "7":
            opcion_ordenar(paises)
        elif opcion == "8":
            opcion_estadisticas(paises)
        elif opcion == "9":
            mostrar_paises(paises)
        elif opcion == "0":
                print("¡Hasta luego!")
                break
        else:
            print("[Error] Opción inválida. Elegí un número del menú.")

# Esto asegura que main() solo se ejecute si corremos este archivo directamente.
if __name__ == "__main__":
    main()
