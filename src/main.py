import math
import sys
import os

# Configuración para caracteres especiales en Windows
if sys.platform.startswith('win'):
    os.system('chcp 65001 > nul')  # Configura UTF-8 en Windows
    sys.stdout.reconfigure(encoding='utf-8')

def propagacion_errores_suma_resta():
    """
    Programa para calcular la propagación de errores en suma y resta
    """
    
    print("="*60)
    print("    PROPAGACION DE ERRORES EN SUMA Y DIFERENCIA")
    print("="*60)
    print()
    
    # Explicación teórica
    print("TEORIA:")
    print("Cuando realizamos operaciones con medidas que tienen incertidumbre,")
    print("el error se propaga según formulas especificas.")
    print()
    print("Para suma y resta: delta(A +/- B) = sqrt(deltaA² + deltaB²)")
    print("Donde deltaA y deltaB son las incertidumbres absolutas")
    print()
    
    # Solicitar datos al usuario
    print("INGRESE LOS DATOS:")
    print("-" * 20)
    
    try:
        # Primer valor
        A = float(input("Ingrese el valor A: "))
        delta_A = float(input("Ingrese la incertidumbre de A (deltaA): "))
        
        # Segundo valor
        B = float(input("Ingrese el valor B: "))
        delta_B = float(input("Ingrese la incertidumbre de B (deltaB): "))
        
        print("\n" + "="*50)
        print("CALCULOS Y RESULTADOS:")
        print("="*50)
        
        # Realizar cálculos
        suma = A + B
        resta = A - B
        
        # Propagación del error (igual para suma y resta)
        error_propagado = math.sqrt(delta_A**2 + delta_B**2)
        
        # Mostrar resultados detallados
        print(f"\nValores ingresados:")
        print(f"A = {A} +/- {delta_A}")
        print(f"B = {B} +/- {delta_B}")
        
        print(f"\nCalculo de la propagacion del error:")
        print(f"delta(A +/- B) = sqrt(deltaA² + deltaB²)")
        print(f"delta(A +/- B) = sqrt({delta_A}² + {delta_B}²)")
        print(f"delta(A +/- B) = sqrt({delta_A**2:.4f} + {delta_B**2:.4f})")
        print(f"delta(A +/- B) = sqrt({delta_A**2 + delta_B**2:.4f})")
        print(f"delta(A +/- B) = {error_propagado:.4f}")
        
        print(f"\nRESULTADOS FINALES:")
        print(f"Suma (A + B) = {suma:.4f} +/- {error_propagado:.4f}")
        print(f"Resta (A - B) = {resta:.4f} +/- {error_propagado:.4f}")
        
        # Cálculo del error relativo
        error_relativo_suma = (error_propagado / abs(suma)) * 100 if suma != 0 else 0
        error_relativo_resta = (error_propagado / abs(resta)) * 100 if resta != 0 else 0
        
        print(f"\nERRORES RELATIVOS:")
        print(f"Error relativo de la suma: {error_relativo_suma:.2f}%")
        print(f"Error relativo de la resta: {error_relativo_resta:.2f}%")
        
        # Interpretación de resultados
        print(f"\nINTERPRETACION:")
        print(f"- La suma tiene una precision del {100-error_relativo_suma:.1f}%")
        print(f"- La resta tiene una precision del {100-error_relativo_resta:.1f}%")
        
    except ValueError:
        print("Error: Por favor ingrese valores numericos validos.")
        return
    except Exception as e:
        print(f"Error inesperado: {e}")
        return

