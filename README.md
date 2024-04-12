# Сipher
## Описание
Приложение для зашифровки/расшифровки файлов различного формата
## Функционал
1. Шифрование и дешифрование текстовых файлов шифрами Цезаря, Виженера, Вернама и возможно другими
2. Стеганография над bmp, jpg, png, mp3, wav
3. Графический интерфейс через PyQt
4. Возможность работы с командной строкой
## Архитектура
Примерная диаграмма классов 
![cipher Class diagram](https://github.com/artlvruran/cipher/blob/documentation/cipher%20Class%20diagram.png)
1. Crypter - класс-интерфейс шифрования/дешифрования текста. Его реализации отвечают за конкретные алгоритмы шифрования.   
  - encrypt() - зашифровывает текст
  - decrypt() - расшифровывает текст
2. DecoderTool - класс-интерфейс для шифрования/дешифрования файлов. Его реализации отвечают за соответствующие типы файлов
  - encode() - зашифровывает файл
  - decode() - расшифровывает файл
## Работа с командной строкой
``` bash
usage: cipher.py [-h] [--mode {encode,decode}] [--type {text,image,audio}] [--cipher {caesar,vernam,vigenere}] [--key KEY] [--hack | --no-hack] [--message MESSAGE] --input INPUT [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --mode {encode,decode}
                        Enable encode/decode mode
  --type {text,image,audio}
                        Choose file type
  --cipher {caesar,vernam,vigenere}
                        Select cipher. Requires text file type
  --key KEY             Cipher key
  --hack, --no-hack     Automatically determine cipher key. Requires --cipher=caesar
  --message MESSAGE     Message to encrypt
  --input INPUT         input file path
  --output OUTPUT       output file path
```

