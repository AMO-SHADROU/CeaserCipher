import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
dict1 = {row.letter: row.code for index, row in df.iterrows()}


def generate_phonetic_alphabet():
    user_word = input('Enter a word: ').upper()
    try:
        user_letter = [dict1[letter] for letter in user_word]
    except KeyError:
        print('Sorry, only letters are allowed')
        generate_phonetic_alphabet()
    else:
        print(user_letter)

