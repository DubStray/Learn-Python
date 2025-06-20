from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):                               # Creo delle funzioni con i vari operatori matematici con la quale
    return num1 - num2                                  # la calcolatrice lavorerà.

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {                                          # Dictionary creato sfruttando i simboli cone key e il titolo della
    "+": add,                                           # funzione stessa come value.
    "-": subtract,
    "*": multiply,                                      # Questa cosa è fatta in modo tale che nell'input poi l'utente potrà
    "/": divide                                         # inserire i simboli per scegliere l'operatore.
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
                                                        # For loop che itera attraverso il dictionary per printare tutta la lista di operatori disponibili
                                                        # seguito poi dall'input con la quale l'utente interagirà.
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
                                                        # Quella sotto è un variabile che prende i simboli nel dictionary e tramite i [] prende l'input richiesto.
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)       # Poi tramite quest'altra variabile si va appunto a calcolare.
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating {result}, or type 'n' to to start a new calculation.: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()