#!/usr/bin/env python3
"""Calculadora Prefix

    Funcionamento:
        
        [operação] [n1] [n2]

    Operações:
        
        sum -> +
        sub -> -
        mul -> *
        div -> /

    Utilização:
        
        $ prefixcalc.py sum 5 2
        7

        $ prefixcalc.py mul 10 5
        50

        $ prefixcalc.py
        Operação: sum
        n1: 5
        n2: 4
        9
"""
__version__ = "0.1.0"

import sys

"""Minha solução
arguments = {
    "operacao": None,
    "n1": None,
    "n2": None,
}

if len(sys.argv) != 4:
    arguments["operacao"] = input("Insira a operação desejada: ")
    arguments["n1"] = input("Insira o primeiro número: ")
    arguments["n2"] = input("Insira o segundo número: ")
else:
    arguments["operacao"], arguments["n1"], arguments["n2"] = sys.argv[1:]

total = None
if arguments["operacao"] == "sum":
    total = int(arguments["n1"]) + int(arguments["n2"])
elif arguments["operacao"] == "sub":
    total = int(arguments["n1"]) - int(arguments["n2"])
elif arguments["operacao"] == "mul":
    total = int(arguments["n1"]) * int(arguments["n2"])
elif arguments["operacao"] == "div":
    total = int(arguments["n1"]) / int(arguments["n2"])

print(f"Operação: {arguments['operacao']}")
print(f"n1: {arguments['n1']}")
print(f"n2: {arguments['n2']}")
print(f"{total}")
"""

arguments = sys.argv[1:]

# TODO: exceptions
if not arguments:
    operation = input("Insira a operação desejada: ")
    n1 = input("Insira o primeiro número: ")
    n2 = input("Insira o segundo número: ")

if len(arguments) != 3:
    print("Quantidade de argumentos inválida.")
    print("Exemplo: sum 1 2")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida.")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: repetição com while + exceptions
    if not num.replace(".","").isdigit():
        print(f"Número inválido `{num}`.")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
        validated_nums.append(num)

n1, n2 = validated_nums

# TODO: usar dict de funções
if operation == "sum":
    result = n1 + n2
if operation == "sub":
    result = n1 - n2
if operation == "mul":
    result = n1 * n2
if operation == "div":
    result = n1 / n2

print(f"Operação: {operation}")
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"Resultado: {result}")
