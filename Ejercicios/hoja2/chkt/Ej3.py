import numpy
import matplotlib.pyplot
import random
import math

SRATE = 44100
# time = 2

def osc(nHz, time):
    # título 
    matplotlib.pyplot.title("Sinusoide Generalizado")

    wave = numpy.arange(SRATE*nHz, dtype=numpy.float32)
    for i in range(len(wave)):
        wave[i] = numpy.sin(wave[i]/SRATE*(time*2*numpy.pi))

    return wave

def saw(nHz, time):
    # título 
    matplotlib.pyplot.title("Sierra")

    wave = numpy.arange(SRATE*nHz, dtype=numpy.float32)
    for i in range(len(wave)):
        wave[i] = (2/numpy.pi) * numpy.arctan(numpy.tan(wave[i]/SRATE*(time*2*numpy.pi)/2))

    return wave

def square(nHz, time):
        # título 
    matplotlib.pyplot.title("Cuadrado")

    wave = numpy.arange(SRATE*nHz, dtype=numpy.float32)
    for i in range(len(wave)):
        wave[i] = 1 if numpy.sin(wave[i]/SRATE*(time*2*numpy.pi)) > 0 else -1

    return wave

def triangle(nHz, time):
        # título 
    matplotlib.pyplot.title("Triangulo")

    wave = numpy.arange(SRATE*nHz, dtype=numpy.float32)
    for i in range(len(wave)):
        wave[i] = (2/numpy.pi) * numpy.arcsin(numpy.sin(wave[i]/SRATE*(time*2*numpy.pi)))

    return wave

def setGraphics(wave):
    x = list(range(len(wave)))
    y = [a for a in wave]

    matplotlib.pyplot.plot(x, y)

wave = square(3, 1)
setGraphics(wave)
wave = triangle(3, 1)
setGraphics(wave)
wave = saw(3, 1)
setGraphics(wave)
wave = osc(3, 1)
setGraphics(wave)

# mostrar el resultado
matplotlib.pyplot.show()