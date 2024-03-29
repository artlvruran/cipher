from src.caesar_crypter import *
from src.constants import en_alphabet

s = "Zai itqz u tmhq kagd mffqzfuaz, wzai ftue. Itmfqhqd kag nguxp tqdq, kag iuxx fqef bqdeazmxxk"

hacker = CaesarHacker()
offset = hacker.break_cipher(s)
crypter = CaesarCrypter(offset, en_alphabet)
print(crypter.decrypt(s.lower()))