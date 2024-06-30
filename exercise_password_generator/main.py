import random

def clean():
    print("\n" * 5)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Password Generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))

# Si crea una variabile con una lista vuota che si riempie in base agli input.
password_list = []
for i in range(1, nr_letters + 1):
    random_l = random.choice(letters)
    password_list += random_l

for i in range(1, nr_symbols + 1):
    random_s = random.choice(symbols)
    password_list += random_s

for i in range(1, nr_numbers + 1):
    random_n = random.choice(numbers)
    password_list += random_n

# Si fa uno shuffle della lista creata e riempita prima.
random.shuffle(password_list)

# Ed infine si crea una varibile di stringa vuota che verrà riempita con un for loop.
password = ""
for char in password_list:
    password += char

clean()
print(f"Your password is {password}")