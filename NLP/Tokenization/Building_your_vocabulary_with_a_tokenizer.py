import numpy as np
import pandas as pd

sentence = """Thomas Jefferson began building Monticello at the age of 26."""
sentence.split()
# ['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']
str
# ['Thomas', 'Jefferson', 'began', 'building', 'Monticello', 'at', 'the', 'age', 'of', '26.']

""" this built-in Python method(split()) already does a decent job tokenizing a simple sentence.
Its only "mistake" was on the last word, where it includedthe sentence-ending punctuation with the the token "26."""

token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
# ['26.', 'Jefferson', 'Monticello', 'Thomas', 'age', 'at', 'began', 'building', 'of', 'the']
', '.join(vocab)
# 26., Jefferson, Monticello, Thomas, age, at, began, building, of, the

num_token = len(token_sequence) #10
vocab_size = len(vocab) #10
onehot_vectors = np.zeros((num_token, vocab_size)) #10X10

""" You can create a numerical vector representation for each word. These vectors are called one-hot vectors.
A sequence of these one-hot vectors fully captures the original document text in a sequence of vectors, a table of numbers.
That will solve the first problem of NLP, turning words into numbers."""

for i, word in enumerate(token_sequence) :
  onehot_vectors[i , vocab.index(word)] = 1

# [[0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

"""For each word in the sentence, mark the column for that word in your vocabulary with a '1'"""

df = pd.DataFrame(pd.Series(dict([(token,1) for token in sentence.split()])), columns=['sent']).T

#    26.  Jefferson  Monticello  Thomas  age  at  began  building  of  the
# 0    1          1           1       1    1   1      1         1   1    1

"""Pandas DataFrames can help make this a little easier on the eyes and more informative."""
