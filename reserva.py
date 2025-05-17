#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao usuário um lista dos quartos disponíveis para alugar e a diária de cada quarto. Estas informações estão disponíveis no arquivo`quartos.txt`, conforme abaixo:

    `quartos.txt`:
        #código,nome,diaria
        1,Suíte Master,500
        2,Quarto Família,200
        3,Quarto Single,100
        4,Quarto Simples,50

O programa pergunta ao usuário o seguinte:
    - Seu nome
    - Número do quarto
    - Quantidade de diárias

Ao final, será exibido o valor total da reserva. Se o usuário confirmar, o programa salva o resultado no arquivo `reservas.txt`:

    `reservas.txt`:
        #cliente,quarto,diarias
        Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma mensagem informando que já está reservado.
"""
