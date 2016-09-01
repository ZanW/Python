'''
Created on Aug 22, 2016

@author: Administrator
'''
# this program finds a magic number

'''
another way to comment
'''
name = "john"
print("buck " + name) # "+" is used to connect two values with the same type
print(5, "buck") # use "," to connect two values of different types


magicnumber = 10

for n in range(20):
    if n is magicnumber:
        print("I find the magicnumber", n)
        break
    else:
        print(n)
        
for n in range(100 , 201):
    while (n % 4 == 0):
        print(n, "is a multiple of 4")
        break