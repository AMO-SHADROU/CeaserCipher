# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters", mode="r") as letter_file:
    letter = letter_file.read()
    for name in names:
        new_letter = letter.replace("[names]", name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
