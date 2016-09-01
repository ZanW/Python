'''
Created on Aug 26, 2016

@author: Administrator
'''



def add_number(*args):
    total = 0
    for a in args:
        total += a
    print(total)
    
add_number(1)

add_number(1, 2, 3)

add_number(234, 23423, 5435, 45345,  545654)