
'''
The code,
- reads the inverted index stored in a json file(faster read).
- gets the user query
- gives the result by rank

'''


import json
import os 
import math

## opening the inverted index json file
#
os.chdir('/Users/hmashrique/IR-HW/HW7/ProcessedMash')

# Opening JSON file
f = open('aaaabbb.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# # Closing file
# f.close()
###################################################

# Iterating through the json
# list

#find='sen'

#print(data[find])
  

query="sajib"  ## enter any query here to check the result

parse_query=query.split(" ") ## tokenize the query into words
###################################################################

## generate the query dictionary for cosine calculation
#
query_dict={}

for i in parse_query:
    if i not in query_dict:
        query_dict[i]=1
    else:
        query_dict[i]+=1    

print(f"query_dict is: {query_dict}")
###################################################################

## get value of the query dict vector
#
val1=0

for i in query_dict.values():
    val1 += i*i

val1= round(math.sqrt(val1),2)

#result = round(my_float, 3)
#print(f"query dict vector value: {val1}")
###################################################################

## get all the docs that has the query words in it
# 
ans=set()

rank={}


for i in parse_query:
    if i in data:        
        for key in data[i]:
            ans.add(key)
###################################################################

## compare each result file with query vector to find cosine similarity
#
for file in ans:

    #print(file)

    freq={}
    if file.endswith(".txt"):
        with open(file, 'r') as f:
                url= f.readline().strip("\n")
                #vocablist= f.readlines().strip("\n")
                vocablist= f.readlines()

    for i in range(len(vocablist)):
        vocablist[i]= vocablist[i].strip("\n")

    for i in vocablist:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1    

    #print(f"freq doc {freq}")

    cosineval= 0

    for i in query_dict:
        if i in freq:
            #print(i,freq[i])
            cosineval+= query_dict[i]*freq[i] 

    #print(f"cosineval : {cosineval}")
    
    ## get value of the document dict vector
    val2=0

    for i in freq.values():
        val2 += i*i

    val2= round(math.sqrt(val2),2)

    #print(f"val2 is: {val2}")
    ##############################################################
    
    ## calculate cosine similarity value
    #
    simvalue= round(cosineval/(val1*val2),3)
    
    #print(f"{file} similarity value: {simvalue}")
      
    ##############################################################
    
    ## put the similarity value in a rank list (dictionary)
    #
    rank[url]=simvalue
    #################################################################

## sort the query results in descending order
#
sorted_dic={}

sortkeys= sorted(rank, key=rank.get, reverse=True)
#print(sortkeys) # 2 3 1

for i in sortkeys:
  sorted_dic[i]=rank[i]

count=0
for i in sorted_dic:
    print(i,sorted_dic[i])
    count+=1

print(count)    
##################################################################