#!/usr/bin/env python3

""" Bloco de Notas
    
    1. Criar notas
    1.1. [TO-DO] Passar o título da nota como parâmetro
        $ notes.py new "título da nota"
        tag: tag-da-nota
        text:
        texto-da-nota
    1.2. Sem passar nenhum parâmetro
        $ notes.py new
        title: título-da-nota
        tag: tag-da-nota
        text:
        texto-da-nota

    2. Ler notas
    2.1. Passar o nome da tag como parâmetro
        $ notes.y read --tag=nome-da-tag
    2.2. [TO-DO] Passar o título como parâmetro
        $ notes.py read --title=título-da-nota
    2.3. [TO-DO] Passar uma palavra-chave como parâmetro (busca realizada na tag, no título e no texto)
        $ notes.py read --search=palavra-chave

    3. Remover notas
    3.1. [TO-DO] Baseadas na tag
        $ notes.py remove --tag=tag-da-nota
    3.2. [TO-DO] Baseadas no título
        $ notas.py remove --title=título-da-nota

"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("new", "read", "remove")
params = ("--tag", "--title", "all")
arguments = sys.argv[1:]

# Validar comandos contigos em 'cmds'
if not arguments or arguments[0] not in cmds:
    print(f"Invalid usage.\nAllowed commands: {cmds}")
    sys.exit(1)

# Validar parâmetros para os comandos 'read' e 'remove'
if arguments[0] in cmds[1:]:
    if len(arguments) != 2 or arguments[1].split("=")[0] not in params:
        print(f"Invalid usage.\nAllowed parameters for command {arguments[0]}: {params}")
        sys.exit(1)

# Código para leitura das notas
# TO-DO: ler usando separação com tab (/t)
if arguments[0] == "read":
    tag_key, tag_value = arguments[1].split("=")
    for line in open(filepath):
        tag, text = line.split(":")
        if tag == tag_value:
            print(f"tag: {tag}\ntext: {text}")

# Código para criação das notas
# TO-DO: salvar usando separação com tab (/t)
if arguments[0] == "new":
    tag = input("tag: ")
    text = input("text:\n")
    with open(filepath, "a") as file_:
        file_.write(f"{tag}: {text}\n")
