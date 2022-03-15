import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os            

SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024
A = 220

class KarplusStrong:
    def __init__(self, frec):
        self.frec = frec
        self.index = 0
        self.init = False

    def initNote(self):
        N = SRATE // int(self.frec) # la frecuencia determina el tamanio del buffer
        self.buf = np.random.rand(N) * 2 - 1 # buffer inicial: ruido
        self.init = True

        nSamples = (int)(SRATE)
        self.samples = np.empty(nSamples, dtype=np.float64) # salida
        for i in range(nSamples):
            #if i >= len(self.buf): break
            self.samples[i] = self.buf[(i) % N] # recorrido de buffer circular
            self.buf[i % N] = 0.5 * (self.buf[i % N] 
                            + self.buf[(1 + i) % N]) # filtrado

    def extractChunk(self):
        # obtener chunk a reproducir 
        outputChunk = self.samples[:CHUNK]
        self.samples = self.samples[CHUNK:]

        return outputChunk

    def extractFullNote(self):
        return self.samples

stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()

kb = kbhit.KBHit()
c = ' '
playedNotes = []

scale = [1.0, 1.12, 1.25, 1.33, 1.5, 1.69, 1.88]
high = [2.0, 2.24, 2.51, 2.66, 2.99, 3.36, 3.78, 4]

while c!='0':
    play = np.zeros(CHUNK)

    removeNote = []
    for elem in range(len(playedNotes)):
        sample = playedNotes[elem].extractChunk()
        if len(sample) < CHUNK: 
            removeNote.append(playedNotes[elem])
            sample = np.append(sample, np.zeros(CHUNK- len(sample)))
        play += sample

    for elem in range(len(removeNote)):
        playedNotes.remove(removeNote[elem])

    removeNote.clear()

    stream.write(np.float32(play))

    if kb.kbhit():
        c = kb.getch()
        if (c=='q'):
            ks = KarplusStrong(A * scale[0])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='w'): 
            ks = KarplusStrong(A * scale[1])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='e'): 
            ks = KarplusStrong(A * scale[2])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='r'): 
            ks = KarplusStrong(A * scale[3])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='t'): 
            ks = KarplusStrong(A * scale[4])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='y'): 
            ks = KarplusStrong(A * scale[5])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='u'): 
            ks = KarplusStrong(A * scale[6])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='z'): 
            ks = KarplusStrong(A * high[0])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='x'): 
            ks = KarplusStrong(A * high[1])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='c'): 
            ks = KarplusStrong(A * high[2])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='v'): 
            ks = KarplusStrong(A * high[3])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='b'): 
            ks = KarplusStrong(A * high[4])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='n'): 
            ks = KarplusStrong(A * high[5])
            ks.initNote()
            playedNotes.append(ks)
        if (c=='m'): 
            ks = KarplusStrong(A * high[6])
            ks.initNote()
            playedNotes.append(ks)
        if (c==','): 
            ks = KarplusStrong(A * high[7])
            ks.initNote()
            playedNotes.append(ks)

stream.stop()