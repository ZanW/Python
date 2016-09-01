'''
Created on Aug 24, 2016

@author: Administrator
'''
def get_gender(sex = "unknown"):
    if sex is "m":
        print("male")
    elif sex is "f":
        print("female")
    else:
        print(sex)
        
get_gender("f")
get_gender("u")
get_gender("m")
get_gender()