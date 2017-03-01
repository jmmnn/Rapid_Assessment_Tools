import nltk
import pandas as pd
import itertools

def extract_entity_names(t):
    '''helper function'''
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

def entity_extractor(string):
    '''Invoque this function with a string as a parameter. E.g.
    entity_extractor('OCHA started operations in Indonesia')
    '''
    sentences = nltk.sent_tokenize(string)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sent) for sent in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))
    #Return unique entity names
    return set(entity_names)

def entity_extractor_from_file(file):
    '''Invoque this function with a text file as a parameter. E.g.
    entity_extractor_from_file('sample3.txt')
    '''
    with open(file, 'r') as f:
        text = f.read()
    return entity_extractor(text)

def entity_ext_from_csv_rows(csvfile):
    df = pd.read_csv(csvfile, encoding = "ISO-8859-1")
    row_iterator = df.iterrows()
    list = []
    for i, row in row_iterator:
        list.append(entity_extractor(row['Text']))
    df['entities'] = list
    return df.entities

result_series = entity_ext_from_csv_rows('daily_report_content_gregs.csv')
#result_series = entity_ext_from_csv_rows('daily_report_test.csv')

with open('entities.csv', 'w') as f:
    for row in result_series:
        line = ''
        for word in row:
            line = line + word + ','
        #print(line)
        f.writelines(line + "\n")
