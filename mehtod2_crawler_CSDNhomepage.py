# this application crawls all blogs on home page of http://blog.csdn.net/ using method 2

import urllib.request
import re

url = "http://blog.csdn.net/"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0")
opener = urllib.request.bulid_opener()
opener.addheaders = [headers]
data = opener.open().read().decode("utf-8","ignore")
