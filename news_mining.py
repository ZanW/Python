
# coding: utf-8

# In[145]:

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
    
    
    
    #print(tweet.text.encode('utf-8').decode(‘utf-8’))


# In[147]:

docker[0].timestamp


# In[148]:

time # docker[0].timestamp = time[0] ?


# In[149]:

type(docker[0].timestamp.timetuple()[5])


# In[150]:

# compare timestamp in docker(compare min first, sec second)
for i in range(len(docker)):
    for j in range(i + 1, len(docker)):
        if docker[i].timestamp.timetuple()[4] < docker[j].timestamp.timetuple()[4]:
            temp = docker[i] 
            docker[i] = docker[j]
            docker[j] = temp
        elif (docker[i].timestamp.timetuple()[5] == docker[j].timestamp.timetuple()[5]) and (docker[i].timestamp.timetuple()[5] < docker[j].timestamp.timetuple()[5]):
            temp = docker[i] 
            docker[i] = docker[j]
            docker[j] = temp


# In[151]:


# compare timestamp
#for i in range(len(time)):
#    for j in range(i + 1, len(time)):
#        if time[i].timetuple()[4] < time[j].timetuple()[4]:
#            temp = docker[i] 
#            docker[i] = docker[j]
#            docker[j] = temp


# In[152]:

# docker timestamp after sorting
time2 = []
for dockerTime in docker:
    time2.append(dockerTime.timestamp)


# In[153]:

time2


# In[156]:

for tweet2 in docker:
    text = tweet2.text.encode('utf-8').decode('utf-8')
    text = re.sub(r"http\s+","",text)
    testdata = text.encode('utf-8')
    print(testdata)


# In[ ]:



