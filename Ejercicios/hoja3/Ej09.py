import kbhit
import sounddevice as sd
import soundfile as sf
import numpy as np  # arrays    

SRATE = 44100
CHUNK = 2048

# clase Delay, contiene buffer 
class Delay:
    def __init__(self, dT):
        self.delayTime = dT
        # generar buffer con tamaño del silencio
        self.buf = np.zeros(dT * SRATE) 

    def processChunk(self, audioChunk): # procesar chunk
        # obtener chunk a reproducir 
        outputChunk = self.buf[:CHUNK]
        # añadir nuevo chunk a la cola
        self.buf = np.append(self.buf, audioChunk, axis = 0)
        # eliminamos chunk a reproducir (ambas versiones sirven)
        self.buf = self.buf[CHUNK:] # np.delete(self.buf, np.s_[:CHUNK], axis = 0)

        # print(len(self.buf))
        return outputChunk


data, SRATE = sf.read('piano.wav')

# abrir stream
stream = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=len(data.shape))

# arrancar stream
stream.start()

kb = kbhit.KBHit()
delay = Delay(3)
numBloque = 0
c = ' '

while c != 'q': 
     # numero de samples a procesar
    nSamples = min(CHUNK, data.shape[0] - (numBloque + 1) * CHUNK)

    # nuevo bloque
    bloque = data[numBloque * CHUNK : numBloque * CHUNK + nSamples]

    # procesar nuevo bloque y retornar bloque a reproducir
    stream.write(np.float32(delay.processChunk(bloque)))

    if kb.kbhit():
        c = kb.getch()

    numBloque += 1

kb.set_normal_term()        
stream.stop()
exit()