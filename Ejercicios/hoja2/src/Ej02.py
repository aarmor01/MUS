import numpy
import matplotlib.pyplot

# wave = numpy.arange(44100, dtype = numpy.float32)
hz, time = 44100.0, 2
wave = numpy.arange(hz * 3, dtype = numpy.float32)

for i in range(len(wave)):
    wave[i] = numpy.sin(wave[i] / hz * (time * 2 * numpy.pi))

x = list(range(len(wave)))
y = [sample for sample in wave]

matplotlib.pyplot.title("Sinusoide") # título 
matplotlib.pyplot.plot(x, y) # genera grafo
matplotlib.pyplot.show() # mostrar el resultado