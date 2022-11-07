import nltk
import numpy as np
import pandas as pd
from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
import matplotlib.pyplot as plt

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

# def vectores(texto_palabras,target_palabras):
#     x = np.zeros(len(texto_palabras)) #eje de las x inamovible: una para cada token del texto
#     matriz_palabras = pd.DataFrame() #esta matriz contiene el eje de las x, y las variables con sus constantes (las palabras mas comunes)
#     matriz_palabras = matriz_palabras.append(list(x))
#     for palabra in target_palabras:
#         indice_palabra = [i for i, item in enumerate(texto_palabras) if item.lower() == palabra] #el indice de la palabra en el texto
#         for indice in indice_palabra:
#             x[indice] = target_palabras.index(palabra)
#         matriz_palabras[palabra] = x
#     return matriz_palabras

def puntos(texto_palabras,target_palabras):
    x = np.zeros(len(texto_palabras)) #eje de las x inamovible: una para cada token del texto
    for palabra in target_palabras:
        indice_palabra = [i for i, item in enumerate(texto_palabras) if item.lower() == palabra] #el indice de la palabra en el texto
        for indice in indice_palabra:
            x[indice] = target_palabras.index(palabra) + 1
    return x

direccion_corpus = 'C:/Users/chej_/Documents/Filomemia/corpus'
nolan_corpus = PlaintextCorpusReader(direccion_corpus, '.*')
# nolan_corpus_tokens = nltk.corpus.gutenberg.words('carroll-alice.txt') #aquí se escoge que tanto del texto se quiere
# nolan_corpus_tokens = nolan_corpus.words() #aquí se escoge que tanto del texto se quiere
# nolan_frecuencia_palabras = nltk.FreqDist(p.lower() for p in nolan_corpus_tokens if p.isalpha())
# nolan_palabras_mas_comunes = sorted([palabra[0] for palabra in nolan_frecuencia_palabras.most_common()]) #aqui se escoge cuantas palabras de las mas comunes se quieren
# nolan_puntos = puntos(nolan_corpus_tokens,nolan_palabras_mas_comunes)
#Este código es para graficar los puntos
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.scatter(range(0,len(nolan_corpus_tokens)), nolan_puntos)
# ax.set_xlabel('Token')
# ax.set_ylabel('Palabra')
# ax.set_title('Posición de palabras mas comunes en texto')
# plt.show()

#codigo para tagear oraciones
nolan_corpus_oraciones = nolan_corpus.sents()
nolan_corpus_oraciones_tag = nltk.pos_tag_sents(nolan_corpus_oraciones)


















