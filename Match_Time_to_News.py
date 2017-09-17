

from twitterscraper import query_tweets
import re
import nltk
from string import digits
from datetime import datetime



docker = []
for tweet in query_tweets("bitcoin", 20)[:40]:
    docker.append(tweet)
    text = tweet.text.encode('utf-8').decode('utf-8')
    text = re.sub(r"http\s+","",text)
    testdata = text.encode('utf-8')
    time.append(tweet.timestamp)



# compare timestamp in docker(compare min firstly, sec secondly), sorted in descending order
for i in range(len(docker)):
    for j in range(i + 1, len(docker)):
        if docker[i].timestamp.timetuple()[4] < docker[j].timestamp.timetuple()[4]:
            temp = docker[i] 
            docker[i] = docker[j]
            docker[j] = temp
        elif (docker[i].timestamp.timetuple()[4] == docker[j].timestamp.timetuple()[4]) and (docker[i].timestamp.timetuple()[5] < docker[j].timestamp.timetuple()[5]):
            temp = docker[i] 
            docker[i] = docker[j]
            docker[j] = temp


timeStr = [[] for l in range(len(docker))]
# for i in range(len(locker)):
# get year,month, divide by "/"
# get hour,minute,second, divide by ":"
for i in range(len(docker)):
    for j in range(6):
        timeStr[i].append(str(docker[i].timestamp.timetuple()[j]))
        if j <= 2:
            timeStr[i].append("/")
        elif j != 5:
            timeStr[i].append(":")
        else: break


temp = []
for i in range(len(docker)):
    temp.append(''.join(timeStr[i]))


TupleList = []
for i in range(len(docker)):
    TupleList.append((temp[i],docker[i].text.encode('utf-8')))



assort = dict()
for i in range(len(TupleList)): # Num of Touplist equals that of dockers
    if TupleList[i][0] in assort:
        assort[TupleList[i][0]].append(TupleList[i][1])
    else:
        assort[TupleList[i][0]] = [TupleList[i][1]] # [TupleList[i][1]] here guarantees one key gives one list


