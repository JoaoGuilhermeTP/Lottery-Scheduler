# Importar módulos necessário 
import random
from config import *
from lottery import *

# Criar objeto com as definições de confuguracao
config = Config()

# Gerar lista com processos aleatórios 
list = generate_random_processes(
    # N° de processos a serem gerados
    config.processes,
    # Max n° de cartas por processo 
    config.cards_limit,
    # Tempo de exec max. por processo 
    config.execution_time_limit
)

# Printar descrição dos processos na lista 
describe(list)

# Executar simulação 
execute(config.raffles, list)

# Printar informação após simulação 
report(list, config.raffles)