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

path = os.curdir
filepath_rooms = os.path.join(path, "reserva_quartos.txt")
filepath_reservations = os.path.join(path, "reserva_reservas.txt")
spaces = 30
separator = "-" * spaces

with open(filepath_rooms, "w") as file_:
    file_.write("1,Suíte Master,500\n")
    file_.write("2,Quarto Família,200\n")
    file_.write("3,Quarto Single,100\n")
    file_.write("4,Quarto Simples,50\n")

room_list = []
for line in  open(filepath_rooms):
    room_number, *room_other = line.split(",")
    room_list.append(room_number)

room_check = []
try:
    for line in open(filepath_reservations):
        room_name, room_number, *room_other = line.split(",")
        room_check.append(room_number)
except FileNotFoundError:
    with open(filepath_reservations, "w"):
        pass

print(separator)
print("HOTEL PYTHONICO - RESERVAS".center(spaces))
print(separator)

if len(room_list) == len(room_check):
    print("Hotel lotado".center(spaces))
    print(separator)
    sys.exit(1)

print("Lista de quartos".center(spaces))
print(separator)

for line in open(filepath_rooms):
    room_number, room_name, room_cost = line.split(",")
    if room_number in room_check:
        room_status = "Reservado"
    else:
        room_status = "Disponível"
    print(f"{room_number} - {room_name} - {room_cost.strip()} - {room_status}\n", end="")

print("\nSolicitação de informações:")

while True:
    user_name = input("Nome: ").strip()
    if user_name == "":
        print(f"[AVISO] Insira um nome válido.")
        print(separator)
    else:
        print(separator)
        break

while True:
    user_room = input("Número do quarto: ").strip()
    if user_room not in room_list:
        print(f"[AVISO] Insira um número válido.")
        print(separator)
    else:
        if user_room in room_check:
            print(f"[AVISO] Quarto indisponível.")
            print(separator)
        else:
            print(separator)
            break

while True:
    try:
        user_days = int(input("Quantidade de diárias: ").strip())
    except ValueError:
        print("[AVISO] Insira uma quantidade válida.")
        print(separator)
    else:
        print(separator)
        break

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
    print(separator)
