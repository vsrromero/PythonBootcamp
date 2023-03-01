import string

alphabet = list(string.ascii_lowercase)

def caesar(direction, text, shift):

    def encrypt(text, shift):
        encrypted_message = ''
        for char in text:
            if char in alphabet:
                char_index = alphabet.index(char)
                shifted_index = (char_index + shift) % 26
                encrypted_char = alphabet[shifted_index]
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        print(f'The encoded text is: {encrypted_message}')

    def decrypt(text, shift):
        decrypted_message = ''
        for char in text:
            if char in alphabet:
                char_index = alphabet.index(char)
                shifted_index = (char_index - shift) % 26
                decrypted_char = alphabet[shifted_index]
                decrypted_message += decrypted_char
            else:
                decrypted_message += char   
        print(f'The decoded text is: {decrypted_message}')

    if direction == 'encode':
        encrypt(text=text, shift=shift)
    else:
        decrypt(text=text, shift=shift)