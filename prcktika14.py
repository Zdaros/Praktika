# Priklad 1
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='параметрична крива')
ax.legend()
plt.show()


#prikalad 2
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy
def makeData():
 x = numpy.arange(-10, 10, 0.5)
 y = numpy.arange(-10, 10, 0.5)
 xgrid, ygrid = numpy.meshgrid(x, y)
 zgrid = numpy.sin(xgrid * 0.3) * numpy.cos(ygrid * 0.75)
 return xgrid, ygrid, zgrid
if __name__ == '__main__':
 x, y, z = makeData()
 fig = pylab.figure()
 axes = Axes3D(fig)
 axes.plot_surface(x, y, z, rstride=1, cstride=1)
 pylab.show()

# Priklad 3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Вхідні дані
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
# Побудова поверхні
ax.plot_surface(x, y, z, color='b')
plt.show()

# Priklad 4
from math import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def data_gen(t=0):
 cnt = 0
 while cnt < 1000:
  cnt += 1
  t += 0.1
  yield t, sin(2*pi*t) * exp(-t/10.)
def init():
 ax.set_ylim(-1.1, 1.1)
 ax.set_xlim(0, 10)
 del xdata[:]
 del ydata[:]
 line.set_data(xdata, ydata)
 return line,
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
def run(data):
 # update the data
 t, y = data
 xdata.append(t)
 ydata.append(y)
 xmin, xmax = ax.get_xlim()
 if t >= xmax:
  ax.set_xlim(xmin, 2*xmax)
  ax.figure.canvas.draw()
 line.set_data(xdata, ydata)
 return line,
ani = animation.FuncAnimation(fig, run, data_gen, interval=10, repeat=False, init_func=init)
plt.show()

# Task 1
f = open("data/task1_1.txt", "r")
file = str(f.read())
f.close()
l_num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
l_num[0] = 0
l_num[1] = 0
l_num[2] = 0
l_num[3] = 0
l_num[4] = 0
l_num[5] = 0
l_num[6] = 0
l_num[7] = 0
l_num[8] = 0
l_num[9] = 0
l_num[10] = 0
l_num[11] = 0
l_num[12] = 0
l_num[13] = 0
l_num[14] = 0
l_num[15] = 0
l_num[16] = 0
l_num[17] = 0
l_num[18] = 0
l_num[19] = 0
l_num[20] = 0
l_num[21] = 0
l_num[22] = 0

for char in range(0, len(file)):
    if file[char] == "A" or file[char] == "a":
        l_num[0] += 1
    elif file[char] == "B" or file[char] == "b":
        l_num[1] += 1
    elif file[char] == "C" or file[char] == "c":
        l_num[2] += 1
    elif file[char] == "D" or file[char] == "d":
        l_num[3] += 1
    elif file[char] == "E" or file[char] == "e":
        l_num[4] += 1
    elif file[char] == "F" or file[char] == "f":
        l_num[5] += 1
    elif file[char] == "G" or file[char] == "g":
        l_num[6] += 1
    elif file[char] == "H" or file[char] == "h":
        l_num[7] += 1
    elif file[char] == "I" or file[char] == "i":
        l_num[8] += 1
    elif file[char] == "K" or file[char] == "k":
        l_num[9] += 1
    elif file[char] == "L" or file[char] == "l":
        l_num[10] += 1
    elif file[char] == "M" or file[char] == "m":
        l_num[11] += 1
    elif file[char] == "N" or file[char] == "n":
        l_num[12] += 1
    elif file[char] == "O" or file[char] == "o":
        l_num[13] += 1
    elif file[char] == "P" or file[char] == "p":
        l_num[14] += 1
    elif file[char] == "Q" or file[char] == "q":
        l_num[15] += 1
    elif file[char] == "R" or file[char] == "r":
        l_num[16] += 1
    elif file[char] == "S" or file[char] == "s":
        l_num[17] += 1
    elif file[char] == "T" or file[char] == "t":
        l_num[18] += 1
    elif file[char] == "V" or file[char] == "v":
        l_num[19] += 1
    elif file[char] == "x" or file[char] == "x":
        l_num[20] += 1
    elif file[char] == "Y" or file[char] == "y":
        l_num[21] += 1
    elif file[char] == "z" or file[char] == "z":
        l_num[22] += 1

import matplotlib.pyplot as plt
rng = np.array(l_num)
_ = plt.hist(rng, bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])  
plt.title("Histogram with leter_count in txt (leters are in alfabet order)")
plt.savefig("data/praktika14.png")
plt.show()

#plt.savefig("data/praktika14.png")

# Task 2
from numpy import *
import matplotlib.pyplot as plt

def data_gen1(t=0):
 cnt = 0
 while cnt < 1000:
  cnt += 1
  t += 0.1
  yield t, 5*cos(10*t)*sin(3*t)/(t ** (1/2))
def init1():
 ax.set_ylim(-15, 15)
 ax.set_xlim(0, 10)
 del xdata[:]
 del ydata[:]
 line.set_data(xdata, ydata)
 return line,
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
def run1(data):
 # update the data
 t, y = data
 xdata.append(t)
 ydata.append(y)
 xmin, xmax = ax.get_xlim()
 if t >= xmax:
  ax.set_xlim(xmin, 2*xmax)
  ax.figure.canvas.draw()
 line.set_data(xdata, ydata)
 return line,

ani = animation.FuncAnimation(fig, run1, data_gen1, interval=10, repeat=False, init_func=init1)
plt.show()
