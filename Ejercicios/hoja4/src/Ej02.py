# sintesis fm con osciladores variables

import numpy as np         # arrays    
import sounddevice as sd   # modulo de conexión con portAudio
import soundfile as sf     # para lectura/escritura de wavs
import kbhit
import os            

SRATE = 44100       # sampling rate, Hz, must be integer
CHUNK = 1024

# fc, carrier = pitch, fm frecuencia moduladora, beta = indice de modulacion
def oscFM(fc,fm,beta,vol,frame, waveType):
    # sin(2πfc+βsin(2πfm))   http://www.mrcolson.com/2016/04/21/Simple-Python-FM-Synthesis.html
    sample = np.arange(CHUNK)+frame
    mod = beta*np.sin(2*np.pi*fm*sample/SRATE)

    if waveType == "sin":
        res = np.sin(2*np.pi*fc*sample/SRATE + mod)
    elif waveType == "square":
        squareWav = 1 if np.sin((2 * np.pi) * fc*sample / SRATE) > 0 else -1
        res = np.sin(squareWav + mod)
    elif waveType == "triangle":   
        res = (2 / np.pi) * np.arcsin(np.sin((2 * np.pi) * fc*sample / SRATE) + mod)
    elif waveType == "saw": 
        res = (2 / np.pi) * np.arctan(np.tan(((2 * np.pi) * fc*sample / SRATE)/2) + mod)
    return vol*res
    
stream = sd.OutputStream(samplerate=SRATE,blocksize=CHUNK,channels=1)  
stream.start()

kb = kbhit.KBHit()
c = ' '

fc = 440
fm = 300
beta = 1
vol = 0.8
frame = 0

while c!='q':
    # samples = oscFM(fc,fm,beta,vol,frame, "sin")
    # samples = oscFM(fc,fm,beta,vol,frame, "square")
    samples = oscFM(fc,fm,beta,vol,frame, "saw")
    # samples = oscFM(fc,fm,beta,vol,frame, "triangle")

   
    stream.write(np.float32(0.5*samples)) 
 
    frame += CHUNK

    if kb.kbhit():
        os.system('clear')
        c = kb.getch()
        print(c)        
        if c =='q': break
        elif c=='C': fc += 1
        elif c=='c': fc -= 1    
        elif c=='M': fm += 1    
        elif c=='m': fm -= 1            
        elif c=='B': beta += 0.1    
        elif c=='b': beta -= 0.1            

        print("[C/c] Carrier (pitch): ", fc)
        print("[M/m] Frec moduladora: ", fm)
        print("[B/b] Factor (beta): ",beta)
        print("q quit")

stream.stop()
