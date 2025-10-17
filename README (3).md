[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UQ-PIKtr)
# Sistema de Gestión de Bibliotecas

Una biblioteca necesita un sistema para gestionar los préstamos sus materiales bibliográficos.

• **Libros físicos**: tienen un costo de mantenimiento de $100 por cada 30 días prestados.
• **E-books**: no tienen costo de mantenimiento físico, pero tiene un costo de 5% sobre el valor de venta en concepto de licencias de uso.
• **Revistas**: tienen un costo de $50 por cada ejemplar prestado, con un recargo del 20% si es una revista importada.

## Archivo material.csv:

    • Tipo de material (1 = libro físico, 2 = e-book, 3 = revista)
    • Código
    • Título
    • Autor
    • Precio base
    • Característica extra (días prestados, valor de venta, nacional/importada)

## Funcionalidades:

    1. Cargar materiales desde el archivo.
    2. Calcular el promedio entero de los precios base de todos.
    3. Obtener el material con mayor costo de mantenimiento.
    4. Calcular la suma de costo de mantenimiento de todos los préstamos.
    5. Contar cuántos libros físicos se prestaron por más de 30 días.
    6. Contar cuántas revistas son importadas.
    7. Calcular en un diccionario la cantidad de materiales de cada tipo, las claves del diccionario deben ser "Libro", "Ebook" y "Revista".
