import chunk
import numpy
import matplotlib.pyplot

BUF_SIZE = 1024

def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    matplotlib.pyplot.plot(x, y)

class Osc:
    def __init__(self, f = 0):
        self.frec = f
        self.index = 0

    def next(self):
        chunkWave = numpy.arange(BUF_SIZE, dtype = numpy.float32)

        for i in range(len(chunkWave)):
            chunkWave[i] = self.index + i # convert chunk
            chunkWave[i] = numpy.sin(chunkWave[i] * (2 * numpy.pi) / self.frec) # asumimos time = 1

        self.index += BUF_SIZE

        return chunkWave

frequency = 22050
oscil = Osc(frequency)
wave = numpy.empty(0, dtype = numpy.float32)

chunks = 11
for i in range(chunks):
    wave = numpy.concatenate((wave, oscil.next()), axis = None)

setGraphics(wave)

matplotlib.pyplot.show() # mostrar el resultado