import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
example_sentence=unicode("??? ????? ????? ???? ??? ?? ? ???????","utf-8")
s=pos_tag(word_tokenize("he are you"))

print s


