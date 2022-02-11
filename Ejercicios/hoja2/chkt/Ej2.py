import numpy
import matplotlib.pyplot
import random
import math

hz = 44100
time = 2
# v = numpy.arange(44100, dtype=numpy.float32)
t = numpy.arange(hz*3, dtype=numpy.float32)

for i in range(len(t)):
    t[i] = numpy.sin(t[i]/hz* (time*2*numpy.pi))

x = list(range(len(t)))
y = [a for a in t]

matplotlib.pyplot.plot(x, y)

# título 
matplotlib.pyplot.title("Sinusoide")

# mostrar el resultado
matplotlib.pyplot.show()