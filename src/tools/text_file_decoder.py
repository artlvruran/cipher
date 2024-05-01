from src.tools.crypters.crypter import Crypter
from src.tools.decoder_tool import DecoderTool


class TextFileDecoder(DecoderTool):
    crypter: Crypter

    def __init__(self, input_path: str, output_path: str):
        super().__init__(input_path, output_path)

    def get_file_text(self):
        with open(self.input_path, mode='r', encoding='utf-8') as input_file:
            return input_file.read()

    def encode(self):
        with open(self.input_path, mode='r', encoding='utf-8') as input_file:
            output_message = self.crypter.encrypt(input_file.read())
            with open(self.output_path, mode='w', encoding='utf-8') as output_file:
                output_file.write(output_message)

    def decode(self):
        output_message: str
        with open(self.input_path, mode='r', encoding='utf-8') as input_file:
            output_message = self.crypter.decrypt(input_file.read())
            if self.output_path != '':
                with open(self.output_path, mode='w', encoding='utf-8') as output_file:
                    output_file.write(output_message)
        return output_message
