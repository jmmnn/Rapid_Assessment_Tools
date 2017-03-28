from targets import *

SDGTargets = Targets('SDGtargets.csv')    #initialize with a csv file
DummyTargets = Targets('SDGtargets.csv')

def compareItems (nameItem1, elementIdItem1, nameItem2, elementIdItem2):
    score = 0
    item1 = nameItem1.targets[elementIdItem1]
    item2 = nameItem2.targets[elementIdItem2]
    tokenScore =  sum([i in item1.tokens for i in item2.tokens]) / len(item1.tokens)
    lemmasScore =  sum([i in item1.lemmas for i in item2.lemmas]) / len(item1.lemmas)
    bigramsScore =  sum([i in item1.bigrams for i in item2.bigrams]) / len(item1.bigrams)
    trigramsScore =  sum([i in item1.trigrams for i in item2.trigrams]) / len(item1.trigrams)
    synonymsScore =  sum([i in item1.synonyms for i in item2.synonyms]) / len(item1.synonyms)

    return tokenScore , lemmasScore , bigramsScore , trigramsScore , synonymsScore


print (compareItems(SDGTargets , 16 , DummyTargets , 17 ))
