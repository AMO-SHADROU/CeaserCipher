import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
dict1 = {row.letter: row.code for index, row in df.iterrows()}

user_word = input('Enter a word: ').upper()
user_letter = [dict1[letter] for letter in user_word]

print(user_letter)
