import sounddevice as sd
import soundfile as sf
import numpy as np  # arrays    

SRATE = 44100

# abrimos stream
stream = sd.OutputStream(samplerate=SRATE, 
    channels=1)

# arrancamos stream
stream.start()

# Happy Birthday
notas = "A.BC.D.EF.G.a.bc.d.ef.g."
songFrec = [440 * (2**(i/12)) for i in range(24)]
songIndex = 0

part = [('G', 0.5), ('G', 0.5), ('a', 1), ('G', 1),
('c', 1), ('b',2), ('G', 0.5), ('G', 0.5), ('a', 1), ('G', 1),
('d', 1), ('c',2), ('G', 0.5), ('G',0.5), ('g', 1), ('e', 1),
('c', 1), ('b', 1), ('a', 1), ('f', 0.5), ('f', 0.5), ('e', 1),
('c', 1), ('d', 1),('c', 2)]

while len(part) > songIndex:
    # tiempo y frecuencia de la wave
    actFrec = songFrec[notas.index(part[songIndex][0])]
    time = part[songIndex][1]

    # Crear Wave
    wave = np.sin(2 * np.pi * np.arange(int(SRATE*time)) * actFrec/SRATE)

    silence = np.zeros(10)

    wave = np.append(wave, silence)

    songIndex +=1
    stream.write(np.float32(wave))       
       
stream.stop()
exit()