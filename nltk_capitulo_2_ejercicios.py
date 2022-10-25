import math, random

import matplotlib.pyplot as plt
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.corpus import udhr
from nltk.corpus import state_union
from nltk.corpus import names
print('II')
austen = nltk.Text(nltk.corpus.gutenberg.words('austen-persuasion.txt'))
print(len(austen))
print(len(set(austen)))
print('III')
bible = nltk.Text(nltk.corpus.gutenberg.words('bible-kjv.txt'))
web_text = nltk.Text(nltk.corpus.webtext.words('grail.txt'))
print(bible[:30])
print(web_text[:30])
#IV
# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in state_union.fileids()
#     for w in state_union.words(fileid)
#     for target in ['men','women','people']
#     if w.lower().startswith(target))
# cfd.plot()
print('V')
print(wn.synset('king.n.01').part_meronyms())
print(wn.synset('king.n.01').substance_meronyms())
print(wn.synset('king.n.01').member_meronyms())
print(wn.synset('king.n.01').part_holonyms())
print(wn.synset('king.n.01').substance_holonyms())
print(wn.synset('king.n.01').member_holonyms())
# print('VIII')
# cfd1 = nltk.ConditionalFreqDist(
#     (gender,word[0])
#     for gender in names.fileids()
#     for word in names.words(gender))
# cfd1.plot()
print('IX')
print(len(set(bible)))
print(len(set(web_text)))
print(len(set(bible))/len(bible))
print(len(set(web_text))/len(web_text))
print('X')
gutenberg = [w for w in nltk.corpus.gutenberg.words() if w.isalpha()]
fdist = nltk.FreqDist(w.lower() for w in gutenberg)
suma = 0
i = 0
tercio = []
while suma < len(gutenberg)/3:
    suma = fdist.most_common()[i][1] + suma
    tercio = [fdist.most_common()[i][0]] + tercio
    i += 1
print(tercio)
print('XII')
cmu = nltk.corpus.cmudict.entries()
print(len(cmu))
palabras_cmu = [pal for pal,pron in cmu]
print(len(set(palabras_cmu)))
print((len(cmu)-len(set(palabras_cmu)))/len(cmu))
#XIII
#XIV ERROR
# def supergloss(s):
#     definicion = wn.synsets(s).definition()
#     def_hyponyms = [wn.synsets(hypo).definition()  for hypo in synsets(s).hyponyms()]
#     def_hypernyms = [wn.synsets(hyper).definition()  for hyper in synsets(s).hypernyms()]
#     return print('Definicion: {} \n Hyponyms: {} \n Hypernyms: {}'.format(definicion, def_hyponyms, def_hypernyms) )
# supergloss('car.n.01')
print('XV')
almenos_tres = []
for palabra,frecuencia in fdist.most_common():
    if frecuencia >=3:
        almenos_tres = [palabra] + almenos_tres

print(len(almenos_tres))
print(len(fdist))

print('XVI')
print('Género \t\t Tokens \t\t Tipos \t\t Diversidad Léxica')
for categoria in brown.categories():
    categoria_palabras = [p for p in brown.words(categories= categoria) if p.isalpha()]
    tokens = len(categoria_palabras)
    tipos = len(set(categoria_palabras))
    div_lex = tipos/tokens
    print('{}\t\t{}\t\t{}\t\t{}'.format(categoria, tokens, tipos, div_lex))

print('XVII')
def comunes_50_stop(texto):
    stopwords = nltk.corpus.stopwords.words('english')
    contenido = [p for p in texto if p.lower() not in stopwords and p.isalpha()]
    fdist = nltk.FreqDist(contenido)
    return fdist.tabulate(50)

print(comunes_50_stop(brown.words(categories= 'science_fiction')))

# print('XVIII')
# def comunes_50_bigrama(texto):
#     stopwords = nltk.corpus.stopwords.words('english')
#     bigramas = nltk.bigrams(texto)
#     bigramas_stop = []
#     for p1,p2 in bigramas:
#         if p1.lower() and p2.lower() not in stopwords and p1.isalpha() and p2.isalpha():
#             bigramas_stop = [p1,p2] + bigramas_stop
#     cfd = nltk.ConditionalFreqDist(bigramas_stop)
#     return cfd.conditions()[:50]
#
# print(comunes_50_bigrama(brown.words(categories= 'science_fiction')))

print('XIX')
cfd = nltk.ConditionalFreqDist(
    (categoria,palabra)
    for categoria in brown.categories()
    for palabra in brown.words(categories=categoria))

palabras = ['god','sun','water','live','die','circle']
cfd.tabulate(samples=palabras)

print('XX')
def frecuencia_palabras(palabra, texto):
    conteo = texto.count(palabra)
    return conteo

print(frecuencia_palabras('took',brown.words()[:50]))

print('XXI')
prondict = nltk.corpus.cmudict.dict()
def estimacion_silabas(texto):
    silabas = 0
    for palabra in texto:
        if palabra in palabras_cmu:
            silabas += len(prondict[palabra])
    return silabas

print(estimacion_silabas(brown.words()[:50]))

print('XXII')
def hedge(texto):
    for i in range(3,len(texto),4):
        texto.insert(i,'like')
    return texto

print(hedge(brown.words()[:30]))

# print('XXIII')
# def ley_zipf(texto):
#     fdist = nltk.FreqDist(w.lower() for w in texto if w.isalpha())
#     return fdist
#
# # def aleatorio(veces):
# #     oracion = []
# #     while i <= veces:
# #         oracion.append(random.choice('abcdefg '))
# #         i+=1
# #     return oracion
#
# ley_zipf(brown.words()[:150]).plot()
# # ley_zipf(aleatorio(600)).plot()

print('XXIV')
def generate_model(cfdist,word, num = 10):
    for i in range(num):
        print(word, end=' ')
        words = cfdist[word]
        word = random.choice(list(words))

bigramas_lore = nltk.bigrams(brown.words(categories = 'lore'))
cfd_brown = nltk.ConditionalFreqDist(bigramas_lore)

bigramas_hibrido = nltk.bigrams(brown.words(categories = ['religion','lore']))
cfd_hibrido = nltk.ConditionalFreqDist(bigramas_hibrido)

generate_model(cfd_brown, 'world')
print('\n')
generate_model(cfd_brown, 'love')
print('\n')
generate_model(cfd_hibrido, 'world')
print('\n')
generate_model(cfd_hibrido, 'love')
print('\n')

print('XXV')
def find_lenguage(palabra):
    idiomas = []
    for idioma in udhr.fileids():
        if idioma.endswith('Latin1'):
            if palabra in udhr.words(idioma):
                idiomas.append(idioma)
    return idiomas

print(find_lenguage('life'))

print('XXVI')
freq_dist = nltk.FreqDist(len(synset.hyponyms()) for synset in wn.all_synsets('n'))
freq_dist.tabulate()

# print('XXVII')
# cfd = nltk.ConditionalFreqDist(
#     (tipo,len(wn.synsets(synset,tipo)))
#     for tipo in ['n','v','s','r']
#     for synset in wn.all_synsets())
#
# cfd.tabulate()

print('XXVIII')


























