from Score import add_score

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."
def load_game():
    final = {'game': None, 'difficulty': None}
    while True:
        game = input("""Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2. Guess Game - guess a number and see if you chose like the computer
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """)
        if game.isdigit():
            game = int(game)
            if 1 <= game <= 3:
                final['game'] = game
                while True:
                    diff = input("Please choose game difficulty from 1 to 5: ")
                    if diff.isdigit():
                        diff = int(diff)
                        if 1<= diff <= 5:
                            final['difficulty'] = diff
                            add_score(diff)
                            return final
                        else:
                            print("Please choose a difficulty in the mentioned range.")
                    else:
                        print("Please make sure to enter numbers only and in the mentioned range.")
                break
            else:
                print("Please choose a game in the mentioned range.")
        else:
            print("Please make sure to enter numbers only and in the mentioned range.")
