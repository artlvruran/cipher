from PIL import Image, ImageDraw

from src.constants import end_of_message
from src.tools.steganographs.steganograph import Steganograph


class ImageSteganograph(Steganograph):

    def __init__(self, input_path: str, output_path: str):
        super().__init__(input_path, output_path)

    def modify_pixels(self, message: str):

        image = Image.open(self.input_path)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()

        not_encoded = len(message)
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                for number, color in enumerate([r, g, b]):
                    if not_encoded > 0:
                        pixels[i, j] = pixels[i, j][:number] + \
                                        (int(bin(color)[2:-1] + message[len(message) - not_encoded], 2),) + \
                                        pixels[i, j][number + 1:]
                        draw.point((i, j), pixels[i, j])
                        not_encoded -= 1
        image.save(self.output_path)

    def encode(self, message: str):
        byte_message = self.byte_string(message)
        self.modify_pixels(byte_message)

    def decode(self) -> str:

        image = Image.open(self.input_path)
        width = image.size[0]
        height = image.size[1]
        pixels = image.load()

        message_data = ''
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                for color in [r, g, b]:
                    message_data += bin(color)[-1]
                    if len(message_data) >= len(end_of_message):
                        if message_data[-len(end_of_message):] == end_of_message:
                            return self.get_message(message_data[:-len(end_of_message)])
        return self.get_message(message_data[:-len(end_of_message)])
