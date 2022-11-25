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


The code follows the below steps:

Step 1: The code first scraps the website news.yahoo.com and fetches 10 articles from it.
Step 2: Loops through each article and write them into text files inside a folder
Step 3: Reads the content of the text files from that folder and stores in a string
Step 4: Tokenizes the string using tokenize_words()
Step 5: Removes the stopwords from tokenized words()
Step 6: Lemmitizes the remaining words using lemmitizeWords()

Finally, the code returns a list(no_stopwords) consisting of the vocabulary after preprocessing the text files.

VERSION HISTORY:
Modified by: Hasan Mashrique, 10/12/2022
             Hasan Mashrique, 10/20/2022

'''

from enum import unique
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import requests
import random
from nltk.tokenize import word_tokenize
import os
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk
from nltk.stem.snowball import SnowballStemmer
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')


## tokenizes the full texts into tokens/words
def tokenize_words(text):       
        
    text=re.sub('([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})','', text) # remove emails 

    # regex for utrl= ^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
    #print(text)

    word_token = re.findall('[a-zA-Z]+',text)     ## tokenize the words from file

    word_token=[i.lower() for i in word_token]    ## convert all tokens into lowercase
    #print(word_token)
    
    #print("word token size:",len(word_token))
     
    unique_tokens= set()    # get all the unique tokens from word_token
    for i in word_token:
        unique_tokens.add(i)

    #print(unique_tokens)
    print("unique tokens size:",len(unique_tokens))
    
    return unique_tokens


## removes the stopwords from the unique_token list    
def remove_stopwords(tokens):       
    
    stop_words=set(stopwords.words("english"))
    #print(stop_words)

    stopwords_out=[]

    for i in tokens:
        if i not in stop_words:
            if len(i)>1:
                stopwords_out.append(i)

    print("tokens after removing stopwords:",len(stopwords_out))        

    # for i in stopwords_out:
    #     print(i)

    return stopwords_out    


## lemmitize the stopwords_out list and returns it as final vocabulary list
def lemmitize_words(no_stopwords):    
    
    lemmatizer = WordNetLemmatizer()

    #final_clean=[]

    for i in range(len(no_stopwords)):
        #print(no_stopwords[i] + "--->" + lemmatizer.lemmatize(no_stopwords[i]))
        no_stopwords[i]=lemmatizer.lemmatize(no_stopwords[i])
    
    result=set()

    for i in no_stopwords:     ## store the unique words after lemmitizing
        result.add(i)
    print("tokens after lemmitizing", len(result))    

    print(result)       ## print the final vocabulary list
    
    with open('processed_data.txt', 'w') as fp: ## write prepocessed vocab in a file
        for i in result:
            fp.write(i + "\n")
        fp.close()           

# main function()
# soup = BeautifulSoup(html_page, "lxml")
url = "https://news.yahoo.com"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

links = []        ##list for saving links
count=0           ## counter for 10 html links  
articles=[]       ## list for 10 html links

for link in soup.findAll('a'):   ## save all the links from page
    links.append(link.get('href'))

# for i in links:
#     print(i)

for i in links:                 ### save 10 html links
    if i!=None:
        if '.html' in i:
            articles.append(i)
            count+=1
    if count>=10:
        break    

# for i in articles:
#     print(i)    

for i in range(len(articles)):  ## convert all the pages into html links 

    add="https://news.yahoo.com"
    
    if "https:" not in articles[i]:
       articles[i]= add + articles[i]
       #print(i)

print("Articles to parse ....\n")   ## view the html pages to traverse
for i in articles:
    print(i)    

#parse articles and write in .txt file
for i in articles:

    url = i
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    texts= soup.get_text(" ",strip=True)         ## gets only the readable texts from the soup object
    #print(texts)

    filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.txt'     ## write the texts into a text file
    with open(filename, 'w') as f:         
        f.write(texts)        

cwd= os.getcwd()      ## get current working directory

#print(cwd)

text_from_file=""    ## string to store all the text files content

for file in os.listdir():  ## read the text files into a string
    #
    if file.endswith(".txt"):
        print(file)
        with open(file, 'r') as f:
            text_from_file += f.read()

#print(text_from_file)

## do the pre-processing

textTotoken=tokenize_words(text_from_file)  ## tokenize all the text file words
noStopwords=remove_stopwords(textTotoken)   ## remove all the stopwords
lemmitize_words(noStopwords)                 ## Lemmitize the remaining words

