import jieba
sentence = "我喜欢上海东方明珠"
# entire mining
w1 = jieba.cut(sentence, cut_all=True)
for item in w1:
    print(item)
    
#precise mining(default mode in jieba)
print("")
w2 = jieba.cut(sentence, cut_all=False)
for item in w2:
    print(item)
    
#search engine mining
print("")
w3 = jieba.cut_for_search(sentence)
for item in w3:
    print(item)

# part of speech
print("")
import jieba.posseg
w5 = jieba.posseg.cut(sentence)
#flag 词性
#word 词语
for item in w5:
    print(item.word+"------"+item.flag)

#add new dict: jieba.load_userdict("")
'''   
# alter word frequency
print("")
sentence = "我喜欢上海东方明珠"
w7 = jieba.cut(sentence)
for item in w7:
    print(item)
print("-----after adding words-------")
jieba.suggest_freq("上海东方"，True)
w8 = jieba.cut(sentence)
for item in w8:
    print(item)
'''
# return high frequency word
import jieba.analyse
tags = jieba.analyse.extract_tags(sentence, 3)
print(tags)

# return word location
print()
w9 = jieba.tokenize(sentence)
for item in w9:
    print(item)
w10 = jieba.tokenize(sentence, mode = "search")
for item in w10:
    print(item)

# analyze one passage
print("--------------analyze one passage-----------------")
data = open("C:/Users/Administrator/Desktop/血尸.txt").read()
tag = jieba.analyse.extract_tags(data)
print(tag)

print("--------------analyze one novel: 盗墓笔记-----------------")
# how to encode
# approach 1
#data = open("C:/Users/Administrator/Desktop/盗墓笔记.txt", "r", encoding = "utf-8").read()

#approach 2: place novel in phpstudy's www folder
#import urllib.request
#data = urllib.request.urlopen("http://127.0.0.1/盗墓笔记.html").read().decode("utf-8", "ignore")
# tag = jieba.analyse.extract_tags(data)

#approach 3
data = open("C:/Users/Administrator/Desktop/daomubiji.txt", "r", encoding = "utf-8").read()
tag = jieba.analyse.extract_tags(data)
print(tag)
