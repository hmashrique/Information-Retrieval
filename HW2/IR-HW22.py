'''
Problem 2 [20 points]. 
Write a Python/Perl script (or in another programming language)
that counts how many words are in the main page of the course website. Also, 
display the vocabulary of the page in alphabetical order showing for each word 
its frequency in the page.
'''

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re


'''
The program reads the html version file (websearch.html) of the course website page, gets all the words from it and counts
its number of occurence. Finally it prints the occurence of each word in an alphabetical order.

VERSION HISTORY:

Modified by Hasan Mashrique, 9/8/2022
'''


with open("/Users/hmashrique/Documents/IR-HW/HW2/websearch.html","r") as fp:          # open the html file in read mode
    webPage = BeautifulSoup(fp, 'html.parser')  # converts the html file into beautifulsoup object

texts= webPage.get_text(" ",strip=True)         # gets only the readable texts from the soup object
#print(texts)

wordCount= re.split(r'! |, | |; |: |:|\n|,', texts) # gets all the words from the texts as individual items

print(wordCount)                                # prints out each parsed word

print(pd.value_counts(np.array(wordCount)).sort_index(ascending=True))    # counts every word occurence in the wordcount list and prints it 
                                                                          #  in ascending order



