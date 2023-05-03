import sys
a = int
c=[]
while a!=0:
 a,b = map(int,sys.stdin.readline().split())
 d=(a+b)
 c.append(d)
c.pop()
for i in c:
 print(i)