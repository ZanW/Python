# inverse output of mutiplication formula table

a = [9,8,7,6,5,4,3,2,1]
for i in a:
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j)+" ", end = "")
    print()
