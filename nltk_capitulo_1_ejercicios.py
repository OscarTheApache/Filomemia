from nltk.book import *

def permutation(n):
    factorial = 1
    if int(n) >=1:
        for i in range(1,int(n)+1):
            factorial = factorial * i
    return factorial

def lexical_diversity(text):
    return len(set(text))/ len(text)

def percentage(count, total):
    return 100 * count / total

#I
print(12/(4+1))
#II PESADO
# n = 26 ** 10
# r = 100
# n_nom = permutation(n)
# n_den = permutation(n-r)
# print(n_nom/n_den)
#III
print(['Monty', 'Python'] * 20)
#IV
print(len(text2),len(set(text2)))
#V
print(0.213>0.121)
#VI
# text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])
#VII
text5.collocations()
#VIII
print(len(set(text4)))
#IX
string1 = 'I told that joke in Mississippi and this guy was what'
print(string1)
print(string1+string1+string1)
print(string1*3)
#X
print(string1.split())
print(' '.join(string1.split()))
#XI
phrase1 = 'No mas no le han avisado'.split()
phrase2 = 'Mexicanos al grito de guerra'.split()
phrase3 = 'Ya llego su lodo pinches puercas'.split()
phrase4 = 'Entre los individuos como entre las naciones, el respeto al derecho ajeno es la paz'.split()
print(phrase3 + phrase1)
#XII
print('Monthly Python'[6:12])
print(['Monty', 'Python'][1])
#XIII (ERRORES)
# print(string1[2][2]=='a')
#XIV
text3.concordance('the')
#XV
print([palabra for palabra in text5 if palabra.startswith('b')][:25])
#XVI
print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))
print(list(range(20,10,-2)))
#XVII
print(text9.index('sunset'))
#XVIII
sentences = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]
vocabulary = []
for sent in sentences:
    vocabulary = vocabulary + sorted(set(sent))
print(sorted(vocabulary)[:20])
#XIX
print(len(sorted(set(w.lower() for w in text1))))
print(len(sorted(w.lower() for w in set(text1))))
#XXI
print(text2[-2:])
#XXII
fdist1 = FreqDist(text5)
print(sorted(w for w in fdist1 if len(w)<4))
#XXIII
print([w for w in text6 if w[0].isupper()])
#XXIV
print([w for w in text6 if w.istitle() and w.endswith('ise') and 'z' in w and 'pt' in w])
#XXV
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the','sea','shore']
print([w for w in sent if w.startswith('sh')])
print([w for w in sent if len(w)>4])
#XXVI
print(sum(len(w) for w in text1))
#XXVII
def vocab_size(text):
    return len(set(text))
print(vocab_size(text1))
#XXVIII
def percent(word, text):
    return text.count(word)
print(percent('sea',text1))
#XXIX
print(set(sent3) < set(text1))
