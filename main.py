from src.caesar_crypter import *
from src.constants import en_alphabet
from src.image_steganograph import ImageSteganograph

steganograph = ImageSteganograph('saitama.png', 'hidden.png')
steganograph.encrypt('Hello')
steganograph.input_path = 'hidden.png'
print(steganograph.decrypt())
