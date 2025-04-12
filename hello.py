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

__version__ = "0.1.4"
__author__ = "Márcio Almeida"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("teste", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
        )
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
                "%s. You typed %s, but you need to use '='. Try with --key=value, as in: --lang=fr_FR", str(e), arg
        )
        """
        print(f"[Error] {str(e)}.")
        print(f"You typed '{arg}'. You need to use '='.")
        print("Example: --lang=fr_FR")
        """
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit(1)
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

try:
    print(msg[current_language] * int(arguments["count"]))
except KeyError as e:
    print(f"[ERROR] Language {str(e)} is invalid.")
    print(f"Supported languages: {list(msg.keys())}")
    sys.exit(1)
