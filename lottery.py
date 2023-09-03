import random
from config import Process

# Function for generating a list of random processes
def generate_random_processes(number_of_processes, cards_limit, execution_time_limit):
    list = []
    for i in range(number_of_processes):
        id = i
        cards = random.randint(1, cards_limit)
        execution_time = random.randint(1, execution_time_limit)
        process = Process(id, cards, execution_time)
        list.append(process)
    list = sorted(list, key = lambda x: x.cards, reverse = True)
    return list

def describe(list):
    print("Processos a serem executados: ")
    total = sum([process.cards for process in list])
    for process in list:
        print(f"\tID do processo: {process.id} - Número de cartas: {process.cards} - Chance: {round(process.cards / total, 2) * 100}%")
    print()

# Function for getting the right process from list
def get_process(list, card):
    sum = 0
    for process in list:
        sum += process.cards
        if card <= sum:
            return process
    return False

def execute(raffles, list):
    print("Log de execução:\n")
    for _ in range(raffles):
        total_cards = sum([process.cards for process in list])
        card = random.randint(0, total_cards)
        process = get_process(list, card)
        if process:
            print(f"\tCARTA SORTEADA: {card}\tID DO PROCESSO: {process.id}\tNº DE CARTAS: {process.cards}")
        else:
            print("\tNão existem processos a serem executados")
            return