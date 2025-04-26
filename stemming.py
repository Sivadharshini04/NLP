import nltk
from nltk.stem import PorterStemmer, LancasterStemmer

#stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()

words = ["running", "jumps", "easily", "better", "studies", "fishing", "happily"]

# apply stemming
porter_stems = [porter.stem(word) for word in words]
lancaster_stems = [lancaster.stem(word) for word in words]

print("Original Words:   ", words)
print("Porter Stemmer:   ", porter_stems)
print("Lancaster Stemmer:", lancaster_stems)
