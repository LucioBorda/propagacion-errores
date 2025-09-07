# 📊 Propagación de Errores - Suma y Diferencia

Programa en Python para calcular la propagación de errores en operaciones básicas según la fórmula:

**δ(A ± B) = √(δA² + δB²)**

**Desarrollado por:** Grupo 10 - Tema 7

## ⚡ Inicio Rápido

```bash
git clone https://github.com/tu-usuario/propagacion-errores.git
cd propagacion-errores
python src/main.py
```

## 🎯 Características

- ✅ Cálculo de propagación de errores (suma y resta)
- ✅ Ejemplos prácticos de 6 áreas científicas
- ✅ Interfaz interactiva con menús
- ✅ Compatible con Windows/Linux/Mac
- ✅ No requiere librerías externas

## 📁 Estructura

```
propagacion-errores/
├── src/
│   └── main.py
├── examples/
│   ├── ejemplo_fisica.txt
│   ├── ejemplo_quimica.txt
│   ├── ejemplo_ingenieria.txt
│   ├── ejemplo_medicina.txt
│   ├── ejemplo_estadistica.txt
│   └── ejemplo_laboratorio.txt
├── README.md
└── requirements.txt
```

## 📚 Ejemplos Incluidos

| Área | Descripción |
|------|-------------|
| 🔬 Física | Medición de velocidades |
| ⚗️ Química | Concentraciones de soluciones |
| 🏗️ Ingeniería | Cargas estructurales |
| 🏥 Medicina | Dosificación de medicamentos |
| 📊 Estadística | Análisis de muestras |
| 🧪 Laboratorio | Experimentos de densidad |

## 🧮 Fórmulas

- **Suma:** A + B → δ(A + B) = √(δA² + δB²)
- **Resta:** A - B → δ(A - B) = √(δA² + δB²)

## 💻 Ejemplo de Uso

```
Ingrese el valor A: 15.2
Ingrese la incertidumbre de A: 0.1
Ingrese el valor B: 8.7
Ingrese la incertidumbre de B: 0.2

Resultado:
Suma: 23.9 ± 0.224
Resta: 6.5 ± 0.224
```

## 📋 Requisitos

- Python 3.6 o superior
- Sin dependencias externas

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama: `git checkout -b nueva-funcionalidad`
3. Commit: `git commit -m 'Agregar funcionalidad'`
4. Push: `git push origin nueva-funcionalidad`
5. Abre un Pull Request

---

**Proyecto académico sobre propagación de errores en operaciones básicas**
