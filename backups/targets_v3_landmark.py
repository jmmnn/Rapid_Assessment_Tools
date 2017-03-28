#sample class
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import pandas as pd

#helper functions to get synonyms
englishStopWords = set(stopwords.words('english'))

def getSynonyms (term):
    synsetList = wn.synsets(term)
    allSynonyms = []
    for i in range (len(synsetList) - 1):
        synomyms = synsetList[i].lemma_names()
        allSynonyms = allSynonyms + synomyms
    return list(set(allSynonyms))

def getAllSynonyms (lists):
    synonyms = []
    for sublist in lists:
        for synonym in sublist:
            if synonym not in synonyms:
                synonyms.append(synonym)
    return synonyms

#this is the main class to manipulate targets
class Target:
    def __init__(self, targetNumber, targetText):
        self.targetNumber = targetNumber
        self.targetText = targetText
        self.tokens = nltk.word_tokenize(self.targetText)
        self.tokensNoStopWords = [token for token in self.tokens if token not in englishStopWords]
        self.lemmas = [nltk.WordNetLemmatizer().lemmatize(token) for token in self.tokens]
        self.bigrams = [item for item in nltk.bigrams(self.tokens)]
        self.trigrams = [item for item in nltk.trigrams(self.tokens)]
        self.synonymsLists = list(map(getSynonyms , self.tokens)) #intermediary step, remove eventually
        self.synonyms = getAllSynonyms(self.synonymsLists)

    def display(self):      #
        allValues = [self.targetNumber, self.targetText , self.tokens , self.lemmas, self.bigrams , self.trigrams, self.synonyms]
        print(allValues)

    def displayTarget(self):      #
        allValues = [self.targetNumber, self.targetText]
        print(allValues)

#########Targets class definition
## Helper class
def analyzeTargets (dataframe):
    """This function is used to process a dataframe with a lists of targets. The Targets will be analyzed and stored
    in a database or file for future use.
    """
    targets = {}
    for i in range(len(dataframe)):
        a = dataframe.iloc[i]['targetNumber']
        b = dataframe.iloc[i]['targetText']
        targets[a] = Target(a,b)
    return targets

class Targets:
    def __init__(self, csvfile):
        self.mydata = pd.read_csv(csvfile, encoding = "ISO-8859-1") #csv to dataframe
        self.targets = analyzeTargets(self.mydata)

    def printTargetList(self):
        return [self.targets[i].displayTarget() for i in self.targets]

class Comparer:
    def __init__ (self, nameItem1, elementIdItem1, nameItem2, elementIdItem2):
        ''' compares 2 targets of text to each other. The order matters
        e.g. item1 compared to item2 is NOT equal to the reverse.
        '''
        self.item1 = nameItem1.targets[elementIdItem1]
        self.item2 = nameItem2.targets[elementIdItem2]
        self.tokenScore =  sum([i in self.item1.tokens for i in self.item2.tokens]) / len(self.item1.tokens)
        self.lemmasScore =  sum([i in self.item1.lemmas for i in self.item2.lemmas]) / len(self.item1.lemmas)
        self.tokensNoStopWordsScore =  sum([i in self.item1.tokensNoStopWords for i in self.item2.tokensNoStopWords]) / len(self.item1.tokensNoStopWords)
        self.commonTokens = [token for token in self.item1.tokensNoStopWords if token in self.item2.tokensNoStopWords]
        self.commonBigrams = [bigram for bigram in self.item1.bigrams if bigram in self.item2.bigrams]
        self.bigramsScore =  1.0 if len(self.commonBigrams)>=1 else 0.0
        self.commonTrigrams = [trigram for trigram in self.item1.trigrams if trigram in self.item2.trigrams]
        self.trigramsScore = 1.0 if len(self.commonBigrams)>=1 else 0.0
        self.synonymsScore =  sum([i in self.item1.synonyms for i in self.item2.synonyms]) / len(self.item1.synonyms)
        self.score = (self.trigramsScore + self.bigramsScore + self.tokensNoStopWordsScore + self.synonymsScore) / 4

    def scores(self):
        return self.trigramsScore , self.bigramsScore , self.tokensNoStopWordsScore, self.synonymsScore

##t###### Testing & cheatsheet
# SDGTargets = Targets('SDGtargets.csv')    #initialize with a csv file
#SDGTargets.printTargetList()              #works print all targets
#SDGTargets.targets[1].display()            #works prints one target with all its fields
#SDGTargets.targets[1].displayTarget()            #works prints one target with all its fields
# print(SDGTargets.targets[1].tokens)         #works prints the tokens of target '1'
# print(SDGTargets.targets[1].lemmas)         #works prints the lemmas of target '1'
# print(SDGTargets.targets[1].tokensNoStopWords)         #works prints the tokens of target '1' without stopwords
#finding strings in the text
# answer = 'eradicate' in SDGTargets.targets[1].tokens      #works
# print(answer)
