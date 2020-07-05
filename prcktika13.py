# Priklad 1
import matplotlib.pyplot as plt
plt.plot([1, 3, 2, 4])
plt.show()

# Priklad 2
from numpy import * # для використання функцій exp та linspace
import matplotlib.pyplot as plt
def f(t):
 return t ** 2 * exp(-t ** 2)
t = linspace(0, 3, 51) # 51 точка між 0 та 3
y = f(t)
plt.plot(t, y)
plt.show()


# Priklad 3
import matplotlib.pyplot as plt
t = linspace(0, 3, 51)
y = t ** 2 * exp(-t ** 2)
plt.plot(t, y, 'g--', label='t^2*exp(-t^2)')
plt.axis([0, 3, -0.05, 0.5]) # [xmin, xmax, ymin, ymax]
plt.xlabel('t') # позначення вісі абсцис
plt.ylabel('y') # позначення е вісі ординат
plt.title('My first normal plot') # назва графіка
plt.legend() # вставка легенди (тексту в label)
plt.show()

# Priklad 4
from numpy import *
import matplotlib.pyplot as plt
t = linspace(0, 3, 51)
y1 = t ** 2 * exp(-t ** 2)
y2 = t ** 4 * exp(-t ** 2)
y3 = t ** 6 * exp(-t ** 2)
plt.plot(t, y1, 'g^', t, y2, 'b--',  t, y3, 'ro-') # червоні круглі маркери
# з'єднані суцільною лінією
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plotting with markers')
plt.legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)', 't^6*exp(-t^2)'], loc='upper left') # положення легенди
plt.show()

# Task
#from math import *
t = linspace(0, 10, 51)
y = 5*cos(10*t)*sin(3*t)/(t ** (1/2))

plt.plot(t, y, 'g--^', label="")
plt.axis([0, 11, -20 , 20])
plt.xlabel('t')
plt.ylabel('y')
plt.title('Task')
plt.legend("5*cos(10*t)*sin(3*t)/(pow(x,1/2))")
plt.show()
