MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def splash_screen():
    '''Fa vedere la welcome page della macchinetta del caffè con tutte le opzioni disponibili'''

    print('''
        Welcome to the coffee machine!
        
        ----MENU----
        Espresso: 1.50$
        Latte: 2.50$
        Cappuccino: 3.00$
        ------------
        
        Type 'report' to check the resources
        Type 'off' to log out from the machine
        ''')

def show_report():
    '''Opzione di report che permette di mostrare le resources disponibili della macchinetta'''

    print("Resources: ")
    for k in resources:
        print(k)
        print(resources[k])

def main():
    splash_screen()

    user_choose = input("        Type here: ")
    if user_choose.lower() == "report":
        show_report()
    if user_choose.lower() == "off":
        # Rompere il loop