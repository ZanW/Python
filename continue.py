'''
Created on Aug 23, 2016

@author: Administrator
'''

numbertaken = [3, 6, 8, 11, 15, 19]
print("the number has not been taken yet: ")
"\n"
for n in range(0, 20):
    if n in numbertaken:
        continue
    else:
        print(n)
