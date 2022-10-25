Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> import re, pprint
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> nltk.pos_tag(tokens)

>>> nltk.pos_tag(tokens)[:10]
[('TENET', 'NNP'), ('Written', 'NNP'), ('by', 'IN'), ('Christopher', 'NNP'), ('Nolan', 'NNP'), ('ORCHESTRA', 'NNP'), ('TUNING', 'NNP'), (',', ','), ('audience', 'NN'), ('settling', 'NN')]
>>> text = word_tokenize("They refuse to permit us to obtain the refuse permit")
>>> nltk.pos_tag(text)
[('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> POS_tagger.similar('man')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    POS_tagger.similar('man')
AttributeError: 'list' object has no attribute 'similar'
>>> palabras_crudo.similar('man')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    palabras_crudo.similar('man')
AttributeError: 'str' object has no attribute 'similar'
>>> tokens.similar('man')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tokens.similar('man')
AttributeError: 'list' object has no attribute 'similar'
>>> palabras.similar('man')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    palabras.similar('man')
AttributeError: 'list' object has no attribute 'similar'
>>> tagged_token = nltk.tag.str2tuple('fly/NN')
>>> tagged_token
('fly', 'NN')
>>> tagged_token[0]
'fly'
>>> tagged_token[1]
'NN'
>>> 
>>> sent = '''
... The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
... other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
... Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
... said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
... accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
... interest/NN of/IN both/ABX governments/NNS ''/'' ./.
... '''
>>> [nltk.tag.str2tuple(t) for t in sent.split()]
[('...', None), ('The', 'AT'), ('grand', 'JJ'), ('jury', 'NN'), ('commented', 'VBD'), ('on', 'IN'), ('a', 'AT'), ('number', 'NN'), ('of', 'IN'), ('...', None), ('other', 'AP'), ('topics', 'NNS'), (',', ','), ('AMONG', 'IN'), ('them', 'PPO'), ('the', 'AT'), ('Atlanta', 'NP'), ('and', 'CC'), ('...', None), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('purchasing', 'VBG'), ('departments', 'NNS'), ('which', 'WDT'), ('it', 'PPS'), ('...', None), ('said', 'VBD'), ('``', '``'), ('ARE', 'BER'), ('well', 'QL'), ('operated', 'VBN'), ('and', 'CC'), ('follow', 'VB'), ('generally', 'RB'), ('...', None), ('accepted', 'VBN'), ('practices', 'NNS'), ('which', 'WDT'), ('inure', 'VB'), ('to', 'IN'), ('the', 'AT'), ('best', 'JJT'), ('...', None), ('interest', 'NN'), ('of', 'IN'), ('both', 'ABX'), ('governments', 'NNS'), ("''", "''"), ('.', '.'), ('...', None)]
>>> nltk.corpus.brown.tagged_words()
[('The', 'AT'), ('Fulton', 'NP-TL'), ...]
>>> nltk.corpus.brown.tagged_words(tagset='universal')
[('The', 'DET'), ('Fulton', 'NOUN'), ...]
>>> nltk.corpus.treebank.tagged_words(tagset='universal')
[('Pierre', 'NOUN'), ('Vinken', 'NOUN'), (',', '.'), ...]
>>> nltk.corpus.conll2000.tagged_words(tagset='universal')
[('Confidence', 'NOUN'), ('in', 'ADP'), ('the', 'DET'), ...]
>>> nltk.corpus.sinica_treebank.tagged_words(tagset='universal')
Traceback (most recent call last):
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93msinica_treebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('sinica_treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/sinica_treebank.zip/sinica_treebank/[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nltk.corpus.sinica_treebank.tagged_words(tagset='universal')
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93msinica_treebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('sinica_treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/sinica_treebank[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

>>> nltk.corpus.sinica_treebank.tagged_words()
Traceback (most recent call last):
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93msinica_treebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('sinica_treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/sinica_treebank.zip/sinica_treebank/[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nltk.corpus.sinica_treebank.tagged_words()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93msinica_treebank[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('sinica_treebank')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/sinica_treebank[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

>>> nltk.corpus.indian.tagged_words()
Traceback (most recent call last):
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mindian[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('indian')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/indian.zip/indian/[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    nltk.corpus.indian.tagged_words()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 121, in __getattr__
    self.__load()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 86, in __load
    raise e
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mindian[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('indian')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/indian[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

>>> from nltk.corpus import brown
>>> brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
>>> tag_fd = nltk.FreqDistt(tag for (word, tag) in brown_news_tagged)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tag_fd = nltk.FreqDistt(tag for (word, tag) in brown_news_tagged)
AttributeError: module 'nltk' has no attribute 'FreqDistt'
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
>>> tag_fd.most_common()
[('NOUN', 30654), ('VERB', 14399), ('ADP', 12355), ('.', 11928), ('DET', 11389), ('ADJ', 6706), ('ADV', 3349), ('CONJ', 2717), ('PRON', 2535), ('PRT', 2264), ('NUM', 2166), ('X', 92)]
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in tokens)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tag_fd = nltk.FreqDist(tag for (word, tag) in tokens)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\probability.py", line 102, in __init__
    Counter.__init__(self, samples)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py", line 593, in __init__
    self.update(iterable, **kwds)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\probability.py", line 140, in update
    super().update(*args, **kwargs)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\collections\__init__.py", line 679, in update
    _count_elements(self, iterable)
  File "<pyshell#29>", line 1, in <genexpr>
    tag_fd = nltk.FreqDist(tag for (word, tag) in tokens)
ValueError: too many values to unpack (expected 2)
>>> tokens.tagged_words()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tokens.tagged_words()
AttributeError: 'list' object has no attribute 'tagged_words'
>>> tokens.tagged_words(palabras)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tokens.tagged_words(palabras)
AttributeError: 'list' object has no attribute 'tagged_words'
>>> POS_tagger.tagged_words()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    POS_tagger.tagged_words()
AttributeError: 'list' object has no attribute 'tagged_words'
>>> POS_tagger[:10]
[('TENET', 'NNP'), ('Written', 'NNP'), ('by', 'IN'), ('Christopher', 'NNP'), ('Nolan', 'NNP'), ('ORCHESTRA', 'NNP'), ('TUNING', 'NNP'), (',', ','), ('audience', 'NN'), ('settling', 'NN')]
>>> POS_tagger.tagged_words()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    POS_tagger.tagged_words()
AttributeError: 'list' object has no attribute 'tagged_words'
>>> tag_fd.plot(cumulative=True)
<AxesSubplot:xlabel='Samples', ylabel='Cumulative Counts'>
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in POS_tagger)
>>> tag_fd.most_common()
[('NNP', 8184), ('NN', 3855), ('DT', 3233), ('.', 2754), ('IN', 2616), ('PRP', 1815), (',', 1470), ('VBZ', 1441), ('JJ', 1087), ('RB', 957), ('VB', 875), ('NNS', 832), ('VBP', 758), (':', 621), ('VBD', 614), ('PRP$', 598), ('VBG', 565), ('TO', 559), ('CC', 441), ('CD', 317), ('(', 305), (')', 305), ('RP', 268), ('VBN', 260), ('WP', 148), ('MD', 145), ('WRB', 116), ('WDT', 41), ('JJR', 38), ('NNPS', 23), ('EX', 19), ('RBR', 17), ('JJS', 16), ('UH', 12), ('FW', 11), ('PDT', 10), ("''", 6), ('WP$', 6), ('RBS', 3), ('$', 1)]
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in POS_tagger)
>>> tag_fd.most_common()
[('NOUN', 12894), ('.', 5462), ('VERB', 4658), ('DET', 3303), ('ADP', 2616), ('PRON', 2567), ('ADJ', 1141), ('ADV', 1093), ('PRT', 827), ('CONJ', 441), ('NUM', 317), ('X', 23)]
>>> tag_fd.plot(cumulative=True)
<AxesSubplot:xlabel='Samples', ylabel='Cumulative Counts'>
>>> tokens[:10]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling']
>>> len(tokens)
35342
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> tag_fd = nltk.FreqDist(tag for (word, tag) in POS_tagger)
>>> tag_fd.most_common()
[('NOUN', 1565), ('VERB', 1007), ('ADJ', 606), ('ADV', 199), ('ADP', 58), ('PRON', 29), ('DET', 19), ('NUM', 13), ('CONJ', 6), ('PRT', 6), ('X', 2)]
>>> tag_fd.plot(cumulative=True)
<AxesSubplot:xlabel='Samples', ylabel='Cumulative Counts'>
>>> word_tag_pairs= nltk.bigrams(brown_news_tagged)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    word_tag_pairs= nltk.bigrams(brown_news_tagged)
NameError: name 'brown_news_tagged' is not defined
>>> brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
NameError: name 'brown' is not defined
>>> from nltk.corpus import brown
>>> brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
>>> word_tag_pairs= nltk.bigrams(brown_news_tagged)
>>> noun_preceders = [a[1] for (a,b) in word_tag_pairs if b[1] == 'NOUN']
>>> fdist = nltk.
SyntaxError: invalid syntax
>>> fdist = nltk.FreqDist(noun_preceders)
>>> [tag for (tag, _) in fdist.most_common()]
['NOUN', 'DET', 'ADJ', 'ADP', '.', 'VERB', 'CONJ', 'NUM', 'ADV', 'PRT', 'PRON', 'X']
>>> wsj = nltk.corpus.treebank.tagged_words(tagset = 'universal')
>>> word_tag_fd = nltk.FreqDist(wsj)
>>> [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB']

>>> [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'][:10]
['is', 'said', 'was', 'are', 'be', 'has', 'have', 'will', 'says', 'would']
>>> POS_tagger_completo = nltk.pos_tag(tokens)
>>> word_tag_fd = nltk.FreqDist(POS_tagger)
>>> [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'][:10]
['abandoned', 'accelerating', 'accomplished', 'acquired', 'acted', 'activates', 'adds', 'admires', 'affect', 'afraid']
>>> POS_tagger_completo = nltk.pos_tag(tokens, tagset = 'universal')
>>> word_tag_fd = nltk.FreqDist(POS_tagger)
>>> [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'][:10]
['abandoned', 'accelerating', 'accomplished', 'acquired', 'acted', 'activates', 'adds', 'admires', 'affect', 'afraid']
>>> tokens[:20]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed-in', 'boxes', 'toast', 'each', 'other', '.']
>>> word_tag_fd = nltk.FreqDist(POS_tagger_completo)
>>> [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'][:10]
['â\x80\x93', 'is', 'looks', 'have', 'be', 'do', 'are', 'donâ\x80\x99t', 'know', 'pulls']
>>> cfd1 = nltk.ConditionalFreqDist(wsj)
>>> cfd1['yield'].most_common()
[('VERB', 28), ('NOUN', 20)]
>>> wsj = nltk.corpus.treebank.tagged_words()
>>> cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
>>> list(cfd2['VBN'])

>>> list(cfd2['VBN'])[:20]
['been', 'expected', 'made', 'compared', 'based', 'used', 'priced', 'sold', 'named', 'designed', 'held', 'fined', 'taken', 'paid', 'traded', 'increased', 'said', 'filed', 'reached', 'called']
>>> cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in POS_tagger_completo)
>>> list(cfd2['VBN'])[:20]
[]
>>> POS_tagger_completo = nltk.pos_tag(tokens)
>>> cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in POS_tagger_completo)
>>> list(cfd2['VBN'])[:20]
['been', 'seen', 'inverted', 'done', 'dressed', 'taken', 'reversed', 'shown', 'followed', 'gone', 'made', 'confused', 'compromised', 'synchronized', 'tied', 'divided', 'told', 'set', 'dropped', 'approached']
>>> [w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
[]
>>> [w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
[]
>>> wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
>>> word_tag_fd = nltk.FreqDist(wsj)
>>> cfd1 = nltk.ConditionalFreqDist(wsj)
>>> [w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
[]
>>> [w for w in POS_tagger_completo.conditions() if 'VBD' in cfd1[w] and 'VBN' in POS_tagger_completo[w]]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    [w for w in POS_tagger_completo.conditions() if 'VBD' in cfd1[w] and 'VBN' in POS_tagger_completo[w]]
AttributeError: 'list' object has no attribute 'conditions'
>>> cfd1 = nltk.ConditionalFreqDist(POS_tagger_completo)
>>> [w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
['â\x80\x93', 'held', 'hit', 'made', 'shot', 'trained', 'confused', 'tied', 'weâ\x80\x99re', 'pulled', 'divided', 'right', 'told', 'set', 'inverted', 'dropped', 'caught', 'moved', 'put', 'left', 'supposed', 'approached', 'led', 'happened', 'asked', 'bemused', 'acquired', 'forced', 'threatened', 'let', 'vanished', 'missed', 'started', 'marked', 'lost', 'sealed', 'killed', 'recruited', 'destroyed', 'lied', 'lined', 'founded', 'pinned']
>>> idx1 = wsj.index(('kicked', 'VBD'))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    idx1 = wsj.index(('kicked', 'VBD'))
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\collections.py", line 194, in index
    raise ValueError("index(x): x not in list")
ValueError: index(x): x not in list
>>> idx1 = POS_tagger_completo.index(('kicked', 'VBD'))
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    idx1 = POS_tagger_completo.index(('kicked', 'VBD'))
ValueError: ('kicked', 'VBD') is not in list
>>> idx1 = POS_tagger_completo.index(('lost', 'VBD'))
>>> POS_tagger_completo[idx1-4:idx1+1]
[('.', '.'), ('PROTAGONIST', 'NNP'), ('Or', 'NNP'), ('Iâ\x80\x99ve', 'NNP'), ('lost', 'VBD')]
>>> idx2 = POS_tagger_completo.index(('lost', 'VBN'))
>>> POS_tagger_completo[idx2-4:idx2+1]
[('Swift', 'NNP'), ('extradition', 'NN'), (',', ','), ('then', 'RB'), ('lost', 'VBN')]
>>> def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text) if tag.startswith(tag_prefix)
	
SyntaxError: invalid syntax
>>> def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text) if tag.startswith(tag_prefix)
	
SyntaxError: invalid syntax
>>> def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text) if tag.startswith(tag_prefix)
	
SyntaxError: invalid syntax
>>> def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text) if tag.startswith(tag_prefix)
	
SyntaxError: invalid syntax
>>> def findtags(tag_prefix, tagged_text):
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text) if tag.startswith(tag_prefix)
	
SyntaxError: invalid syntax
>>> def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

>>> tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
>>> for tag in sorted(tagdict):
	print(tag, tagdict[tag])

	
NN [('year', 137), ('time', 97), ('state', 88), ('week', 85), ('man', 72)]
NN$ [("year's", 13), ("world's", 8), ("state's", 7), ("nation's", 6), ("city's", 6)]
NN$-HL [("Golf's", 1), ("Navy's", 1)]
NN$-TL [("President's", 11), ("Administration's", 3), ("Army's", 3), ("League's", 3), ("University's", 3)]
NN-HL [('sp.', 2), ('problem', 2), ('Question', 2), ('cut', 2), ('party', 2)]
NN-NC [('ova', 1), ('eva', 1), ('aya', 1)]
NN-TL [('President', 88), ('House', 68), ('State', 59), ('University', 42), ('City', 41)]
NN-TL-HL [('Fort', 2), ('Mayor', 1), ('Commissioner', 1), ('City', 1), ('Oak', 1)]
NNS [('years', 101), ('members', 69), ('people', 52), ('sales', 51), ('men', 46)]
NNS$ [("children's", 7), ("women's", 5), ("men's", 3), ("janitors'", 3), ("taxpayers'", 2)]
NNS$-HL [("Dealers'", 1), ("Idols'", 1)]
NNS$-TL [("Women's", 4), ("States'", 3), ("Giants'", 2), ("Princes'", 1), ("Bombers'", 1)]
NNS-HL [('Wards', 1), ('deputies', 1), ('bonds', 1), ('aspects', 1), ('Decisions', 1)]
NNS-TL [('States', 38), ('Nations', 11), ('Masters', 10), ('Communists', 9), ('Rules', 9)]
NNS-TL-HL [('Nations', 1)]
>>> tagdict = findtags('NN', POS_tagger_completo)
>>> for tag in sorted(tagdict):
	print(tag, tagdict[tag])

	
NN [('â\x80\x93', 142), ('door', 69), ('Protagonist', 52), ('phone', 42), ('gun', 41)]
NNP [('â\x80\x93', 638), ('PROTAGONIST', 411), ('Protagonist', 371), ('Neil', 158), ('NEIL', 154)]
NNPS [('Americans', 5), ('Russians', 3), ('CARS', 2), ('Paramilitaries', 2), ('PLIERS', 1)]
NNS [('backwards', 30), ('eyes', 22), ('nods', 18), ('people', 17), ('hands', 13)]
>>> brown_learned_text = brown.words(categories='learned')
>>> sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a =='often'))
[',', '.', 'accomplished', 'analytically', 'appear', 'apt', 'associated', 'assuming', 'became', 'become', 'been', 'began', 'call', 'called', 'carefully', 'chose', 'classified', 'colorful', 'composed', 'contain', 'differed', 'difficult', 'encountered', 'enough', 'equate', 'extremely', 'found', 'happens', 'have', 'ignored', 'in', 'involved', 'more', 'needed', 'nightly', 'observed', 'of', 'on', 'out', 'quite', 'represent', 'responsible', 'revamped', 'seclude', 'set', 'shortened', 'sing', 'sounded', 'stated', 'still', 'sung', 'supported', 'than', 'to', 'when', 'work']

>>> brown_learned_tagged = brown.tagged_words(categories='learned', tagset='universal')
>>> tags = [b[1] for (a,b) in nltk.bigrams(brown_learned_tagged) if a[0] == 'often']
>>> fd.nltk.FreqDist(tags)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    fd.nltk.FreqDist(tags)
NameError: name 'fd' is not defined
>>> fd=nltk.FreqDist(tags)
>>> fd.tabulate
<bound method FreqDist.tabulate of FreqDist({'VERB': 37, 'ADV': 8, 'ADP': 7, 'ADJ': 6, '.': 4, 'PRT': 2})>
>>> fd.tabulate()
VERB  ADV  ADP  ADJ    .  PRT 
  37    8    7    6    4    2 
>>> tags = [b[1] for (a,b) in nltk.bigrams(POS_tagger_completo) if a[0] == 'eyes']
>>> fd=nltk.FreqDist(tags)
>>> fd.tabulate()
  . VBP   :  RB   ,  CC NNP VBG  NN  IN 
  5   3   3   3   2   2   2   1   1   1 
>>> from nltk.corpus import bworn
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    from nltk.corpus import bworn
ImportError: cannot import name 'bworn' from 'nltk.corpus' (C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\__init__.py)
>>> from nltk.corpus import brown
>>> def proccess(sentence):
	for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
		if(t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
			print(w1, w2, w3)

			
>>> for tagged_sent in brown.tagged_sents():
	process(tagged_sent)

	
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    process(tagged_sent)
NameError: name 'process' is not defined
>>> for tagged_sent in brown.tagged_sents():
	proccess(tagged_sent)

	
combined to achieve
continue to place
serve to protect
wanted to wait
allowed to place
expected to become
expected to approve
expected to make
intends to make
seek to set
like to see
designed to provide
get to hear
expects to tell
expected to give
prefer to pay
required to obtain
permitted to teach
designed to reduce
Asked to elaborate
got to go
raised to pay
scheduled to go
cut to meet
needed to meet
hastened to add
found to prevent
continue to insist
compelled to make
made to remove
revamped to give
want to risk
appear to spark
fails to consider
plans to call
going to examine
plans to name
come to pass
voted to accept
happens to hold
authorized to adopt
hesitated to prosecute
try to make
decided to spend
taken to preserve
left to preserve
stand to bring
decided to seek
trying to induce
proposing to make
decided to run
directed to investigate
expected to pass
expected to make
expected to encounter
hopes to pass
came to pay
expected to receive
understood to follow
wanted to vote
decide to call
begin to flow
appears to face
fails to pass
care to acknowledge
like to convey
continued to wage
try to avoid
done to arouse
tried to economize
agreed to cooperate
want to find
expected to raise
agreed to form
threatened to form
failed to sign
trying to build
plan to absorb
working to establish
expects to evacuate
need to hear
scheduled to hold
decided to ask
scheduled to fill
going to determine
urged to move
conpired to use
used to carry
needed to face
failed to tally
failed to produce
tried to stretch
hopes to melt
slated to oppose
scheduled to share
plans to bring
seek to trim
seems to improve
appeared to win
gets to play
hopes to start
tried to teach
seem to get
started to form
like to keep
want to talk
continue to abide
refused to reconsider
expected to put
resigned to take
sought to convince
tried to blast
tried to keep
happened to think
expected to continue
plans to open
recovering to make
supposed to deliver
get to like
want to thank
set to play
going to pass
paid to play
wanted to pop
expect to establish
going to try
try to get
signed to play
fly to collect
helps to bridge
wants to pick
relearns to mingle
watching to see
learn to readjust
promises to follow
expect to offer
like to come
like to bring
combined to form
chosen to rule
attempted to stop
required to use
prepared to grant
refused to return
demanded to know
decided to end
offered to supply
designed to seek
get to know
get to know
going to call
attempted to end
forbidden to drive
failed to reach
wish to appear
hopes to rebuild
used to provide
wanted to make
trying to land
prepared to accept
continue to operate
taken to overcome
intend to make
desiring to study
designed to assure
intend to attend
failed to cooperate
agree to attend
decided to attend
scheduled to begin
agreed to meet
failed to show
declined to name
tried to subdue
planning to expand
thought to infest
voted to decertify
designed to give
continued to run
failed to place
started to turn
bought to provide
asked to set
vote to appeal
failed to reach
failed to destroy
encouraged to try
try to get
managed to maneuver
obligated to make
promised to get
attempting to connect
prepared to answer
failed to report
attempted to cash
wanting to get
combined to make
continue to grab
designed to provide
appear to favor
declined to suggest
expected to advance
required to reach
fail to give
began to come
undertake to reply
found to deal
forced to buy
starting to get
inclined to explain
supposed to look
chose to take
used to emphasize
seem to realize
happen to grow
tried to compromise
scheduled to arrive
prefer to see
set to open
expected to prove
try to influence
strive to set
decided to try
try to let
asked to read
prepared to demonstrate
led to believe
went to see
begun to pall
going to get
painted to match
appointed to serve
expected to register
failed to materialize
wanted to buy
begin to implement
tended to confirm
want to appear
try to probe
determined to apply
come to warn
known to rely
try to exploit
tended to cancel
cease to marvel
seem to represent
seems to show
declines to gamble
needs to feel
advanced to argue
undertakes to fight
decided to keep
advertising to attract
wants to operate
varied to provide
designed to reduce
use to deny
combining to lower
combining to raise
intended to effect
tend to convert
exist to raise
wish to prevent
wish to preserve
attempting to extend
made to take
continue to set
trying to persuade
attempted to take
decided to break
braced to move
needed to keep
used to carry
decided to go
happens to benefit
attempted to work
decided to join
said to regard
sought to bring
want to give
voting to cut
prepared to choke
used to approach
trying to hit
refused to let
began to acquire
proceeded to sink
proceeded to follow
hoping to slice
chose to hit
like to hit
tries to answer
want to talk
got to get
used to follow
try to play
conspired to lose
needed to revive
chosen to run
hopes to visit
got to see
arranged to sell
delighted to get
want to enjoy
tried to get
try to close
required to furnish
obliged to dole
wished to wait
decided to act
hoped to attend
like to woo
prepared to discuss
wanted to go
allowed to file
tried to persuade
began to tell
hoped to peddle
intended to insure
decided to provide
expected to go
expected to sign
like to eat
like to talk
ceased to grumble
tending to bid
start to pay
failed to measure
going to take
needed to push
trying to get
try to get
want to increase
wants to bring
threaten to strike
begun to grow
combine to serve
helping to strengthen
designed to promote
threatening to expand
seeks to get
begin to see
continue to expand
failing to render
decided to tackle
expects to sign
tends to become
came to understand
deserve to breathe
advised to seek
attempting to make
try to gun
began to fill
proposes to preserve
asked to approve
seeking to break
tends to spread
want to amend
rejected to seek
continued to speak
trying to make
expected to head
tempted to let
appear to cost
attempt to shore
seeking to achieve
expected to report
born to play
promising to build
minded to read
hope to win
threatened to ignite
beginning to take
flew to exert
proceed to validate
continues to feel
want to make
going to get
attempt to rewrite
purport to advocate
seeking to capitalize
exist to aid
learn to put
tends to create
promised to eat
hopes to include
moving to create
prepared to undertake
conspired to overthrow
seem to feel
decided to keep
applied to serve
try to seize
lead to involving
cut to allow
hope to enjoy
likes to receive
delighted to learn
going to expand
authorized to deliver
going to can
going to close
supposed to make
try to raise
tried to settle
pass to enter
came to tell
wanted to grab
stops to think
expect to get
chosen to answer
motivated to seek
disposed to covet
like to lie
going to tell
prepared to accept
try to stop
try to stop
sought to break
inclined to look
begun to act
elect to slow
like to challenge
going to move
asked to carry
expect to stop
expect to reduce
expected to supply
supposed to win
seems to lack
tends to treat
like to share
try to treat
try to bring
try to give
continue to lack
learn to color
slated to replace
strive to put
intends to provide
try to solve
decided to use
try to end
going to take
trying to organize
permitted to repair
trying to find
planned to rival
seems to speak
tried to dissuade
tends to shimmy
designed to teach
prepared to teach
wanted to sign
made to act
continue to influence
begins to notice
expected to win
seek to find
join to defeat
meant to repeat
trying to downgrade
tried to guard
want to separate
seem to indicate
afford to buy
try to develop
attempting to attract
compelled to write
failed to set
continue to shape
wants to study
wants to study
equipped to care
expected to survive
shocked to see
going to play
voted to aid
died to uphold
urged to reduce
wish to state
expected to give
trying to maintain
attempt to seek
wishes to commend
qualified to teach
want to let
informed to report
planning to shelter
plans to sit
continue to inquire
began to realize
refuse to acknowledge
required to certify
desire to participate
hasten to join
like to question
needed to help
prepared to care
like to suggest
fear to negotiate
tried to prevent
refusing to pay
like to quote
transfer to ride
managed to automate
expected to pay
collected to buy
continue to provide
wish to congratulate
help to turn
try to keep
try to frighten
wish to advocate
expect to see
refuse to aid
needs to stand
strives to emulate
refusing to show
seems to match
decided to rake
entitled to stay
bringing to bear
beginning to get
threaten to use
begin to play
begin to hunt
induced to see
going to hang
continue to test
choose to agree
chosen to find
compelled to conduct
need to realize
used to justify
fail to respond
intends to economize
bound to say
trying to mollify
used to say
came to reassert
choose to call
intend to re-enter
conscripted to enact
continues to feed
tried to integrate
poised to strike
try to force
attempting to reach
afford to take
forbidden to sit
plans to import
likes to imagine
used to get
trying to make
ceased to suggest
going to work
wanting to cut
choose to persuade
trying to keep
like to embark
suited to defeat
hastened to put
like to add
want to preserve
required to participate
happened to save
doing to promote
tempted to quote
continuing to capture
need to communicate
like to see
interested to know
allowed to rust
chose to devote
left to choose
want to own
plan to become
persuaded to restock
seems to improve
arranged to permit
seem to lend
allowed to mix
starts to swing
seems to stop
ordered to hold
fitted to endure
trying to follow
threatening to explode
rides to break
managed to make
dancing to display
hasten to report
seems to come
reassuring to see
profess to know
help to explain
forced to rely
attempt to homogenize
like to put
continue to try
try to come
seem to deal
decide to let
tries to take
trying to forget
trying to acquire
threatens to linger
decided to forego
managed to hold
intended to illustrate
tried to get
learn to live
helping to move
striving to hold
choose to work
tried to see
trying to create
made to appear
failed to make
seemed to deserve
managed to mix
want to hurt
liked to nip
manages to acquire
widened to enchant
serve to contradict
dare to experiment
tried to humanize
tries to preserve
helps to rebut
seems to make
began to play
cares to remember
serve to show
want to collect
designed to invite
attempt to make
designed to belong
seem to come
wanted to identify
neglect to cultivate
chooses to lead
chosen to sing
expected to follow
formed to spur
tends to shy
seeking to become
tries to make
began to change
try to solve
formed to fill
determined to avoid
seems to work
began to fall
began to depart
refused to give
like to sniff
continue to demonstrate
begins to wilt
going to murder
trying to puzzle
expects to profit
chooses to die
wishes to pay
conditioned to expect
hoped to tell
refusing to make
intended to stop
failed to lead
need to discipline
attempts to trace
conspire to defy
learning to think
wants to know
wants to supply
begin to look
start to think
attempt to say
come to feel
supposed to put
called to work
continue to exist
observed to characterize
continue to alienate
continue to preach
means to say
fit to place
concerned to stand
strive to formulate
proceeded to give
offer to remind
offered to allow
requested to teach
said to repeat
mean to say
inclined to extenuate
came to rescue
venture to assert
come to destroy
compelled to ask
begins to look
refuse to accept
entitled to excoriate
come to occupy
prepared to resort
obliged to become
disposed to allow
prepared to give
trying to continue
continue to use
attempting to bridge
destined to live
daring to trust
called to stand
die to save
told to express
supposed to perform
designed to give
fear to negotiate
threatening to devour
try to escape
tried to swim
learn to say
threatening to eat
remains to show
attempted to analyze
tried to consider
begin to talk
tended to stifle
begin to understand
fail to achieve
made to keep
desiring to unite
invited to speak
hesitate to ask
trying to make
help to determine
combine to provide
attempt to compensate
learn to recognize
serve to promote
claim to incarnate
led to emphasize
tend to consider
expected to seek
disposed to compromise
served to provide
mean to imply
mean to imply
attempts to face
need to submit
prepared to run
asked to choose
continuing to incur
seems to think
begin to amass
sought to limit
bring to bear
invited to participate
sought to bring
attempting to explore
seen to consist
committed to avoid
claim to serve
determined to avoid
trying to converse
started to adjust
trying to make
decided to take
forced to conclude
beginning to make
helped to make
made to give
determined to exclude
sought to win
sought to avoid
meant to incur
supposed to result
cited to show
supposed to possess
burned to make
wanted to find
helps to meet
rejoiced to see
began to suspect
began to review
called to sit
began to write
decided to try
takes to tell
seemed to widen
proceeded to teach
helps to make
remember to make
supposed to like
working to improve
like to make
added to encourage
like to shear
needs to tell
like to grow
allowed to mature
used to attack
continued to threaten
decide to build
used to destroy
going to develop
put to see
fail to develop
seem to fall
serve to emphasize
tend to stamp
fail to enter
rehearing to acquire
fail to convey
needed to attain
seem to reduce
continue to show
sponsored to win
invited to judge
asked to pick
qualified to judge
helping to create
qualified to win
continuing to donate
found to take
built to accommodate
bothered to make
wanted to purchase
managing to get
formed to develop
used to indicate
meant to pertain
designed to cater
equipped to handle
pulled to clear
Tend to make
progresses to insure
Endeavor to get
used to separate
used to separate
seems to know
wanted to trot
likes to trot
wants to trot
started to pace
starting to go
expected to race
designed to push
looks to run
began to motor
trained to drag
fled to make
seemed to know
used to say
preferred to get
hope to cover
want to miss
scheduled to vanish
vanish to make
continued to live
seem to cascade
forget to buy
fail to shorten
intend to cook
sized to fit
continue to release
wish to create
trim to fit
cut to fit
help to prevent
designed to take
used to transport
want to buy
used to fasten
help to keep
needed to build
designed to accommodate
adjusted to suit
used to cut
want to avoid
agreed to take
planned to destroy
allowed to issue
managed to coerce
want to know
planning to bring
urged to keep
come to swim
enjoined to look
prepared to cope
want to make
allowed to dry
pays to buy
want to play
expected to last
plan to add
want to start
plan to buy
going to need
continue to reduce
needed to arrive
done to correct
cost to make
settled to find
grew to fulfill
attempted to restrict
conceived to affirm
prefer to believe
tried to refashion
begin to fear
linger to haunt
disciplined to serve
trained to fulfill
organized to furnish
continued to paint
made to weave
try to place
hesitate to add
seemed to emphasize
mean to project
wishes to convey
beginning to learn
start to study
said to start
wished to get
Try to push
taken to see
promises to open
selected to operate
used to measure
employed to measure
used to detect
tend to reflect
used to scan
decided to enter
preparing to matriculate
continued to help
intend to carry
lived to see
manage to experiment
tempted to compare
made to see
caused to glow
made to flow
happened to place
used to construct
used to fill
examine to make
designed to counter
tend to become
try to share
continue to make
come to expect
used to keep
bound to increase
trying to match
going to take
continue to exceed
extended to compare
continue to divorce
fail to lower
supposed to stand
prepared to teach
school to cover
make to assess
try to set
encouraged to take
try to maintain
plan to limit
make to assure
afford to spend
Aim to balance
Check to see
called to determine
cooperate to launch
designed to expose
existing to acquaint
like to organize
begin to appreciate
inclined to think
needed to protect
struggling to meet
helping to account
want to learn
used to think
fights to change
tends to rise
expects to extend
learn to wear
tried to make
appears to lie
attempted to provide
found to allow
planned to duplicate
wants to interest
want to risk
want to use
continue to learn
meant to convey
used to minimize
try to wrestle
trying to install
plan to build
equipped to handle
equipped to package
equipped to receive
equipped to save
plan to increase
hopes to cut
bound to swell
begin to feel
want to change
arrange to rent
plan to travel
plan to visit
like to start
wish to budget
wanting to rent
want to see
want to throw
designed to work
trying to prepare
began to develop
used to suggest
wanted to polish
pays to consider
compelled to use
began to fall
begun to write
made to seem
attempting to direct
pleased to call
scheduled to nominate
come to spend
managed to irrigate
stooped to scoop
fall to show
try to push
begins to deteriorate
used to like
offered to ship
hopes to find
invented to hold
learn to like
labored to set
set to receive
entered to compete
seem to make
seemed to answer
decided to use
began to show
Wishing to show
learned to set
forced to fly
hope to break
came to recognize
turning to cup
seems to creep
going to live
got to learn
learn to live
going to live
like to sew
love to run
love to crack
yearn to make
tried to see
love to dust
like to become
decide to write
cause to exist
learn to portray
learn to portray
began to advise
taught to yield
prefer to cope
helps to explain
surprised to bump
seemed to brave
begins to regard
began to embezzle
appears to endorse
expected to like
begin to assert
began to challenge
going to become
helping to make
began to stress
began to describe
fails to gain
liked to play
love to audition
wanted to show
like to see
loved to dance
try to bid
wanted to go
asked to leave
continued to promote
wished to meet
hoping to see
got to know
paused to comfort
hesitate to quote
decided to see
wanted to take
need to know
need to look
beginning to protrude
try to speak
decides to proceed
interested to hear
seems to probe
preferring to consider
known to go
amazed to realize
seeking to help
interpreted to conform
explored to find
trying to throw
designed to find
required to mark
asked to consider
seem to involve
seems to smell
seems to see
learned to develop
arranged to meet
need to work
want to raise
need to bring
expect to grow
expected to work
want to include
going to produce
want to hire
want to buy
want to hire
going to farm
need to know
want to undertake
want to buy
wish to locate
plan to sell
want to go
intend to raise
cost to live
expected to produce
expect to get
forced to lay
trying to explain
happened to light
began to turn
intended to warn
used to transform
forced to overcome
begins to give
failed to post
refused to permit
encouraged to beget
obliged to obey
united to push
try to oppose
made to impose
wanted to clarify
proposed to sail
determined to catch
forced to turn
seemed to sense
seemed to know
tried to brush
turning to repeat
tried to persuade
wanted to turn
preparing to pacify
forced to retreat
contracted to supply
forced to leave
offering to bring
attempt to bring
decided to cast
liked to tease
going to buy
com to sea
drilled to follow
born to command
come to recognize
allowed to account
created to fan
come to mean
trying to make
refusing to keep
wishes to discuss
want to ask
want to tap
said to use
employed to see
shoot to kill
refused to touch
threatened to shoot
said to let
begin to roll
held to assure
going to make
managed to get
wanted to play
prepared to counterattack
failed to rally
tried to rape
refused to speak
called to look
refused to say
mean to suggest
prepared to carry
designed to overthrow
trying to put
needed to work
disposed to exploit
fail to see
bound to fall
tempted to place
need to ask
seek to undermine
hand to show
begun to spit
threatened to ignite
invited to take
rushing to keep
like to wander
like to follow
professing to believe
want to show
enabled to attend
determined to exercise
inclined to exaggerate
like to go
determined to marry
said to sprinkle
used to stop
bought to apply
supposed to cause
said to give
allowed to rest
enters to spoil
wish to deny
allowed to warm
wishes to entertain
allowed to stand
refused to accept
wished to continue
persuaded to accept
decided to charge
decided to go
allowed to see
agreed to take
decide to send
allowed to delay
request to leave
promised to treat
declined to enter
added to reinforce
obliged to publish
continue to serve
plans to serve
Hoping to cut
obliged to announce
wish to preserve
heard to remark
hopes to redress
desires to walk
prefer to take
likes to measure
proposed to corral
intended to stay
ceased to look
manages to overlook
troubled to read
destined to go
expected to go
used to characterize
helping to raise
decided to stay
used to refer
needs to educate
tended to tamp
like to underline
begun to falter
intend to include
wish to improve
try to take
prefers to designate
want to join
seeking to increase
used to make
used to make
inclined to remain
heard to say
stopped to receive
used to describe
claimed to own
tried to find
meant to pay
given to go
wanted to make
began to gallop
attempting to lasso
failing to encircle
got to get
trying to maneuver
beginning to go
began to pull
began to draw
like to go
tend to compete
doing to help
begins to see
Desiring to fill
tends to look
try to match
played to win
failed to make
began to involve
learning to bunt
dared to dream
dared to taunt
refused to come
undertook to set
essayed to down
began to prosper
liked to wring
happened to sit
hastened to place
began to offer
seemed to indicate
liked to imagine
expected to know
began to appear
begin to store
continue to sanction
intended to demonstrate
permitted to exercise
encouraged to develop
failing to behave
appeared to regard
seek to disprove
tends to fuse
prefers to adduce
empowered to compel
designed to prevent
disposed to heed
agree to let
seeking to reform
used to crowd
Ask to see
interested to learn
pass to add
demanding to know
seems to threaten
tried to describe
tried to explain
seem to feel
got to play
ceased to need
like to live
came to see
threatens to break
begins to fade
begins to appear
equipped to tell
used to increase
hired to repeat
wished to make
seems to exist
means to choose
struggle to insulate
serves to crystallize
doomed to become
serves to illuminate
failed to furnish
encouraged to trade
continued to come
promised to send
attempted to understand
decided to send
assigned to arrest
planned to build
offered to surrender
gone to live
returned to succeed
expected to arrange
expected to supply
expected to entertain
tried to bring
provoked to use
refused to let
needed to outwit
purporting to inform
inspired to remind
mean to tell
trying to demonstrate
went to visit
continued to teach
beginning to devise
learn to like
stood to watch
planned to go
trying to plan
continues to grow
learn to keep
learned to polish
left to meet
fails to make
resolved to maintain
register to vote
needs to make
going to march
proposed to defeat
proposed to enter
seems to require
seem to violate
tended to obscure
continue to view
try to coerce
likes to believe
continue to affect
served to overcome
tends to further
help to reveal
struggle to assert
said to exist
taken to guard
done to increase
ready to tick
forced to hypothesize
used to challenge
permitted to authorize
decides to break
required to pass
decide to clobber
decided to reverse
tried to start
forbidden to fly
required to copy
began to move
run to live
started to glance
try to memorize
turned to look
trying to talk
started to decline
continues to take
continues to center
come to see
come to walk
beginning to complain
gather to sing
began to converse
began to relax
hoped to become
forced to restrict
began to give
asked to become
trying to sell
serves to stimulate
seemed to lack
offered to make
assembled to warrant
returned to preside
sought to prevent
expect to stand
compelled to face
continue to live
refused to move
refused to obey
doomed to become
tended to romanticize
supposed to keep
left to rest
wants to see
tended to dress
designed to become
begins to feel
tends to depict
transferred to become
impelled to make
seeks to make
made to look
happen to meet
told to lie
wanted to write
tempted to say
omitting to assert
continue to live
refused to permit
served to maintain
seem to make
help to dispel
trained to describe
daring to abandon
seem to resemble
appears to lie
tend to persist
tried to describe
like to call
began to speak
try to say
attempting to make
attempt to answer
wanted to know
designed to enhance
intended to provide
continue to suffer
serves to make
fails to reach
beginning to crack
drawn to join
made to bite
forbidden to swing
seemed to hear
hired to drive
try to work
forbidden to love
made to represent
starts to ride
tries to stop
begins to gather
brought to pass
tends to reflect
tended to stratify
chosen to use
used to mean
forced to respond
tends to lose
tends to express
made to integrate
try to get
attempted to restrain
wished to continue
failed to flourish
propose to go
wished to segregate
liked to fancy
Deciding to become
strove to see
used to play
returned to live
proceeded to find
likes to catch
seems to care
intends to save
compelled to find
wishes to continue
ceasing to write
stops to ask
expected to fulfill
tailored to meet
want to say
want to quote
seems to realize
primed to catch
try to diagnose
want to point
used to regard
seems to represent
trying to draw
wish to see
used to include
allowed to operate
urged to produce
afford to present
decides to drop
expect to abolish
needed to pit
tempted to blame
hope to serve
tried to remedy
tends to express
seem to believe
permitted to return
attempted to make
prepared to demonstrate
calculated to suggest
seemed to disconcert
known to make
going to talk
learns to focus
chooses to subordinate
wish to preserve
cease to exist
seem to constitute
destined to fail
wants to get
began to understand
wanted to capture
liked to tell
decided to migrate
continued to trouble
labored to finish
decided to return
waiting to go
chosen to serve
came to know
helped to escape
opened to admit
happened to see
brought to bear
inclined to argue
seeming to say
prompted to write
come to dominate
used to illustrate
prepared to find
wish to argue
begin to read
plan to discuss
come to call
expect to find
come to believe
continue to pay
tend to thump
determined to prove
learn to control
used to frustrate
trying to assert
trying to expose
comes to regard
felt to indicate
came to speak
needed to explain
required to make
sought to make
accustomed to think
come to look
undertook to give
came to study
bound to go
tried to dazzle
got to know
presumed to address
obliged to defend
coming to spend
learned to write
obliged to send
began to trail
began to fly
tried to calm
inspired to complete
began to talk
compelled to spend
expected to carry
tend to make
liked to think
trying to emulate
wanted to know
seemed to remember
asked to yield
made to look
begun to lose
failed to learn
wanted to take
writing to devote
vowed to kneel
hoping to lift
forced to seek
continue to urge
prepared to assist
hope to make
continue to maintain
scheduled to go
taken to program
begun to probe
attempting to present
instructed to burn
attempted to conclude
equipped to handle
trying to check
mean to write
wished to pursue
refused to attend
decided to dance
failed to amaze
continued to search
threatening to swallow
pleased to see
tried to discover
disturbed to find
failed to realize
manage to get
wanted to buy
decided to bypass
allowed to preach
allowed to pass
dared to drop
expected to move
means to ridicule
hesitate to sacrifice
forced to move
taken to effect
hoped to imprint
tailored to fit
obliged to describe
tried to block
chosen to edit
plotted to take
tried to halt
wanted to die
returned to make
like to believe
bother to look
used to go
seemed to thaw
came to give
wanted to see
used to look
meant to help
like to straighten
hope to give
bark to let
dash to get
tried to talk
decided to leave
used to tell
continue to reflect
appear to preach
intend to let
need to test
learned to meet
said to give
serves to reduce
thought to provide
tends to give
wish to deny
expect to find
seek to capture
allowed to claim
seeks to recapture
determined to bulldoze
sought to run
needed to make
hurry to catch
planned to bolt
fit to nominate
intend to support
refusing to abandon
begun to parallel
help to give
fail to convey
tends to lose
aimed to write
granted to serve
tends to underestimate
permitted to cross
demanding to know
obliged to remain
delighted to make
seem to shake
assigned to check
volunteered to advance
went to hurry
refused to notice
began to select
began to specify
failed to work
care to come
helped to deepen
come to say
fitted to live
stoop to argue
obliged to insist
managed to annex
going to prove
preparing to test
came to know
got to know
persuaded to lend
expected to report
began to experience
attempted to get
happened to catch
chanced to soil
begins to besiege
beginning to attract
come to learn
serve to lead
try to get
longing to see
long to see
trying to promote
beginning to fill
wants to linger
chiseled to match
trying to track
determined to get
began to develop
continued to grow
decided to capitalize
came to favor
used to describe
began to play
gathered to hear
guaranteed to excite
invited to deliver
sent to knoe
preparing to deport
told to leave
constrained to move
refused to let
managed to get
trying to get
tending to arouse
sent to get
tried to arbitrate
tried to arbitrate
ordered to knock
refused to attend
determined to compel
refused to sanction
going to let
attempt to prorate
leaving to come
please to write
want to go
want to teach
wanted to go
tried to picture
waiting to hear
came to live
began to show
tends to weaken
seems to rise
permitted to see
continues to discuss
serve to sublimate
wanted to close
wished to keep
want to describe
began to denounce
afford to place
try to fit
decides to enter
expected to prefer
tend to bring
tend to become
tend to assimilate
tend to converge
disposed to question
forced to realize
assembled to bear
beginning to tell
hastened to dispatch
ordered to attack
going to trouble
wanted to borrow
trying to pick
helping to prevent
preferred to sell
think to take
ordered to approach
prepared to move
come to pay
refused to grant
want to offend
seeming to invalidate
want to drive
left to resist
tempted to consider
empowered to swear
allowed to appoint
wanted to invest
decided to stay
live to see
began to put
decided to leave
wanted to leave
want to see
come to say
began to move
went to visit
got to drink
seem to know
wanted to help
seem to fall
tends to obscure
beginning to point
trying to prove
trying to sort
Start to prepare
obliged to go
declined to introduce
enter to ask
seems to lie
continued to shape
seem to pass
prepared to accept
done to obtaine
expected to reach
seems to refer
tried to consult
came to put
seemed to promise
needed to possess
seem to indicate
purports to examine
attempts to understand
tend to disprove
forced to admit
attempt to ascertain
forced to demonstrate
sought to maintain
determined to resist
compelled to make
threatening to murder
agreed to see
learned to know
written to say
came to see
liked to think
chosen to follow
went to see
forced to depict
expect to find
hoped to persuade
decided to go
compelled to spend
indisposed to appear
try to keep
arrived to see
try to keep
made to write
training to keep
decided to give
wanted to apologize
began to cry
going to make
forced to learn
required to absorb
learned to write
learned to dispute
learned to dispute
ceased to exist
inclined to inquire
like to say
permitted to write
wait to see
choose to fill
served to confirm
like to suggest
wanted to know
expected to happen
asked to join
seem to regard
inclined to say
cease to haunt
wishes to express
continue to bridge
struggle to keep
begin to look
began to feel
begins to doubt
seemed to survive
begins to dream
refuses to surrender
began to discover
decided to seek
seek to eliminate
organized to deal
expected to consist
beginning to use
tried to enter
forced to play
want to quibble
used to make
love to suffer
love to suffer
came to believe
trying to outdo
used to say
castigates to liberate
helped to educate
expect to find
supposed to supplant
wanted to write
asked to see
planned to lay
wanted to put
decide to disown
wanted to pay
known to make
trying to prove
required to meet
designed to improve
designed to assist
wish to buy
made to establish
required to carry
established to provide
desire to explore
required to own
required to attain
decide to support
prepared to depart
designed to provide
designed to raise
designed to prevent
aimed to attract
like to press
take to show
designed to prevent
persuaded to take
induced to establish
persuaded to adopt
persuaded to adopt
prepared to give
prepared to enter
dedicated to secure
like to think
like to think
afford to lose
continues to add
helping to pilot
prefer to speak
go to discuss
made to replace
continuing to seek
seem to add
seem to fix
known to tax
like to see
continued to run
voted to continue
entitled to benefit
needed to establish
designed to give
remain to preserve
gathered to thank
continue to protect
amended to read
construed to alter
required to correlate
amended to read
directed to make
directed to establish
continued to display
required to move
planned to furnish
agreed to submit
initiated to resolve
found to exist
taken to isolate
modified to reduce
tending to separate
established to gather
used to study
used to measure
used to calculate
directed to mail
offers to pay
promises to pay
construed to limit
directed to pay
directed to cover
failed to offer
intends to pursue
helping to create
wish to merge
pleased to note
continue to serve
pleased to note
inclined to drag
trying to get
made to enlist
try to run
designed to help
designed to reflect
designed to avoid
designed to reflect
required to help
working to develop
installed to increase
prepared to stay
used to keep
came to receive
tend to create
attempting to bring
designed to arrest
attempt to monopolize
held to appoint
prepared to submit
allowed to petition
ordered to terminate
required to pass
required to pass
permitted to endanger
compelled to testify
permitted to rebut
failed to show
permitted to rebut
refused to require
ordered to report
ordered to report
fail to see
sought to secure
failed to show
entitled to inspect
hopes to find
like to make
found to enable
need to concern
fail to bring
fail to act
want to stimulate
want to make
tended to ignore
expected to take
expected to know
expected to supervise
begins to go
moved to think
beginning to box
surprised to find
hope to win
began to talk
begins to take
decided to make
asked to give
formed to give
taken to link
put to use
use to pay
going to work
combine to provide
wish to serve
expected to increase
needed to maintain
needed to obtain
planned to maintain
needed to meet
proposed to authorize
decided to stop
scheduled to become
seek to assure
agrees to furnish
prepared to consider
prepared to act
prepared to act
required to cease
required to operate
designed to operate
permitted to operate
taken to minimize
permitted to operate
permitted to operate
permitted to operate
required to operate
required to afford
elect to use
required to file
required to file
elect to use
required to file
obligated to furnish
trained to read
made to assure
tend to create
rejoicing to remember
permitted to run
came to work
decided to bring
found to permit
helping to strengthen
began to ship
believed to provide
designed to provide
expect to make
developed to facilitate
set to hold
continuing to carry
designed to increase
improved to obtain
purchased to permit
extended to provide
sought to meet
designed to handle
invited to participate
planned to provide
inclined to advance
aims to give
wish to pursue
expected to increase
expected to exceed
begun to make
continues to expand
began to make
need to learn
learn to delegate
working to attain
begun to translate
besieged to serve
help to create
assumed to originate
used to describe
expected to cause
taken to study
required to ensure
used to measure
used to start
started to strike
allowed to pull
used to measure
generalized to include
eliminated to obtain
extended to include
used to derive
adjusted to minimize
required to make
taken to prevent
attempts to present
evaporate to leave
tend to stick
helps to float
acts to remove
tend to accelerate
appear to offer
allowed to take
allowed to distil
undertaken to see
allowed to stand
thought to contribute
made to characterize
expect to find
known to cause
allowed to stand
allowed to stand
used to test
allowed to clot
need to make
try to key
manage to keep
seem to prefer
continues to add
begin to play
begin to appear
begin to dig
cease to lay
manages to slip
seem to recognize
like to burrow
like to think
estimated to contain
love to visit
fail to show
attempts to weigh
given to complete
required to reach
prove to belong
varied to allow
noted to draw
noted to occur
permitted to speculate
designed to stop
failing to demonstrate
failed to demonstrate
applied to man
begin to ossify
seen to begin
constructed to serve
wishes to study
attempted to simplify
coupled to form
appear to affect
appear to act
presumed to occur
found to contain
appears to result
used to obtain
like to re-emphasise
adopted to make
failed to change
failed to show
thought to represent
failed to show
attempting to improve
allowed to react
used to filter
photographed to show
thought to represent
seems to follow
known to contribute
fail to elicit
failed to evoke
fail to eat
trying to study
try to study
wish to show
need to find
like to give
chosen to give
need to know
plans to go
tossed to decide
want to know
want to study
expect to face
choose to derive
seeking to become
mobilized to achieve
required to make
work to realize
seek to encourage
prefer to live
afford to wait
begin to see
committed to move
continue to satisfy
begun to develop
programming to go
fail to push
attempt to communicate
fitted to perform
seeks to satisfy
tends to integrate
tends to support
threatened to burst
helped to understand
combined to prevent
needed to bolster
helping to further
seem to vary
seem to act
obliged to organize
expected to show
used to adjust
tended to break
delegated to cooperate
expect to obtain
planned to double
began to plan
attempted to design
hastened to add
seem to indicate
decided to hold
appear to drop
get to take
began to get
began to meet
increased to include
chose to report
expected to read
expected to confront
appeared to reach
continued to give
invoked to explain
wanted to go
mean to imply
supposed to happen
learning to read
asked to describe
learning to read
expected to earn
expected to earn
surprised to find
struggle to induce
asked to learn
prefer to test
told to purchase
seemed to antagonize
designed to develop
refused to change
refused to change
refused to accept
supposed to know
working to become
led to see
asked to vote
duplicated to form
learn to play
want to change
learns to become
began to emerge
used to annoy
stooping to dispense
come to see
preferred to keep
used to give
came to feel
used to accomplish
found to match
required to store
saved to represent
saved to represent
created to accommodate
inspected to determine
used to look
serve to illustrate
intended to decrease
required to improve
italicized to guide
seems to center
operate to center
serves to focus
purport to represent
hesitates to suggest
mentioned to make
trying to develop
compelled to omit
continue to show
planning to use
expecting to recover
meant to move
preferred to continue
trying to find
planned to exterminate
trying to marry
pledged to hold
determined to create
seemed to assure
attempted to marry
obliged to concede
expected to democratize
Failing to heed
determined to keep
tend to procrastinate
even to repudiate
served to minimize
encouraged to state
trying to unearth
decided to remove
decide to encourage
prefer to hire
go to work
intended to provide
continues to stress
encouraged to adopt
motivated to take
expected to respond
training to meet
used to pay
taken to indicate
afford to trade
afford to lose
taken to exemplify
Try to imagine
trying to outfox
trying to get
invited to try
try to imagine
begin to affect
tend to move
required to pay
seek to force
act to accentuate
begin to edge
move to restrain
continue to press
trying to win
bound to mean
continue to move
continue to rise
operate to keep
expected to put
presumed to realize
assembled to legislate
sought to find
tend to view
wished to minimize
designed to deal
ordered to retain
refused to permit
refuse to exercise
prepared to read
wants to displace
authorized to fashion
choose to assert
used to impose
chooses to enforce
heard to object
goes to prove
intended to obstruct
entitled to sue
entitled to sue
appear to permit
applied to eliminate
entitled to sue
entitled to sue
elected to file
elect to continue
intended to ease
permitted to survive
furnished to probe
want to make
designed to minimize
designed to elicit
continued to arrive
coded to permit
wishing to sell
endeavored to maintain
directed to provide
seeking to continue
refused to assume
concerned to leave
attempt to settle
continue to make
seems to increase
exists to show
learning to control
want to explore
struggling to meet
trying to learn
continues to increase
like to tease
begins to decline
begins to substitute
learned to cooperate
begins to participate
helping to make
failing to achieve
trying to say
learn to identify
failing to make
needs to know
fails to meet
expected to administer
used to store
permitted to see
expected to study
wish to note
required to furnish
want to provide
attempt to represent
hopes to encourage
designed to help
appointed to act
expected to vote
appointed to study
tended to take
attempted to act
attempt to act
attempt to act
intend to act
fail to take
try to serve
tended to use
found to behave
impelled to make
attempt to analyze
designed to reflect
deemed to vary
held to constitute
seem to support
designed to cover
found to vary
taken to rest
needs to know
attempts to stand
wishing to know
made to appear
attempts to supply
like to record
claims to show
mean to assert
mean to assert
prepared to say
mean to say
sought to express
said to learn
mean to say
meant to say
meant to say
meant to express
forced to go
disposed to quarrel
seem to present
allowed to move
tended to reflect
beginning to appreciate
begun to disturb
venture to assign
crystallized to find
begin to show
beginning to expand
dared to give
continued to employ
began to creep
seems to appear
rode to arrest
serve to quiet
decided to ride
prepared to fight
allowed to see
refused to give
compelled to kill
desiring to leave
wanted to clean
needed to hire
continued to spring
extended to include
intending to use
need to commit
sought to place
want to know
want to know
serve to contrast
obligated to regard
tried to make
attempting to falsify
continued to accuse
continued to accuse
dare to instigate
acting to deliver
seeking to free
endeavoring to deliver
doomed to suffer
adopted to accomplish
fails to honor
began to mix
began toTraceback (most recent call last):
  File "<pyshell#131>", line 2, in <module>
    proccess(tagged_sent)
  File "<pyshell#126>", line 4, in proccess
    print(w1, w2, w3)
KeyboardInterrupt
>>> brown_news_tagged = brown.tagged_words(categories = 'news', tagset='universal')
>>> data = nltk.ConditionalFreqDist((word.lower(), tag)
				for(word, tag) in brown_news_tagged)

>>> for word in sorted(data.conditions()):
	if len(data[word]) > 3:
		tags = [tag for (tag, _) in data[word].most_common()]
		print(word, ' '.join(tags))

		
best ADJ ADV VERB NOUN
close ADV ADJ VERB NOUN
open ADJ VERB NOUN ADV
present ADJ ADV NOUN VERB
that ADP DET PRON ADV
>>> POS_tagger_completo = nltk.pos_tag(tokens, tagset= 'universal')
>>> data = nltk.ConditionalFreqDist((word.lower(), tag)
				for(word, tag) in POS_tagger_completo)
>>> for word in sorted(data.conditions()):
	if len(data[word]) > 3:
		tags = [tag for (tag, _) in data[word].most_common()]
		print(word, ' '.join(tags))

		
amongst ADP VERB ADJ PRT NOUN
around ADP ADV PRT NOUN
back ADV NOUN ADJ VERB PRT
close ADV ADJ NOUN VERB
donât VERB NOUN ADJ ADV
down ADV PRT NOUN ADP
heâs NOUN VERB ADJ DET PRON
itâll NOUN ADJ VERB ADV
like ADP NOUN VERB ADJ
neil NOUN CONJ VERB ADJ ADP DET
no DET NOUN X ADV CONJ
off ADP PRT NOUN ADV
okay NOUN VERB X ADJ ADV
out PRT ADP NOUN ADV
over ADP PRT NOUN ADV
priya NOUN VERB . CONJ
protagonist NOUN VERB ADJ CONJ
right ADV NOUN ADJ VERB
sator NOUN VERB . ADJ NUM
ten NOUN VERB NUM ADJ
thatâs NOUN VERB ADJ ADP
tight ADJ VERB ADV NOUN
towards ADP NOUN VERB ADV
up PRT ADV ADP NOUN
weâre NOUN VERB ADJ ADP
whatever DET VERB ADP NOUN
which DET NOUN ADJ ADP
wonât VERB NOUN DET ADV
youâd ADV NOUN PRON VERB CONJ ADJ
youâll NOUN ADV . ADJ
youâre NOUN ADV VERB CONJ ADJ PRT DET PRON .
youâve NOUN VERB ADV CONJ ADJ
â NOUN VERB ADJ ADP X ADV NUM PRT DET PRON CONJ
>>> nltk.app.concordance()

**********************************************************************
  Resource [93malpino[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('alpino')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/alpino[0m

  Searched in:
    - 'C:\\Users\\chej_/nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\share\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Local\\Programs\\Python\\Python39\\lib\\nltk_data'
    - 'C:\\Users\\chej_\\AppData\\Roaming\\nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
**********************************************************************

>>> pos = {}
>>> pos
{}
>>> pos['colourless'] = 'ADJ'
>>> pos
{'colourless': 'ADJ'}
>>> pos['ideas'] = 'N'
>>> pos['sleep'] = 'V'
>>> pos['furiously'] = 'ADV'
>>> pos
{'colourless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
>>> pos['ideas']
'N'
>>> pos['N']
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    pos['N']
KeyError: 'N'
>>> pos[:'N']
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    pos[:'N']
TypeError: unhashable type: 'slice'
>>> len(pos)
4
>>> list(pos)
['colourless', 'ideas', 'sleep', 'furiously']
>>> sorted(pos)
['colourless', 'furiously', 'ideas', 'sleep']
>>> [w for w in pos if w.endswith('s')]
['colourless', 'ideas']
>>> for word in sorted(pos):
	print(word + ":", pos[word])

	
colourless: ADJ
furiously: ADV
ideas: N
sleep: V
>>> list(pos.keys())
['colourless', 'ideas', 'sleep', 'furiously']
>>> list(pos.values())
['ADJ', 'N', 'V', 'ADV']
>>> list(pos.items())
[('colourless', 'ADJ'), ('ideas', 'N'), ('sleep', 'V'), ('furiously', 'ADV')]
>>> for key, val in sorted(pos.items()):
	print(key + ":", val)

	
colourless: ADJ
furiously: ADV
ideas: N
sleep: V
>>> pos['sleep']='V'
>>> pos['sleep']
'V'
>>> pos['sleep']='N'
>>> pos['sleep']
'N'
>>> pos['sleep']=['V','N']
>>> pos['sleep']
['V', 'N']
>>> for key, val in sorted(pos.items()):
	print(key + ":", val)

	
colourless: ADJ
furiously: ADV
ideas: N
sleep: ['V', 'N']
>>> pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
>>> pos
{'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
>>> pos = dict(colorless='ADJ', ideas='N', sleep='V', furiously='ADV')
>>> pos
{'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
>>> from collections import defaultdict
>>> frequency = defaultdict(int)
>>> frequency['colourless'] = 4
>>> frequency['ideas']
0
>>> pos = defaultdict(list)
>>> pos['sleep'] = ['NOUN', 'VERB']
>>> pos['ideas']
[]
>>> frequency
defaultdict(<class 'int'>, {'colourless': 4, 'ideas': 0})
>>> pos = defaultdict(lambda: 'NOUN')
>>> pos['colourless'] = 'ADJ'
>>> pos['blog']
'NOUN'
>>> list(pos.items())
[('colourless', 'ADJ'), ('blog', 'NOUN')]
>>> alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
>>> vocab = nltk.FreqDist(alice)
>>> v1000 = [word for (word, _) in vocab.most_common(1000)]
>>> mapping = defaultdict(lamba: 'UNK')
SyntaxError: invalid syntax
>>> mapping = defaultdict(lambda: 'UNK')
>>> for v in v1000:
	mapping[v] = v

	
>>> alice2 = [mapping[v] for v in alice]
>>> alice2[:100]
['[', 'Alice', "'", 's', 'Adventures', 'in', 'Wonderland', 'by', 'UNK', 'UNK', 'UNK', 'UNK', 'CHAPTER', 'I', '.', 'Down', 'the', 'Rabbit', '-', 'UNK', 'Alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'of', 'sitting', 'by', 'her', 'sister', 'on', 'the', 'bank', ',', 'and', 'of', 'having', 'nothing', 'to', 'do', ':', 'once', 'or', 'twice', 'she', 'had', 'peeped', 'into', 'the', 'book', 'her', 'sister', 'was', 'reading', ',', 'but', 'it', 'had', 'no', 'pictures', 'or', 'UNK', 'in', 'it', ',', "'", 'and', 'what', 'is', 'the', 'use', 'of', 'a', 'book', ",'", 'thought', 'Alice', "'", 'without', 'pictures', 'or', 'conversation', "?'", 'So', 'she', 'was', 'considering', 'in', 'her', 'own', 'mind', '(', 'as', 'well', 'as', 'she', 'could', ',']
>>> len(set(alice))
3016
>>> len(set(alice2))
1001
>>> from collections import defaultdict
>>> counts = defaultdict(int)
>>> from nltk.corpus import brown
>>> for (word, tag) in brown.tagged_words(categories= 'news', tagset='universal'):
	counts[tag] += 1

	
>>> 
>>> counts['NOUN']
30654
>>> sorted(counts)
['.', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB', 'X']
>>> from operator import itemgetter
>>> sorted(counts.items(), key=itemgetter(1), reverse=True)
[('NOUN', 30654), ('VERB', 14399), ('ADP', 12355), ('.', 11928), ('DET', 11389), ('ADJ', 6706), ('ADV', 3349), ('CONJ', 2717), ('PRON', 2535), ('PRT', 2264), ('NUM', 2166), ('X', 92)]
>>> [t for t , c in sorted(count.items(), key=itegmetter(1), reverse=True)]
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    [t for t , c in sorted(count.items(), key=itegmetter(1), reverse=True)]
NameError: name 'count' is not defined
>>> [t for t , c in sorted(counts.items(), key=itemgetter(1), reverse=True)]
['NOUN', 'VERB', 'ADP', '.', 'DET', 'ADJ', 'ADV', 'CONJ', 'PRON', 'PRT', 'NUM', 'X']
>>> pair = ('NP', 8336)
>>> pair[1]
8336
>>> itemgetter(1)(pair)
8336
>>> last_letters = defaultdict(list)
>>> words = nltk.corpus.words.words('en')
>>> for word in words:
	key = word[-2:]
	last_letters[key].append(word)

	
>>> last_letters['ly']

>>> last_letters['ly'][:10]
['abactinally', 'abandonedly', 'abasedly', 'abashedly', 'abashlessly', 'abbreviately', 'abdominally', 'abhorrently', 'abidingly', 'abiogenetically']
>>> last_letters['zy'][:10]
['blazy', 'bleezy', 'blowzy', 'boozy', 'breezy', 'bronzy', 'buzzy', 'Chazy', 'cozy', 'crazy']
>>> anagrams = defaultdict(list)
>>> for word in words:
	key = ''.join(sorted(word))
	anagrams[key].append(word)

	
>>> anagrams['aeilnrt']
['entrail', 'latrine', 'ratline', 'reliant', 'retinal', 'trenail']
>>> ['lucky']
['lucky']
>>> anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
>>> ['lucky']
['lucky']
>>> anagrams['aeilnrt']
['entrail', 'latrine', 'ratline', 'reliant', 'retinal', 'trenail']
>>> pos = defaultdict(lambda: defaultdict(int))
>>> brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
>>> for ((w1,t1), (w2,t2)) in nltk.bigrams(brown_news_tagged):
	pos[(t1, w2)][t2] += 1

	
>>> pos[('DET', 'right')]
defaultdict(<class 'int'>, {'NOUN': 5, 'ADJ': 11})
>>> counts = default dict(int)
SyntaxError: invalid syntax
>>> counts = defaultdict(int)
>>> for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
	counts[word] +=1

	
>>> [key for (key, value) in counts.items() if value == 32]
['mortal', 'Against', 'Him', 'There', 'brought', 'King', 'virtue', 'every', 'been', 'thine']
>>> pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
>>> pos2 = dict((value, key) for (key, value) in pos.items())
>>> pos2['N']
'ideas'
>>> pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
>>> pos2 = defaultdict(list)
>>> for key, value in pos.items():
	pos2[value].append(key)

	
>>> pos2['N']
['ideas', 'cats']
>>> pos2 = nltk.INdex((value, key) for key, value in pos.items())
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    pos2 = nltk.INdex((value, key) for key, value in pos.items())
AttributeError: module 'nltk' has no attribute 'INdex'
>>> pos2 = nltk.Index((value, key) for key, value in pos.items())
>>> pos2['N']
['ideas', 'cats']
>>> from nltk.corpus import brown
>>> brown_tagged_sents = brown.tagged_sents(categories='news')
>>> brown_sents = brown.sents(categories=''news)
SyntaxError: invalid syntax
>>> brown_sents = brown.sents(categories='news')
>>> tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
>>> nltk.FreqDist(tags).max()
'NN'
>>> raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
>>> tokens = nltk.word_tokenize(raw)
>>> default_tagger = nltk.DefaultTagger('NN')
>>> default_tagger.tag(tokens)
[('I', 'NN'), ('do', 'NN'), ('not', 'NN'), ('like', 'NN'), ('green', 'NN'), ('eggs', 'NN'), ('and', 'NN'), ('ham', 'NN'), (',', 'NN'), ('I', 'NN'), ('do', 'NN'), ('not', 'NN'), ('like', 'NN'), ('them', 'NN'), ('Sam', 'NN'), ('I', 'NN'), ('am', 'NN'), ('!', 'NN')]
>>> default_tagger.evaluate(brown_tagged_sents)

Warning (from warnings module):
  File "<pyshell#274>", line 1
DeprecationWarning: 
  Function evaluate() has been deprecated.  Use accuracy(gold)
  instead.
0.13089484257215028
>>> patterns = [
	(r'.*ing$', 'VGB'),			#gerunds
	(r'.ed$','VBD'),			#simple past
	(r'.*es$','VBZ'),			#3rd singular present
	(r'.*ould$','MD'),			#modals
	(r'.*\'s','NN$'),			#posessive nouns
	(r'.*s$','NNS'),			#plural nouns
	(r'^-?[0-9]+(\.[0-9]+)?$','CD'),	#cardinal numbers
	(r'.*','NN')				#nounds (default)
	]
>>> 
>>> regexp_tagger = nltk.RegexpTagger(patterns)
>>> regexp_tagger.tag(brown_sents[3])
[('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'NN'), ("''", 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('considering', 'VGB'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('of', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'), ('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')]
>>> regexp_tagger.evaluate(brown_tagged_sents)
0.1741651252063568
>>>  patterns = [
...     (r'.*ing$', 'VBG'),                # gerunds
...     (r'.*ed$', 'VBD'),                 # simple past
...     (r'.*es$', 'VBZ'),                 # 3rd singular present
...     (r'.*ould$', 'MD'),                # modals
...     (r'.*\'s$', 'NN$'),                # possessive nouns
...     (r'.*s$', 'NNS'),                  # plural nouns
...     (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
...     (r'.*', 'NN')                      # nouns (default)
... ]
 
SyntaxError: unexpected indent
>>> patterns = [
...     (r'.*ing$', 'VBG'),                # gerunds
...     (r'.*ed$', 'VBD'),                 # simple past
...     (r'.*es$', 'VBZ'),                 # 3rd singular present
...     (r'.*ould$', 'MD'),                # modals
...     (r'.*\'s$', 'NN$'),                # possessive nouns
...     (r'.*s$', 'NNS'),                  # plural nouns
...     (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
...     (r'.*', 'NN')                      # nouns (default)
... ]
SyntaxError: invalid syntax
>>> patterns = [
	(r'.*ing$', 'VGB'),			#gerunds
	(r'.ed$','VBD'),			#simple past
	(r'.*es$','VBZ'),			#3rd singular present
	(r'.*ould$','MD'),			#modals
	(r'.*\'s','NN$'),			#posessive nouns
	(r'.*s$','NNS'),			#plural nouns
	(r'^-?[0-9]+(\.[0-9]+)?$','CD'),	#cardinal numbers
	(r'.*','NN')				#nounds (default)
]
>>> regexp_tagger.tag(brown_sents[3])
[('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'NN'), ("''", 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('considering', 'VGB'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('of', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'), ('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')]
>>> regexp_tagger.evaluate(brown_tagged_sents)
0.1741651252063568
>>> regexp_tagger = nltk.RegexpTagger(patterns)
>>> regexp_tagger.tag(brown_sents[3])
[('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'NN'), ("''", 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('considering', 'VGB'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('of', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'), ('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')]
>>> regexp_tagger.evaluate(brown_tagged_sents)
0.1741651252063568
>>> patterns = [
	(r'.*ing$', 'VGB'),			#gerunds
	(r'.*ed$','VBD'),			#simple past
	(r'.*es$','VBZ'),			#3rd singular present
	(r'.*ould$','MD'),			#modals
	(r'.*\'s','NN$'),			#posessive nouns
	(r'.*s$','NNS'),			#plural nouns
	(r'^-?[0-9]+(\.[0-9]+)?$','CD'),	#cardinal numbers
	(r'.*','NN')				#nounds (default)
]
>>> regexp_tagger = nltk.RegexpTagger(patterns)
>>> regexp_tagger.tag(brown_sents[3])
[('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'VBD'), ("''", 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('considering', 'VGB'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('of', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'), ('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')]
>>> default_tagger.evaluate(brown_tagged_sents)
0.13089484257215028
>>> fd = nltk.FreqDist(brown.words(categories='news'))
>>> cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
>>> most_freq_words = fd.most_common(100)
>>> likely_tags = dict((word, cfd[word].max()) for (word,_) in most_freq_words)
>>> baseline_tagger = nltk.UnigramTagger(model = likely_tags)
>>> baseline_tagger.evaluate(brown_tagged_sents)
0.45578495136941344
>>> brown.words(categories='news')[:20]
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', 'Friday', 'an', 'investigation', 'of', "Atlanta's", 'recent', 'primary', 'election', 'produced', '``', 'no', 'evidence', "''", 'that']
>>> tokens[:20]
['I', 'do', 'not', 'like', 'green', 'eggs', 'and', 'ham', ',', 'I', 'do', 'not', 'like', 'them', 'Sam', 'I', 'am', '!']
>>> sent = brown.sents(categories='news'[3])
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    sent = brown.sents(categories='news'[3])
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\reader\api.py", line 409, in sents
    return super().sents(self._resolve(fileids, categories))
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\reader\api.py", line 398, in _resolve
    return self.fileids(categories)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\corpus\reader\api.py", line 388, in fileids
    raise ValueError("Category %s not found" % categories)
ValueError: Category s not found
>>> sent = brown.sents(categories='news')[3]
>>> baseline_tagger.tag(sent)
[('``', '``'), ('Only', None), ('a', 'AT'), ('relative', None), ('handful', None), ('of', 'IN'), ('such', None), ('reports', None), ('was', 'BEDZ'), ('received', None), ("''", "''"), (',', ','), ('the', 'AT'), ('jury', None), ('said', 'VBD'), (',', ','), ('``', '``'), ('considering', None), ('the', 'AT'), ('widespread', None), ('interest', None), ('in', 'IN'), ('the', 'AT'), ('election', None), (',', ','), ('the', 'AT'), ('number', None), ('of', 'IN'), ('voters', None), ('and', 'CC'), ('the', 'AT'), ('size', None), ('of', 'IN'), ('this', 'DT'), ('city', None), ("''", "''"), ('.', '.')]
>>> baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
>>> baseline_tagger.tag(sent)
[('``', '``'), ('Only', 'NN'), ('a', 'AT'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'IN'), ('such', 'NN'), ('reports', 'NN'), ('was', 'BEDZ'), ('received', 'NN'), ("''", "''"), (',', ','), ('the', 'AT'), ('jury', 'NN'), ('said', 'VBD'), (',', ','), ('``', '``'), ('considering', 'NN'), ('the', 'AT'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'IN'), ('the', 'AT'), ('election', 'NN'), (',', ','), ('the', 'AT'), ('number', 'NN'), ('of', 'IN'), ('voters', 'NN'), ('and', 'CC'), ('the', 'AT'), ('size', 'NN'), ('of', 'IN'), ('this', 'DT'), ('city', 'NN'), ("''", "''"), ('.', '.')]
>>> brown.tagged_sents(categories='news')[0]
[('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ('Grand', 'JJ-TL'), ('Jury', 'NN-TL'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'), ('investigation', 'NN'), ('of', 'IN'), ("Atlanta's", 'NP$'), ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('produced', 'VBD'), ('``', '``'), ('no', 'AT'), ('evidence', 'NN'), ("''", "''"), ('that', 'CS'), ('any', 'DTI'), ('irregularities', 'NNS'), ('took', 'VBD'), ('place', 'NN'), ('.', '.')]
>>> palabras_crudo[:30]
'TENET\nWritten by\nChristopher N'
>>> tokens_sents = sents_tokenize(palabras_crudo)
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    tokens_sents = sents_tokenize(palabras_crudo)
NameError: name 'sents_tokenize' is not defined
>>> tokens_sents = sent_tokenize(palabras_crudo)
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    tokens_sents = sent_tokenize(palabras_crudo)
NameError: name 'sent_tokenize' is not defined
>>> sents = nltk.sent_tokenize(palabras_crudo)
>>> def performance(cfd, wordlist):
	lt = dict((word, cfd[word].max()) for word in wordlist)
	baseline_tagger = nltk.UnigramTAgger(model=lt, backoff=nltk.DefaultTagger('NN'))
	return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

>>> def display():
	import pylab
	word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
	words_by_freq = [w for (w, _) in word_freqs]
	cfd = nltk-ConditionalFreqDist(brown.tagged_words(categories='news'))
	sizes = 2 ** pylab.arrange(15)
	perfs = [performance(cfd, words_by_freq[size]) for size in sizes]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Lookup Tagger Performance With Varying Model Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()

	
>>> display()
Traceback (most recent call last):
  File "<pyshell#337>", line 1, in <module>
    display()
  File "<pyshell#336>", line 5, in display
    cfd = nltk-ConditionalFreqDist(brown.tagged_words(categories='news'))
NameError: name 'ConditionalFreqDist' is not defined
>>> def display():
	import pylab
	word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
	words_by_freq = [w for (w, _) in word_freqs]
	cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
	sizes = 2 ** pylab.arrange(15)
	perfs = [performance(cfd, words_by_freq[size]) for size in sizes]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Lookup Tagger Performance With Varying Model Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()

	
>>> display()
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    display()
  File "<pyshell#339>", line 6, in display
    sizes = 2 ** pylab.arrange(15)
AttributeError: module 'pylab' has no attribute 'arrange'
>>> def display():
	import pylab
	word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
	words_by_freq = [w for (w, _) in word_freqs]
	cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
	sizes = 2 ** pylab.arange(15)
	perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Lookup Tagger Performance With Varying Model Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()

	
>>> display()
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    display()
  File "<pyshell#342>", line 7, in display
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
  File "<pyshell#342>", line 7, in <listcomp>
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
  File "<pyshell#323>", line 3, in performance
    baseline_tagger = nltk.UnigramTAgger(model=lt, backoff=nltk.DefaultTagger('NN'))
AttributeError: module 'nltk' has no attribute 'UnigramTAgger'
>>> def performance(cfd, wordlist):
	lt = dict((word, cfd[word].max()) for word in wordlist)
	baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
	return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

>>> def display():
	import pylab
	word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
	words_by_freq = [w for (w, _) in word_freqs]
	cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
	sizes = 2 ** pylab.arange(15)
	perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Lookup Tagger Performance With Varying Model Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()

	
>>> display()

Warning (from warnings module):
  File "<pyshell#345>", line 4
DeprecationWarning: 
  Function evaluate() has been deprecated.  Use accuracy(gold)
  instead.
>>> from nltk.corpus import brown
>>> brown_tagged_sents = brown.tagged_sents(categories='news')
>>> brown_sents = brown.sents(categories='news')
>>> unigram_tagger = nltk.UnigramTAgger(brown_tagged_sents)
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    unigram_tagger = nltk.UnigramTAgger(brown_tagged_sents)
AttributeError: module 'nltk' has no attribute 'UnigramTAgger'
>>> unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
>>> unigram_tagger.tag(brown_sents[2007])
[('Various', 'JJ'), ('of', 'IN'), ('the', 'AT'), ('apartments', 'NNS'), ('are', 'BER'), ('of', 'IN'), ('the', 'AT'), ('terrace', 'NN'), ('type', 'NN'), (',', ','), ('being', 'BEG'), ('on', 'IN'), ('the', 'AT'), ('ground', 'NN'), ('floor', 'NN'), ('so', 'QL'), ('that', 'CS'), ('entrance', 'NN'), ('is', 'BEZ'), ('direct', 'JJ'), ('.', '.')]
>>> unigram_tagger.evaluate(brown_tagged_sents)

Warning (from warnings module):
  File "<pyshell#355>", line 1
DeprecationWarning: 
  Function evaluate() has been deprecated.  Use accuracy(gold)
  instead.
0.9349006503968017
>>> size = int(len(brown_tagged_sents) * 0.9)
>>> size
4160
>>> train_sents = brown_tagged_sent[:size]
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    train_sents = brown_tagged_sent[:size]
NameError: name 'brown_tagged_sent' is not defined
>>> train_sents = brown_tagged_sents[:size]
>>> train_sents = brown_tagged_sents[size:]
>>> unigram_tagger = nltk.UnigramTagger(train_sents)
>>> unigram_tagger.evaluate(test_sents)
Traceback (most recent call last):
  File "<pyshell#362>", line 1, in <module>
    unigram_tagger.evaluate(test_sents)
NameError: name 'test_sents' is not defined
>>> train_sents = brown_tagged_sents[:size]
>>> test_sents = brown_tagged_sents[size:]
>>> unigram_tagger = nltk.UnigramTagger(train_sents)
unigram_tagger = nltk.UnigramTagger(train_sents)
>>> unigram_tagger.evaluate(test_sents)
0.8121200039868434
>>> bigram_tagger = nltk.BIgramTAgger(train_sents)
Traceback (most recent call last):
  File "<pyshell#367>", line 1, in <module>
    bigram_tagger = nltk.BIgramTAgger(train_sents)
AttributeError: module 'nltk' has no attribute 'BIgramTAgger'
>>> bigram_tagger = nltk.BigramTagger(train_sents)
>>> bigram_tagger.tag(brown_sents[2007])
[('Various', 'JJ'), ('of', 'IN'), ('the', 'AT'), ('apartments', 'NNS'), ('are', 'BER'), ('of', 'IN'), ('the', 'AT'), ('terrace', 'NN'), ('type', 'NN'), (',', ','), ('being', 'BEG'), ('on', 'IN'), ('the', 'AT'), ('ground', 'NN'), ('floor', 'NN'), ('so', 'CS'), ('that', 'CS'), ('entrance', 'NN'), ('is', 'BEZ'), ('direct', 'JJ'), ('.', '.')]
>>> unseen_sent = brown_sents[4203]
>>> bigram_tagger.tag(unseen_sent)
[('The', 'AT'), ('population', 'NN'), ('of', 'IN'), ('the', 'AT'), ('Congo', 'NP'), ('is', 'BEZ'), ('13.5', None), ('million', None), (',', None), ('divided', None), ('into', None), ('at', None), ('least', None), ('seven', None), ('major', None), ('``', None), ('culture', None), ('clusters', None), ("''", None), ('and', None), ('innumerable', None), ('tribes', None), ('speaking', None), ('400', None), ('separate', None), ('dialects', None), ('.', None)]
>>> bigram_tagger.evaluate(test_sents)
0.10206319146815508
>>> t0 = nltk.DefaultTagger('NN')
>>> t1 = nltk.UnigramTagger(train_sents, backoff = t0)
>>> t2 = nltk.BigramTagger(train_sents, backoff = t1)
>>> t2.evaluate(test_sents)
0.8452108043456593
>>> t3 = nltk.TrigramTagger(train_sents, backoff = t2)
>>> t3.evaluate(test_sents)
0.843317053722715
>>> for t in [t0, t1, t2, t3]:
	t.evaluate(test_sents)

	

Warning (from warnings module):
  File "<pyshell#381>", line 2
DeprecationWarning: 
  Function evaluate() has been deprecated.  Use accuracy(gold)
  instead.
0.1262832652247583
0.8361407355726104
0.8452108043456593
0.843317053722715
>>> from pickle import dump
>>> output = open('t2.pkl', 'wb')
>>> dump(t2, output, -1)
>>> output.close
<built-in method close of _io.BufferedWriter object at 0x00000237F2CDFCA0>
>>> output.close()
>>> from pickle import load
>>> input = open('t2.pkl', 'rb')
>>> tagger = load(input)
>>> input.close()
>>> text = """The board's action shows what free enterprise is up against in our complex maze of regulatory laws ."""
>>> tokens = text.split()
>>> tagger.tag(tokens)
[('The', 'AT'), ("board's", 'NN$'), ('action', 'NN'), ('shows', 'NNS'), ('what', 'WDT'), ('free', 'JJ'), ('enterprise', 'NN'), ('is', 'BEZ'), ('up', 'RP'), ('against', 'IN'), ('in', 'IN'), ('our', 'PP$'), ('complex', 'JJ'), ('maze', 'NN'), ('of', 'IN'), ('regulatory', 'NN'), ('laws', 'NNS'), ('.', '.')]
>>> cfd = nltk.COnditionalFreqDist(
	((x[1],y[1], z[0]), z[1])
	for sent in brown_tagged_sent
	for x, y, z in nltk.trigrams(sent))
Traceback (most recent call last):
  File "<pyshell#397>", line 1, in <module>
    cfd = nltk.COnditionalFreqDist(
AttributeError: module 'nltk' has no attribute 'COnditionalFreqDist'
>>> cfd = nltk.ConditionalFreqDist(
	((x[1],y[1], z[0]), z[1])
	for sent in brown_tagged_sent
	for x, y, z in nltk.trigrams(sent))
Traceback (most recent call last):
  File "<pyshell#398>", line 3, in <module>
    for sent in brown_tagged_sent
NameError: name 'brown_tagged_sent' is not defined
>>> cfd = nltk.ConditionalFreqDist(
	((x[1],y[1], z[0]), z[1])
	for sent in brown_tagged_sents
	for x, y, z in nltk.trigrams(sent))

8
>>> cfd = nltk.ConditionalFreqDist(
	((x[1],y[1], z[0]), z[1])
	for sent in brown_tagged_sents
	for x, y, z in nltk.trigrams(sent))

>>> ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
>>> sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()
0.049297702068029296
>>> ambiguous_contexts[:20]
[('NN', "''", 'that'), ('NN', 'NNS', 'that'), ('AT', 'NN-TL', 'of'), ('NP', 'NP', 'to'), ('NN', 'IN', 'such'), ('NN', 'VBD', 'it'), ('VB', '``', 'to'), ('CC', 'VBN', 'to'), ('NN', 'VBD', 'on'), ('WDT', 'VB', 'to'), ('BE', 'VBN', 'to'), ('JJ', 'NNS', 'as'), ('VB', 'NNS', 'to'), ('JJ', 'NN', 'so'), ('NN', 'CS', 'that'), ('IN', 'AT', 'Fulton'), ('VBN', 'JJ', 'to'), ('NNS', 'IN', 'all'), ('AT', 'NNS', 'in'), ('PPSS', 'VB', 'that')]
>>> test_tags = [tag for sent in brown.sents(categories = 'editorial')]
>>> test_tags = [tag for sent in brown.sents(categories = 'editorial') for (word, tag) in t2.tag(sent)]
>>> gold_tags = [tag for (word, tag) in brown-tagged_words(categories='editorial')]
Traceback (most recent call last):
  File "<pyshell#406>", line 1, in <module>
    gold_tags = [tag for (word, tag) in brown-tagged_words(categories='editorial')]
NameError: name 'tagged_words' is not defined
>>> gold_tags = [tag for (word, tag) in brown_tagged_words(categories='editorial')]
Traceback (most recent call last):
  File "<pyshell#407>", line 1, in <module>
    gold_tags = [tag for (word, tag) in brown_tagged_words(categories='editorial')]
NameError: name 'brown_tagged_words' is not defined
>>> gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
>>> print(nltk.ConfusionMatrix(gold_tags, test_tags))

>>> print(nltk.ConfusionMatrix(gold_tags, test_tags)[:10])
Traceback (most recent call last):
  File "<pyshell#410>", line 1, in <module>
    print(nltk.ConfusionMatrix(gold_tags, test_tags)[:10])
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\metrics\confusionmatrix.py", line 89, in __getitem__
    (li, lj) = li_lj_tuple
TypeError: cannot unpack non-iterable slice object
>>> from nltk.tbl import demo as brill_demo
>>> brill_demo.demo()
Loading tagged data from treebank... 
Read testing data (200 sents/5251 wds)
Read training data (800 sents/19933 wds)
Read baseline data (800 sents/19933 wds) [reused the training set]
Trained baseline tagger
    Accuracy on test set: 0.8358
Training tbl tagger...
TBL train (fast) (seqs: 800; tokens: 19933; tpls: 24; min score: 3; min acc: None)
Finding initial useful rules...
    Found 12799 useful rules.

           B      |
   S   F   r   O  |        Score = Fixed - Broken
   c   i   o   t  |  R     Fixed = num tags changed incorrect -> correct
   o   x   k   h  |  u     Broken = num tags changed correct -> incorrect
   r   e   e   e  |  l     Other = num tags changed incorrect -> incorrect
   e   d   n   r  |  e
------------------+-------------------------------------------------------
  23  23   0   0  | POS->VBZ if Pos:PRP@[-2,-1]
  18  19   1   0  | NN->VB if Pos:-NONE-@[-2] & Pos:TO@[-1]
  14  14   0   0  | VBP->VB if Pos:MD@[-2,-1]
  12  12   0   0  | VBP->VB if Pos:TO@[-1]
  11  11   0   0  | VBD->VBN if Pos:VBD@[-1]
  11  11   0   0  | IN->WDT if Pos:-NONE-@[1] & Pos:VBP@[2]
  10  11   1   0  | VBN->VBD if Pos:PRP@[-1]
   9  10   1   0  | VBD->VBN if Pos:VBZ@[-1]
   8   8   0   0  | NN->VB if Pos:MD@[-1]
   7   7   0   1  | VB->NN if Pos:DT@[-1]
   7   7   0   0  | VB->VBP if Pos:PRP@[-1]
   7   7   0   0  | IN->WDT if Pos:-NONE-@[1] & Pos:VBZ@[2]
   7   8   1   0  | IN->RB if Word:as@[2]
   6   6   0   0  | VBD->VBN if Pos:VBP@[-2,-1]
   6   6   0   1  | IN->WDT if Pos:-NONE-@[1] & Pos:VBD@[2]
   5   5   0   0  | POS->VBZ if Pos:-NONE-@[-1]
   5   5   0   0  | VB->VBP if Pos:NNS@[-1]
   5   5   0   0  | VBD->VBN if Word:be@[-2,-1]
   4   4   0   0  | POS->VBZ if Pos:``@[-2]
   4   4   0   0  | VBP->VB if Pos:VBD@[-2,-1]
   4   6   2   3  | RP->RB if Pos:CD@[1,2]
   4   4   0   0  | RB->JJ if Pos:DT@[-1] & Pos:NN@[1]
   4   4   0   0  | NN->VBP if Pos:NNS@[-2] & Pos:RB@[-1]
   4   5   1   0  | VBN->VBD if Pos:NNP@[-2] & Pos:NNP@[-1]
   4   4   0   0  | IN->WDT if Pos:-NONE-@[1] & Pos:MD@[2]
   4   8   4   0  | VBD->VBN if Word:*@[1]
   4   4   0   0  | JJS->RBS if Word:most@[0] & Word:the@[-1] & Pos:DT@[-1]
   3   3   0   0  | VBD->VBN if Pos:VBN@[-1]
   3   4   1   0  | VBN->VB if Pos:TO@[-1]
   3   4   1   1  | IN->RB if Pos:.@[1]
   3   3   0   0  | JJ->RB if Pos:VBD@[1]
   3   3   0   0  | PRP$->PRP if Pos:TO@[1]
   3   3   0   0  | NN->VBP if Pos:NNS@[-1] & Pos:DT@[1]
   3   3   0   0  | VBP->VB if Word:n't@[-2,-1]
Trained tbl tagger in 4.89 seconds
    Accuracy on test set: 0.8564
Tagging the test data
>>> print(open('errors.out').read())
Traceback (most recent call last):
  File "<pyshell#413>", line 1, in <module>
    print(open('errors.out').read())
FileNotFoundError: [Errno 2] No such file or directory: 'errors.out'
>>> print(open("errors.out").read())
Traceback (most recent call last):
  File "<pyshell#414>", line 1, in <module>
    print(open("errors.out").read())
FileNotFoundError: [Errno 2] No such file or directory: 'errors.out'
>>> 