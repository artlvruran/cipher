import random

from src.tools.crypters.crypter import Crypter


class VernamCrypter(Crypter):
    key = ''

    def __init__(self, key: str):
        self.key = key

    def encrypt(self, text: str) -> str:
        if self.key == '':
            self.key = [chr(random.randint(0, 255)) for _ in range(len(text))]
        result = ''
        count = 0
        for i in range(len(text)):
            if ord(text[i]) <= 255:
                result += chr(ord(text[i]) ^ ord(self.key[count % len(self.key)]))
                count += 1
            else:
                result += text[i]
        return result

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)




