# Priklad 1

a = 5
b = 7.0
c = 2 > 4
d = "World"
e = 1.5 + 0.5j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(a, b, c, d, e.real, e.imag)
print("")
# Priklad 2

a = 5
b = 7.0
c = 1 + 2
d = 5 - 3
e = a * b
f = 3.0 / 2
g = 3 / 2
h = 5 % 3
j = 10 ** 7.3
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(j))
print(a, b, c, d, e, f, g, h, j)
print("")

# Priklad 3

from math import *
a = 1
b = 2
x = sqrt(a*b)/(exp(a)*b)+a*exp((2*a)/b)
print(x)
print("")

# Task variant 10

x = 10.0
e = 2.72 # 2.71828
y = pow(e,2)*log10(pow(x,4))*((pow((x-0.5),2)-cos(x))/(pow((abs(x+1)+abs(x)),-2)))
print(y)
