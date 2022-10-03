# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на 
# определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, 
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

import shutil
from dataclasses import replace
import re
from tkinter.filedialog import askopenfilename
from pathlib import Path
from dataclasses import replace
import shutil

def encrypt_caesar(msg, shift=3):
    small_symbols1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big_symbols1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small_symbols1)
    small_symbols2 = small_symbols1[shift:] + small_symbols1[:shift]
    big_symbols2 = big_symbols1[shift:] + big_symbols1[:shift]
    translation = msg.maketrans(small_symbols1 + big_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)
 
 
def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)

def overwriting_file(a,shift):
    str_new=[]
    student=open(a, 'r', encoding="utf-8")
    while True:
        line = student.readline()
        if not line:
            break
        line=encrypt_caesar(line,shift)
        str_new.append(line)
    student.close()
    student_new=open('student_new.txt', 'w',encoding="utf-8")
    for element in str_new:
        student_new.write(element)
    student_new.close()
    shutil.copyfile('student_new.txt', a)
   
shift=int(input("введите величину сдвига : "))
filename = askopenfilename()
filename: Path = Path(filename)
overwriting_file(filename,shift)