
from flask import Flask, request, jsonify, render_template
import json
import math
import os
# Create the app object
app = Flask(__name__)


# importing function for calculations
#from basic_calculator_function import basic_calculator

# Define calculator
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/predict',methods=['POST'])
def predict():

   # a = request.form['a']
   # b = request.form['b']
    query_text = str(request.form['query'])
    
    ## get the processed file path
    #document_path=""
    #document_path = os.getcwd()+'/ProcessedMash'

    ## READ THE INVERTED INDEX FILE
    with open('aaaabbb.json', 'r') as f:
        data = json.loads(f.read())
    ############################################    

    ### PROCESSING THE QUERY STRING
    
    ## parse the query string into words
    parse_query=query_text.split(" ") ## tokenize the query into words
    
    ## get the query words in dictionary
    query_dict={}

    for i in parse_query:
        if i not in query_dict:
            query_dict[i]=1
        else:
            query_dict[i]+=1    

    ## get value of the query dict vector
    val1=0

    for i in query_dict.values():
        val1 += i*i

    val1= round(math.sqrt(val1),2)
    #########################################################

    ## get all the docs that has the query words in it
    ans=set()
    rank={}

    for i in parse_query:
        if i in data:        
            for key in data[i]:
                ans.add(key)
    #result = basic_calculator(a,b,operation)

    #f = open('aaaabbb.json')
    
    # returns JSON object as 
    # a dictionary
   # data = json.load(f)

   ## compare each result file with query vector to find cosine similarity
    os.chdir('/Users/hmashrique/IR-HW/IR-searchengine/ProcessedMash')

    for file in ans:

        #vocablist=[]
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

        cosineval= 0

        for i in query_dict:
            if i in freq:
                #print(i,freq[i])
                cosineval+= query_dict[i]*freq[i] 

        ## get value of the document dict vector
        val2=0

        for i in freq.values():
            val2 += i*i

        val2= round(math.sqrt(val2),2)

        ## calculate cosine similarity value
        simvalue= round(cosineval/(val1*val2),3)
        
        ## put the similarity value in a rank list (dictionary)
        rank[url]=simvalue
    
    ## sort the query results in descending order
    sorted_dic={}

    sortkeys= sorted(rank, key=rank.get, reverse=True)
    #print(sortkeys) # 2 3 1

    for i in sortkeys:
        sorted_dic[i]=rank[i]

    count=0
    for i in sorted_dic:
        print(i,sorted_dic[i])
        count+=1

    #print(count)    

    

    return render_template('result.html', sorted= sorted_dic, query=query_text)


if __name__ == "__main__":
    app.run(debug=True)
