# Class from which configuration object is created
class Config:
    def __init__(self):
        self.processes = 3
        self.cards_limit = 100
        self.execution_time_limit = 500
        self.raffles = 1000

# Class from which Process objects are created
class Process:
    def __init__(self, id, cards, execution_time):
        self.id = id
        self.cards = cards
        self.execution_time = execution_time