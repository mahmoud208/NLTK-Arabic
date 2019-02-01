# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------

import nltk

from nltk.tokenize import  sent_tokenize, word_tokenize

example_text=unicode("كتب الولد الدرس","utf-8")
s=(word_tokenize(example_text))
#s=s.decode('unicode-escape')
for ss in s:
    print ss
