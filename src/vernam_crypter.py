from src.crypter import Crypter


class VernamCrypter(Crypter):
    key: str

    def __init__(self, key: int):
        self.key = key

    def encrypt(self, text: str) -> str:
        result = ''
        for char in text:
            ...
# TODO
