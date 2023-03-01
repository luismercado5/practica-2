# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:14:16 2023

@author: luis mercado
"""

import random

# abre el archivo de texto
with open('practica 2.txt', 'r') as file:
    
    file_contents = file.read()

# diccionario de datos
letras_a_numeros = {'a': ['0', '1', '2'], 'b': ['0', '1', '2'], 'c': ['0', '1', '2'], 'd': ['1', '2', '3'], 'e': ['1', '2', '3'], 'f': ['1', '2', '3'], 'g': ['2', '3', '4'], 'h': ['2', '3', '4'], 'i': ['2', '3', '4'], 'j': ['3', '4', '5'], 'k': ['3', '4', '5'], 'l': ['3', '4', '5'], 'm': ['4', '5', '6'], 'n': ['4', '5', '6'], 'o': ['4', '5', '6'], 'p': ['5', '6', '7'], 'q': ['5', '6', '7'], 'r': ['5', '6', '7'], 's': ['6', '7', '8'], 't': ['6', '7', '8'], 'u': ['6', '7', '8'], 'v': ['7', '8', '9'], 'w': ['7', '8', '9'], 'x': ['7', '8', '9'], 'y': ['8', '9'], 'z': ['8', '9'], 'A': ['9'], 'B': ['9'], 'C': ['9']}

# remplaza las letras por numeros de manera aleatoria segun nuestro diccionario de datos
for letras, numeros in letras_a_numeros.items():
    for i in range(len(numeros)):
        file_contents = file_contents.replace(letras, random.choice(numeros))
# abre un nuevo archivo txt con el remplazo de numero txt        
with open('numero.txt', 'w') as file:
            file.write(file_contents)


# abre el archivo de texto anteriormente cambiado
with open('numero.txt', 'r') as file:
    
    file_contents = file.read()

# diccionario de datos
numero_a_letra = {'0': ['A', 'B', 'C'], '1': ['D', 'E', 'F'], '2': ['G', 'H', 'I'], '3': ['J', 'K', 'L'], '4': ['M', 'N', 'O'], '5': ['P', 'Q', 'R'], '6': ['S', 'T', 'U'], '7': ['V', 'W', 'X'], '8': ['Y', 'Z'], '9': ['A', 'B', 'C']}

# reemplaza los numeros por letras
for numero, letra in numero_a_letra.items():
    for i in range(len(letra)):
        file_contents = file_contents.replace(numero, random.choice(letra))

# abre un nuevo archivo txt con el remplazo de numero txt
with open('letra.txt', 'w') as file:
    file.write(file_contents)