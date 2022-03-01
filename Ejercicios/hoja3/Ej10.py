import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit               # para lectura de teclas no bloqueante

CHANNELS = 1
CHUNK = 2048
SRATE = 44100.0

class Delay:
    def __init__(self, dT):
        self.delayTime = dT
        self.buf = np.zeros(int(round(dT * SRATE)))
        print(int(round(dT * SRATE)))

    def extractChunk(self):  
        outputChunk = self.buf[:CHUNK]
        self.buf = self.buf[CHUNK:] # np.delete(self.buf, np.s_[:CHUNK], axis = 0)

        # print(len(self.buf))
        return outputChunk

    def processChunk(self, audioChunk):
        self.buf = np.append(self.buf, audioChunk, axis = 0)

delayTime = -1.0
while delayTime < 0 or delayTime > 1:
    print("Inserte delay (mayor que 0.0 y 1.0 [poner con este formato]): ", end='')
    delayTime = float(input())

delay = Delay(delayTime)
def callback(indata, outdata, frames, time, status):
    global delay
    delay.processChunk(np.copy(indata[:, 0]))
    outdata[:, 0] = delay.extractChunk()


# stream de entrada con callBack
stream = sd.Stream(samplerate=SRATE,
    dtype="float32",
    channels=CHANNELS,
    blocksize=CHUNK, 
    callback=callback)


# arrancamos stream
stream.start()

# bucle para grabacion 
kb = kbhit.KBHit()
c = ' '

while c != 'q': 
    if kb.kbhit():
        c = kb.getch()


stream.stop() 

kb.set_normal_term()
