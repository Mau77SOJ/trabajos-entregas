import numpy as np
from IPython.display import Audio

# Simular 8 bits (cuantización más burda)
y = (audio * 2**3).astype(np.int8)

# Reproducir
Audio(y, rate=sr)
