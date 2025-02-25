from Live import welcome, load_game
from GuessGame import play as guess
from MemoryGame import play as memory
from CurrencyRouletteGame import play as currency

print(welcome("Edi"))
config = load_game()
if config['game'] == 1:
    memory(config['difficulty'])
elif config['game'] == 2:
    guess(config['difficulty'])
else:
    currency(config['difficulty'])