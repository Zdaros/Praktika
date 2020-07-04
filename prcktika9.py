# Priklad 1
import os.path # Модуль, який містить функції для роботи з шляхом у файловій системі
text = '''Hello!
I am a text file. And I had been written with a Python
script
before you opened me, so look up the docs and try to delete
me using Python, too.'''
def write_text_to_file(filename, text):
 """Функція для запису у файл filename рядка text"""
 f = open(filename, "w") # відкриття файла для запису
 f.write(text) # Запис рядка text у файл
 f.close() # Закриття файлу
if __name__ == '__main__':
 write_text_to_file(os.path.join('data', 'example01.txt'), text)

# Priklad 2
import datetime
text = '''This text was added in example 2!
Updated
'''
if __name__ == '__main__':
 log_file = os.path.join('data', 'example01.txt')
 with open(log_file, 'a') as log:
  print('\n', text, str(datetime.datetime.now()), file=log)

# Priklad 3
def read_file(fname):
 """Функція для зчитування файла fname
 та виведення його вмісту на екран"""
 file = open(fname, 'r') # відкриття файлу для зчитування
 print('File ' + fname + ':') # виведення назви файлу
 # зчитування вмісту файла по рядках
 for line in file:
  print(line, end='') # виведення рядка s
 file.close() # закриття файлу
if __name__ == '__main__':
 # функція os.path.join з'єднує частини шляху у файловій системі
 # необхідним роздільником
 read_file(os.path.join('data', 'example01.txt'))

# Task 1
import os

while True:
    File_name = input("Enter file name: ")
    mod = input("Read 1 Add data 2 rewrite 3  serch for file 4 sercg for data in file 5 else exit")
    if mod == '1':
        try:
            f = open("data/"+File_name, "r")
            print(f.read())
        except FileNotFoundError:
                continue
    elif mod == '2':
        try:
            f = open("data/"+File_name, "w")
            f.write(input("What to re write:"))
        except FileNotFoundError:
                continue
    elif mod == '3':
        try:
            f = open("data/"+File_name, "a")
            f.write(input("What to re write:"))
        except FileNotFoundError:
                continue
    elif mod == '4':
        try:
            files = os.listdir("data/")
            for f in files:
                print(f)
            f = open("data/"+File_name, "r")
        except FileNotFoundError:
                continue
    elif mod == '5':
        search = input("What are you searching for: ")
        line_num = 0
        try:
            f = open("data/"+File_name, "r")
            Lines = f.readlines()
            for line in Lines:
                line_num += 1
                if search in str(line):
                    print("there is sach data at line", line_num)
                    break
                else:
                    print("There is no sach data in this file")
                    break
        except FileNotFoundError:
                continue
    else:
       break
    f.close()

# Task 2

f = open("data/task2.txt", "r")
Lines = f.readlines()
f.close()

num_a = 0
num_i = 0
num_i5 = 0

for line in Lines:
    if str(line)[0] == "A" or str(line)[0] == 'a':
        num_a += 1
    for i in range(len(str(line))):
        if str(line)[i] == 'i':
            num_i += 1
    if num_i == 5:
        num_i5 += 1
        num_i = 0
    else:
        num_i = 0
print(num_a)
print(num_i5)
