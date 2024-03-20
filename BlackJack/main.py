from art import logo
import random

print(logo)

cards = {"ace": [11, 1], "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
         "j": 10, "Q": 10, "k": 10}
game_is_on = True
user_hand = []
dealer_hand = []


def show_hands():
    print("Your hand: ")
    print(user_hand)
    print("Dealer's first card: ")
    print(dealer_hand[0])


def new_round():
    random_key = random.choice(list(cards.keys()))
    random_value = cards[random_key]
    if random_key == "ace":
        user_ace_choice = int(input("Do you want to go with 1 or 11 for ace? "))
        random_value = user_ace_choice
    user_hand.append(random_value)
    random_key = random.choice(list(cards.keys()))
    random_value = cards[random_key]
    if random_key == "ace" and sum(dealer_hand) < 21:
        random_value = 11
    elif random_key == "ace":
        random_value = 1
    dealer_hand.append(random_value)
    show_hands()


def check_hands():
    global game_is_on
    if sum(user_hand) > 21:
        print("Sorry dealer wins!")
        game_is_on = False
    if sum(dealer_hand) > 21:
        print("You've won!")
        game_is_on = False


new_round()

while game_is_on:
    user_choice = input("Do you want to continue? (y/n): ").lower()
    check_hands()
    if user_choice == "y":
        new_round()
        check_hands()
    elif user_choice == "n":
        check_hands()
        if sum(dealer_hand) < 17:
            dealer_hand.append(random.choice(list(cards.keys())))
        if sum(user_hand) == 21 or sum(user_hand) > sum(dealer_hand):
            print("You won!")
            game_is_on = False
        elif sum(dealer_hand) > sum(user_hand):
            print("You lose!")
            game_is_on = False
