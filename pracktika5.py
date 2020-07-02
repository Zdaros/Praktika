# Priklad 1

def function():
    # визначення локальної змінної
    var = 'локальна змінна'
    # виведення значення локальної змінної на екран
    print(var)
# визначення глобальної змінної
var = 'глобальна змінна'
function()
# виведення на екран значення глобальної змінної
print(var)

def function():
    global var
    #виведення значення глобальної змінної на екран
    print(var)
    # зміна глобальної змінної
    var = 'нове значення'
    # виведення значення глобальної змінної на екран
    print(var)
var = 'глобальна змінна'
function();
print(var)

def function(c, d):
    # a, b – глобальні змінні; c, d -- локальні
    global a, b
    # зміна значення глобальної змінної
    a = 5
    b = 7
    # зміна значення локальної змінної
    c = 10
    d = 12
a, b, c, d = 1, 2, 3, 4 # множинне присвоєння
print(a, b, c, d) # 1 2 3 4
function(c, d)
print(a, b, c, d) # 5 7 3 4
print()

# Priklad 2

import itertools
import math
import random

def my_sqrt(a,n,Epsilon):
    term1=(a+n-1)/2
    term2=(2/3)*term1 +(a/(3*term1**2))
    k=1
    while (abs(term2- term1) > Epsilon):
        term1= term2
        term2=((k-1)/k)* term1 + a/(k*(term1**(k-1)))
        k+=1
    return term2
print(" х ", ": "," y ", " : "," yt", " : "," error " )
print("-- ")
Epsilon=0.0001
a=0.1;b=1
for i in itertools.count(start=a, step=0.2):
    if i>b:
        break
    n=3
    y= my_sqrt(i,n,Epsilon)
    y1=i**(1/n) # точне значення функції
    error=abs(y-y1)
    print('%.2f' %i, ":", '%.4f' %y, " : ", '%.4f' %y1, " : ", '%.4f' %error)

# Taks 1

def split_line(text):
    words = text.split()

    return words

text = input("Enter a text: ")

print(split_line(text))

# Task 2

def factorial(num):
    i = 1
    factorial = 1
    while i <= num:
        factorial *= i
        i+=1
    return factorial

"""def taylor_ray(start, end, E, M):
    Fx = []
    Num = 0
    Fxn = 0
    Fx.append(0)
    Fx.append(pow(start,0)/factorial(1))
    Fx.append(Num)
    Fx.append(1)
    Num_of_repeat = 0
    for n in range(1, M):
        while True:
            Num = random.randint(start, end)
            Fxn = pow(start,Num)/factorial(Num)
            Num_of_repeat += 1
            if abs(Fx[n-1]-Fxn) <= E:
                Fx.append(Fxn)
                Fx.append(Num)
                break
            Fx.append(Num_of_repeat)
        Num_of_repeat = 0
    return Fx"""

def taylor_ray(a,n,Epsilon):
    term1=(a+n-1)/2
    term2=(2/3)*term1 +(a/(3*term1**2))
    k=1
    while (abs(term2- term1) > Epsilon):
        term1= term2
        term2=((k-1)/k)* term1 + a/(k*(term1**(k-1)))
        k+=1
    return term2

while True:
    a = float(input("Enter A:"))
    b = float(input("Enter B:"))
    if abs(a-b) < 10:
        print("|A-B| can't be les tean 10")
        continue
    else:
        break
E = float(input("Enter E:"))
while True:
    m = float(input("Enter M:"))
    if m < 10:
        print("M can't be les tean 10")
        continue
    else:
        break

function_a = taylor_ray(a,b,E)
e = 2.78

print(" хi ", ": "," f(xi) ", " : "," f_close(xi)", " : "," E ", " : "," Number of repeat ")
print("-- ")

for i in itertools.count(start=a, step=0.2):
    if i>b:
        break
    n=3
    y= taylor_ray(i,n,E)
    y1=i**(1/n)
    error=abs(y-y1)
    print('%.2f' %i, ":", '%.4f' %y, " : ", '%.4f' %y1, " : ", E , " : ", '%.4f' %error)

"""count = 0
num = 0
f = 0
for n in range(0,M*3):
    if count == 0:
        f = function_a[n]
        f1 = function_a[n+3]
        count+=1
    elif count == 1:
        num = function_a[n]
        count+=1
    else:
        count = 0
        print(num,  f, f1 , e, function_a[n] )
"""