def ejemplo_simple():
    """Función con un ejemplo práctico simple"""
    print("\n" + "="*60)
    print("    EJEMPLO SIMPLE")
    print("="*60)
    
    print("Ejemplo: Medicion de longitudes")
    print("L1 = 15.2 +/- 0.1 cm")
    print("L2 = 8.7 +/- 0.2 cm")
    print()
    
    L1, delta_L1 = 15.2, 0.1
    L2, delta_L2 = 8.7, 0.2
    
    suma_ej = L1 + L2
    resta_ej = L1 - L2
    error_ej = math.sqrt(delta_L1**2 + delta_L2**2)
    
    print("Calculos paso a paso:")
    print(f"L1 + L2 = {L1} + {L2} = {suma_ej} cm")
    print(f"L1 - L2 = {L1} - {L2} = {resta_ej} cm")
    print()
    print("Propagacion del error:")
    print(f"delta(L1 +/- L2) = sqrt(0.1² + 0.2²)")
    print(f"delta(L1 +/- L2) = sqrt(0.01 + 0.04)")
    print(f"delta(L1 +/- L2) = sqrt(0.05)")
    print(f"delta(L1 +/- L2) = {error_ej:.3f} cm")
    print()
    print("RESULTADOS FINALES:")
    print(f"Suma: {suma_ej} +/- {error_ej:.3f} cm")
    print(f"Resta: {resta_ej} +/- {error_ej:.3f} cm")

def cargar_ejemplos():
    """Cargar y mostrar ejemplos desde archivos"""
    ejemplos_dir = "examples"
    
    # Verificar si existe la carpeta
    if not os.path.exists(ejemplos_dir):
        print(f"Carpeta '{ejemplos_dir}' no encontrada.")
        print("Por favor, cree la carpeta y agregue los archivos de ejemplo.")
        return
    
    # Buscar archivos .txt en la carpeta examples
    try:
        archivos = [f for f in os.listdir(ejemplos_dir) if f.endswith('.txt')]
        
        if not archivos:
            print("No se encontraron archivos de ejemplo (.txt) en la carpeta examples/")
            return
        
        print("\n" + "="*60)
        print("    EJEMPLOS DISPONIBLES")
        print("="*60)
        
        # Mostrar lista de ejemplos
        for i, archivo in enumerate(archivos, 1):
            nombre = archivo.replace('.txt', '').replace('ejemplo_', '').replace('_', ' ').title()
            print(f"{i}. {nombre}")
        
        print(f"{len(archivos) + 1}. Volver al menu principal")
        
        try:
            opcion = int(input(f"\nSeleccione ejemplo (1-{len(archivos) + 1}): "))
            
            if opcion == len(archivos) + 1:
                return
            elif 1 <= opcion <= len(archivos):
                archivo_seleccionado = archivos[opcion-1]
                ruta_archivo = os.path.join(ejemplos_dir, archivo_seleccionado)
                
                # Leer y mostrar el archivo
                with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido = f.read()
                    print("\n" + "="*60)
                    nombre_ejemplo = archivo_seleccionado.replace('.txt', '').replace('ejemplo_', '').replace('_', ' ').upper()
                    print(f"    EJEMPLO: {nombre_ejemplo}")
                    print("="*60)
                    print(contenido)
                    
                    # Preguntar si quiere usar los datos del ejemplo
                    usar_datos = input("\nDesea usar los datos de este ejemplo en el calculador? (s/n): ").lower()
                    if usar_datos in ['s', 'si', 'y', 'yes']:
                        print("\nPor favor, extraiga los valores A, deltaA, B, deltaB del ejemplo")
                        print("y uselos en la opcion 1 del menu principal.")
                        
            else:
                print("Opcion no valida.")
                
        except ValueError:
            print("Por favor ingrese un numero valido.")
            
    except Exception as e:
        print(f"Error al cargar ejemplos: {e}")

