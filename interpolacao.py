#!/usr/bin/env python

"""
    Imprime mensagem de e-mail para clientes.
    Lista de clientes em arquivo separado.
    Template de e-mail em arquivo separado.
    Usuário precisa passar os dois arquivos como parâmetro.
"""

__version__ = "0.1.1"

import os
import sys

# TODO: validar entradas do usuário:
#       - adicionar opções "--email-file" e "--template-file"
#       - se inseriu a quantidade correta de parâmetros

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de e-mails e do arquivo de template.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(",")

    # TODO: substituir por envio de e-mail
    print(f"Enviando e-mail para: {email}")
    print()
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "escrever muito bem",
            "link": "http://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
        }
    )
    print("-" * 50)
    print()
