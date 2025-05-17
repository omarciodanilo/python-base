#!/usr/bin/env python3

"""
Alarme de temperatura

Faça umscript que pergunta ao usuário a temperatura atual e o índice de umidade do ar. Dependendo das condições, será exibida uma mensagem de alerta.

Condições:
    - Temperatura maior que 45: Alerta! Perigo de calor extremo!
    - Temperatura vezes 3 maior/igual à umidade: Alerta! Perigo de calor úmido
    - Temperatura entre 10 e 30: Normal
    - Temperatura entre 0 e 10: Frio
    - Temperatura menor que 0: Alerta! Frio extremo!
"""

import sys
import logging

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None,
    }

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Insira a {key}: ").strip())
    except ValueError:
        log.error(f"[ERRO] Insira uma {key} válida.")
        sys.exit(1)

temperatura = info["temperatura"]
umidade     = info["umidade"]

if temperatura > 45:
    print("\nAlerta! Perigo de calor extremo!")
elif temperatura * 3 >= umidade:
    print("\nAlerta! Perigo de calor úmido!")
elif temperatura >= 10 and temperatura <= 30:
    print("\nNormal.")
elif temperatura >= 0 and temperatura < 10:
    print("\nFrio.")
elif temperatura < 0:
    print("\nAlerta! Frio extremo!")
