from msilib.schema import FeatureComponents
import kbhit
import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile # para manejo de wavs
#from scipy import signal
import numpy as np  # arrays    
import matplotlib.pyplot as plt
from format_tools import *

# SRATE = 44100
CHUNK = 2048
STDFREC = 440
MODFREC = 27.5

# Muestra matplotlib
def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    plt.plot(x, y)

data, SRATE = sf.read('piano2.wav')

data = toFloat32(data)

# abrimos stream
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(data.shape))

# arrancamos stream
stream.start()

# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
kb = kbhit.KBHit()
numBloque = 0
c = ' '

vol = 1.0
while c != 'q': 
     # numero de samples a procesar: CHUNK si quedan y si no, los que queden
    nSamples = min(CHUNK, data.shape[0] - (numBloque + 1) * CHUNK)

    # nuevo bloque
    bloque = data[numBloque * CHUNK : numBloque * CHUNK + nSamples]

    maxValue = np.amax(np.abs(bloque))
    maxVol = 1 / maxValue

    bloque *= min(maxVol, vol)

    stream.write(bloque)        
    
    if kb.kbhit():
        c = kb.getch()
        if (c=='f'): STDFREC = max(220, STDFREC - 0.5)
        elif (c=='F'): STDFREC = min(880, STDFREC + 0.5)
        if (c=='v'): vol = max(0,vol - 0.05)
        elif (c=='V'): vol = vol + 0.05
        print("Vol: ", min(maxVol, vol))

    numBloque += 1

setGraphics(bloque)
plt.show()

notas = "A.BC.D.EF.G.a.bc.d.ef.g."
happyFrec = [220*(2**(i/12)) for i in range(24)]

x = happyFrec[notas.index('G')]

[('G', 0.5), ('G',0.5), ('A',1), ('G',1),
('c',1),('B',2),
('G', 0.5), ('G',0.5), ('A',1), ('G',1),
('d',1), ('c',2),
('G', 0.5), ('G',0.5), ('g',1),('e',1),
('c',1),('B',1), ('A',1),
('f', 0.5), ('f',0.5), ('e',1),('c',1),
('d',1),('c',2),]

print(x)


kb.set_normal_term()        
stream.stop()
exit()