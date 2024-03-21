import art
from data import data
import random

print(art.logo)
score = 0
wrong = False


def random_item():
    random_case = random.choice(data)
    print(f"{random_case['name']} a {random_case['description']} from {random_case['country']} ")
    return random_case['follower_count']


while not wrong:
    item1 = random_item()
    print(art.vs)
    item2 = random_item()
    if item1 == item2:
        print("\033c")  # CLear terminal
        continue
    user_input = input("Which one has more followers? 1 or 2   ")
    if user_input == "1" and item1 > item2:
        print("right answer !!!")
        score += 1
        print(f"Your score is {score}")
    elif user_input == "2" and item2 > item1:
        print("right answer !!!")
        score += 1
        print(f"Your score is {score}")
    else:
        print(f"wrong answer your answer: {score}")
        wrong = True
