#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala

atividades = [
    ("inglês", aula_ingles),
    ("música", aula_musica),
    ("dança", aula_danca),
]

for nome_atividade, atividade in atividades:
    
    print(f"Alunos da atividade {nome_atividade}:")
    print("-" * 40)

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)
    print("-" * 40)
