
# coding: utf-8

# In[2]:

from twitterscraper import query_tweets
import re
import nltk
from string import digits
from datetime import datetime


# In[146]:

time = []
# docker to store results of query_tweets for one search
docker = []
for tweet in query_tweets("bitcoin", 20)[:40]:
    docker.append(tweet)
    text = tweet.text.encode('utf-8').decode('utf-8')
    text = re.sub(r"http\s+","",text)
    testdata = text.encode('utf-8')
    time.append(tweet.timestamp)


# In[3]:

docker[0].timestamp


# In[4]:

time # docker[0].timestamp = time[0] ?


# In[5]:

type(docker[0].timestamp.timetuple()[5])


# In[6]:

# compare timestamp in docker(compare min first, sec second)
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


# In[7]:

time2 = []
for dockerTime in docker:
    time2.append(dockerTime.timestamp)


# In[8]:

time2


# In[9]:

for tweet2 in docker:
    text = tweet2.text.encode('utf-8').decode()
    #text = re.sub(r"http\s+","",text)
    testdata = text
    print(testdata)


# In[10]:

list = [[[] for j in range(5)] for i in range(3)]


# In[41]:

timeStr = [[] for l in range(len(docker))]
#for i in range(len(locker)):
 # get year,month,hour,minute,second
# divide elements by "/"

for i in range(len(docker)):
    for j in range(6):
        timeStr[i].append(str(docker[i].timestamp.timetuple()[j]))
        if j <= 2:
            timeStr[i].append("/")
        elif j != 5:
            timeStr[i].append(":")
        else: break
        


# In[42]:

timeStr


# In[43]:

''.join(timeStr[i])


# In[44]:

temp = []
for i in range(len(docker)):
    temp.append(''.join(timeStr[i]))


# In[45]:

for i in range(len(docker)):
    for j in range():
        timeStr[i]


# In[ ]:

list = [[] f]

