import targets_dev as ts
import text_extract as ex

##### Use these lines below to extract sentences from your pdf documents.
##### Comment afterwards
# Bhutan = ex.ExtractedDoc('11-Year-Plan_Vol-1.pdf')
# Bhutan.saveCsv()

def analizer (targetsCsv , sentencesCsv , similarityScore = 0):
    """ Use this function to analyze a document (CSV format) against your targets (CSV format)
        You can change the similarity Score from 0 to 1 to be more strict.
    """
    mytargets = ts.Targets(targetsCsv)
    mysentences = ts.Targets(sentencesCsv)
    a = [mysentences.targets[i].targetNumber for i in mysentences.targets] #this works, is the list of identifyers
    b = [mytargets.targets[i].targetNumber for i in mytargets.targets]
    for item in b:     # this works, computes the score for each sentence against each target
        print('\n Target : ')
        print (mytargets.targets[item].displayTarget() )

        for item2 in a :
            if ts.Comparer_1_to_1(mysentences  , item2 , mytargets , item ).score > similarityScore:
                print (ts.Comparer_1_to_1(mysentences  , item2 , mytargets , item ).score)
                print (mysentences.targets[item2].displayTarget() )

#### Runnig it!!
analizer('5Targets.csv' , './output_Folder/11-Year-Plan_Vol-1.pdf.csv' , 0.075)


#### Helpful commands #######
#print(funkySDG.targets[1].targetNumber) ## this works,
# print ('\n funky trigramm')
# print (ts.Comparer(funkySDG , 1 , funkySDG , 25 ).scores())
# print (ts.Comparer(funkySDG  , 1 , funkySDG , 25 ).score)
# print (ts.Comparer(funkySDG  , 1 , funkySDG , 25 ).bigramsScore)
# print(SDGTargets.targets[4].tokensNoStopWords)
# print(len(SDGTargets.targets[4].tokensNoStopWords))
# print(funkySDG.targets[3166].tokensNoStopWords)
# print(len(funkySDG.targets[3166].tokensNoStopWords))
# print('\n compare: ')
# print (ts.Comparer(funkySDG , 3166 , SDGTargets , 4 ).commonTokens)
# print (ts.Comparer(funkySDG , 3166 , SDGTargets , 4 ).tokensNoStopWordsScore)
# print (ts.Comparer(funkySDG , 3166 , SDGTargets , 4 ).tokenScore)
# print (ts.Comparer(funkySDG , 1 , funkySDG , 25 ).commonBigrams)
# print (ts.Comparer(funkySDG , 1 , funkySDG , 25 ).commonTrigrams)
