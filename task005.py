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


