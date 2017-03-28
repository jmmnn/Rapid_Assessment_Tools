# -*- coding: utf-8 -*-
"""
Converts rich files to json using Apache Tika. Instructions:
1) Modify the configurations to suit your folder structure
2) Run $ python text_extract.py
"""

import os
import tika
from tika import parser
import json
import string
import nltk
import re
import uuid
import pandas as pd

###### configurations
tika_server = 'http://localhost:9998/tika'
######

class ExtractedDoc:
    def __init__(self , fileName, docTitle = 'NA', inputFolder = './input_Folder/' , outputFolder = './output_Folder/'):
        self.fileName = fileName
        self.docTitle = docTitle
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.parsed_raw = parser.from_file(self.inputFolder+self.fileName, tika_server)
        self.parsed = json.dumps(self.parsed_raw ,sort_keys = True, indent= 4)
        self.content = self.parsed_raw["content"]
        self.metadata = self.parsed_raw["metadata"]

        self.cleanBody = ''.join(filter(lambda x: x in string.printable, self.content.replace('\n',' ')))
        self.content_pattern = re.compile("[0-9]+\.$")
        self.sentences = [' '.join(sen.split()) for sen in nltk.sent_tokenize(self.cleanBody) if not self.content_pattern.search(sen) and len(sen)>25]
        self.df = pd.DataFrame({'targetNumber': [i for i in range(len(self.sentences))] , 'targetText': self.sentences} )
    def saveCsv (self):
        self.df.to_csv(path_or_buf=self.outputFolder+self.fileName+'.csv')

#Testing # this is working
# myTEXT = ExtractedDoc('test.pdf')
#
# #print (myTEXT.cleanBody)    #works
# #print (myTEXT.sentences)    #works
# # print (myTEXT.df)           #works
# myTEXT.saveCsv()


# passage = myTEXT.content
# #print (myTEXT.content) # Works: returns a nicely formated readable file on screen
# passage =''.join(filter(lambda x: x in string.printable, passage.replace('\n',' ')))
# #print (passage)
#
# content_pattern = re.compile("[0-9]+\.$")
# sentences = list()
# for sen in nltk.sent_tokenize(passage):
#     sen = ' '.join(sen.split())
#     if not content_pattern.search(sen) and len(sen)>25:
#         sentences.append(sen)
#
# sentence_id = [(uuid.uuid4().hex[:10],i) for i in sentences]
# print (sentences)     #works
#print (sentence_id)  #works

## this is not working
# sentence_dic = [dict(map(None,['sentence_id,','sentence'],list(sent))) for sent in sentence_id]
# print (json.dumps(sentence_dic,sort_keys = True, indent= 4))
