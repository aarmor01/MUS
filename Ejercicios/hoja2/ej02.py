import matplotlib.pyplot
import numpy
import math
import random

#%%
wave = numpy.arange(44100, dtype = numpy.float32)
# sinwave = numpy.sin(wave/(2 * math.pi))

for x in range(len(wave)):
    v[x] = numpy.sin(v[x]/(2 * math.pi))

x = list(range(len(wave)))
y = [sample for sample in wave]  # obtiene la lista [0,1...9]

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

print(wave)
# %%
