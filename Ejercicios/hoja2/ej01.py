import matplotlib.pyplot
import numpy
import random

#%%
wave = numpy.random.uniform(1, -1, 44100)

x = list(range(len(wave)))
y = [sample for sample in wave]  # obtiene la lista [0,1...9]

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

print(wave)
# %%
