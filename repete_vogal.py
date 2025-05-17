#!/usr/bin/env python3

"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

Exemplo:

    `python repete_vogal.py`

    'Insira uma palavra (ou tecle <ENTER> para sair): ' Python
    'Insira uma palavra (ou tecle <ENTER> para sair): ' Bruno
    'Insira uma palavra (ou tecle <ENTER> para sair): ' <ENTER>

    Pythoon
    Bruunoo
"""

palavras = []

while True:
    palavra = input("Insira uma palavra (ou tecle <ENTER> para sair): ").strip()
    if not palavra:
        break

    if palavra != "":
        nova_palavra = ""
        for letra in palavra:
            if letra.lower() in "aeiou":
                nova_palavra += letra * 2
            else:
                nova_palavra += letra
            # nova_palavra += letra * 2 if letra.lower() in "aeiou" else letra
        palavras.append(nova_palavra)

print(*palavras, sep="\n")
