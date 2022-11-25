'''
Problem 1 [40 points]. Write a (Perl or Python) program that generates the inverted index of a set of already preprocessed files. The files are stored in a 
directory which is given as an input parameter to the program. Use the files preprocessed in the previous assignment(s) as test data. Use raw term 
frequency (tf) in the document without normalizing it. Think about saving the generated index, including the document frequency (df), in a file so that you 
can retrieve it later.

# The code follows the below steps:

# Read all the words from preprocessed file in a list (vocablist) and create a dictionary for each word
# Iterate through all files in the folder
#     for each file,
#      tokenize the words.
#      for each word,
#       if word is in vocab dictionary:
#         update docname and wordcount to that word dictionary  

Finally, the code outputs and inverted index(doc and its corresponding word count) of the vocablist

VERSION HISTORY:
Modified by: Hasan Mashrique, 10/24/2022
             
'''             
import re
import os
from nltk.stem.wordnet import WordNetLemmatizer

## tokenizes the full texts into tokens/words
def tokenize_words(text):       
        
    text=re.sub('([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})','', text) # remove emails 

    # regex for utrl= ^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
    #print(text)

    word_token = re.findall('[a-zA-Z]+',text)     ## tokenize the words from file

    word_token=[i.lower() for i in word_token]    ## convert all tokens into lowercase
    #print(word_token)
    
    #print("word token size:",len(word_token))
     
    return word_token

## lemmitize the stopwords_out list and returns it as final vocabulary list
def lemmitize_words(tokens):    
    
    lemmatizer = WordNetLemmatizer()

    #final_clean=[]

    for i in range(len(tokens)):
        #print(tokens[i] + "--->" + lemmatizer.lemmatize(tokens[i]))
        tokens[i]=lemmatizer.lemmatize(tokens[i])

    return tokens
 
# main

## change this directory
os.chdir('/Users/hmashrique/IR-HW/HW5')   ## change directory to working directory

vocablist=[]

with open("processed_data.txt", 'r') as fp:     ## reading the preprocessed file to a list(vocablist)
    vocablist= fp.readlines()
    #print(type(word))
    for i in range(len(vocablist)):
        vocablist[i]= vocablist[i].strip("\n")

    #print(vocablist)    

invert = {}     ## initialize inverted index dictionary

for i in vocablist:   ## create nested dict for vocablist words
  if i not in invert:
    invert[i]={}
  else:
    continue

#print(invert)

# compare each docs token with invert. if words in invert, update invert vocab with docname and occurence

for file in os.listdir():  ## read the text files into a string
    #print(file)
    if file.endswith(".txt"):  
        if 'data' in file:   ## avoid the processed data file
            continue
        else:
            #print(file)
            text_from_file=""           ## string to store all the text files content
            with open(file, 'r') as f:
                text_from_file += f.read()
                #f.close()
            tokens_from_docs= tokenize_words(text_from_file)        ## tokenize words from file
            lemmitize_tokens= lemmitize_words(tokens_from_docs)     ## lemmitize the tokens
                     
            for i in lemmitize_tokens:    ## update the vocab inverted index for each document
                if i in invert:
                    if file not in invert[i]:
                        invert[i][file]=1
                    else:
                        invert[i][file]+=1

for i in invert:
    print(i , "--->" , invert[i])    ## print the invert index for vocablist




