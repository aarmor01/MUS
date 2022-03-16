import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHANNELS = 1
CHUNK = 2048
FADE_TIME = 300


# 0,3980 sube
# 1,045 baja
class Sampler:
    # constructura de la clase
    def __init__(self, sample, start, end, isLooping):
        self.sampleAudio = np.copy(sample)
        self.startLoop = start
        self.endLoop = end
        self.isLooping = isLooping
        self.index = 0

    def nextChunk(self):
        if not self.isLooping:
            samples = CHUNK
            if CHUNK > len(self.sampleAudio):
                samples = samples - (CHUNK - len(self.sampleAudio))

            outChunk = self.sampleAudio[self.index : self.index + samples]

            if len(outChunk) < CHUNK:
                outChunk = np.append(outChunk, np.zeros(CHUNK - len(outChunk), dtype=np.float64))
            
            self.index += samples
            return outChunk

        else:
            end = 0
            if self.index + CHUNK > self.endLoop: end = self.endLoop
            else: end = self.index + CHUNK

            outChunk = self.sampleAudio[self.index : end]

            if end == self.endLoop:
                self.index = self.startLoop + (CHUNK - len(outChunk))
                outChunk = np.append(outChunk, self.sampleAudio[self.startLoop : self.index])
            else:
                self.index += CHUNK 

            return outChunk
        
    def setLooping(self, loop):
        self.isLooping = loop
        if self.isLooping: 
            if self.index >= len(self.sampleAudio): self.index = 0
            else: self.index = self.startLoop
        else: self.index = self.startLoop

# leemos wav en array numpy (data)
# por defecto lee en formato dtype="float64". No hay problema para reproducción simple (hace conversiones internas)
data, SRATE = sf.read('flauta.wav', dtype=np.float64)

sampler = Sampler(data,  23896, 44134, False)
def callbackO(outdata, frames, time, status):
    outdata[:,0] = sampler.nextChunk()

stream = sd.OutputStream(samplerate = SRATE,            # frec muestreo 
    blocksize = CHUNK,                                  # tamaño del bloque (muy recomendable unificarlo en todo el programa)
    channels = 1,
    dtype = np.float32,
    callback=callbackO)                                 # num de canales

# arrancamos stream
stream.start()

kb = kbhit.KBHit()
c= ' '

while c != 'q':
 if kb.kbhit():
        c = kb.getch()
        if c == 'l': sampler.setLooping(True)
        elif c == 'n': sampler.setLooping(False)

kb.set_normal_term()