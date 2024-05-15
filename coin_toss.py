import random

def flip_coin():
    return 'Heads' if random.randint(0, 1) == 0 else 'Tails'

while True:
    print(f"The coin shows: {flip_coin()}")
    again = input("Do you want to flip again? (yes/no): ").lower()
    if again != 'yes':
        break
