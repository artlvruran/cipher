import wave

from src.constants import *
from src.tools.steganographs.steganograph import Steganograph


class AudioSteganograph(Steganograph):

    def __init__(self, input_path: str, output_path: str):
        super().__init__(input_path, output_path)

    def modify_audio(self, message: str):
        audio = wave.open(self.input_path, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

        for i, bit in enumerate(message):
            frame_bytes[i] = (frame_bytes[i] & 254) | int(bit)

        output = wave.open(self.output_path, mode='wb')
        output.setparams(audio.getparams())
        output.writeframes(bytes(frame_bytes))

        audio.close()
        output.close()

    def encode(self, message: str):
        byte_message = self.byte_string(message)
        self.modify_audio(byte_message)

    def decode(self) -> str:
        audio = wave.open(self.input_path, mode='rb')
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
        least_significant_bits = [byte & 1 for byte in frame_bytes]

        audio.close()
        byte_string = ""
        for bit in least_significant_bits:
            byte_string += str(bit)
            if len(byte_string) >= len(end_of_message):
                if byte_string[-len(end_of_message):] == end_of_message:
                    return self.get_message(byte_string[:-len(end_of_message)])

        return self.get_message(byte_string[:-len(end_of_message)])