def mostrar_teoria():
    """Muestra la teoría completa sobre propagación de errores"""
    print("\n" + "="*60)
    print("    TEORIA COMPLETA")
    print("="*60)
    
    teoria = """
PROPAGACION DE ERRORES EN OPERACIONES BASICAS

1. CONCEPTOS BASICOS:
   - Error absoluto (delta_x): Incertidumbre en la medida
   - Error relativo: (delta_x/x) × 100%
   - Toda medida se expresa como: x +/- delta_x

2. REGLAS DE PROPAGACION:

   Para SUMA y RESTA: A +/- B
   delta(A +/- B) = sqrt(deltaA² + deltaB²)
   
   Caracteristicas:
   - El error propagado es el mismo para suma y resta
   - Los errores se combinan cuadraticamente
   - El error nunca es menor que el mayor de los errores individuales

3. INTERPRETACION:
   - El resultado final mantiene la incertidumbre combinada
   - La precision del resultado depende de ambas medidas
   - Es importante considerar cifras significativas

4. EJEMPLO NUMERICO:
   Si A = 10.0 +/- 0.2 y B = 5.0 +/- 0.1
   
   Suma: A + B = 15.0 +/- sqrt(0.2² + 0.1²) = 15.0 +/- 0.22
   Resta: A - B = 5.0 +/- sqrt(0.2² + 0.1²) = 5.0 +/- 0.22

5. APLICACIONES:
   - Mediciones en laboratorio
   - Calculos de ingenieria
   - Analisis de datos experimentales
   
6. VENTAJAS DE ESTE METODO:
   - Proporciona una estimacion realista del error
   - Permite comparar la precision de diferentes mediciones
   - Es fundamental en el analisis de datos cientificos

7. CONSEJOS PRACTICOS:
   - Siempre expresar el resultado con la incertidumbre
   - Mantener cifras significativas apropiadas
   - Considerar todas las fuentes de error posibles
"""
    print(teoria)

def calculadora_avanzada():
    """Función adicional para cálculos múltiples"""
    print("\n" + "="*60)
    print("    CALCULADORA AVANZADA")
    print("="*60)
    
    valores = []
    errores = []
    
    print("Ingrese hasta 5 medidas para calcular su suma total")
    print("(Presione Enter sin valor para terminar)")
    
    i = 1
    while i <= 5:
        try:
            valor_str = input(f"Valor {i} (o Enter para terminar): ")
            if valor_str == "":
                break
                
            valor = float(valor_str)
            error = float(input(f"Error de la medida {i}: "))
            
            valores.append(valor)
            errores.append(error)
            i += 1
            
        except ValueError:
            print("Por favor ingrese valores numericos validos")
            continue
    
    if len(valores) > 0:
        suma_total = sum(valores)
        error_total = math.sqrt(sum(e**2 for e in errores))
        
        print(f"\nRESULTADOS:")
        print(f"Valores ingresados: {len(valores)}")
        for i, (v, e) in enumerate(zip(valores, errores), 1):
            print(f"  Medida {i}: {v} +/- {e}")
        
        print(f"\nSuma total: {suma_total:.4f} +/- {error_total:.4f}")
        print(f"Error relativo: {(error_total/suma_total)*100:.2f}%")

def menu_principal():
    """Menú principal del programa"""
    while True:
        print("\n" + "="*60)
        print("    MENU PRINCIPAL")
        print("="*60)
        print("1. Calcular propagacion de errores (datos propios)")
        print("2. Ver ejemplo simple")
        print("3. Explorar ejemplos por area (fisica, quimica, etc.)")
        print("4. Ver teoria completa")
        print("5. Calculadora avanzada (multiples valores)")
        print("6. Salir")
        print()
        
        opcion = input("Seleccione una opcion (1-6): ")
        
        if opcion == '1':
            propagacion_errores_suma_resta()
        elif opcion == '2':
            ejemplo_simple()
        elif opcion == '3':
            cargar_ejemplos()
        elif opcion == '4':
            mostrar_teoria()
        elif opcion == '5':
            calculadora_avanzada()
        elif opcion == '6':
            print("Gracias por usar el programa!")
            print("Desarrollado por Grupo 10 - Tema 7")
            break
        else:
            print("Opcion no valida. Por favor seleccione 1, 2, 3, 4, 5 o 6.")

if __name__ == "__main__":
    # Mensaje de bienvenida
    print("Iniciando programa de Propagacion de Errores...")
    print("Version: 3.0 - Con ejemplos dinamicos")
    print("Tema: Propagacion de errores en suma y diferencia")
    
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        print("Hasta luego!")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        print("Por favor reinicie el programa.")