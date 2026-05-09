#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction):
    cipher_text = ""
    if direction == "encode":
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % 26
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")

    elif direction == "decode":
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position = shifted_position % 26
            cipher_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {cipher_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("How many times would you like to shift your alphabets?\n"))
    caesar(original_text=text, shift_amount=shift, direction=direction)
    next = input("Type yes to continue else type no: ").lower()
    if next == "no":
        break