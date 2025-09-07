cat > README.md << 'EOF'
# Propagación de Errores - Suma y Diferencia

## Descripción
Programa en Python para calcular la propagación de errores en operaciones básicas (suma y resta) según la fórmula:

**δ(A ± B) = √(δA² + δB²)**

Desarrollado como proyecto académico - **Grupo 10, Tema 7**

## Características
- Cálculo de propagación de errores para suma y resta
- Ejemplos prácticos de múltiples áreas científicas
- Interfaz de usuario interactiva
- Calculadora avanzada para múltiples valores
- Teoría completa incluida
- Compatible con Windows/Linux/Mac

## Estructura del Proyecto

propagacion-errores/
├── src/
│   └── main.py              # Programa principal
├── docs/
│   └── README.md            # Documentación
├── examples/
│   ├── ejemplo_fisica.txt   # Ejemplo de física
│   ├── ejemplo_quimica.txt  # Ejemplo de química
│   ├── ejemplo_ingenieria.txt
│   ├── ejemplo_medicina.txt
│   ├── ejemplo_estadistica.txt
│   └── ejemplo_laboratorio.txt
└── requirements.txt         # Dependencias (ninguna externa)

## Instalación y Uso

### Prerrequisitos
- Python 3.6 o superior

### Instalación
```bash
git clone https://github.com/tu-usuario/propagacion-errores.git
cd propagacion-errores

Ejecución
python src/main.py

🧮 Fórmulas Utilizadas

Suma: A + B → δ(A + B) = √(δA² + δB²)
Resta: A - B → δ(A - B) = √(δA² + δB²)