from src.caesar_crypter import *
from src.constants import en_alphabet
from src.image_steganograph import ImageSteganograph
from src.audio_steganograph import AudioSteganograph

steganograph = AudioSteganograph('onepunchman_-_Opening_1_71148983.wav', 'hidden.wav')
#steganograph.encrypt('Hello')
steganograph.input_path = 'hidden.wav'
print(steganograph.decrypt())