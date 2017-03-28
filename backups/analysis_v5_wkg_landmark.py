import targets_dev as ts
import text_extract as ex
import pandas as pd
import json

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
    a = [mysentences.targets[i].targetNumber for i in mysentences.targets] #the list of sentence identifyers
    b = [mytargets.targets[i].targetNumber for i in mytargets.targets] #the list of targets identifyers
    #for target in b:     # this prints on the screen, the score for each sentence against each target
        # print('\n Target : ')
        # print (mytargets.targets[target].displayTarget() )

        # for sentence in a :
        #     if ts.Comparer_1_to_1(mysentences  , sentence , mytargets , target ).score > similarityScore:
                # print (ts.Comparer_1_to_1(mysentences  , sentence , mytargets , target ).score)
                # print (mysentences.targets[sentence].displayTarget() )

    # this generates and saves a json lines file
    output_name = sentencesCsv + '.json'
    with open(output_name, 'w') as f:
        for sentence in a:
            scoreMatrix = []
            row = []
            row.append(sentence)
            row.append(mysentences.targets[sentence].targetText)
            for target in b:
                single_score = ts.Comparer_1_to_1(mysentences  , sentence , mytargets , target ).score
                row.append(single_score)
            scoreMatrix.append(row)
            result_df = pd.DataFrame(scoreMatrix , columns = ['sentenceId'] + ['sentenceText'] + b)
            line = result_df.to_json(orient='records') + '\n'
            f.write(line)

    # This generates a pandas matrix, but it is too time comsuming for a large matrix
    # scoreMatrix = []
    # for sentence in a:
    #     row = []
    #     row.append(sentence)
    #     for target in b:
    #         single_score = ts.Comparer_1_to_1(mysentences  , sentence , mytargets , target ).score
    #         row.append(single_score)
    #     scoreMatrix.append(row)
    # result_df = pd.DataFrame(scoreMatrix , columns = ['sentenceId'] + b)
    # print(result_df)

#### Runnig it!!
#analizer('SDGTargets.csv' , './output_Folder/11-Year-Plan_Vol-1.pdf.csv')   #careful, this takes for ever to run =)
#analizer('5Targets.csv' , './output_Folder/11-Year-Plan_Vol-1.pdf.csv')
analizer('5Targets.csv' , './output_Folder/test.pdf.csv')


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
