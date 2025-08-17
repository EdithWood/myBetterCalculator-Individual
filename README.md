# 🧮 Calculadora en Python

Este proyecto es una **mini calculadora interactiva en Python** que permite sumar, multiplicar, verificar si un número es par y comprobar si un número es un entero.  
Incluye pruebas automáticas con `pytest` para garantizar que las funciones principales funcionan correctamente.

---

## 📂 Estructura del proyecto

📂 CALCULADORA AVANZADA
 ├──  📂 myBetterCalculator-Individual
      ├── main.py # Código principal de la calculadora
      ├── test_main.py # Conjunto de pruebas automáticas (pytest)
      └── README.md # Este archivo


---

## 🚀 Funcionalidades

La calculadora implementa las siguientes funciones:

- `addmultiplenumbers([num, num, ..])`  
  Retorna la suma de una lista de números.  

- `multiplymultiplenumbers([num, num, ..])`  
  Retorna el producto de una lista de números.  

- `isiteven(num)`  
  Devuelve `True` si el número es **entero y par**, `False` en caso contrario.  

- `isitaninteger(num)`  
  Devuelve `True` si el número es **un entero** (sin parte decimal), `False` en caso contrario.  

Además, incluye un **modo interactivo** que te permite usar la calculadora desde la terminal.

---

## ▶️ Ejecución

Para iniciar la calculadora en modo interactivo:

```bash
python main.py
