
from nltk.chunk.regexp import tag_pattern2re_pattern


print("Chunk Pattern : ", tag_pattern2re_pattern('<DT>?<NN.*>+'))

!pip install svgling

from nltk.chunk import RegexpParser


chunker = RegexpParser(r'''
NP:
{<DT><NN.*><.*>*<NN.*>}
}<VB.*>{
''')

chunker.parse([('the', 'DT'), ('book', 'NN'), (
    'has', 'VBZ'), ('many', 'JJ'), ('chapters', 'NNS')])
