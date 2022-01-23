import sounddevice
from scipy.io.wavfile import write

fs = 44193
tempo = int(input('Tempo de gravação: '))

print('gravando...')

#capturando a gravação
record_voice = sounddevice.rec(int(tempo * fs), samplerate=fs, channels=2)
sounddevice.wait()

#salvando arquivo
write("nova_gravacao.wav", fs, record_voice)

print('Finalizamos sua gravação')