import urllib.request
# -> using urlretrieve(), urlcleanup(), info(),getcode(),geturl()

# data = urllib.request.urlretrieve("http://www.baidu.com", filename = "C:/Users/Administrator/Desktop/baidu.html")

# urllib.request.urlcleanup()

# fp = urllib.request.urlopen("http://www.baidu.com")
# fp.info()

# for getcode(), return 200 indicates right, 403 indicates abnormity
#data1= fp.getcode()
#print(data1)

#data2 = fp.geturl()
#print(data2)

# usting timeout()
# urllib.request.urlopen("http://www.baidu.com", timeout = 1) 

for i in range(1, 30):
    try:
        urllib.request.urlopen("http://www.baidu.com", timeout = 0.5)
    except Exception as e:
        print("abnormality happens: " +str(e))
