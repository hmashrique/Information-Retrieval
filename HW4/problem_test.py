'''
Problem 1 [30 points]. Write a (Perl or Python) program that preprocesses a 
collection of documents using the recommendations given in the 
Text Operations lecture. The input to the program will be a directory
containing a list of text files. Use the files from assignment #3 as
test data as well as 10 documents (manually) collected from news.yahoo.com . 
The yahoo documents must be converted to text before using them.

Remove the following during the preprocessing:
- digits
- punctuation
- stop words (use the generic list available at ...ir-websearch/papers/english.stopwords.txt)
- urls and other html-like strings
- uppercases
- morphological variations
'''
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import os
#import nltk
import nltk
from nltk.tokenize import word_tokenize
import re
import string

def read_text_file(file_to_read):  ## read the .txt files
    input=''
    with open(file_to_read, 'r') as f:
        input+=f.read()
    return input    



# main
filepath="/Users/hmashrique/IR-HW/HW4"
# Change the directory
os.chdir(filepath)

# read the .txt files in the directory
for file in os.listdir():
    print(file)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~\''''
    if file.endswith(".txt"):
        filein=read_text_file(file)
        #print(filein)
        #word_tokens = word_tokenize(filein)
        new_string = re.findall('[a-zA-Z]+',filein) 
        #ll=word_tokenize(new_string)

        for i in new_string:
            print(i) 

'''
#test html to text

# with open("/Users/hmashrique/Downloads/yahooarticle.html","r") as fp:          # open the html file in read mode
#     webPage = BeautifulSoup(fp, 'html.parser')  # converts the html file into beautifulsoup object

# texts= webPage.get_text(" ",strip=True)         # gets only the readable texts from the soup object
# print(texts)
'''

## read from text files in a folder 
    ## read from one text file    
## preprocess the text file
'''
Remove the following during the preprocessing:
- digits
- punctuation
- stop words (use the generic list available at ...ir-websearch/papers/english.stopwords.txt)
- urls and other html-like strings
- uppercases
- morphological variations

'''
