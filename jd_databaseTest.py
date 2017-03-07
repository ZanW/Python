import pymysql

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test")
title = "title1"
shopLink = "shopLink1"
shop = "shop1"
price = "price1"
rate = "rate1"
 #sql = "insert into books(title, link, comment) values('" + title + "','" + link + "','" + comment + "')"
sql = "insert into jd(title, shop, shopLink, price, rate) values ('"+title+"','"+shop+"','"+shopLink+"','"+price+"','"+rate+"')"
result = conn.query(sql)
print(result)
