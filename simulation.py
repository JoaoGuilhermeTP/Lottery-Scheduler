# Import required files
import random
from config import *
from lottery import *

# Set configuration
config = Config()

# Generate list of random processes
list = generate_random_processes(
    config.processes,
    config.cards_limit,
    config.execution_time_limit
)

# Execute simulation
execute(config.raffles, list)

# Describe the processes
describe(list)