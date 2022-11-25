'''
Problem 1 [30 points]. 

Develop a retrieval program that takes as input an user query in the form of 
a set of keywords, uses the inverted index to retrieve documents containing
at least one of the keywords, and then ranks these documents based on
cosine values between query vector and document vectors. The output should be 
a ranked list of documents with links to the original documents, i.e. URLs to
the original documents on the web.


The solution code does the following:
- Reads the preprocessed data from a directory and creates the inverted index
- Get the user query( in the code)
- Collect all the documents that has the query words in it
- For each document(url), compare with the query to get the cosine similarity and store the similarity value with the document 
- Sorts the similarity list in descending order and displays it

'''


import os
import math
import json

# main


os.chdir('/Users/hmashrique/IR-HW/HW7/ProcessedMash') ## file location for the processed files

index_store= set() ## initialize vocabulary store for all unique words in 10k documents

## iterate all the 10k files to get the unique words and add them in index_store
#
for file in os.listdir():  ## read the text files into a string
    
    vocablist=[]
    
    if file.endswith(".txt"):
        with open(file, 'r') as f:
            print(f.readline())
            #vocablist= f.readlines().strip("\n")
            vocablist= f.readlines()
            f.close()

            #print(vocablist)

        for i in range(len(vocablist)):
            vocablist[i]= vocablist[i].strip("\n")
            index_store.add(vocablist[i])  ## store unique words in index store
############################################################    

## create inverted index dictionary for all the unique words
#
invert = {}     ## initialize inverted index dictionary

for i in index_store:   ## create nested dict for vocablist words
  if i not in invert:
    invert[i]={}
  else:
    continue

# with open("sample4.json", "w") as outfile:
#     json.dump(invert, outfile, indent=4)

#print(invert)
##############################################################

## read all the files again to generate the inverted index
#
for file in os.listdir():  ## read the text files into a string
  
  #print(file)  
  text_from_file=""           ## string to store all the text files content
  if file.endswith(".txt"):
    with open(file, 'r') as f:
        url= f.readline()
        #f.close()
        vocabs= f.readlines()
    
  for i in range(len(vocabs)):
    vocabs[i]= vocabs[i].strip("\n")
  
 ## generate inverted index for all files
 ##           
  for i in vocabs:    ## update the vocab inverted index for each document
      if i in invert:
          if file not in invert[i]:
              invert[i][file]=1
          else:
              invert[i][file]+=1
      else:
           continue

with open("aaaabbb.json", "w") as outfile:
    json.dump(invert, outfile, indent=4)

# for i in invert:
#     print(i , "--->" , invert[i])    ## print the invert index for vocablist
###################################################################

## get user query for searching
#
# query="azim ullah"  ## enter any query here to check the result

# parse_query=query.split(" ") ## tokenize the query into words
# ###################################################################

# ## generate the query dictionary for cosine calculation
# #
# query_dict={}

# for i in parse_query:
#     if i not in query_dict:
#         query_dict[i]=1
#     else:
#         query_dict[i]+=1    

# print(f"query_dict is: {query_dict}")
# ###################################################################

# ## get value of the query dict vector
# #
# val1=0

# for i in query_dict.values():
#     val1 += i*i

# val1= round(math.sqrt(val1),2)

# #result = round(my_float, 3)
# #print(f"query dict vector value: {val1}")
# ###################################################################

# ## get all the docs that has the query words in it
# # 
# ans=set()

# rank={}


# for i in parse_query:
#     if i in invert:        
#         for key in invert[i]:
#             ans.add(key)
# ###################################################################

# ## compare each result file with query vector to find cosine similarity
# #
# for file in ans:

#     #print(file)

#     freq={}
#     if file.endswith(".txt"):
#         with open(file, 'r') as f:
#                 url= f.readline().strip("\n")
#                 #vocablist= f.readlines().strip("\n")
#                 vocablist= f.readlines()

#     for i in range(len(vocablist)):
#         vocablist[i]= vocablist[i].strip("\n")

#     for i in vocablist:
#         if i not in freq:
#             freq[i]=1
#         else:
#             freq[i]+=1    

#     #print(f"freq doc {freq}")

#     cosineval= 0

#     for i in query_dict:
#         if i in freq:
#             #print(i,freq[i])
#             cosineval+= query_dict[i]*freq[i] 

#     #print(f"cosineval : {cosineval}")
    
#     ## get value of the document dict vector
#     val2=0

#     for i in freq.values():
#         val2 += i*i

#     val2= round(math.sqrt(val2),2)

#     #print(f"val2 is: {val2}")
#     ##############################################################
    
#     ## calculate cosine similarity value
#     #
#     simvalue= round(cosineval/(val1*val2),3)
    
#     #print(f"{file} similarity value: {simvalue}")
      
#     ##############################################################
    
#     ## put the similarity value in a rank list (dictionary)
#     #
#     rank[url]=simvalue
#     #################################################################

# ## sort the query results in descending order
# #
# sorted_dic={}

# sortkeys= sorted(rank, key=rank.get, reverse=True)
# #print(sortkeys) # 2 3 1

# for i in sortkeys:
#   sorted_dic[i]=rank[i]

# count=0
# for i in sorted_dic:
#     print(i,sorted_dic[i])
#     count+=1

# print(count)    
# ##################################################################