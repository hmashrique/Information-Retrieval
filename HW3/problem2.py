'''
Problem 2 [30 points]. Write a (Perl or Python) script that displays the vocabulary and frequency of each word in the main page of the class' website and
on all other documents directly linked from the main page. For each
word, also compute in how many different documents it occurs in this
small collection. You must use hashes.


The code has two methods. HTMLreader() and PDFreader(). These function parses the pdf and html links given in a list(workinglinks) and accumulates its results 
in two dictionaries.

The code outputs two dictionaries.
- main_dict: the total frequency of all the words from all links.
- inv_dict: the document frequency of each word from the links.

VERSION HISTORY:
Modified by: Hasan Mashrique, 9/28/2022

'''
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import requests
import PyPDF2
import random
import string

'''
The HTMLreader function read the html links and parses the html document. It parses each unique word and
counts its frequency and returns a dictionary of html link words frequency.

'''
def HTMLreader(link):

    baseUrl= link
    result= requests.get(baseUrl)
    doc= BeautifulSoup(result.text, 'html.parser')
    texts=doc.get_text(" ",strip=True)
    #print(texts)
    wordCount= re.findall("[a-zA-Z_]+",texts)
    lowecase= [x.lower() for x in wordCount]  ## convert words to lowercase

    word_frequency={}

    for i in lowecase:         ## storing main page unique word count in dictionary
        if i not in word_frequency:
            word_frequency[i]=1
        else:
            word_frequency[i]+=1    

    return word_frequency    


'''
The PDFreader function takes pdf links from workinglinks and parses the pdf documents. It first writes the content of pdf 
by creating a pdf file and writing its content. Then it parses the words in  pdf and returns a dictionary of pdf words frequency.

'''
def PDfreader(link):

    pdf_dict={}                     ## dictionary to store all words and frequency count
    testURL= link
    result= requests.get(testURL)
    filename= ''.join(random.choices(string.ascii_lowercase,k=5)) + '.pdf'  
    with open(filename, 'wb') as f:         
        f.write(result.content)         ## create a pdf file and write the pdf data in it


    pdf = open(filename, 'rb')
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

    
    for i in lower_letter:         ## store the unique word count in a dictionary
        if i not in pdf_dict:
            pdf_dict[i]=1
        else:
            pdf_dict[i]+=1    

    return pdf_dict



## Main Function

## these links are the only workable links that can be parsed ..other links are either permission locked or
## not working

workinglinks=['https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/syllabus.COMP78130.pdf',
'https://sites.google.com/view/dr-vasile-rus/home',
'https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/papers/codingStyle.html',
'https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-01.txt',
'https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/papers/perlTutorial.pdf',
'https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-02.txt',
'https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-03.txt',
'https://cs.memphis.edu/~vrus/teaching/ir-websearch/papers/mapReduce.pdf',
'https://cs.memphis.edu/~vrus/teaching/ir-websearch/papers/PageRankFranceschet.pdf']

main_dict={}              ## main page word frequency dictionary

main_dict= HTMLreader('https://www.cs.memphis.edu/~vrus/teaching/ir-websearch/')

inv_dict={}               ## base dict for counting doc frequency

for i in main_dict:       ## convert the main freq dict to base frequency of 1          
    inv_dict[i]=1


'''
iterate the working links and add frequency of words to main_dict 
Also add the doc frequency of each word into inv_dict 

'''

for i in workinglinks:      
    if '.pdf' in i:
        temp_dict= PDfreader(i)
        for i in temp_dict:
            if i not in main_dict:
                main_dict[i] = temp_dict[i]
                inv_dict[i]= 1
            else:
                main_dict[i] += temp_dict[i]
                inv_dict[i]+=1    
        temp_dict={}
    else:
        temp_dict= HTMLreader(i)
        for i in temp_dict:
            if i not in main_dict:
                main_dict[i] = temp_dict[i]
                inv_dict[i]= 1
            else:
                main_dict[i] += temp_dict[i]
                inv_dict[i]+= 1    
        temp_dict={}

    #print(len(main_dict))

print("The freq doc is \n",main_dict)  ## print total frequency of all words from all the docs available
print("\n")
print("The inv_doc is \n\n",inv_dict)   ## print the doc frequency of words





