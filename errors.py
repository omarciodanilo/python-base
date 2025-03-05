#!/usr/bin/env python3

"""Tratamento de Erros

    Abordagens para tratamento de erros.

"""

__version__ = "0.1.0"

import sys
import os

# Abordagem 1: LBYL - Look Before You Leap

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
