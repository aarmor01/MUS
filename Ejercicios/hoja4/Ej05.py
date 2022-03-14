import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os            

SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024

class KarplusStrong:
    def __init__(self, frec):
        self.frec = frec
        self.index = 0
        self.init = False

    def initNote(self):
        N = SRATE // int(self.frec) # la frecuencia determina el tamanio del buffer
        self.buf = np.random.rand(N) * 2 - 1 # buffer inicial: ruido
        self.init = True

    def extractChunk(self, nSamples):
        samples = np.empty(nSamples, dtype=np.float64) # salida
        # generamos los nSamples haciendo recorrido circular por el buffer
        for i in range(nSamples):
            if i >= len(self.buf): break
            samples[self.index + i] = self.buf[(self.index + i) % len(self.buf)] # recorrido de buffer circular
            self.buf[(self.index + i) % len(self.buf)] = 0.5 * (self.buf[(self.index + i) % len(self.buf)] 
                                                        + self.buf[(1 + (self.index + i)) % len(self.buf)]) # filtrado


        return samples

stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()

kb = kbhit.KBHit()
c = ' '
playedNotes = []

while c!='0':
    play = np.zeros(CHUNK)

    for elem in range(len(playedNotes)):
        sample = playedNotes[elem].extractChunk(CHUNK)
        play += sample
        if len(sample) < CHUNK: playedNotes.remove(elem)

    stream.write(np.float32(play))

    if kb.kbhit():
        c = kb.getch()
        if (c=='q'):
            ks = KarplusStrong(44100)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='w'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='e'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='r'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='t'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='y'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='u'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='z'): 
            ks = KarplusStrong(880)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='x'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='c'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='v'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='b'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='n'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c=='m'): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)
        if (c==','): 
            ks = KarplusStrong(440)
            ks.initNote()
            playedNotes.append(ks)

stream.stop()