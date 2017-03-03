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

def processTargets (csvfile):
    ''' This is the main class which calls on helper classes to process the lists of targets.
    '''
    mydata = loadTargetCsv(csvfile)            #load your csv file
    allTargets = analyzeTargets(mydata)        #analyzes them
    return allTargets

def loadTargetCsv (csvfile):
    '''
    Loads a list of Targets from a csv file. The file must have at least 2 columns with these headers: first "targetNumber" (the values should be integers or text) & second "targetText"
    '''
    df = pd.read_csv(csvfile, encoding = "ISO-8859-1")
    return df

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

def printTargetList(dataframe):
    return [dataframe[i].displayTarget() for i in dataframe]

##testing & cheatsheet
# t1_1 = Target(1.1 , 'reduce poverty for all women') #create a new target
# t1_1.display()                                      #display the details of target
#mydata = loadTargetCsv('SDGtargets.csv')              #load your csv file
#print (mydata['targetNumber'])                       # this prints only one columnTarget
#print (mydata[0:2])                                  # this prints a range of rows
#print(mydata.iloc[3])                                # this prints just one specific row
#print(mydata.iloc[3]['targetNumber'])                # this prints a specific value in a specific row
#print(mydata.iloc[3]['targetText'])                  # same as above

## Execution
SDGTargets = processTargets('SDGtargets.csv')
printTargetList(SDGTargets)                 #prints the list of targets
SDGTargets[1].displayTarget()               #prints one target
SDGTargets[168].display())                  #working!! this displays all the fields for target labeled 169
