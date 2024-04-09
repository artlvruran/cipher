from src.crypter import Crypter
from src.constants import frequencies, en_alphabet, rus_alphabet


class CaesarCrypter(Crypter):
    offset: int
    alphabet: str
    positions: dict

    def __init__(self, offset: int, alphabet: str = en_alphabet):
        self.offset = offset
        self.alphabet = alphabet
        self.positions = dict()
        for i in range(len(alphabet)):
            self.positions[alphabet[i]] = i

    def encrypt(self, text: str) -> str:
        result = ''
        for char in text:
            if char.lower() in self.alphabet:
                if char.isupper():
                    result += self.alphabet[(self.positions[char.lower()] + self.offset) % len(self.alphabet)].upper()
                else:
                    result += self.alphabet[(self.positions[char] + self.offset) % len(self.alphabet)]
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        self.offset = -self.offset
        result = self.encrypt(text)
        self.offset = -self.offset
        return result


class CaesarHacker:
    alphabet: str

    def __init__(self, lang='en'):
        self.lang = lang
        self.alphabet = en_alphabet if lang == 'en' else rus_alphabet

    def difference(self, text: str) -> float:
        return sum(
            [
                abs(
                    text.count(letter) * 100 / len(text) - frequencies[letter]
                    )
                for letter in self.alphabet
            ]
        ) / len(self.alphabet)

    def break_cipher(self, text: str) -> int:
        min_difference = float('inf')
        encryption_key = 0

        for key in range(1, len(self.alphabet)):
            crypter = CaesarCrypter(key, self.alphabet)
            current_text = crypter.decrypt(text)
            current_difference = self.difference(current_text)

            if current_difference < min_difference:
                min_difference = current_difference
                encryption_key = key
        return encryption_key


    def hack(self, text: str, key: int) -> str:
        encryption_key = self.break_cipher(text)
        crypter = CaesarCrypter(key, self.mode)
        return crypter.encrypt(text)


