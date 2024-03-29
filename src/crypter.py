from abc import ABC, abstractmethod


class Crypter(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def encrypt(self, text: str) -> str:
        ...


    @abstractmethod
    def decrypt(self, text: str) -> str:
        ...