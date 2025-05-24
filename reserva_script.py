#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao usuário um lista dos quartos disponíveis para alugar e a diária de cada quarto. Estas informações estão disponíveis no arquivo `reserva_quartos.txt`, conforme abaixo:

    `reserva_quartos.txt`:
        #código,nome,diaria
        1,Suíte Master,500
        2,Quarto Família,200
        3,Quarto Single,100
        4,Quarto Simples,50

O programa pergunta ao usuário o seguinte:
    - Seu nome
    - Número do quarto
    - Quantidade de diárias

Ao final, será exibido o valor total da reserva. Se o usuário confirmar, o programa salva o resultado no arquivo `reserva_reservas.txt`:

    `reserva_reservas.txt`:
        #cliente,quarto,diarias,total
        Bruno,3,10,1000

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma mensagem informando que já está reservado.
"""

import os
import sys
import logging
from logging import handlers

path = os.curdir
filepath_rooms = os.path.join(path, "reserva_quartos.txt")
filepath_reservations = os.path.join(path, "reserva_reservas.txt")

try:
    for line in open(filepath_rooms):
        room_number, room_name, room_cost = line.split(",")
        print(f"{room_number} - {room_name} - {room_cost}", end="")
        print(separator)
except FileNotFoundError:
    with open(filepath_rooms, "w") as f:
        f.write("1,Suíte Master,500\n")
        f.write("2,Quarto Família,200\n")
        f.write("3,Quarto Single,100\n")
        f.write("4,Quarto Simples,50\n")

spaces = 30
separator = "-" * spaces
print(separator)
print("Lista de quartos".center(spaces))
print(separator)

print("\nSolicitação de informações:")
user_name = input("Nome: ").strip()
if user_name == "":
    print(f"[AVISO] Insira um nome válido.")
    sys.exit(1)

try:
    user_days = int(input("Quantidade de diárias: ").strip())
except ValueError:
    print("[AVISO] Insira uma quantidade válida.")
    sys.exit(1)

room_check = []
try:
    for line in open(filepath_reservations):
        room_name, room_number, *room_other = line.split(",")
        room_check.append(room_number)
except FileNotFoundError:
    with open(filepath_reservations, "w"):
        pass

while True:
    user_room = input("Número do quarto: ").strip()
    if user_room not in "1234":
        print(f"[AVISO] Insira um número válido.")
        sys.exit(1)
    else:
        if user_room in room_check:
            print(f"[AVISO] Quarto indisponível.")
            print(separator)
        else:
            break

print(separator)
for line in open(filepath_rooms):
    room_number, room_name, room_cost = line.split(",")
    if int(room_number) == int(user_room):
        total_cost = int(room_cost) * user_days
        print(f"Valor total da reserva: {total_cost}")
        print(separator)

confirmation = input("Confirmar reserva (s/n)? ")
if confirmation in "sS":
    with open(filepath_reservations, "a") as file_:
        file_.write(f"{user_name},{user_room},{user_days},{total_cost}\n")
    print(separator)
    print(
        f"Reserva confirmada. Segue resumo:\n"
        f"- Nome   : {user_name}\n"
        f"- Diárias: {user_days}\n"
        f"- Quarto : {room_number} - {room_name}\n"
        f"- Total  : {total_cost}\n\n"
        f"Agradecemos a preferência e volte sempre."
    )
