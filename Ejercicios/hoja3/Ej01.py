# 1_numPy/playNumPyVol.py reproductor con control de volumen
import numpy as np  # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
from format_tools import *

SRATE = 44100
CHUNK = 2048
frec = 440

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

# abrimos wav y recogemos frecMuestreo y array de datos
#fs, data = wavfile.read('../0_basics/expousure.wav')
# SRATE, data = wavfile.read('ex1.wav')

bloque = np.arange(CHUNK, dtype = np.float32)

# print("Sample rate ", SRATE)
# print("Sample format: ", data.dtype)
# print("Num channels: ", len(data.shape))
# print("Len ", data.shape[0])

# arrancamos sounddevice
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(bloque.shape))

stream.start()

# En data tenemos el wav completo, ahora procesamos por bloques (chunks)
kb = kbhit.KBHit()
osc = Osc(frec)
numBloque = 0
c = ' '

while c != 'q': 
    # nuevo bloque 
    bloque = osc.next() 

    # modificación del volumen: multiplicacion de todas las muestras * vol
    # bloque = bloque*frec/SRATE

    stream.write(bloque)        
    
    if kb.kbhit():
        c = kb.getch()
        if (c=='f'): frec = max(220, frec - 0.5)
        elif (c=='F'): frec = min(880, frec + 0.5)
        print("Frec: ", frec)

    osc.changeFrec(frec)

    numBloque += 1

kb.set_normal_term()        
stream.stop()