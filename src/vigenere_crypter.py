from src.crypter import Crypter
from abc import ABC, abstractmethod
from src.constants import en_alphabet


class VigenereCrypter(Crypter):
    key = ''
    alphabet: str
    positions: dict

    def __init__(self, key: str, alphabet: str = en_alphabet):
        self.key = key
        self.alphabet = alphabet
        self.positions = dict()
        for i in range(len(alphabet)):
            self.positions[alphabet[i]] = i

    def decrypt(self, text: str) -> str:
        old_key = self.key
        new_key = ''.join([self.alphabet[(-self.positions[elem]) % len(self.alphabet)] for elem in self.key])
        self.key = new_key
        result = self.encrypt(text)
        self.key = old_key
        return result

    def encrypt(self, text: str) -> str:
        result = ''
        count = 0
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    result += self.alphabet[(self.positions[text[i].lower()] +
                                             self.positions[self.key[count % len(self.key)]]) %
                                            len(self.alphabet)].upper()
                else:
                    result += self.alphabet[(self.positions[text[i]] +
                                             self.positions[self.key[count % len(self.key)]]) %
                                            len(self.alphabet)]
                count += 1
            else:
                result += text[i]
        return result
