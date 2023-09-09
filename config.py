# Classe a partir da qual objeto de configuração da simulação é criado
class Config:
    def __init__(self):
        # Número de processos a serem criados
        self.processes = 2
        # Número máximo de cartas por processo
        self.cards_limit = 100
        # Tempo máximo de execução por processo
        self.execution_time_limit = 1001
        # Número de sorteios a serem executados
        self.raffles = 500
        # Tamanho de um quantum
        self.quantum = 5

# Classe a partir da qual os Processos são criados como objetos
class Process:
    def __init__(self, id, cards, execution_time):
        # Nùmero de ID do processo
        self.id = id
        # Quantidade de cartas dadas ao processo
        self.cards = cards
        # Tempo de execução do processo
        self.execution_time = execution_time
        # Número de vezes que o processo foi executado
        self.executions = 0