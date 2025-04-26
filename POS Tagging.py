import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from tabulate import tabulate

#downloading required NLTK resources
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


text = "John is running quickly to catch the train at the station."

#tokenize
words = word_tokenize(text)

#pos tagging
pos_tags = pos_tag(words)

table = tabulate(pos_tags, headers=["Word", "POS Tag"], tablefmt="grid")
print(table)
