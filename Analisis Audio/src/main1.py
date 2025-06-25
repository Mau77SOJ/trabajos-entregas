#%%
import soundfile as sf
import matplotlib.pyplot as plt
from IPython.display import Audio

# Leer el audio
audio, sr = sf.read('AnalisisTextos_16khz_mono.wav')

# Mostrar información
print("Vector de señal (segmentado):", audio[:10])  # muestra primeros 10 valores
print("Cantidad de elementos:", len(audio))
print("Frecuencia de muestreo:", sr)
print("Duración (segundos):", len(audio) / sr)

# Graficar señal
plt.plot(audio)
plt.title("Señal Sonora")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()

# Reproducir audio
Audio(audio, rate=sr)
