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

# Muestra matplotlib
def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    plt.plot(x, y)

# Modulador de Amplitud
def balance(sample_i, sample_d, bal):
    for i in range(len(bal)):
        if bal[i] > 0:
            sample_d[i] *= bal[i]
            sample_i[i] = 0
        elif bal[i] < 0:
            sample_d[i] = 0
            sample_i[i] *= bal[i]
        else:
            sample_d[i] = 0
            sample_i[i] = 0

bloque_i = np.arange(CHUNK, dtype = np.float32)
bloque_d = np.arange(CHUNK, dtype = np.float32)

# abrimos stream
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(bloque_i.shape))

# arrancamos stream
stream.start()

# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
kb = kbhit.KBHit()
osc_i = Osc(STDFREC)
osc_d = Osc(STDFREC)
oscMod = Osc(MODFREC)
numBloque = 0
c = ' '

vol = 1.0
while c != 'q': 
     # numero de samples a procesar: CHUNK si quedan y si no, los que queden
    bloque_i = osc_i.next() 
    bloque_d = osc_d.next() 
    sin = oscMod.next()

    balance(bloque_i, bloque_d, sin)
    
    result = np.array([bloque_i, bloque_d])

    stream.write(np.float32(result))      

    if kb.kbhit():
        c = kb.getch()
        if (c=='f'): STDFREC = max(220, STDFREC - 0.5)
        elif (c=='F'): STDFREC = min(880, STDFREC + 0.5)
        if (c=='v'): vol = max(0,vol - 0.05)
        elif (c=='V'): vol = vol + 0.05

    numBloque += 1

# setGraphics(bloque)
# plt.show()

kb.set_normal_term()        
stream.stop()
exit()