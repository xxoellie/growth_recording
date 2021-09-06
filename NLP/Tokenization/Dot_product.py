import pandas as pd

sentences = """Thomas Jefferson began building Monticello at the age of 26.\n"""
sentences += """Construction was done mostly by local masons and carpenters.\n"""
sentences += "He moved into the South Pavilion in 1770.\n"
sentences += """Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."""

sentences.split('\n')
corpus = {}

for i, sent in enumerate(sentences.split('\n')) :
  corpus['sent{}'.format(i)] = dict((tok,1) for tok in sent.split())

df = pd.DataFrame(corpus).fillna(0).astype(int).T
df.iloc[:,:10]

#        Thomas  Jefferson  began  ...  masterpiece  Jefferson's  obsession.
# sent0       1          1      1  ...            0            0           0
# sent1       0          0      0  ...            0            0           0
# sent2       0          0      0  ...            0            0           0
# sent3       0          0      0  ...            1            1           1

"""We need to be able to compute this overlap within your pipeline whenever you want to compare documents or search for similar documents. 
One way to check for the similarities between sentences is to count the number of overlapping tokens using a dot product."""
df1 = df.T

df1.sent0.dot(df1.sent1))  #0
df1.sent0.dot(df1.sent2))  #1
df1.sent0.dot(df1.sent3))  #1

"""If we can measure the bag of words overlap for two vectors, we can get a good estimate of how similar they are in the words they use.      
And this is a good estimate of how similar they are in meaning"""

[(k,v) for (k,v) in (df1.sent0 & df1.sent3).items() if v]  #[('Monticello', 1)]

""" This overlap of words is a measure of the similarity. """
