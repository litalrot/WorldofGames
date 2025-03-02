SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')