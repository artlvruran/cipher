from src.steganograph import Steganograph
from src.constants import *
import wave


class AudioSteganograph(Steganograph):
    input_path: str
    output_path: str

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

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

    def encrypt(self, message: str):
        byte_message = self.byte_string(message)
        self.modify_audio(byte_message)

    def decrypt(self) -> str:
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

