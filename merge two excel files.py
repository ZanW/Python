global i
i = 0
f1 = open("C:/Users/Administrator/Desktop/py assignment/1.xlsx", "w")
f2 = open("C:/Users/Administrator/Desktop/py assignment/2.xlsx", "w")

while (i <= 6):
    len1 = f1.readline()
    if len(len1)== 0:
        f1.write("star")
        i = i +1

R1 = f1.readline()
while True:
    len2 = f2.readline()
    if len(len2)== 0:
        f2.write(R1)
        length = len(f1)-1
        if(length == 0):
            break

f1.close()
f2.close()
