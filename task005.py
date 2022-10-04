# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def rle_encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding

def rle_decode(data): 
    decode = '' 
    count = ''
    for char in data: 
        if char.isdigit():
           count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

with open('file_first.txt', 'w') as data:
    data.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

with open('file_first.txt', 'r') as file:
    first_string = file.read()

compressed_text=rle_encode(first_string)

with open('file_second.txt', 'w') as file:
    decoded_string = rle_decode(compressed_text)
    file.write(decoded_string)

print('First string: \t\t' + first_string)
print('Decode string: \t\t' + decoded_string)
print('Compressed_text:\t' + compressed_text)
print(f'Compress ratio: \t {round(len(first_string) / len(compressed_text), 1)}')

