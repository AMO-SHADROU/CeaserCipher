import random
from gui import gui, logo

print(logo)

with open("words.csv", mode='r') as words:
    words_list = words.readlines()

random_word = random.choice(words_list).strip("\n")

display = []

for _ in range(len(random_word)):
    display.append("_")

lives = 7

while lives > 0:
    print(gui[lives - 1])
    if "_" not in display:
        print("You won")
        break
    else:
        user_letter = input("Enter a letter: ").lower()
        if user_letter not in random_word:
            lives -= 1
        else:
            for index, letter in enumerate(random_word):
                if user_letter == random_word[index]:
                    display[index] = letter
    print(display)

print(f"You lose!!!\n The word was this: {random_word}")
