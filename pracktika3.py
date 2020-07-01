# Priklad 1

# Параметр i приймає значення
for i in range(10):
    print('i =', i)
# Параметр i приймає значення
for i in range(5, 10):
    print('i =', i)
# Параметр i приймає значення в діапазоні [5, 10) з кроком 2
for i in range(5, 10, 2):
    print('i =', i)
# Цикл буде повторюватися 3 рази, якщо користувач не завершить його раніше
for i in range(3):
    response = input('Введіть stop, щоб зупинити цикл(інакше що завгодно): ')
    if response == 'stop':
        break
    else:
        # цю гілку виконують тільки якщо цикл не був перерваний
        print('Цикл сам був завершений')
print('Кінець програми')
# Функція reversed дозволяє обходити послідовність в зворотномунапрямку
for i in reversed(range(5)):
    print(i)
print()

# Priklad 2

# Створення списку чисел
my_list = [5, 7, 9, 1, 1, 2]
# Отримання передостаннього значення
pre_last = my_list [-2] # pre_last == «1»
print(pre_last)
# Обчислення суми першого і останнього значень
result = my_list[0] + my_list[-1];
print(result)

my_list = [5, 7, 9, 1, 1, 2] # Створення списку чисел
# Отримання зрізу списка від нульового (першого) елемента # включаючи його) до третього (четвертого) (не включаючи)
sub_list = my_list[0:3]
print(sub_list) # Виведення отриманого списку
# Виведення елементів списка від другого до передостаннього
print(my_list[2:-2])
# Виведення ел-тів списка від 4-ого (5-ого) до 5-ого (6-ого)
print(my_list[4:5])
my_list = [5, 7, 9, 1, 1, 2]
# Вибір кожного другого ел-та списку (починаючи з першого),
# не включаючи останній елемент
sub_list = my_list[0:-1:2]
print(sub_list) # виведення отриманого списку
# Виведення елементів від 2-ого (3-ього) до передостаннього # з кроком 2
print(my_list[2:-2:2])
# Виведення ел-тів списка, крім першого, в зворотному порядку
print(my_list[-1:0:-1])
my_list=[5, 7, 9, 1, 1, 2]
# Виведення елементів списка від 2-ого (3-ього) значення до кінця
print(my_list[2:])
# Виведення всіх ел-тів списка від початку до передостанньогоел-та
print(my_list[:-2])
# Виведення всіх елементів списку в зворотному порядку
print(my_list[::-1])
print()

# Priklad 3

import random
arr1 = []
arr = random.sample(range(-6, 6), 12)
print("ourrandom list: ", arr)
flag = 0
while flag == 0:
    if 0 in arr: # перевіряємо чи є 0 в списку
        first_zero_index = arr.index(0) # індекс першого 0
        flag = 1;
    else:
        print("we have not at list one zero in list: ")
        arr1 = []
if flag == 1:
    for i in arr[first_zero_index:]:
        arr1.append(i)
        print(arr1)
print()
# Task 1

b_array = [0, 0, 1, 0, 2, 3, 0, 4, 5, 6, 7, 8, 0, 0, 24, 4, 0, 1]
length = len(b_array)
sorted_array = []
num_zero = 0

for i in b_array:
    if i == 0:
        num_zero += 1
    else:
        sorted_array.append(i)
for i in range(0,num_zero):
    sorted_array.append(0)

print(sorted_array)

# Task 2
print()
matrix = [[1,24,5,6],[25,6,5,123],[0,3,29,69],[85,4,0,11]]
for i in matrix:
    print(i)
min_sum = 0
sum_of_elements = 0
first_run_flag = True
for i in matrix:
    for y in i:
        sum_of_elements += y
    if min_sum > sum_of_elements and first_run_flag == False:
        min_sum = sum_of_elements
    if first_run_flag:
        min_sum = sum_of_elements
        first_run_flag = False
    sum_of_elements = 0
print(min_sum)
