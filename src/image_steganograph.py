import base64

from src.steganograph import Steganograph
from PIL import Image, ImageDraw
from abc import ABC, abstractmethod
from src.constants import end_of_message


class ImageSteganograph(Steganograph):
    image: Image
    draw: ImageDraw
    pixels: Image
    width: int
    height: int

    def __init__(self, path: str):
        self.image = Image.open(path)
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pixels = self.image.load()
        self.path = path

    def modify_pixels(self, message: str):
        not_encoded = len(message)
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pixels[i, j]
                for number, color in enumerate([r, g, b]):
                    if not_encoded > 0:
                        self.pixels[i, j] = self.pixels[i, j][:number] + \
                                            (int(bin(color)[2:-1] + message[len(message) - not_encoded], 2),) + \
                                            self.pixels[i, j][number + 1:]
                        self.draw.point((i, j), self.pixels[i, j])
                        not_encoded -= 1
        self.image.save(self.path[:self.path.rfind('.')] + '(1)' + self.path[self.path.rfind('.'):])

    def encrypt(self, message: str):
        byte_message = self.byte_string(message)
        self.modify_pixels(byte_message)

    def decrypt(self) -> str:
        message_data = ''
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pixels[i, j]
                for color in [r, g, b]:
                    message_data += bin(color)[-1]
                    if len(message_data) >= len(end_of_message):
                        if message_data[-len(end_of_message):] == end_of_message:
                            return self.get_message(message_data[:-len(end_of_message)])
        return self.get_message(message_data[:-len(end_of_message)])
