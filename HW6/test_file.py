
import os
import random
import string
import time
import requests 
from bs4 import BeautifulSoup
import PyPDF2
import re

os.chdir("/Users/hmashrique/IR-HW/HW6")

# print("This is the start of the program.")
# time.sleep(5)
# print("This prints five seconds later.")

# url= "https://www.memphis.edu/coronavirusupdates/index.php"
# #filename='mash.txt'

# file_words=["apple","banana","orange","grape"]

# filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.txt'

# with open(filename, 'w') as fp: ## write prepocessed vocab in a file
#     fp.write(url+"\n")
#     for i in file_words:
#         fp.write(i + "\n")
#

#  data=[] 
# with open('npkqf.txt','r') as fp:
#     link= fp.readline().strip("\n")
#     while True:
#         line = fp.readline()
#         data.append(line.strip("\n"))
#         if not line:
#             break
#     data.pop()    

# print(link)
# print(data)      

#print(len(os.listdir()))
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
    #print("unique tokens size:",len(unique_tokens))
    
    return unique_tokens


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


            if len(textTotoken)>50:
                filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.txt'
                with open(filename, 'w') as fp: ## write prepocessed vocab in a file
                    fp.write(url+"\n")
                    for i in textTotoken:
                        fp.write(i + "\n")


        except Exception as exc:
            print("PDF read error:--->", exc)            
        

                #noStopwords=remove_stopwords(textTotoken)   ## remove all the stopwords
        #file_words=lemmitize_words(noStopwords)                 ## Lemmitize the remaining words
                                        # print(texts)

    except requests.exceptions.HTTPError as errh:
            print ("Http Error: -->",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting: -->",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error: -->",errt)
    except requests.exceptions.RequestException as err:
        print ("OOPS: Something Else",err)
    

PDfreader('https://www.memphis.edu/nursing/archive/programs/bsn-degree.pdf')