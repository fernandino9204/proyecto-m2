"""
PROYECTO MÚDULO 2: CONSOLIDACIÓN DE RETOS
Integración de estructuras de control, manejo de excepciones, 
colecciones de datos y casting de variables.
"""

def reto_longitud_palabra():
    """
    Reto 1: Encuentra la longitud de una palabra ingresada por el usuario.
    Incluye validación de entrada de entre 4 y 8 letras.
    """
    print("\n--- RETO 1: LONGITUD DE UNA PALABRA ---")
    
    while True:
        palabra = input("Ingresa una palabra (debe tener entre 4 y 8 letras): ").strip()
        longitud = len(palabra)
        
        # Validación de rango
        if 4 <= longitud <= 8:
            print(f"Correcto. La palabra '{palabra}' es adecuada y tiene {longitud} letras.")
            break
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras. Intenta de nuevo.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras. Intenta de nuevo.")


def reto_cuadrantes():
    """
    Reto 2: Identificación del cuadrante según coordenadas (X, Y).
    Utiliza casting explícito (str a float) y una tupla para almacenar los cuadrantes.
    """
    print("\n--- RETO 2: IDENTIFICACIÓN DE CUADRANTE ---")
    
    # Uso de tupla para almacenar los nombres de los cuadrantes
    CUADRANTES = (
        "Cuadrante I (+X, +Y)",
        "Cuadrante II (-X, +Y)",
        "Cuadrante III (-X, -Y)",
        "Cuadrante IV (+X, -Y)"
    )
    
    # Manejo de excepciones para asegurar el casting correcto
    while True:
        try:
            # Demostración de casting explícito de string a float
            x_input = input("Ingresa la coordenada X: ").strip()
            y_input = input("Ingresa la coordenada Y: ").strip()
            
            x = float(x_input)
            y = float(y_input)
            
            if x == 0 or y == 0:
                print("Error: Las coordenadas X e Y no deben ser 0. Intenta de nuevo.")
                continue
            
            # Evaluación de cuadrantes accediendo a la tupla por índice
            if x > 0 and y > 0:
                print(f"El punto ({x}, {y}) se encuentra en el: {CUADRANTES[0]}")
            elif x < 0 and y > 0:
                print(f"El punto ({x}, {y}) se encuentra en el: {CUADRANTES[1]}")
            elif x < 0 and y < 0:
                print(f"El punto ({x}, {y}) se encuentra en el: {CUADRANTES[2]}")
            elif x > 0 and y < 0:
                print(f"El punto ({x}, {y}) se encuentra en el: {CUADRANTES[3]}")
                
            break # Salir del ciclo una vez evaluado correctamente

        except ValueError:
            print("Error: Ingresa un número válido (ejemplos: 5, -3.2). Intenta de nuevo.\n")


def menu_principal():
    """
    Menú de navegación principal para seleccionar ambos retos.
    """
    while True:
        print("\n========================================")
        print("     MENÚ PRINCIPAL - PROYECTO M2       ")
        print("========================================")
        print("1. Ejecutar Reto 1: Longitud de Palabra")
        print("2. Ejecutar Reto 2: Cuadrantes")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == '1':
            reto_longitud_palabra()
        elif opcion == '2':
            reto_cuadrantes()
        elif opcion == '3':
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()