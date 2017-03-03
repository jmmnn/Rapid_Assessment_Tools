#sample class
import nltk
from nltk.corpus import wordnet as wn
import pandas as pd

#helper functions to get synonyms
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

##testing & cheatsheet
SDGTargets = Targets('SDGtargets.csv')
#SDGTargets.printTargetList()              #works print all targets
#SDGTargets.targets[1].display()            #works prints one target with all its fields
SDGTargets.targets[1].displayTarget()            #works prints one target with all its fields
#print(SDGTargets.targets[1].tokens)         #works prints the tokens of target '1'
