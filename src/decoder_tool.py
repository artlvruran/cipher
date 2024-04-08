from abc import ABC, abstractmethod


class DecoderTool(ABC):
    input_path: str
    output_path: str

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

