from logo import logo

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encrypt(plaintext, shift):
    encrypted_text = []
    for char in plaintext.lower():
        if char in alphabet:
            index = alphabet.index(char)+shift
            while index > 26:
                index -= 26
            while index < 0:
                index += 26
            encrypted_text.append(alphabet[index])
        else:
            encrypted_text.append(char)
    encrypted_text = "".join(encrypted_text)
    return encrypted_text


def decrypt(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext.lower():
        if char in alphabet:
            index = alphabet.index(char)-shift
            while index > 26:
                index -= 26
            while index < 0:
                index += 26
            decrypted_text.append(alphabet[index])
        else:
            decrypted_text.append(char)
    decrypted_text = "".join(decrypted_text)
    return decrypted_text


running = True
print(logo)

while running:
    mod = input("Do you want to encrypt or decrypt?  ").lower().strip()
    if mod == "encrypt":
        text = input("Enter the text to encrypt: ")
        shift_amount = int(input("Enter the shift amount: "))
        print(f"Encrypted text is {encrypt(text, shift_amount)}")
    elif mod == "decrypt":
        text = input("Enter the text to decrypt: ")
        shift_amount = int(input("Enter the shift amount: "))
        print(f"Decrypted text is {decrypt(text, shift_amount)}")
    continue_flag = input("Do you want to continue? yes or no : ").lower().strip()
    if continue_flag == "no":
        running = False
        print("Goodbye!")

