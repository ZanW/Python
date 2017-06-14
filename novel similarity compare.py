#similarity calculation
#steps:
#1 read file
#2 separate words in the file
#3 set file to certain format in order to handle easily later
#4 attain the frequency of word
#5 filter the words with low frequency
#6 build dictionary with corpora
#7 load text file intended to compare
#8 change intended compared text file into sparse vector via doc2boe
#9 further handle the sparse vector to have a new corpora
#10 handle new corpora with tfidf model to gain tfidf
#11 get feature number via token2id
#12 calculate similarity of sparse matrix, in order to build index
#13 obtain the final similairy results

from gensim import corpora, models, similarities
import jieba
from collections import defaultdict
import urllib.request

#1 read file
d1 = urllib.request.urlopen("http://127.0.0.1/ljm.html").read().decode("utf-8","ignore")
d2 = urllib.request.urlopen("http://127.0.0.1/gcd.html").read().decode("utf-8","ignore")

#2 separate words in the file
data1 = jieba.cut(d1)
data2 = jieba.cut(d2)

#3 set file to certain format in order to handle easily later
data11 = ""
for item in data1:
    data11 += item + " "
data21 = ""
for item in data2:
    data21 += item + " "
documents = [data11, data21]
texts = [[word for word in document.split()] for document in documents] # note that texts has 2 dimensions.

#4 attain the frequency of word
# defaultdict: dict subclass that calls a factory function to supply missing values, can return value without key: https://docs.python.org/2/library/collections.html#collections.defaultdict
frequency = defaultdict(int) 
for text in texts:
    for token in text:
        frequency[token] += 1

#5 filter the words with low frequency, filter word with frequency smaller than 3
filtered = [[word for word in text if frequency[token] > 3] for text in texts]

#6 build dictionary with corpora and save
dictionary = corpora.Dictionary(texts)
dictionary.save("C:/Users/Administrator/Desktop/text similarity test/newDicforNovel.txt")

#7 load text file intended to compare
d3 = urllib.request.urlopen("http://127.0.0.1/dmbj.html").read().decode("utf-8","ignore")
data3 = jieba.cut(d3)
data31 = ""
for item in data3:
    data31 += item+" "
#data31 = [data31]

#8 change intended compared text file into sparse vector via doc2boe
new_doc = data31
new_vec = dictionary.doc2bow(new_doc.split()) # bulid sparce vector
# corpora.dictionary.doc2bow: Convert document (a list of words) into the bag-of-words format = list of (token_id, token_count) 2-tuples. Each word is assumed to be a tokenized and normalized string (either unicode or utf8-encoded). No further preprocessing is done on the words in document; apply tokenization, stemming etc. before calling this method.

#9 further handle the sparse vector to have a new corpora
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize("C:/Users/Administrator/Desktop/text similarity test/deerwester.mm",corpus)
#10 handle new corpora with tfidf model to gain tfidf
tfidf = models.TfidfModel(corpus)

#11 get feature number via token2id, actually it is just the number of keys
featureNum = len(dictionary.token2id.keys()) 

#12 calculate similarity of sparse matrix, in order to build index
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = featureNum)
sim = index[tfidf[new_vec]]
print(sim)
