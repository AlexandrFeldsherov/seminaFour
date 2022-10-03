# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

import shutil
from dataclasses import replace
import re
from tkinter.filedialog import askopenfilename
from pathlib import Path
from dataclasses import replace
import shutil

from dataclasses import replace
import re
import shutil

str_new=[]
student=open('student.txt', 'r', encoding="utf-8")
while True:
        line = student.readline()
        if not line:
            break
        num = re.findall('(\d+)', line)
        num = int(num[0])
        if num > 4:
            str_new.append(line.upper())
        else:
            str_new.append(line)
student.close()
student_new=open('student_new.txt', 'w',encoding="utf-8")
for element in str_new:
     student_new.write(element)
student_new.close()
shutil.copyfile('student_new.txt', 'student.txt')