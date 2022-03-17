import kbhit
import sounddevice as sd
import soundfile as sf

# obtener nota piano.wav
data, SRATE = sf.read('piano.wav')

# abrir stream
stream = sd.OutputStream(samplerate=SRATE, 
    channels=len(data.shape))

# arrancar stream
stream.start()

kb = kbhit.KBHit()
c = ' '

# establecer multiplicador pitch para generar notas en base
# a la nota base de piano.wav
scale = [1.0, 1.12, 1.25, 1.33, 1.5, 1.69, 1.88]
high = [2.0, 2.24, 2.51, 2.66, 2.99, 3.36, 3.78, 4]

while c != '1': 
    if kb.kbhit(): # notas piano
        c = kb.getch()
        if (c=='q'): sd.play(data, SRATE * scale[0])
        elif (c=='w'): sd.play(data, SRATE * scale[1])
        elif (c=='e'): sd.play(data, SRATE * scale[2])
        elif (c=='r'): sd.play(data, SRATE * scale[3])
        elif (c=='t'): sd.play(data, SRATE * scale[4])
        elif (c=='y'): sd.play(data, SRATE * scale[5])
        elif (c=='u'): sd.play(data, SRATE * scale[6])
        elif (c=='z'): sd.play(data, SRATE * high[0])
        elif (c=='x'): sd.play(data, SRATE * high[1])
        elif (c=='c'): sd.play(data, SRATE * high[2])
        elif (c=='v'): sd.play(data, SRATE * high[3])
        elif (c=='b'): sd.play(data, SRATE * high[4])
        elif (c=='n'): sd.play(data, SRATE * high[5])
        elif (c=='m'): sd.play(data, SRATE * high[6])
        elif (c==','): sd.play(data, SRATE * high[7])

kb.set_normal_term()        
stream.stop()
exit()