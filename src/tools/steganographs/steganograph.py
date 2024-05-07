from abc import abstractmethod

from src.constants import end_of_message
from src.tools.decoder_tool import DecoderTool


class Steganograph(DecoderTool):

    def __init__(self, input_path: str, output_path: str):
        super().__init__(input_path, output_path)

    @staticmethod
    def byte_string(message: str) -> str:
        bytestring = ''.join([bin(ord(char))[2:].rjust(16, '0') for char in message])
        bytestring += end_of_message
        return bytestring

    @staticmethod
    def get_message(byte_string: str) -> str:
        return ''.join([chr(int(byte_string[i:i+16], 2)) for i in range(0, len(byte_string), 16)])

    @abstractmethod
    def encode(self, message: str):
        ...

    @abstractmethod
    def decode(self) -> str:
        ...

