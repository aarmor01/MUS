import matplotlib.pyplot
import random
import numpy

# wave = numpy.random.uniform(1, -1, 44100)
wave = numpy.arange(44100, dtype=numpy.float32)

# i = 0
# while i < len(v):
for i in range(len(wave)):
    wave[i] = random.uniform(-1,1)
    # i += 1

x = list(range(len(wave)))
y = [sample for sample in wave]

matplotlib.pyplot.title("Ruido") # título 
matplotlib.pyplot.plot(x, y) # genera grafo
matplotlib.pyplot.show() # mostrar el resultado