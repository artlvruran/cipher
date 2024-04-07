from src.caesar_crypter import *
from src.constants import en_alphabet
from src.image_steganograph import ImageSteganograph

steganograph = ImageSteganograph('saitama.png')
steganograph.encrypt('Hello')
steganograph = ImageSteganograph('saitama(1).png')
print(steganograph.decrypt())
