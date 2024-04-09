import argparse
from src.text_file_decoder import *
from src.crypter import *
from src.caesar_crypter import CaesarCrypter
from src.vernam_crypter import VernamCrypter
from src.vigenere_crypter import VigenereCrypter
from src.constants import *
from src.steganograph import *
from src.audio_steganograph import *
from src.image_steganograph import *

main_parser = argparse.ArgumentParser()

main_parser.add_argument('--mode',
                         choices=['encode', 'decode'],
                         default='encode')

tp = main_parser.add_argument('--type',
                              choices=['text', 'image', 'audio'],
                              default='text')


class TextAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        did_text = getattr(namespace, 'type', 'text')
        if did_text != 'text':
            parser.error('Text type is required')
        else:
            key = getattr(namespace, 'key', None)
            if key is None:
                setattr(namespace, self.dest, values)
            elif isinstance(key, int) and getattr(namespace, 'cipher', '') != 'caesar':
                parser.error('String key type is required')
            elif not isinstance(key, int) and getattr(namespace, 'cipher', '') == 'caesar':
                parser.error('Int key type is required')
            else:
                setattr(namespace, self.dest, values)


class SteganographAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        did_text = getattr(namespace, 'type', 'text')
        if did_text == 'text':
            parser.error('Text type is deprecated')
        else:
            output = getattr(namespace, 'output', '')
            mode = getattr(namespace, 'mode', '')
            if mode == 'encode' and output == '':
                parser.error('Output filename is required')
            else:
                setattr(namespace, self.dest, values)


main_parser.add_argument('--cipher',
                         choices=['caesar', 'vernam', 'vigenere'],
                         default='caesar',
                         action=TextAction)

main_parser.add_argument('--key',
                         action=TextAction)

main_parser.add_argument('--message',
                         type=str,
                         action=SteganographAction)

main_parser.add_argument('--input',
                         type=str,
                         required=True)

main_parser.add_argument('--output',
                         type=str)

args = main_parser.parse_args()

if args.type == 'text':
    decoder = TextFileDecoder(args.input, args.output)
    if args.cipher == 'caesar':
        decoder.crypter = CaesarCrypter(args.key)
    elif args.cipher == 'vernam':
        decoder.crypter = VernamCrypter(args.key)
    elif args.cipher == 'vigenere':
        decoder.crypter = VigenereCrypter(args.key)
    if args.mode == 'encode':
        decoder.encode()
    else:
        decoder.decode()
else:
    if args.type == 'audio':
        decoder = AudioSteganograph(args.input, args.output)
    else:
        decoder = ImageSteganograph(args.input, args.output)
    if args.mode == 'encode':
        decoder.encode(args.message)
    else:
        print(decoder.decode())
