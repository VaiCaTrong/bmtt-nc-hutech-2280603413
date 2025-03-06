from Cipher.Caesar import Alphabet

class CaesarCipher:
    def __init_(self):
        self.Alphabet = Alphabet
        
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.Alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.Alphabet.index(letter)
            output_index = (letter_index+key) % alphabet_len
            output_letter = self.Alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text:str, key:int) -> str:
        Alphabet_len = len(self.Alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.Alphabet.index(letter)
            output_index = (letter_index - key) % Alphabet_len
            output_letter = self.Alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)
    
    