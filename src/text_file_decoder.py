from src.decoder_tool import DecoderTool
from abc import ABC, abstractmethod
from src.crypter import Crypter


class TextFileDecoder(DecoderTool):
    crypter: Crypter

    def __init__(self, input_path: str, output_path: str):
        super().__init__(input_path, output_path)

    def encode(self):
        with open(self.input_path, mode='r') as input_file:
            output_message = self.crypter.encrypt(input_file.read())
            with open(self.output_path, mode='w') as output_file:
                output_file.write(output_message)

    def decode(self):
        pass
