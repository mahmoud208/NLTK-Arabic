# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps= PorterStemmer()

example_words=[unicode("قالت","utf-8"),unicode("قالوا","utf-8"),unicode("قالتا","utf-8")]

for w in example_words:
    print(ps.stem(w))