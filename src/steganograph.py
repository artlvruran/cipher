from abc import ABC, abstractmethod
from src.constants import end_of_message


class Steganograph(ABC):
    path: str

    @abstractmethod
    def __init__(self, path: str):
        ...

    @staticmethod
    def byte_string(message: str) -> str:
        bytestring = ''.join([bin(ord(char))[2:] for char in message])
        bytestring += end_of_message
        return bytestring

    @staticmethod
    def get_message(byte_string: str) -> str:
        return ''.join([chr(int(byte_string[i:i+7], 2)) for i in range(0, len(byte_string), 7)])

