import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cargar_documentos():
    return {
        "doc1": "El veloz zorro marrón salta sobre el perro perezoso.",
        "doc2": "Un perro marrón persiguió al zorro.",
        "doc3": "El perro es perezoso."
    }

def calcular_tfidf(textos):
    vectorizador = TfidfVectorizer()
    return vectorizador.fit_transform(textos)

def mostrar_similitud(sim_matrix, nombres):
    print("Matriz de similitud (coseno):")
    for nombre, fila in zip(nombres, sim_matrix):
        print(f"{nombre}: {fila}")

def graficar_matriz(sim_matrix, etiquetas):
    fig, ax = plt.subplots()
    cax = ax.matshow(sim_matrix, cmap='Greens')
    plt.title("Matriz de Similitud de Coseno", pad=20)
    plt.colorbar(cax)

    ax.set_xticks(range(len(etiquetas)))
    ax.set_yticks(range(len(etiquetas)))
    ax.set_xticklabels(etiquetas)
    ax.set_yticklabels(etiquetas)

    for i in range(len(etiquetas)):
        for j in range(len(etiquetas)):
            ax.text(j, i, f"{sim_matrix[i, j]:.2f}", va='center', ha='center', color='black')

    plt.tight_layout()
    plt.show()

def main():
    documentos = cargar_documentos()
    nombres = list(documentos.keys())
    textos = list(documentos.values())

    tfidf_matrix = calcular_tfidf(textos)
    sim_matrix = cosine_similarity(tfidf_matrix)

    mostrar_similitud(sim_matrix, nombres)
    graficar_matriz(sim_matrix, nombres)

# Ejecutar el programa
if __name__ == "__main__":
    main()