# Proyecto Módulo 2: Estructuras de Control y Colecciones en Python

Este repositorio contiene la consolidación de los dos retos desarrollados durante el Módulo 2 del curso de Fundamentos de Ciencia de Datos.

## Contenido del Repositorio

- `NOMBRE_APELLIDO_proyectoM2.py`: Script principal ejecutable que integra un menú interactivo para evaluar los retos de Longitud de Palabra y Cuadrantes Cartesianos.
- `README.md`: Explicación del proyecto y reflexión sobre la lógica de programación.

---

## Explicación de los Retos

1. **Reto 1: Longitud de palabra**
   - Recibe una palabra ingresada por el usuario y valida que la longitud se encuentre en un rango de 4 a 8 caracteres.
   - Emplea un ciclo `while` y condicionales `if-elif-else` para guiar al usuario hasta ingresar un texto correcto.

2. **Reto 2: Ubicación de Cuadrantes**
   - Solicita las coordenadas numéricas `X` e `Y` al usuario.
   - Realiza un **casting de datos** de `string` a `float` validando entradas numéricas con un bloque `try-except`.
   - Utiliza una **tupla** inmutable para almacenar el nombre de los 4 cuadrantes.

---

## Reflexión

El uso de estructuras de control (`if`, `elif`, `else`, `while`), junto con el correcto manejo de colecciones (`tuplas`) y el casteo seguro de datos mediante `try-except`, transformó el código en una herramienta resiliente y ordenada. 

Anteriormente, el ingreso de datos erróneos por parte del usuario detenía abruptamente la ejecución del programa. La integración de la validación mediante casting a `float` asegura que el programa siga en ejecución sin interrupciones y la modularización en funciones junto a un menú interactivo mejoró la escalabilidad y limpieza visual del desarrollo bajo el estándar PEP8.