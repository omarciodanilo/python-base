#!/usr/bin/env python3

"""Hello World Multi Idiomas.

Descrição:
    Dependendo do idioma configurado no ambiente (variável LANG),
    o programa exibirá a mensagem correspondente.

Utilização:
    1. Tenha a variável LANG devidamente configurada.
    Exemplo: export LANG=pt_BR

    2. Informe através de CLI argument "--lang=en_US"

    3. Inserção de idioma pelo usuário.

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.1.3"
__author__ = "Márcio Almeida"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: usar repetição
    if current_language is None:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))
