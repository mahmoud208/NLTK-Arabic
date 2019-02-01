# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------

import codecs
import nltk
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG

grammar = nltk.CFG.fromstring(unicode("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'انا'
VP -> V NP | VP PP
Det -> 'ال' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""",'utf-8'))
sent = [unicode('انا','utf-8'), 'shot', 'an', 'elephant','in', 'my', 'pajamas']
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent):
     print(tree)
#nltk.corpus.sinica_treebank.parsed_sents()[1.0].draw()

for sent in generate(grammar,n=1):
    ss= (' '.join(sent))
    print ss


