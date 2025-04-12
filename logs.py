#!/usr/bin/python3

import os
import logging

"""
1. Criar instância personalizada de logging
2. Criar handler responsável por enviar mensagem  ao console
3. Configurar level do handler
4. Criar objeto de formatação da mensagem de log
5. Colocar objeto de formatação dentro do handler
6. Adicionar handler à instância de log criada
"""

# TODO: transformar esses passos numa função
# TODO: usar lib (loguru)
# Usuário pode controlar o nível de log através de variável de ambiente, executando no terminal, por exemplo: export LOG_LEVEL=DEBUG
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("teste", log_level) # log = logging.Logger("nome do logger", logging.LEVEL) --> log = logging.Logger("teste", logging.DEBUG)
ch = logging.StreamHandler() # StreamHandler: objeto que permite escrever em qualquer destino (como um arquivo); sem parâmetros, envia para stderr
ch.setLevel(log_level) # ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
        )
ch.setFormatter(fmt)
log.addHandler(ch)

"""
log.debug("mensagem pro dev, qa, sysadmin")
log.info("mensagem geral para usuários")
log.warning("aviso que não causa erro")
log.error("erro que afeta uma única execução")
log.critical("erro geral, ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("%s", str(e))
    #print(f"[ERRO] {str(e)}")
