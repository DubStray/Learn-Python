alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction.lower() == "encode":

    # Blocco per creare un messaggio criptato.
    def encrypt(plain_text, shift_amount): # Creo una funzione che riprende i comandi 'text' e 'shift'.
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter) # Con .index() vado a trovare l'indice della lettera e il suo numero.
            new_position = position + shift_amount # In questo modo si fa l'addizione tra la posizione della lettera e la 'shifta' di un numero dato dall'input.
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    encrypt(plain_text=text, shift_amount=shift)

else:

    # Blocco per decrittare un messaggio criptato.
    def decrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount # La posizione delle lettere devono tornare normali, quindi al contrario si usa il -
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The decrypted text is {cipher_text}")

    decrypt(plain_text=text, shift_amount=shift)
