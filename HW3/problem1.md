### Problem 1 [20 points] 
 Design an extension of the basic Boolean model that 
would allow for ranking of the retrieved documents. Be as detailed as possible.


### Answer:

Information retrieval (IR) in computing and information science is the process of obtaining information system resources that are relevant to the users information need from a collection of those resources. For computer science it can be defined as "The act of finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers)"

Information retrieval begins when a user enters their query for the information. That query both structed or unstructured. The most basic model for information is the standard boolean model.  

|        | doc1 | doc2 | doc3 | doc4 |
|--------|------|------|------|------|
| ship   | 0    | 1    | 0    | 1    |
| travel | 1    | 1    | 0    | 1    |
| ocean  | 0    | 0    | 1    | 1    |


The boolean model searches document in the basis of boolean queries such as OR , AND, NOT. For the above example, search for 'ship' AND 'travel', it will return doc2 and doc4. So the search strictly follows the boolean rule , that docs that satisfies the search conditions are returned and the others are not. 

So, we can see there are a few weakness for the basic boolean model.
- Since the queries return all the results that satisfies the conditions, there is no ranking of the documents done. So a user will have go through all the documents to find the most relevant ones.
- For queries such as 'a' AND 'b' AND 'c' will only give results of docs containing a b and c. But the user might be interested in the docs 'a' AND 'b'.

therefore, there is no way to assign importance or rank the documents which advanced users may desire.

### The Extended Boolean Model

The extended boolean model is an improvement to the standard boolean model. there are a few models that are proposed. We will discuss the **P-Norm** model. 

The **P-Norm** model is similar to the standard boolean model with some small addition of features. The most important addition is the use to **term weighting** of words which is basically a way to measure and note how relevant is a term in a document. For example, in this document, the term 'boolean' will have more weight than the term 'travel' since it has more relevance to this document. 

There are few ways to measure the weight of a term in a document. One of the most common way is using TF-IDF.
TF-IDF takes these factors into account when weighting terms:

- How often is the term used in the document.
- How long is the document.
- How many other document use the same term.

These factors can be expressed by the following formulas:
- TF(t) = (Number of Times Term t Appears) / (Total Number of Terms)
- IDF(t) = log_e(Total Number of Documents / Number of Documents with Term t in it)
- TF.IDF(t) = TF(t) x IDF(t)

With this formula (or using other method you prefer), each term appearance in a document can be given an appropriate weight. With all of these changes, the query processing process is changed as well. P-Norm had a very different query processing method compared to the Standard Boolean Model. Previously the model can only give a binary result, either a document fullfills the query or it didn’t.

The P-Norm model changes this into a formula that results in an arbitrary number, which portray the document likeliness to the query. The value of this number vary largely between system depend on the weighting method used(TF-IDF) on the document and query. A high likeliness value document is put above a low one, this way we can rank the result according to how well it fullfills the query. Finally, we can sort the query results in descending order and show them to the user.

#### Source:
https://en.wikipedia.org/wiki/Boolean_model_of_information_retrieval
http://irkwan.github.io/irkwan/tugas/2016/06/03/13514104-Extended-Boolean-Model/