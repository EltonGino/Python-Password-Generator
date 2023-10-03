import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Python Password Generator!")
user_letters = int(input("Quantas letras você gostaria de ter na sua senha? \n"))
user_numbers = int(input("Quantos números você gostaria de ter na sua senha? \n"))
user_symbols = int(input("Quantos símbolos você gostaria de ter na sua senha? \n"))

password_list = []

for char in range(1, user_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, user_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, user_symbols + 1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"A sua senha é: {password}")