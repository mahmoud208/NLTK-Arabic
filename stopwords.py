# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
example_sentence=unicode("كتب الولد الدرس الذى كان هو ف المدرسة","utf-8")
stopwords=set(stopwords.words("arabic"))

words=wordpunct_tokenize(example_sentence)

filtered_sentence=[]

for i in words:
    if i not in stopwords:
       print i
