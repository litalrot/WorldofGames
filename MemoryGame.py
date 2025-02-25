import random, time

def generate_sequence(diff):
    return [random.randint(1, 101) for _ in range(diff)]

def get_list_from_user():
    return [int(x) for x in input("Enter the numbers you remember separated by commas: ").split(',')]

def is_list_equal(random_list, user_list):
    if random_list == user_list:
        return True
    else:
        return False

def play(diff):
    random_list = generate_sequence(diff)
    print(random_list,  end='', flush=True)
    time.sleep(0.7)
    print("\r" + " " * 30, end='', flush=True)
    print("\rNow it's your turn.")
    user_list = get_list_from_user()
    result = is_list_equal(random_list, user_list)
    if result:
        print("Bingo!")
    else:
        print("Not quite there, need a little more practice.")