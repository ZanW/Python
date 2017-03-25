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
#11 get characteristic number via token2id
#12 calculate similarity of sparse matrix, in order to build index
#13 obtain the final similairy results

from gensim import corpora, models, similarities
import jieba
from collections import defaultdict

#1 read file
doc1 = "C:/Users/Administrator/Desktop/text similarity test/d1.txt"
doc2 = "C:/Users/Administrator/Desktop/text similarity test/d2.txt"
d1 = open(doc1).read()
d2 = open(doc2).read()

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
texts = [[word for word in document.split()] for document in documents] # note that texts has tow dimensions.

#4 attain the frequency of word
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
        
