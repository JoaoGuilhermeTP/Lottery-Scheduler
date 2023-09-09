import random
from config import *

# Função para gerar uma lista de processos com características aleatórias
def generate_random_processes(number_of_processes, cards_limit, execution_time_limit):
    # Criar uma lista vazia
    list = []
    # Repetir pelo número de processos a serem criados
    for i in range(number_of_processes):
        # Criar variável para conter o ID deste processo
        id = i
        # Criar variável com número aleatório de cartas para este processo, até o limite definido
        cards = random.randint(1, cards_limit)
        # Criar variável com tempo de execução aleatório para este processo, até o limite definido
        execution_time = random.randint(1, execution_time_limit)
        # Criar um objeto Processo com as variáveis anteriores como atributos
        process = Process(id, cards, execution_time)
        # Adicionar processo à lista
        list.append(process)
    # Ordenar a lista pelo número de cartas dos processos, em ordem decrescente
    list = sorted(list, key = lambda x: x.cards, reverse = True)
    # Função retorna a lista criada
    return list

# Função para printar uma descrição dos processos na lista
def describe(list):
    print("Processos a serem executados: \n")
    # Criar variável com a soma total de cartas de todos os processos
    total = sum([process.cards for process in list])
    # Para cada processo na lista
    for process in list:
        # Printar descrição do processo
        print(f"\tID do processo: {process.id} - Número de cartas: {process.cards} - Chance: {round(process.cards / total, 2) * 100}% - Tempo de execução: {process.execution_time}")
    print()

# Função para pegar um processo na lista de acordo com um número de carta
def get_process(list, card):
    # Criar variável para ir somando o número de cartas de cada processo
    sum = 0
    # Para cada processo na lista
    for process in list:
        # Variábel soma com número de cartas deste processo
        sum += process.cards
        # Se o número da carta for menor do que a atual soma, a função retorna este processo
        if card <= sum:
            return process
    # A função retorna Falso caso não haja processo correspondente com o número da carta
    return False

# Função para executar a simulação de execução dos processos
# Argumentos: número de sorteios, lista de processos, e boolean para mostrar ou não a execução
def execute(raffles, list, show = False):
    print("Log de execução:\n")
    # Repetir pelo número de sorteios definido
    for i in range(raffles):
        # Criar variável contendo a soma total de cartas dos processos
        total_cards = sum([process.cards for process in list])
        # Gerar um número de carta aleatório, entre 0 e a soma total de cartas dos processos
        card = random.randint(0, total_cards)
        # Pegar processo correspondente à carta gerada na lista de processos
        process = get_process(list, card)
        # Se a função para pegar processo retornou um processo da lista
        if process:
            # Somar 1 ao atributo de número de execuções deste processo
            process.executions += 1
            # Se variável para mostrar processos for verdadeira
            if show:
                # Printar descrição do processo executado
                print(f"\tCARTA SORTEADA: {card}\tID DO PROCESSO: {process.id}\tNº DE CARTAS: {process.cards}")
        # Se a função para pegar processo não retornou nenhum processo
        else:
            # Printar informação
            print("\tNão existem processos a serem executados")
    # Função tem retorno vazio
    return

# Função para printar relatório de execução dos processos
def report(list, raffles):
    print("Relatório pós execução: \n")
    # Criar variável com o total de cartas
    total = sum([process.cards for process in list])
    # Para cada processo na lista
    for process in list:
        # Printar informação de execução do processo
        print(f"\tID do processo: {process.id} - Executado: {round(process.executions / raffles, 2) * 100}%")
    print()