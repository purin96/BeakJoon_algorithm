import sys
a,b = map(int,sys.stdin.readline().split())
list=[]
for i in range(a):
    i=0
    list.append(i)

for i in range(b):
    c,d,e = map(int,sys.stdin.readline().split())
    for i in range(c-1,d):
       list[i]=e
for i in list:
    print(i, end=" ")