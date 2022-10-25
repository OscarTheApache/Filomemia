pipimport nltk, re, pprint
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from collections import defaultdict

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def find_chunks(grammar, text):
    cp = nltk.RegexpParser(grammar)
    for sent in text.tagged_sents():
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'CHUNK': print(subtree)

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos),chunktag)
                     in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

class ConsecutiveNPChunkTagger(nltk.TaggerI):

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(
            train_set, algorithm='megam', trace=0)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)

def npchunk_features(sentence, i, history):
    word,pos =sentence[i]
    return {'pos':pos}

grammar1 = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """
grammar2 = nltk.CFG.fromstring('''
                               S -> NP VP
                               VP -> V NP | V NP PP 
                               PP -> P NP
                               V -> 'saw' | 'ate' | 'walked'
                               NP -> 'John' | 'Mary' |'Bob' | Det N | Det N PP
                               Det -> 'a' | 'an' | 'the' | 'my'
                               N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
                               P -> 'in' | 'on' | 'by' | 'with'
                               ''')

grammar3 = nltk.PCFG.fromstring("""
    S    -> NP VP              [1.0]
    VP   -> TV NP [0.4] | IV [0.3] | DatV NP NP [0.3]
    TV   -> 'saw'              [1.0]
    IV   -> 'ate'              [1.0]
    DatV -> 'gave'             [1.0]
    NP   -> 'telescopes' [0.8] | 'Jack' [0.2]
    """)


cp = nltk.RegexpParser(grammar)
#cp.parse(text)

# pdp = nltk.ProjectiveDependencyParser(grammar)
# sent = 'I shot an elephant in my pajamas'.split()
# trees = pdp.parse(sent)
# for tree in trees:
#     print(tree)

def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    wfst = [[None for i in range(numtokens+1)] for j in range(numtokens+1)]
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        wfst[i][i+1] = productions[0].lhs()
    return wfst

def complete_wfst(wfst, tokens, grammar, trace=False):
    index =dict((p.rhs(), p.lhs()) for p in grammar.productions())
    numtokens = len(tokens)
    for span in range(2, numtokens+1):
        for start in range(numtokens+1-span):
            end = start + span
            for mid in range(start+1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1, nt2) in index:
                    wfst[start][end] = index[(nt1,nt2)]
                    if trace:
                        print("[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" % \
                              (start, nt1, mid, nt2, end, start, index[(nt1, nt2)], end))
    return  wfst

def display(wfst, tokens):
    print('\nWFST ' + ' '.join(('%-4d' % i) for i in range(1, len(wfst))))
    for i in range(len(wfst)-1):
        print('%d  ' % i, end=' ')
        for j in range(1, len(wfst)):
            print('%-4s' % (wfst[i][j] or '.'), end=' ')
        print()

tokens = []
wfst0 = init_wfst(tokens, grammar1)

print(nltk.FeatStruct("[A='a', B=(1)[C='c'], D->(1), E->(1)]"))
fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
fs2 = nltk.FeatStruct(CITY='Paris')
print(fs1.unify(fs2))

tokens = 'ich folge den Katzen'.split()
cp = load_parser('grammars/book_grammars/german.fcfg')
for tree in cp.parse(tokens):
    print(tree)


def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=' ')
    else:
        #Now we know that t.node is defined
        print('(', t.label(), end=' ')
        for child in t:
            traverse(child)
        print(')', end=' ')





direccion_corpus = 'C:/Users/chej_/Documents/Filomemia/corpus'
archivos_corpus = PlaintextCorpusReader(direccion_corpus, '.*')
print(archivos_corpus.fileids())


print('Done')

from nltk import load_parser
parser = load_parser('grammars/book_grammars/simple-sem.fcfg', trace=0)
sentence = 'Angus gives a bone to every dog'
tokens = sentence.split()
for tree in parser.parse(tokens):
    print(tree.label()['SEM'])






