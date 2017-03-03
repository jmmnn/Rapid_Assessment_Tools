from targets import *

SDGTargets = Targets('SDGtargets.csv')    #initialize with a csv file
DummyTargets = Targets('SDGtargets.csv')

# for i in SDGTargets.targets[1].tokens:            #this works! compare tokens
#     print(i in DummyTargets.targets[2].tokens)

# for i in SDGTargets.targets[1].tokens:            #this works! compare tokens with lemmas
#     print(i in DummyTargets.targets[2].lemmas)

# answer = SDGTargets.targets[1].trigrams             #this works! compare tokens
# print(answer)
#
# answer2 = DummyTargets.targets[1].synonyms         #this works! compare tokens
# print(answer2)


for i in SDGTargets.targets[1].tokens:            #this works! compare tokens with synomyms
    print(i in DummyTargets.targets[2].synonyms)
