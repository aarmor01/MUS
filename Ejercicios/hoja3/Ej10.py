# basic/record0.py Grabacion de un archivo de audio 'q' para terminar
import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHUNK = 2048
CHANNELS = 1
SRATE = 44100

class Delay:
    def __init__(self, dT):
        self.delayTime = dT
        self.buf = np.zeros(dT * SRATE)

    def extractChunk(self):  
        outputChunk = self.buf[:CHUNK]
        self.buf = self.buf[CHUNK:] # np.delete(self.buf, np.s_[:CHUNK], axis = 0)

        # print(len(self.buf))
        return outputChunk

    def processChunk(self, audioChunk):
        self.buf = np.append(self.buf, audioChunk, axis = 0)

# buffer para acumular grabación.
# (0,1): con un canal (1), vacio (de tamaño 0)
# buffer = np.empty((0, 1), dtype="float32")
delay = Delay(1)
def callback(indata, frames, time, status):
    global delay
    delay.processChunk(indata);


# stream de entrada con callBack
stream = sd.InputStream( samplerate=SRATE, dtype="float32",
    channels=CHANNELS,
    blocksize=CHUNK, 
    callback=callback)


streamOut = sd.OutputStream(samplerate=SRATE, 
    blocksize=CHUNK,
    channels=CHANNELS)

# arrancamos stream
stream.start()
streamOut.start()


# bucle para grabacion 
kb = kbhit.KBHit()
c = ' '
numBloque = 0

while c != 'q': 
    print('.')

    streamOut.write(np.float32(delay.extractChunk()))

    if kb.kbhit():
        c = kb.getch()


stream.stop() 
streamOut.stop() 

kb.set_normal_term()
