import numpy
import matplotlib.pyplot

SRATE = 44100.0
frequency = 3

def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    matplotlib.pyplot.plot(x, y)

def osc(nHz, time):
    wave = numpy.arange(SRATE * nHz, dtype = numpy.float32)
    for i in range(len(wave)):
        wave[i] = numpy.sin(wave[i]/SRATE*(time*2*numpy.pi))

    matplotlib.pyplot.title("Sinusoide Generalizado") # título 

    return wave

def vol(sample, vol):
    for i in range(len(sample)):
        sample[i] *= vol

def modulaVol(sample, frec):
    for i in range(len(sample)):
        sample[i] *= frec[i]

wave = osc(frequency, 1)

setGraphics(wave)
vol(wave, 0.5)
setGraphics(wave)

wave = osc(frequency, 1)
oscWave = osc(frequency, 2)

modulaVol(wave, oscWave)
setGraphics(wave)
setGraphics(oscWave)

matplotlib.pyplot.show() # mostrar el resultado