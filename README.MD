# 🐍 Curso de Python PCAP

Curso de **Programming Essentials in Python** preparado para la certificación **PCAP: Python Certified Associate Programmer**.

Este repositorio contiene los códigos, apuntes y ejercicios prácticos desarrollados a lo largo de los diferentes módulos del curso.

---

## 📂 Estructura del Proyecto

### `Clases/`
Contiene los scripts principales organizados por módulo de aprendizaje.

#### 📘 Python Essentials - Parte 1: Básico
- **Módulo 1 (`modulo1.py`)**: Introducción a Python y a la programación. Primeros pasos con `print()`.
- **Módulo 2 (`modulo2.py`)**: Tipos de datos, variables, operaciones de entrada y salida (`input`, `print`), operadores matemáticos y literales.
- **Módulo 3 (`modulo3.py`)**: Valores booleanos, ejecución condicional (`if`, `elif`, `else`), bucles (`while`, `for`), listas, ordenamiento de listas (burbuja) y arreglos multidimensionales.
- **Módulo 4 (`modulo4.py`)**: Creación de funciones, retornos, ámbito (scope) de las variables, recursividad, tuplas y diccionarios.

#### 📙 Python Essentials - Parte 2: Intermedio
- **Módulo 5 (`modulo5.py`)**: Uso de módulos estándar (`math`, `random`, `platform`), excepciones (`try`, `except`, `raise`, `assert`), y métodos para manipulación de cadenas (ej. cifrado César, anagramas).
- **Módulo 6**: El enfoque orientado a objetos: clases, métodos, manejo de excepciones y manejo de archivos. *(En desarrollo)*

### `Modulos/`
- **`modulo.py`**: Código de ejemplo diseñado para ilustrar la creación de módulos propios y la ejecución condicional mediante `if __name__ == "__main__":`.

### `progs/`
- **`main2.py`**: Ejemplos de uso e importación de paquetes o módulos externos alojados en otros directorios, modificando la ruta de ejecución con `sys.path.append()`.

---
## 🚀 Cómo ejecutar los ejemplos
Puedes ejecutar cualquier archivo `.py` de las clases directamente desde tu terminal. Por ejemplo:
```bash
python Clases/modulo2.py
```