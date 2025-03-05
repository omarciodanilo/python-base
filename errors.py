#!/usr/bin/env python3

"""Tratamento de Erros

    Abordagens para tratamento de erros.

"""

__version__ = "0.1.0"

import sys
import os

# Abordagem 1: LBYL - Look Before You Leap
"""
if os.path.exists("names.txt"):
    # Race Condition
    print("o arquivo existe.")
    input("...")
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)
"""

# Abordagem 2: EAFP - Easy To Ask Forgiveness Than Permission
# Melhor, mais fácil e com menor complexidade algorítmica

# Se quiser subir um erro por conta própria para testar
# try:
#     raise RuntimeError("Ocorreu um erro.") # Pode ser qualquer exceção em vez do RuntimeError
# except Exception as e:
#     print(str(e))

try:
    names = open("names.txt").readlines() # FileNotFoundError
    # 1 / 0 # ZeroDivisionError
    # print(names.banana) # AttributeError
except FileNotFoundError as e:
    print("[Error] File names.txt not found.")
    # print(f"{str(e)}.") # Imprimir mensagem de erro da exceção
    sys.exit(1)
    # TO-DO: usar retry
# else:
    # print("else no try, executado apenas se o não houver exceção capturada.")
# finally:
    # print("finally no try, executado sempre ao final do bloco.")

# except ZeroDivisionError:
    # print("[Error] Cannot divide by zero.")
    # sys.exit(1)
# except AttributeError:
    # print("[Error] List does not have banana.")
    # sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
