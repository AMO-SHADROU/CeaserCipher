from art import logo

print(logo)
operations = ["+", "-", "/", "*"]

num1 = int(input("Enter a number: "))
for operation in operations :
    print(operation)
operation = input("Enter a operation: ")
num2 = int(input("Enter a number: "))


def calc(num1, num2) :
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2


end = False
answer = calc(num1, num2)

while not end:
    print(answer)
    user_input = input(f"If you want to continue with previews answer {answer} enter yes\n").lower()
    if user_input == "yes":
        operation = input("Enter a operation: ")
        new_num = int(input("Enter new number: "))
        answer = calc(answer, new_num)
    else:
        end = True
        print("Thanks for using this program :) ")
