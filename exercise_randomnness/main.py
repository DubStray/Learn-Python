import random
coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])



def somma(num1, num2):
    return num1 + num2

print(int(somma(1, 2)))