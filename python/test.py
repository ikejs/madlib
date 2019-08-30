import nltk
# nltk.download('wordnet')
# ^ Remove hash on first run to download!
from nltk.corpus import wordnet as wn
words = ['amazing', 'hairy', str(24), 'great', 'nice', 'apples']

i = 0

while i < len(words):
    tmp = wn.synsets(words[i]).pos()
    print w, ":", tmp
    i += 1
