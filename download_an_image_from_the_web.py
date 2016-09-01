'''
Created on Aug 27, 2016

@author: Administrator
'''

import random
import urllib.request

def down_load_image(url):
    number = random.randrange(1, 5)
    full_name = str(number) + '.jpg'
    urllib.request.urlretrieve(url, full_name)
    print('download completed')
    
down_load_image("http://www.sinaimg.cn/dy/slidenews/4_img/2015_21/704_1633863_171372.jpg")