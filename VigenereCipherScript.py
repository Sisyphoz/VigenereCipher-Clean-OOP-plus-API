class VigenereCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.vigenere_square = [[self.alphabet[(i + j) % 26] for i in range(26)] for j in range(26)]

    def clean_text(self, text):
        cleaned_text = "".join([char for char in text if char.isalpha()]).upper()
        return cleaned_text

    def repeat_key(self, key, length):
        repeated_key = (key * (length // len(key) + 1))[:length]
        return repeated_key

    def encrypt(self, plaintext, key):
        cleaned_plaintext = self.clean_text(plaintext)
        cleaned_key = self.clean_text(key)
        repeated_key = self.repeat_key(cleaned_key, len(cleaned_plaintext))
        ciphertext = ""

        for i in range(len(cleaned_plaintext)):
            plaintext_char = cleaned_plaintext[i]
            key_char = repeated_key[i]

            row = self.alphabet.index(plaintext_char)
            col = self.alphabet.index(key_char)
            ciphertext_char = self.vigenere_square[row][col]

            ciphertext += ciphertext_char

        return ciphertext

    def decrypt(self, ciphertext, key):
        cleaned_ciphertext = self.clean_text(ciphertext)
        cleaned_key = self.clean_text(key)
        repeated_key = self.repeat_key(cleaned_key, len(cleaned_ciphertext))
        plaintext = ""

        for i in range(len(cleaned_ciphertext)):
            ciphertext_char = cleaned_ciphertext[i]
            key_char = repeated_key[i]

            row = self.alphabet.index(key_char)
            col = self.vigenere_square[row].index(ciphertext_char)
            plaintext_char = self.alphabet[col]

            plaintext += plaintext_char

        return plaintext


vc = VigenereCipher()

plaintext = "Fresh magdalenas are amazing. Maybe not?"
key = "SECRET"

ciphertext = vc.encrypt(plaintext, key)
print(ciphertext)

decrypted_plaintext = vc.decrypt(ciphertext, key)
print(decrypted_plaintext)
