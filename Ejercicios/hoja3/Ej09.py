import kbhit
import sounddevice as sd
import soundfile as sf
import numpy as np  # arrays    

SRATE = 44100
CHUNK = 2048
STDFREC = 440
MODFREC = 27.5

class Delay:
    def __init__(self, dT):
        self.delayTime = dT
        self.buf = np.zeros(dT * SRATE)

    def processChunk(self, audioChunk):
        outputChunk = self.buf[:CHUNK]
        self.buf = np.append(self.buf, audioChunk, axis = 0)
        self.buf = self.buf[CHUNK:] # np.delete(self.buf, np.s_[:CHUNK], axis = 0)

        # print(len(self.buf))
        return outputChunk


data, SRATE = sf.read('piano.wav')

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

delay = Delay(3)

vol = 1.0
while c != 'q': 
     # numero de samples a procesar: CHUNK si quedan y si no, los que queden
    nSamples = min(CHUNK, data.shape[0] - (numBloque + 1) * CHUNK)

    # nuevo bloque
    bloque = data[numBloque * CHUNK : numBloque * CHUNK + nSamples]

    stream.write(np.float32(delay.processChunk(bloque)))

    if kb.kbhit():
        c = kb.getch()
    #     if (c=='f'): STDFREC = max(220, STDFREC - 0.5)
    #     elif (c=='F'): STDFREC = min(880, STDFREC + 0.5)
    #     if (c=='v'): vol = max(0,vol - 0.05)
    #     elif (c=='V'): vol = vol + 0.05
    #     print("Vol: ", min(maxVol, vol))

    numBloque += 1

kb.set_normal_term()        
stream.stop()
exit()