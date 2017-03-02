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

#Loads a list of Targets from a csv file. Must have columns "targetNumber" & "targetText"
def loadTargetCsv (csvfile):
    df = pd.read_csv(csvfile, encoding = "ISO-8859-1")
    return df

def createClasses (dataframe):
    for i in len(dataframe):
        a = dataframe.iloc[i]['targetNumber']
        b = dataframe.iloc[i]['targetText']
        newTarget = Target(a,b)
        str('Target'+ str(i)) = newTarget

##testing & cheatsheet
# t1_1 = Target(1.1 , 'reduce poverty for all women') #create a new target
# t1_1.display()                                      #display the details of target
mydata = loadTargetCsv('SDGtargets.csv')              #load your csv file
#print (mydata['targetNumber'])                       # this prints only one columnTarget
#print (mydata[0:2])                                  # this prints a range of rows
#print(mydata.iloc[3])                                # this prints just one specific row
#print(mydata.iloc[3]['targetNumber'])                # this prints a specifi value in a specific row
#print(mydata.iloc[3]['targetText'])                  # same as above

# a = mydata.iloc[3]['targetNumber']
# b = mydata.iloc[3]['targetText']
# newTarget = Target(a,b)
# newTarget.display()
createClasses(mydata)
Target2.display()
