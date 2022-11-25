

import nltk
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk
from nltk.stem.snowball import SnowballStemmer
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('punkt')

def tokenize_words(text):       ## tokenize the texts into tokens/words
        
    text=re.sub('([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})','', text) # remove emails 

    # regex for utrl= ^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*)*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
    #print(text)

    # tokenize the words from file
    word_token = re.findall('[a-zA-Z]+',text)

    # convert all tokens into lowercase
    word_token=[i.lower() for i in word_token]
    print(word_token)
    print("word token length:",len(word_token))
    return word_token

    
def remove_stopwords(tokens):       ## remove the stopwords from the word token list
    
    stop_words=set(stopwords.words("english"))
    #print(stop_words)

    stopwords_out=[]

    for i in tokens:
        if i not in stop_words:
            if len(i)>1:
                stopwords_out.append(i)

    print(len(stopwords_out))        

    for i in stopwords_out:
        print(i)

    return stopwords_out    


def lemmitizeWords(no_stopwords):    ## lemmitize the filtered list and create the final word list
    
    lemmatizer = WordNetLemmatizer()

    final_clean=[]

    for i in no_stopwords:
        print(i + ' ---> '+ lemmatizer.lemmatize(i))
        #final_clean.append(lemmatizer.lemmatize("programming"))

text ="""Casemiro conundrum
Six weeks after signing in a deal worth £70million ($79m), Casemiro has made one start. 
Had Ten Hag decided to go more defensive against City, the Brazil midfielder would have been the clear 
candidate to replace one of the offensive players, but he was on the bench for the fifth time in his short
 United career. His only start came against Real Sociedad, and United lost 1-0.

Ten Hag referenced results when asked about Casemiro, who he seems to regard as 
an alternative rather than an addition to McTominay. “It had nothing to do with Casemiro, and all to do 
with Scott. When you sum it up: Brentford he wasn’t in the team, we lose, on the day Casemiro signed we 
win (against Liverpool). We played six games, we won five and in those five games, Scott played. One he
didn’t, against Sociedad. For me it’s logical. Scott developed really well.”

Still, it feels a curious situation for a player who in May was starting his fifth Champions 
League final triumph. Casemiro can provide an elite screen on the biggest occasions, even if he is yet 
to fully demonstrate this for United. He was second to Frenkie de Jong as Ten Hag’s preference in that 
position and comes with an entirely different profile. “I’m sure Casa will play a really important role,
” Ten Hag insisted. “We know his background, all the titles he won, you see every day in training he can 
contribute in the team.”"""

textTotoken=tokenize_words(text)
noStopwords=remove_stopwords(textTotoken)
lemmitizeWords(noStopwords)

