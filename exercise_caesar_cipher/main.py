alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


from art import logo
print(logo)


# Funzione che racchiude la funzionalità di encode e di decode.
def caesar(start_text, shift_amount, cipher_direction):

    final_text = "" # Si crea una variabile di testo vuota da riempire col messaggio.

    if cipher_direction == "decode": 
        shift_amount *= -1 # Il '*=' sta a significare 'moltiplica' quindi il numero dell'input moltiplicato per -1 sarà sempre lo stesso numero ma in negativo.
        # Immagina questo sopra come: 5 * -1 = -5

    for char in start_text: # start_text prende l'input di di 'text', quindi per 'char=carattere in text.

        if char in alphabet: # Se quel carattere è nell'alfabeto...

            position = alphabet.index(char) # Variabile che utilizza il .index() per trovare l'indice della lettera.

            new_position = position + shift_amount # Quindi nella posizione attuale della lettera si aggiungerà lo 'shift' dell'input, e quindi verrà 'shiftata' di tot numeri.

            final_text += alphabet[new_position] # Si riempie quindi il final_text con le lettere shiftate.
        else:
            final_text += char # Se quel carattere non è nell'alfabeto allora lo "aggiunge" momentaneamente.
    print(f"Here's the {direction}d result: {final_text}")


# Blocco per iniziare un ciclo per far ripartire o chiudere il codice.
code_ending = False
while not code_ending: # Mentre il codice funziona fa tutto il resto.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 # L'input viene usato per sottratto di 26 ogni volta fino il risultato non è minore di 26 e quindi la frase viene 'shiftato' di quel numero.

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


    restart = input("You want to use the Caesar Cipher again? Y/N ")
    if restart == "n":
        code_ending = True
        print("Goodbye.")