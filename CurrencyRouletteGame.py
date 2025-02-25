import requests, random

def get_exchange_rate():
    try:
        api_rate = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        rate_dict = api_rate.json()
        return rate_dict["rates"].get("ILS", 3.5)
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return 3.5

def get_money_interval(total_value, difficulty):
    interval = 5 - difficulty
    return total_value - interval, total_value + interval

def get_guess_from_user(usd_amount):
    while True:
        try:
            return float(input(f"Guess the value of ${usd_amount} in ILS: "))
        except ValueError:
            print("Invalid input.")

def play(diff):
    exchange_rate = get_exchange_rate()
    usd_amount = random.randint(1, 100)
    total_value = usd_amount * exchange_rate
    lower_int, upper_int = get_money_interval(total_value, diff)
    guess = get_guess_from_user(usd_amount)
    if lower_int <= guess <= upper_int:
        print("You guessed correctly!")
        return True
    else:
        print(f"""Better luck next time, The correct value was between {lower_int:.2f} and {upper_int:.2f}.
The exchange rate is {exchange_rate}.""")
        return False