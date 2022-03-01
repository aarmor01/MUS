import kbhit
import sounddevice as sd
import soundfile as sf
import numpy as np  
import matplotlib.pyplot as plt
import math

SRATE = 44100
CHUNK = 1024
STDFREC = 440

# Muestra matplotlib
def setGraphics(wave):
    x = list(range(len(wave)))
    y = [sample for sample in wave]

    plt.plot(x, y)

data, SRATE = sf.read('piano.wav')

# abrimos stream
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(data.shape))

# arrancamos stream
stream.start()

# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
kb = kbhit.KBHit()
numBloque = int(math.ceil(len(data) / CHUNK))
c = ' '

newRate = SRATE * 1.2
newSRate = bool(0)
while c != 'q': 
      # numero de samples a procesar: CHUNK si quedan y si no, los que queden
    nSamples = min(CHUNK, data.shape[0] - (numBloque + 1) * CHUNK)

    # nuevo bloque
    bloque = data[numBloque * CHUNK : numBloque * CHUNK + nSamples]

    if newSRate:
        newSRate = bool(1)
        stream = sd.OutputStream(samplerate=newRate, 
                    blocksize=CHUNK,
                    channels=len(data.shape))

    if len(bloque) == 0:
        stream.write(np.float32(bloque))

    numBloque += 1

    if kb.kbhit():
        c = kb.getch()
        if (c=='f'):
            newRate = SRATE * 1.2
            newSRate = bool(1)
            numBloque = 0
        if (c=='g'):
            newRate = SRATE * 1.2
            newSRate = bool(1)
            numBloque = 0


# setGraphics(bloque)
# plt.show()

kb.set_normal_term()        
stream.stop()
exit()