from msilib.schema import FeatureComponents
import kbhit
import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile # para manejo de wavs
#from scipy import signal
import numpy as np  # arrays    
import matplotlib.pyplot as plt
from format_tools import *

SRATE = 44100
CHUNK = 2048
STDFREC = 440
MODFREC = 27.5

class Osc:
    def __init__(self, f = 0):
        self.frec = f
        self.index = 0

    def changeFrec(self, frec):
        self.frec = frec

    def next(self):
        chunkWave = np.arange(CHUNK, dtype = np.float32)

        for i in range(len(chunkWave)):
            chunkWave[i] = np.sin((self.index + i) * (2 * np.pi) * self.frec / SRATE) # asumimos time = 1

        self.index += CHUNK

        return chunkWave

    def nextRingMod(self):
        chunkWave = np.arange(CHUNK, dtype = np.float32)

        for i in range(len(chunkWave)):
            chunkWave[i] = (np.sin((self.index + i) * (2 * np.pi) * self.frec / SRATE) + 1)/2  # asumimos time = 1

        self.index += CHUNK

        return chunkWave

    def nextSquare(self):
        chunkWave = np.arange(CHUNK, dtype = np.float32)

        for i in range(len(chunkWave)):
            # chunkWave[i] = signal.square((self.index + i) * (2 * np.pi) * self.frec / SRATE)
            chunkWave[i] = 1 if np.sin((self.index + i) * (2 * np.pi) * self.frec / SRATE) > 0 else -1

        self.index += CHUNK

        return chunkWave

    def nextTriangle(self):
        chunkWave = np.arange(CHUNK, dtype = np.float32)

        for i in range(len(chunkWave)):
            chunkWave[i] = (2 / np.pi) * np.arcsin(np.sin((self.index + i) * (2 * np.pi) * self.frec / SRATE))

        self.index += CHUNK

        return chunkWave

    def nextSaw(self):
        chunkWave = np.arange(CHUNK, dtype = np.float32)

        for i in range(len(chunkWave)):
            #chunkWave[i] = (2 / numpy.pi) * numpy.arctan(numpy.tan(wave[i] / SRATE * (time * 2 * numpy.pi) / 2))
            chunkWave[i] = (2 / np.pi) * np.arctan(np.tan(((self.index + i) * (2 * np.pi) * self.frec / SRATE)/2))

        self.index += CHUNK

        return chunkWave

# Modulador de Amplitud
def modula(sample, modWave):
    for i in range(len(sample)):
        sample[i] *= modWave[i]

# Muestra matplotlib
def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    plt.plot(x, y)

bloque = np.arange(CHUNK, dtype = np.float32)

# abrimos stream
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(bloque.shape))

# arrancamos stream
stream.start()

# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
kb = kbhit.KBHit()
osc = Osc(STDFREC)
oscMod = Osc(MODFREC)
numBloque = 0
c = ' '


# Happy Birthday
notas = "A.BC.D.EF.G.a.bc.d.ef.g."
songFrec = [440*(2**(i/12)) for i in range(24)]
songIndex = 0

part = [('G', 0.5), ('G',0.5), ('a',1), ('G',1),
('c',1),('b',2),
('G', 0.5), ('G',0.5), ('a',1), ('G',1),
('d',1), ('c',2),
('G', 0.5), ('G',0.5), ('g',1),('e',1),
('c',1),('b',1), ('a',1),
('f', 0.5), ('f',0.5), ('e',1),('c',1),
('d',1),('c',2),]



while c != 'q' and songIndex < len(part) - 1: 
    # nuevo bloque 
    bloque = osc.next() 

    osc.changeFrec(songFrec[notas.index(part[songIndex][0])])
    # lastTime = part[songIndex][1]

    stream.write(bloque)        

    
    songIndex += 1
    numBloque += 1


# setGraphics(bloqueMod)
setGraphics(bloque)
plt.show()

kb.set_normal_term()        
stream.stop()