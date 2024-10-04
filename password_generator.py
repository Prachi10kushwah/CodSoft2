import secrets

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F',
                     'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '^', '*', '+']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to password generator")
uppercase = int(input("\nHow many uppercase letters you want in your password? "))
lowercase = int(input("How many lowercase letters you want in your password? "))
symbol = int(input("How many symbols you want in your password? "))
number = int(input("How many numbers you want in your password? "))

password = ""

for i in range(uppercase):
    password += secrets.choice(uppercase_letters)

for i in range(symbol):
    password += secrets.choice(symbols)

for i in range(lowercase):
    password += secrets.choice(lowercase_letters)

for i in range(number):
    password += secrets.choice(numbers)


password_list = list(password)
secrets.SystemRandom().shuffle(password_list)
final_password = ''.join(password_list)

print("Generated Password:", final_password)