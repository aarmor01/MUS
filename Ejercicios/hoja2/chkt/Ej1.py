import numpy
import matplotlib.pyplot
import random

v = numpy.arange(44100, dtype=numpy.float32)

for i in range(len(v)):
# i = 0
# while i < len(v):
    v[i] = random.uniform(-1,1)
    # i += 1

x = list(range(len(v)))
y = [a for a in v]

matplotlib.pyplot.plot(x, y)

# título 
matplotlib.pyplot.title("Ruido")

# mostrar el resultado
matplotlib.pyplot.show()