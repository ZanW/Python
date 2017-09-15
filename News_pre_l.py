
# coding: utf-8

# ## To-do:
# ### Language limited to English

# In[251]:

from twitterscraper import query_tweets
import re
import nltk
from nltk.corpus import stopwords
from string import digits
import string
import snowballstemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer, TfidfTransformer


# In[247]:

textData = []
for tweet in query_tweets("bitcoin%20since%3A2017-09-01%20until%3A2017-09-13", 10)[:40]:
    text = tweet.text.encode('utf-8').decode('utf-8')
    # remove all http links included in the twitter
    text = re.sub(r"http\S+", "",text)
   
    # remove all digits included in the twitter

    remove_digits = str.maketrans('', '', digits)
    text = text.translate(remove_digits)    
    textData.append(text)
    #print(tweet.text.encode('utf-8'))


# In[248]:

def preprocess_document(data):
    # Step 1: strip punctuation
    data = data.lower()
    punctuation = ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']'
    , '{', '}', '#', '\\','/','@','\xa0','\n','&','$','‘','…','•','-'] 
    for punc in punctuation:
        data = data.replace(punc, '')
        
    # Step 2: tokenize 
    data = list(nltk.word_tokenize(data))
    
    # Step 3: strip stopwords
    stop = set(stopwords.words('english'))
    extra_stopwords = ['ok', 'oh', 'via','bc','gon','na'] # add any additional stopwords we want to use here
    stop.update(extra_stopwords)
    stop.update(list(string.ascii_lowercase)) # remove all single letters
    data = [i for i in data if i not in stop] # remove stopwords and sort result
    
    # Step 4: stemming
    stemmer = snowballstemmer.stemmer('english') 
    data = stemmer.stemWords(data)
    
    # Step 5: remove words not in NLTK english corpus
    words = set(nltk.corpus.words.words())
     for w in data:
        if w not in words:
            data.remove(w)
    return data


# In[261]:

## Process the raw text data 
newData = []
for i in range(0, len(textData)):
    text = preprocess_document(textData[i])
    newData.append(text)


# In[273]:

## Calculate the word frecency, get the top 50
fdist = nltk.FreqDist(sum(newData,[]))
fdist.most_common(50) 


# ## TF-IDF
# #### TF-IDF weights words based on two factors: term frequency increases the score based on how often the term appears in the given document, while inverse document frequency decreases the score of terms occur very often in the corpus

# In[259]:

## Vectorize using term frequency-inverse document frequency (TF-IDF)
tfidf_vect = TfidfVectorizer(tokenizer=preprocess_document) 
textVect = tfidf_vect.fit_transform(textData) 
featVect = tfidf_vect.get_feature_names()

