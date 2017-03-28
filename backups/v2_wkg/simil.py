import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

#
# print (cosine_sim('a little bird', 'a little bird'))
# print (cosine_sim('a little bird', 'a little bird chirps'))
# print (cosine_sim('a little bird', 'a big dog barks'))
#
# a = [3166, 'Similarly, Geney Gewog has potential for sustainable harvesting women of masutake and other mushrooms.']
# b = [4, '1.4 By 2030, ensure sustainable harvesting that all men and women, in particular the poor and the vulnerable, have equal rights to economic resources, as well as access to basic services, ownership and control over land and other forms of property, inheritance, natural resources, appropriate new technology and financial services, including microfinance']
# print (cosine_sim(a[1], b[1]))
