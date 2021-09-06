"""We need our tokenizer to split a sentence not just on whitespace, but also on punctuation such as commas, periods, quotes, semicolons, and even hyphens.
In some cases we want these punctuation marks to be treated like words, as independent token.
Now we'd use regular expressions."""

import re
sentence = """Thomas Jefferson began building Monticello at the age of 26."""
tokens = re.split(r'[\s]+', sentence)
# ['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']

"""When it findes a match, it breaks the string right before that matched character and right after it, skipping over the matched character or charachters."""

pattern = re.compile(r'([\s])+')
tokens = pattern.split(sentence)
# [' ', 'at', ' ', 'the', ' ', 'age', ' ', 'of', ' ', '26.']

"""complie our regular expression so that our tokenizer will run faster.
This simple regular expresiion is helping to split off the period from the end of the token "26.".
However, we need to filter the whitespace and punctuation characters you don't want to include in your vocabulary"""

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
pattern = re.compile(r'([\s])+')
tokens = pattern.split(sentence)
[x for x in tokens if x and x not in '- \t\n.,;!?']

#['Thomas','Jefferson','began','building','Monticello','at','the', 'age', 'of', '26']

""" 

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+$[0-9.]+|\S+')
tokenizer.tokenize(sentence)
# ['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']

import nltk
nltk.download("book", quiet=True)
from nltk.book import *
# *** Introductory Examples for the NLTK Book ***
# Loading text1, ..., text9 and sent1, ..., sent9
# Type the name of the text or sentence to view it.
# Type: 'texts()' or 'sents()' to list the materials.
# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908

print(nltk.corpus.gutenberg.fileids())

# ['austen-emma.txt',
#  'austen-persuasion.txt',
#  'austen-sense.txt',
#  'bible-kjv.txt',
#  'blake-poems.txt',
#  'bryant-stories.txt',
#  'burgess-busterbrown.txt',
#  'carroll-alice.txt',
#  'chesterton-ball.txt',
#  'chesterton-brown.txt',
#  'chesterton-thursday.txt',
#  'edgeworth-parents.txt',
#  'melville-moby_dick.txt',
#  'milton-paradise.txt',
#  'shakespeare-caesar.txt',
#  'shakespeare-hamlet.txt',
#  'shakespeare-macbeth.txt',
#  'whitman-leaves.txt']

emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
print(emma_raw[:1302])

# [Emma by Jane Austen 1816]
#
# VOLUME I
#
# CHAPTER I
#
#
# Emma Woodhouse, handsome, clever, and rich, with a comfortable home
# and happy disposition, seemed to unite some of the best blessings
# of existence; and had lived nearly twenty-one years in the world
# with very little to distress or vex her.
#
# She was the youngest of the two daughters of a most affectionate,
# indulgent father; and had, in consequence of her sister's marriage,
# been mistress of his house from a very early period.  Her mother
# had died too long ago for her to have more than an indistinct
# remembrance of her caresses; and her place had been supplied
# by an excellent woman as governess, who had fallen little short
# of a mother in affection.
#
# Sixteen years had Miss Taylor been in Mr. Woodhouse's family,
# less as a governess than a friend, very fond of both daughters,
# but particularly of Emma.  Between _them_ it was more the intimacy
# of sisters.  Even before Miss Taylor had ceased to hold the nominal
# office of governess, the mildness of her temper had hardly allowed
# her to impose any restraint; and the shadow of authority being
# now long passed away, they had been living together as friend and
# friend very mutually attached, and Emma doing just what she liked;
# highly esteeming Miss Taylor's judgment, but directed chiefly by
# her own.

from nltk.tokenize import sent_tokenize
print("1> \n", sent_tokenize(emma_raw[:1000])[0])

# [Emma by Jane Austen 1816]
#
# VOLUME I
#
# CHAPTER I
#
#
# Emma Woodhouse, handsome, clever, and rich, with a comfortable home
# and happy disposition, seemed to unite some of the best blessings
# of existence; and had lived nearly twenty-one years in the world
# with very little to distress or vex her.

from nltk.tokenize import word_tokenize
word_tokenize(emma_raw[:100])

# ['[',
#  'Emma',
#  'by',
#  'Jane',
#  'Austen',
#  '1816',
#  ']',
#  'VOLUME',
#  'I',
#  'CHAPTER',
#  'I',
#  'Emma',
#  'Woodhouse',
#  ',',
#  'handsome',
#  ',',
#  'clever',
#  ',',
#  'and',
#  'rich',
#  ',',
#  'with',
#  'a']

from nltk.tokenize import RegexpTokenizer
retokenize = RegexpTokenizer("[\w]+")
retokenize.tokenize(emma_raw[:100])

# ['Emma',
#  'by',
#  'Jane',
#  'Austen',
#  '1816',
#  'VOLUME',
#  'I',
#  'CHAPTER',
#  'I',
#  'Emma',
#  'Woodhouse',
#  'handsome',
#  'clever',
#  'and',
#  'rich',
#  'with',
#  'a']