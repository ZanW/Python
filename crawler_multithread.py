import re
import urllib.request
import threading
'''
header = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0")
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)
'''

class A(threading.Thread):
    def init(self):
        threading.Thread.init(self)
    def run(self):
        for i in range(1, 6, 2):
             url = "http://www.qiushibaike.com/8hr/page/"+ str(i)+ "/?s=4952764"
             req = urllib.request.Request(url)
             req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0")

            
             rg = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
             data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
             content = re.compile(rg, re.S).findall(data)
             print(content)
             for j in range(0, len(content)):
                print("--------crawling page "+str(i)+" content "+str(j)+" --------")
                datacont = content[j]
                print(datacont)

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(2, 7, 2):
            url = "http://www.qiushibaike.com/8hr/page/"+ str(i)+ "/?s=4952764"
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0")

            
            rg = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
            content = re.compile(rg, re.S).findall(data)
            print(content)
            for j in range(0, len(content)):
                print("--------crawling page "+str(i)+" content "+str(j)+" --------")
                datacont = content[j]
                print(datacont)

t1 = A()
t1.start()
t2 = B()
t2.start()

'''
for i in range(1, 2):
    url = "http://www.qiushibaike.com/8hr/page/"+ str(i)+ "/?s=4952764"
 
    

    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0")

    
    rg = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
    data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
    content = re.compile(rg, re.S).findall(data)
    print(content)
    for j in range(0, len(content)):
        print("--------crawling page "+str(i)+" content "+str(j)+" --------")
        datacont = content[j]
        print(datacont)
'''
