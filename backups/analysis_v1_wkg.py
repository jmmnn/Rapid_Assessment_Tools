import targets_dev as ts

SDGTargets = ts.Targets('SDGtargets.csv')    #initialize with a csv file
DummyTargets = ts.Targets('SDGtargets.csv')

def compareItems (nameItem1, elementIdItem1, nameItem2, elementIdItem2):
    ''' compares 2 chuncks of text to each other. The order matters
    e.g. item1 compared to item2 is NOT equal to the reverse.
    '''
    score = 0
    item1 = nameItem1.targets[elementIdItem1]
    item2 = nameItem2.targets[elementIdItem2]
    tokenScore =  sum([i in item1.tokens for i in item2.tokens]) / len(item1.tokens)
    tokensNoStopWordsScore =  sum([i in item1.tokensNoStopWords for i in item2.tokensNoStopWords]) / len(item1.tokensNoStopWords)
    lemmasScore =  sum([i in item1.lemmas for i in item2.lemmas]) / len(item1.lemmas)
    bigramsScore =  sum([i in item1.bigrams for i in item2.bigrams]) / len(item1.bigrams)
    trigramsScore =  sum([i in item1.trigrams for i in item2.trigrams]) / len(item1.trigrams)
    synonymsScore =  sum([i in item1.synonyms for i in item2.synonyms]) / len(item1.synonyms)

    return tokenScore , tokensNoStopWordsScore, lemmasScore , bigramsScore , trigramsScore , synonymsScore

print (compareItems(SDGTargets , 16 , DummyTargets , 17 ))
print(SDGTargets.targets[16].tokens)
print(SDGTargets.targets[16].tokensNoStopWords)
