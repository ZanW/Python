'''
a = [[1, 2, 3], [4, 5, 6]]
#print(a[0])
#print(a[1])
b = a[0]
#print(b)

#print(a[0][2])

a[0][1] = 6
print(a)
print(b)

b[2] = 9
print(a[0])
print(b)


a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()


n = 3
m = 4
a = [[0] * m] * n
print(a)
a[0][0] = 5
print(a)
'''
n = 3
m = 4
a = []
for i in range(n):
    a.append([0]*m)
    print(a)

b = [[0]*m for i in range(n)]
print(b)

for i in range(n):
    a[i] = [0] * m
print(a)

a = [0]*n
print(a)



