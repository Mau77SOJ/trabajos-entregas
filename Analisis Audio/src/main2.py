# Leer el mismo audio con diferente tasa
from IPython.display import Audio

print("Reproducción rápida:")
Audio(audio, rate=32000)  # más agudo y rápido

print("Reproducción lenta:")
Audio(audio, rate=8000)  # más grave y lento
