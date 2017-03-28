import targets_dev as ts
import text_extract as ex

##### Use these commands to extract sentences from your pdf documents.
# Bhutan = ex.ExtractedDoc('11-Year-Plan_Vol-1.pdf')
# Bhutan.saveCsv()

#### Use these to define what document you compare against what targets
SDGTargets = ts.Targets('5Targets.csv')    #initialize with a csv file
funkySDG = ts.Targets('funkySDG.csv')
#funkySDG = ts.Targets('./output_Folder/test.pdf.csv')
#funkySDG = ts.Targets('./output_Folder/11-Year-Plan_Vol-1.pdf.csv')


a = [funkySDG.targets[i].targetNumber for i in funkySDG.targets] #this works, is the list of identifyers
b = [SDGTargets.targets[i].targetNumber for i in SDGTargets.targets]

for item in b:     # this works, computes the score for each sentence against each target
    print('\n Target : ')
    print (SDGTargets.targets[item].displayTarget() )

    for item2 in a :
        if ts.Comparer_1_to_1(funkySDG  , item2 , SDGTargets , item ).score > 0.1:
            print (ts.Comparer_1_to_1(funkySDG  , item2 , SDGTargets , item ).score)
            print (funkySDG.targets[item2].displayTarget() )












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
