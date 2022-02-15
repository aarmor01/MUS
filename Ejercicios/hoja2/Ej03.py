import numpy
import matplotlib.pyplot

SRATE = 44100.0

def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    matplotlib.pyplot.plot(x, y)

def osc(nHz, time):
    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
    for i in range(len(wave)):
        wave[i] = numpy.sin(wave[i] / SRATE * (time * 2 * numpy.pi))

    matplotlib.pyplot.title("Sinusoide Generalizado") # título 

    return wave

def square(nHz, time):
    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
    for i in range(len(wave)):
        wave[i] = 1 if numpy.sin(wave[i] / SRATE * (time * 2 * numpy.pi)) > 0 else -1
        
    matplotlib.pyplot.title("Cuadrado") 

    return wave

def triangle(nHz, time):
    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
    for i in range(len(wave)):
        wave[i] = (2 / numpy.pi) * numpy.arcsin(numpy.sin(wave[i] / SRATE * (time * 2 * numpy.pi)))
        
    matplotlib.pyplot.title("Triangulo") # título 

    return wave

def saw(nHz, time):
    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
    for i in range(len(wave)):
        wave[i] = (2 / numpy.pi) * numpy.arctan(numpy.tan(wave[i] / SRATE * (time * 2 * numpy.pi) / 2))
    
    matplotlib.pyplot.title("Sierra") # título 

    return wave

wave = osc(3, 1)
setGraphics(wave)
wave = square(3, 1)
setGraphics(wave)
wave = triangle(3, 1)
setGraphics(wave)
wave = saw(3, 1)
setGraphics(wave)

matplotlib.pyplot.show() # mostrar el resultado