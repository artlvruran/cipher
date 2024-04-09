from src.crypter import Crypter
from src.constants import en_alphabet
from random import choice
from src.steganograph import Steganograph
import random


class VernamCrypter(Crypter):
    key = ''

    def encrypt(self, text: str) -> str:
        byte_string = Steganograph.byte_string(text)
        if self.key == '':
            self.key = [chr(random.randint(0, 255)) for _ in range(len(text))]
        result = ''
        for i in range(len(text)):
            if ord(text[i]) <= 255:
                result += ord(text[i]) ^ ord(self.key[i])
            else:
                result += text[i];
        return result

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)




