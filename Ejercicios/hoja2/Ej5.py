from re import S
import numpy
import matplotlib.pyplot
import random
import math

SRATE = 44100.0
# time = 2

def osc(nHz, time):
    # título 
    matplotlib.pyplot.title("Sinusoide")

    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
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

def vol(sample, vol):
    for i in range(len(sample)):
        sample[i] *= vol

def modulaVol(sample, frec):
    for i in range(len(sample)):
        sample[i] *= frec[i]

def fadeIn(sample, t):
    if t < 0:
        print("eres tonto >:(")
        return

    lastSample = round(SRATE * t) if round(SRATE * t) <= len(sample) else len(sample)

    secondWave = numpy.ones(len(sample), dtype = numpy.float32) # array of ones
    for i in range(lastSample):
        secondWave[i] = i / lastSample

    setGraphics(secondWave)
    modulaVol(sample, secondWave)

def fadeOut(sample, t):
    if t < 0:
        print("eres tonto >>>:(")
        return

    lastSample = round(SRATE * t) if round(SRATE * t) <= len(sample) else len(sample)

    secondWave = numpy.ones(len(sample), dtype = numpy.float32) # array of ones
    for i in range(lastSample):
        secondWave[-i - 1] = i / lastSample

    setGraphics(secondWave)
    modulaVol(sample, secondWave)

# wave = square(3, 1)
# setGraphics(wave)
# wave = triangle(3, 1)
# setGraphics(wave)
# wave = saw(3, 1)
# setGraphics(wave)

fecuency = 1

wave = osc(3, 1)
fadeOut(wave, 1)
# fadeIn(wave, 1)
# secondWave = osc(2, 1)

# modulaVol(wave, secondWave)

setGraphics(wave)
# setGraphics(secondWave)

# mostrar el resultado
matplotlib.pyplot.show()