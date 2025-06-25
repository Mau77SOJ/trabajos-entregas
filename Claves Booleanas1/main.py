import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Documentos de ejemplo
corpus = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}

# Stopwords en español
stop_words = set(stopwords.words('spanish'))

def limpiar_y_tokenizar(texto):
    tokens = word_tokenize(texto.lower())
    return {palabra for palabra in tokens if palabra.isalnum() and palabra not in stop_words}

def construir_indice(corpus):
    indice = {}
    for doc_id, contenido in corpus.items():
        for palabra in limpiar_y_tokenizar(contenido):
            indice.setdefault(palabra, set()).add(doc_id)
    return indice

def procesar_consulta(consulta):
    return [token.upper() if token.upper() in {"AND", "OR", "NOT"} else token.lower()
            for token in consulta.split()]

def ejecutar_busqueda(tokens, indice, universo_docs):
    resultado = universo_docs.copy()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in {"AND", "OR", "NOT"} and i + 1 < len(tokens):
            operador, termino = token, tokens[i + 1]
            docs = indice.get(termino, set())
            if operador == "AND":
                resultado &= docs
            elif operador == "OR":
                resultado |= docs
            elif operador == "NOT":
                resultado -= docs
            i += 2
        else:
            resultado &= indice.get(token, set())
            i += 1
    return resultado

def modo_interactivo(corpus):
    indice = construir_indice(corpus)
    universo = set(corpus.keys())
    print("\n--- Búsqueda booleana interactiva ---")
    while True:
        consulta = input("Consulta (o 'salir' para terminar): ").strip()
        if consulta.lower() == "salir":
            print("Saliendo del programa.")
            break
        tokens = procesar_consulta(consulta)
        encontrados = ejecutar_busqueda(tokens, indice, universo)
        if encontrados:
            print("Documentos encontrados:", encontrados)
        else:
            print("No se encontró ningún documento que coincida con la consulta.")

# Iniciar programa
modo_interactivo(corpus)