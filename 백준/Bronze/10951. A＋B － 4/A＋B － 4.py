import sys
c=[]
while True:
 try:
  a,b = map(int,sys.stdin.readline().split())
  c.append(a+b)
 except:
  break
for i in c:
 print(i)