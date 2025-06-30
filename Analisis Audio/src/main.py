# %% [markdown]
# CARGA DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
from IPython.display import Audio, display
# %% [markdown]
# DEFINICIÓN DE FUNCIONES AUXILIARES
def mostrar_info_audio(signal, sample_rate):
    print("Matriz de datos del audio cargado:", signal)
    print(f"Total de muestras: {len(signal)}")
    print(f"Frecuencia de muestreo (Hz): {sample_rate}")
    duracion_seg = len(signal) / sample_rate
    print(f"Duración del archivo de audio: {duracion_seg:.2f} segundos\n")

def graficar_onda(audio_data, titulo, color='red'):
    plt.figure(figsize=(10, 4))
    plt.plot(audio_data, color=color)
    plt.title(titulo)
    plt.xlabel("Índice de muestra")
    plt.ylabel("Amplitud")
    plt.tight_layout()
    plt.show()
# %% [markdown]
# CARGA DEL ARCHIVO DE AUDIO Y VISUALIZACIÓN DE INFORMACIÓN BÁSICA
senal, frecuencia = sf.read("C://Users//olive//OneDrive//Desktop//Analisis Audio//src//AnalisisTextos_16khz_mono.wav")

mostrar_info_audio(senal, frecuencia)
# %% [markdown]
# REPRODUCCIÓN Y GRAFICADO DEL AUDIO ORIGINAL
print("► Reproduciendo audio original:")
display(Audio(senal, rate=frecuencia))

graficar_onda(senal, "Forma de onda - Audio original")
# %% [markdown]
# AUDIO ACELERADO (X2)
print("► Audio con velocidad duplicada:")
display(Audio(senal, rate=frecuencia * 2))

senal_rapida = librosa.resample(senal.astype(float), orig_sr=frecuencia, target_sr=frecuencia * 2)
graficar_onda(senal_rapida, "Forma de onda - Audio acelerado (x2)", color='blue')
# %% [markdown]
# AUDIO RALENTIZADO (0.5X)
print("► Audio con velocidad reducida a la mitad:")
display(Audio(senal, rate=frecuencia // 2))

senal_lenta = librosa.resample(senal.astype(float), orig_sr=frecuencia, target_sr=frecuencia // 2)
graficar_onda(senal_lenta, "Forma de onda - Audio ralentizado (x0.5)", color='blue')
# %% [markdown]
# AUDIO CON CALIDAD REDUCIDA (MENOS BITS)
senal_baja_res = (senal * 2**3).astype(np.int8)
print("► Audio con menor calidad (reducción de bits):")
display(Audio(senal_baja_res, rate=frecuencia))
# %% [markdown]
# GUARDADO DEL ARCHIVO (OPCIONAL)
"""
sf.write('AnalisisTexto_Modificado.wav', senal, samplerate=frecuencia)
print("Archivo exportado como 'AnalisisTexto_Modificado.wav'")
"""
