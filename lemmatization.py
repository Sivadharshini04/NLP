import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#download necessary datasets
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

#initialize lemmatizer
lemmatizer = WordNetLemmatizer()

#function to get POS tag for lemmatization
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)  # Default to NOUN if tag not found

#example text
text = "running jumps easily better"

#tokenize and lemmatize
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in text.split()]
print("Lemmatized:", lemmatized_words)
