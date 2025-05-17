#!/usr/bin/env python3

"""
Faça um programa que imprime os números pares de 1 a 200.

Exemplo:

    `python3 numeros_pares.py`

    2
    4
    6
    8
    ...
"""

# Opção 1
print("--- Opção 1 ---")
for numero in range(1, 201):
    if numero % 2 == 0:
        print(numero)

print()

# Opção 2
print("--- Opção 2 ---")
for numero in range(2, 202, 2):
    print(numero)
