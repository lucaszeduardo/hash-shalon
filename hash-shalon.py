import hashlib
import base64
import os
import sys
from time import sleep

def Md5(text):
    hash_complete = hashlib.md5(f'{text}'.encode()).hexdigest()

    return hash_complete

def Sha1(text):
    hash_complete = hashlib.sha1(f'{text}'.encode()).hexdigest()

    return hash_complete

def Bas64(text):
    byte_string = text.encode('utf-8')
    hash_complete = base64.b64encode(byte_string)

    return hash_complete

args = sys.argv

if len(args) == 2:

    list = args[1]

    file = open(list, 'r').readlines()
    os.system('clear')

    print('''
   )        (       )   (       )        (       )     )
 ( /(  (     )\ ) ( /(   )\ ) ( /(  (     )\ ) ( /(  ( /(
 )\()) )\   (()/( )\()) (()/( )\()) )\   (()/( )\()) )\())
 _((_)\ _ )\(_))  _((_) (_))  _((_)\ _ )\(_))   ((_) _((_)
| || (_)_\(_) __|| || | / __|| || (_)_\(_) |   / _ \| \| |
| __ |/ _ \ \__ \| __ | \__ \| __ |/ _ \ | |__| (_) | .` |
|_||_/_/ \_\|___/|_||_| |___/|_||_/_/ \_\|____|\___/|_|\_|

                            By: LucaSz
                                     CODE
''')



    myhash = input('DIGITE A HASH: ')

    print('''TIPOS DE HASHS:
[1]  MD5        [2]  SHA1
[3]  BASE64\n''')

    op = int(input('TIPO DA HASH: '))
    print()

    if op == 1:
        for fil in file:
            file_r = fil.replace('\n','')

            h = Md5(file_r)

            if myhash == h:
                print ('\n' + '\033[0;32m' + '[*] PASSWORD CRACKED: ' + '\033[0;32m' + f'{file_r}' + '\033[0;37m' + '\n')
                break
            else:
                print ('\033[0;31m' + '[!!?] PASSWORD INVALID: ' + '\033[0;31m' + f'{file_r}' + '\033[0;37m')
                sleep(1)
    elif op == 2:
        for fil in file:
            file_r = fil.replace('\n','')

            h = Sha1(file_r)

            if myhash == h:
                print ('\n' + '\033[0;32m' + '[*] PASSWORD CRACKED: ' + '\033[0;32m' + f'{file_r}' + '\033[0;37m' + '\n')
                break
            else:
                print ('\033[0;31m' + '[!!?] PASSWORD INVALID: ' + '\033[0;31m' + f'{file_r}' + '\033[0;37m')
                sleep(1)
    elif op == 3:
        twohash = myhash

        for fil in file:
            file_r = fil.replace('\n','')

            h = Bas64(file_r)
            string = str(h)
            a = string.replace('b','')
            b = str(a)
            c = b.replace(b[0], "")

            if twohash == c:
                print ('\n' + '\033[0;32m' + '[*] PASSWORD CRACKED: ' + '\033[0;32m' + f'{file_r}' + '\033[0;37m' + '\n')
                break
            else:
                print ('\033[0;31m' + '[!!?] PASSWORD INVALID: ' + '\033[0;31m' + f'{file_r}' + '\033[0;37m')
                sleep(1)
    else:
        print ('OPÇÃO INVALIDA.... ')
else:
    print('USE: python3 hash-shalon.py wordlist.txt')
