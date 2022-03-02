import kbhit
import sounddevice as sd
import soundfile as sf
import numpy as np  # arrays 

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

        return outputChunk

    def processChunk(self, audioChunk):
        self.buf = np.append(self.buf, audioChunk, axis = 0)

# Delay configurable
delayTime = -1.0
while delayTime < 0 or delayTime > 1:
    print("Inserte delay (mayor que 0.0 y 1.0 [poner con este formato]): ", end='')
    delayTime = float(input())

# callback ejecutor del Delay
delay = Delay(delayTime)
def callback(indata, outdata, frames, time, status):
    global delay
    delay.processChunk(np.copy(indata[:, 0])) # procesar canal 0 de entrada
    outdata[:, 0] = delay.extractChunk() # devolver en canal 0 de salida

# stream con callBack
stream = sd.Stream(samplerate=SRATE,
    dtype="float32",
    channels=CHANNELS,
    blocksize=CHUNK, 
    callback=callback)

# arrancar stream
stream.start()

kb = kbhit.KBHit()
c = ' '

while c != 'q': 
    if kb.kbhit():
        c = kb.getch()

kb.set_normal_term()        
stream.stop()
exit()