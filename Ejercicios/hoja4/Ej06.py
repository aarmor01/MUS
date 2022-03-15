import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHANNELS = 1
CHUNK = 2048
FADE_TIME = 300

# leemos wav en array numpy (data)
# por defecto lee en formato dtype="float64". No hay problema para reproducción simple (hace conversiones internas)
data, SRATE = sf.read('flauta.wav', dtype=np.float64)

# 0,3980 sube
# 1,045 baja
class Sampler:
    # constructura de la clase
    def __init__(self, sample, isLooping):
        self.sample = np.copy(sample)
        self.iniSample = int(0.7185 * SRATE)
        self.endSample = int(1.1280 * SRATE)
        self.looping = isLooping
        # compute fade out curve
        # linear fade in
        fade_curve = np.linspace(0.0, 1.0, FADE_TIME)
        # apply the curve
        self.sample[self.iniSample : self.iniSample + (FADE_TIME)] =  self.sample[self.iniSample : self.iniSample + (FADE_TIME)] * fade_curve
        # linear fade out
        fade_curve = np.linspace(1.0, 0.0, FADE_TIME)
         # apply the curve
        self.sample[self.endSample - FADE_TIME : self.endSample] =  self.sample[self.endSample - FADE_TIME : self.endSample] * fade_curve
        plt.plot(self.sample[self.iniSample:self.endSample])
        plt.show()
        self.actSample = 0
    def nextChunk(self):
        limite = 0
        if(self.looping and self.actSample + CHUNK > self.endSample):
            limite = self.endSample
        else:
            limite = CHUNK + self.actSample
        
        outChunk = self.sample[self.actSample : limite]

        print(len(outChunk))
        if(self.looping and limite == self.endSample):
            outChunk = np.append(outChunk, self.sample[self.iniSample : self.iniSample + CHUNK - len(outChunk)])
            self.actSample = self.iniSample + CHUNK - len(outChunk)
        else:
            self.actSample += CHUNK 
        
        if(len(outChunk) < CHUNK):
            outChunk = np.append(outChunk, np.zeros(CHUNK - len(outChunk), dtype=np.float32))
        return outChunk
    def setLooping(self, bool):
        self.looping = bool

sampler = Sampler(data, True)
def callbackO(outdata, frames, time, status):
    outdata[:,0] = sampler.nextChunk()

stream = sd.OutputStream(
    samplerate = SRATE,            # frec muestreo 
    blocksize  = CHUNK,            # tamaño del bloque (muy recomendable unificarlo en todo el programa)
    channels   = 1,
    dtype = np.float32,
    callback=callbackO)  # num de canales

# arrancamos stream
stream.start()

kb = kbhit.KBHit()
# bloqueamos ejecucion para recoger respuesta
while True:
 if kb.kbhit():
        c = kb.getch()
        if(c == 'q'): sampler.setLooping(False)

kb.set_normal_term()