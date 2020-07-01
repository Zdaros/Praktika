# Priklad 1

my_set = {4, 5, 1, 2}
# Кількість елементів множини
print('len({}) = {}'.format(my_set, len(my_set)))
# Перевірка входження елемента
print(4 in my_set)
print(3 not in my_set)
print(9 in my_set)
# Чи перетинаються множини
print({3, 4, 5}.isdisjoint({8, 1, 0}))
print({3, 4, 5}.isdisjoint({1, 2, 3}))
# Перевірка включення однієї множини в іншу
print({1, 7, 9}.issubset({1, 2, 3, 7, 9}))
print({1, 7, 9} <= {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} <= {1, 2, 3, 7, 9})
# Перевірка чіткого включення
print({1, 7, 9} < {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} < {1, 2, 3, 7, 9})
# Перевірка включення однієї множини в іншу
print({1, 2, 3, 4}.issuperset({1, 2}))
print({1, 2, 4, 4} >= {1, 2})
print({1, 2, 3, 4} >= {1, 2, 3, 4})
# Перевірка чіткого включення
print({1, 2, 4, 4} > {1, 2})
print({1, 2, 3, 4} > {1, 2, 3, 4})
# Об'єднання множин
print({1, 3}.union({2, 3, 4}))
print({1, 3} | {2, 3, 4})
# Перетин множин
print({1, 3}.intersection({2, 3, 4}))
print({1, 3} & {2, 3, 4})
# Різниця множин
print({1, 2, 3, 4}.difference({3, 4, 5}))
print({1, 2, 3, 4} - {3, 4, 5})
# Симетрична різниця
print({1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6}))
print({1, 2, 3, 4} ^ {3, 4, 5, 6})
# Копіювання множини
my_set = set('chars')
copy = my_set.copy()
print(copy)

# Priklad 2

phonebook = {
'Олександр': '123-032-846',
'Анатолій': '432-917-333',
'Вадим': '345-120-422',
'Андрій': '111-890-532', # остання кома ігнорується
}
# len(d) – кількість елементів
print(phonebook, '\n', len(phonebook), 'entries found')

print(phonebook['Вадим']) # 345-120-422
#print(phonebook['Олег']) # KeyError: 'Олег'

print(phonebook, '\n', len(phonebook), 'entries found')

for person in ('Анатолій', 'Вадим', 'Микола'):
    if person in phonebook:
        print(person, 'is in the phonebook')
    else:
        print('No entry found for', person)
print()
# Task 1

words = []
for i in range(0,3):
    words.append(input("Enter a word: "))
print(words)
leters = []
for i in words:
    leterW = list(i);
    for leter in leterW:
        if ''.join(leters).count(leter) == 0:
            leters.append(leter)
print(leters)

# Task 2

text = input("Enter a text: ")
text.strip()
text.replace(" ","")
" ".join(text.split())
print(text)

num_vowels = 0
num_numbers = 0
num_consonants = 0
length = len(text)

num_vowels += text.count("a")
num_vowels += text.count("e")
num_vowels += text.count("i")
num_vowels += text.count("o")
num_vowels += text.count("u")
num_vowels += text.count("y")
num_vowels += text.count("A")
num_vowels += text.count("E")
num_vowels += text.count("I")
num_vowels += text.count("O")
num_vowels += text.count("U")
num_vowels += text.count("Y")

num_numbers += text.count("0")
num_numbers += text.count("1")
num_numbers += text.count("2")
num_numbers += text.count("3")
num_numbers += text.count("4")
num_numbers += text.count("5")
num_numbers += text.count("6")
num_numbers += text.count("7")
num_numbers += text.count("8")
num_numbers += text.count("9")

num_consonants = length - num_numbers - num_vowels

if num_vowels > num_consonants:
    print("There are more vowels.")
else:
    print("There are more consonants.")

# task 3

text = input("Enter a text: ")

if text.count("a") != 0 or text.count("A") != 0:
    print("a")
if text.count("e") != 0 or text.count("E") != 0:
    print("e")
if text.count("i") != 0 or text.count("I") != 0:
    print("i")
if text.count("o") != 0 or text.count("O") != 0:
    print("o")
if text.count("u") != 0 or text.count("U") != 0:
    print("u")
if text.count("y") != 0 or text.count("Y") != 0:
    print("y");
