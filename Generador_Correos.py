import os
from typing import List

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("══════════════════════════════════════")
    print("  GENERADOR DE CORREOS/NÚMEROS DE CONTROL")
    print("══════════════════════════════════════")
    print("1. Generar correos completos")
    print("2. Generar solo números de control (formato OR)")
    print("3. Salir")
    print("══════════════════════════════════════")

def cargar_datos(ruta: str) -> List[str]:
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return [linea.strip() for linea in f if linea.strip()]
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ruta}")
        return []
    except Exception as e:
        print(f"Error al leer archivo: {str(e)}")
        return []

def extraer_numeros(datos: List[str]) -> List[str]:
    numeros = []
    for linea in datos:
        for token in linea.split():
            if token.isdigit():
                numeros.append(token)
                break
    return numeros

# Función original para generar correos
def generar_correos(numeros: List[str]) -> List[str]:
    return [f"l{num}@pachuca.tecnm.mx" + " OR" for num in numeros]

# Nueva función para solo números con OR
def generar_numeros_or(numeros: List[str]) -> str:
    return " OR\n".join(numeros) + " OR"  # OR al final del último elemento

def guardar_resultado(contenido: str, ruta_salida: str):
    try:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"✓ Resultados guardados en: {ruta_salida}")
        return True
    except Exception as e:
        print(f"Error al guardar: {str(e)}")
        return False

def procesar_opcion(opcion: int, numeros: List[str]):
    if opcion == 1:
        resultado = "\n".join(generar_correos(numeros))
        nombre_archivo = "correos.txt"
    elif opcion == 2:
        resultado = generar_numeros_or(numeros)
        nombre_archivo = "numeros_control.txt"
    else:
        return False
    
    print("\nResultado generado:")
    print(resultado[:200] + ("..." if len(resultado) > 200 else ""))
    
    ruta = input(f"\nIngrese ruta para guardar (Enter para {nombre_archivo}): ").strip()
    ruta = ruta if ruta else nombre_archivo
    return guardar_resultado(resultado, ruta)

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == '3':
            print("\n¡Hasta luego!")
            break
        
        if opcion not in ('1', '2'):
            input("\nOpción no válida. Presione Enter para continuar...")
            continue
        
        archivo_entrada = input("\nIngrese ruta del archivo de datos: ").strip()
        datos = cargar_datos(archivo_entrada)
        if not datos:
            input("\nPresione Enter para continuar...")
            continue
        
        numeros = extraer_numeros(datos)
        print(f"\n✓ {len(numeros)} números de control encontrados")
        
        if procesar_opcion(int(opcion), numeros):
            input("\nOperación completada. Presione Enter para continuar...")

if __name__ == "__main__":
    main()