#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.2"

# Dados

salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

aulas = {
    "inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "música": ["Erik", "Carlos", "Maria"],
    "dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala

atividades = {
    "inglês": {
        "sala1": [],
        "sala2": [],
    },
    "música": {
        "sala1": [],
        "sala2": [],
    },
    "dança": {
        "sala1": [],
        "sala2": [],
    }
}

for aula, alunos in aulas.items():
    for aluno in alunos:
        if aluno in salas["sala1"]:
            atividades[aula]["sala1"].append(aluno) 
        elif aluno in salas["sala2"]:
            atividades[aula]["sala2"].append(aluno)

    print(f"Alunos da atividade {aula}:")
    print("-" * 40)
    print("- Sala 1: ", atividades[aula]["sala1"])
    print("- Sala 2: ", atividades[aula]["sala2"])
    print()
