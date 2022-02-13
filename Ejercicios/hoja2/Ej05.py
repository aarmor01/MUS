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

def modulaVol(sample, frec):
    for i in range(len(sample)):
        sample[i] *= frec[i]
        
def fadeOut(sample, t):
    if t < 0: return

    lastSample = round(SRATE * t) if round(SRATE * t) <= len(sample) else len(sample)

    oscWave = numpy.ones(len(sample), dtype = numpy.float32) # array of ones
    for i in range(len(sample) - lastSample):
        oscWave[-i - 1] = i / (len(sample) - lastSample) # esto es terrible

    setGraphics(oscWave)
    modulaVol(sample, oscWave)

def fadeIn(sample, t):
    if t < 0: return

    lastSample = round(SRATE * t) if round(SRATE * t) <= len(sample) else len(sample)

    oscWave = numpy.ones(len(sample), dtype = numpy.float32) # array of ones
    for i in range(lastSample):
        oscWave[i] = i / lastSample

    setGraphics(oscWave)
    modulaVol(sample, oscWave)

wave = osc(3, 1)

fadeOut(wave, 1)
fadeIn(wave, 1)

setGraphics(wave)

matplotlib.pyplot.show() # mostrar el resultado