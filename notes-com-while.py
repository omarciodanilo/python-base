#!/usr/bin/env python3

""" Bloco de Notas
"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("add", "read", "remove")
#params = ("--tag", "--title", "all")
arguments = sys.argv[1:]

# Validar comandos contigos em 'cmds'
if not arguments or arguments[0] not in cmds:
    print(f"Invalid usage.\nAllowed commands: {cmds}")
    sys.exit(1)

"""
# Validar parâmetros para os comandos 'read' e 'remove'
if arguments[0] in cmds[1:]:
    if len(arguments) != 2 or arguments[1].split("=")[0] not in params:
        print(f"Invalid usage.\nAllowed parameters for command {arguments[0]}: {params}")
        sys.exit(1)
"""

while True:

    # Código para leitura das notas
    # TODO: ler usando separação com tab (/t)
    if arguments[0] == "read":
        try:
            tag_value = arguments[1].lower()
        except IndexError:
            tag_value = input("tag: ").strip().lower()

        #tag_key, tag_value = arguments[1].split("=")
        for line in open(filepath):
            tag, title, text = line.split(":")
            if tag == tag_value:
                print(f"tag: {tag}\ntitle: {title}\ntext: {text}")

    # Código para criação das notas
    # TODO: salvar usando separação com tab (/t)
    if arguments[0] == "add":
        try:
            title = arguments[1]
        except IndexError:
            title = input("title: ").strip().title()

        tag = input("tag: ")
        text = input("text:\n")
        with open(filepath, "a") as file_:
            file_.write(f"{tag}:{title}:{text}\n")

    cont = input(f"Type 'y' or 'Y' to {arguments[0]} another note or anything else to quit: ").strip().lower()
    if cont != "y":
        break
