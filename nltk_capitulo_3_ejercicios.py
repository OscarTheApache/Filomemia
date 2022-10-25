import nltk, re, pprint
from nltk.corpus import gutenberg
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.corpus import PlaintextCorpusReader

print('I')
s = 'colorless'
print(s[:4] + 'u' + s[4:])

print('II')
print('dishes'[:-2])
print('running'[:-4])
print('nationality'[:-5])
print('undo'[:-2])
print('preheat'[:-4])

print('VI')
palabras_biblia = gutenberg.raw('bible-kjv.txt')
nltk.re_show(r'[a-zA-Z]+',palabras_biblia[2999600:3000000])
print('espacio')
nltk.re_show(r'[A-Z][a-z]*',palabras_biblia[2999600:3000000])
print('espacio')
nltk.re_show(r'p[aeiou]{,2}t',palabras_biblia[2999600:3000000])
print('espacio')
nltk.re_show(r'\d+(\.\d+)?',palabras_biblia[2999600:3000000])
print('espacio')
nltk.re_show(r'([^aeiou][aeiou][^aeiou])*',palabras_biblia[2999600:3000000])
print('espacio')
nltk.re_show(r'\w+|[^\w\s]+',palabras_biblia[2999600:3000000])

print('VII')#hay errores ver despues
nltk.re_show(r'a|an|the',palabras_biblia[5000:5500])
nltk.re_show(r'\d[*+/-]','2+2*8+6-9 son 4, 4+2 son seis, 134*43')
print('VIII')
def url_purificador(url):
    url = request.urlopen(url).read().decode('utf8')
    url_purificado = BeautifulSoup(url, 'html.parser').get_text()
    return url_purificado

print(url_purificador('http://nltk.org/'[:100]))
print('IX')
def load(f):
    texto = open(f).read()
    patron_a = r'''(?x)     # set flag to allow verbose regexps
     (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
   | 
   | \w+(?:-\w+)*       # words with optional internal hyphens
   | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
   | \.\.\.             # ellipsis
   | [][.,;"'?():-_`]   # these are separate tokens; includes ]'''
    tokens = nltk.regexp_tokenize(texto, patron_a)
    return tokens

tokens_texto = load('C:/Users/chej_/Documents/Filomemia/corpus/tenet_CN.txt')
print(tokens_texto[:500])

print('X')
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = [(word, len(word)) for word in sent]
print(result)

print('XI')
raw = 'The reindeer in Spain  was hit mainly     by the      plane'
print(raw.split('s'))

print('XII')
for char in raw:
    print(char)

print('XIII')
print(raw.split())
print(raw.split(' '))

print('XIV')
winter_soldier = '''Longing
Rusted
Seventeen
Dawn
Stove
Nine
Kind-hearted
Homecoming
One
Freight car'''.split('\n')
print(winter_soldier.sort())
print(sorted(winter_soldier))

print('XVIII')
direccion_corpus = 'C:/Users/chej_/Documents/Filomemia/corpus'
nolan_corpus = PlaintextCorpusReader(direccion_corpus, '.*')
nolan_corpus_palabras = nolan_corpus.words()
palabras_con_wh = [p for p in nolan_corpus_palabras if re.search('wh',p) ]
print(len(palabras_con_wh))

print('XIX') #falta que salgan todas las lineas
# texto = open('Genesis 5.txt').readlines()
# for linea in texto:
#     lista = []
#     linea_split = linea.split()
#     linea_split[1:] = [int(num) for num in linea_split if not num.isalpha()]
#     lista.append(linea_split)
#
# print(lista)

print('XX')
# print(url_purificador('https://es.wikipedia.org/wiki/20_de_agosto'))

print('XXI')
# def unknown(url):
#     texto = url_purificador(url)
#     palabras_comunes = [w for w in nltk.corpus.words.words('en') if w.islower()]
#     lista = [p for p in re.findall(r'[a-z]+', texto)] #no puedo obtener la primera letra de ciertas palabras
#     return lista[:20]
#
# print(unknown('https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously'))
#
print('XXII')
# print(unknown('http://news.bbc.co.uk/'))

print('XXIV')
def hAck3r(texto):
    



