'''
Problem 1 [40 points]. Automatically collect from memphis.edu 10,000 
unique documents. The documents should be proper after converting them to txt 
(>50 valid tokens after saved as text); only collect .html, .txt, and and .pdf 
web files and then convert them to text - make sure you do not keep any of 
the presentation tags such as html tags. You may use third party tools to 
convert the original files to text. Your output should be a set of 10,000 text 
files (not html, txt, or pdf docs) of at least 50 textual tokens each. You must 
write your own code to collect the documents - DO NOT use an existing crawler.

Store for each proper file the original URL as you will need it later 
when displaying the results to the user.

'''

from enum import unique
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import requests
import random
import time
from nltk.tokenize import word_tokenize
import os
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import PyPDF2
import nltk
from nltk.stem.snowball import SnowballStemmer


def PDfreader(link):

   # pdf_dict={}                     ## dictionary to store all words and frequency count
    url= link

    try:
        result= requests.get(url)
        filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.pdf'  
        with open(filename, 'wb') as f:         
            f.write(result.content)         ## create a pdf file and write the pdf data in it


        pdf = open(filename, 'rb')
        try:
            pdfReader = PyPDF2.PdfFileReader(pdf)    
            num_pages= pdfReader.numPages
            count=0
            res=''
            while count< num_pages:             ## reading all pages of pdf
                page_info = pdfReader.getPage(count)
                res+=page_info.extractText()
                count+=1
            words= re.findall("[a-zA-Z_]+",res)    ## parse the pdf words into a list

            lower_letter= [x.lower() for x in words]  ## convert all words to lowercase
        
            pdf_texts= " ".join(lower_letter)
            textTotoken=tokenize_words(pdf_texts)  ## tokenize all the text file words
            noStopwords=remove_stopwords(textTotoken)   ## remove all the stopwords
            file_words=lemmitize_words(noStopwords)    ## Lemmitize the remaining words


            if len(file_words)>50:
                filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.txt'
                with open(filename, 'w') as fp: ## write prepocessed vocab in a file
                    fp.write(url+"\n")
                    for i in file_words:
                        fp.write(i + "\n")

        except Exception as exc:
            print("PDF read error:--->", exc)            
                   
    except requests.exceptions.HTTPError as errh:
            print ("Http Error: -->",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting: -->",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error: -->",errt)
    except requests.exceptions.RequestException as err:
        print ("OOPS: Something Else",err)



def tokenize_words(text):       
        
    text=re.sub('([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})','', text) # remove emails 

    # regex for utrl= ^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
    #print(text)

    word_token = re.findall('[a-zA-Z]+',text)     ## tokenize the words from file

    word_token=[i.lower() for i in word_token]    ## convert all tokens into lowercase
    #print(word_token)
    
    #print("word token size:",len(word_token))
     
    # unique_tokens= set()    # get all the unique tokens from word_token
    # for i in word_token:
    #     unique_tokens.add(i)

    #print(unique_tokens)
    #print("unique tokens size:",len(unique_tokens))
    
    return word_token

## removes the stopwords from the unique_token list    
def remove_stopwords(tokens):       
    
    stop_words=set(stopwords.words("english"))
    #print(stop_words)

    stopwords_out=[]

    for i in tokens:
        if i not in stop_words:
            if len(i)>1:
                stopwords_out.append(i)

    #print("tokens after removing stopwords:",len(stopwords_out))        

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
    
    
   # print("tokens after lemmitizing", len(result))    
    print(f"link parsed into cleaned tokens")

    #print(len(result))       ## print the final vocabulary list
    return no_stopwords 


def parse_to_file(link):
    
    url = link 

    try:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')

        texts= soup.get_text(" ",strip=True)         ## gets only the readable texts from the soup object
        #print(texts)
        #tokenize_words(texts)
        textTotoken=tokenize_words(texts)  ## tokenize all the text file words
        noStopwords=remove_stopwords(textTotoken)   ## remove all the stopwords
        file_words=lemmitize_words(noStopwords)                 ## Lemmitize the remaining words
                                        # print(texts)

        if len(file_words)>50:
            filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.txt'
            with open(filename, 'w') as fp: ## write prepocessed vocab in a file
                fp.write(url+"\n")
                for i in file_words:
                    fp.write(i + "\n")
        
    #process_count +=1

    #print(f"link processed {process_count}")            

    except requests.exceptions.HTTPError as errh:
        print ("Http Error: -->",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting: -->",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error: -->",errt)
    except requests.exceptions.RequestException as err:
        print ("OOPS: Something Else",err)
    
    

# main 

url = "https://www.memphis.edu/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

#print(soup.get_text())
count=0
links=[]

for link in soup.findAll('a'):
     ## save all the links from page
    doc= link.get('href')
    if (doc.endswith('.pdf') or doc.endswith('.php')): 
        links.append(doc)

print(f"main page links: {len(links)}")

# for i in links:
#     if (i.endswith('.pdf') or i.endswith('.php')):
#         print(i)    

## Iterate the homepage links to get more links
for link in links:
    #count+=1
        
    url = link
    print(url)

    try:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
    
    except requests.exceptions.HTTPError as errh:
        print ("Http Error: -->",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting: -->",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error: -->",errt)
    except requests.exceptions.RequestException as err:
        print ("OOPS: Something Else",err)
    

    externals=[]
    new_added=[]

    for item in soup.findAll('a'):
        ## save all the links from page
        doc= item.get('href')
        if doc!=None:
            if (doc.endswith('.pdf') or doc.endswith('.php')): 
                externals.append(doc)

    for i in externals:
        if i not in links:
            new_added.append(i)
            links.append(i)

    print(f"newly added: {len(new_added)} links")
    print(f"total added: {len(links)}")
    
    if len(links)>10500:
        break

print(f"total links added: {len(links)}")   # total links added

print(f"total links used {count}")    ## total links used to get to 10k links
 
os.chdir('/Users/hmashrique/IR-HW/HW6/Processedtest')  ## change directory to to save the links parsed in file


#parse_to_file("https://www.memphis.edu/training/index.php")

counting=0

start_time= time.time()

for i in links:
    print(i)
    if '.pdf' in i:
        PDfreader(i)
    else:
        parse_to_file(i)
    
    counting+=1
    print(f"link processed {counting}")

end_time= time.time()    

print(f"Total time to process {len(links)} links {(end_time-start_time)/60} minutes")

#print(len(os.listdir()))

