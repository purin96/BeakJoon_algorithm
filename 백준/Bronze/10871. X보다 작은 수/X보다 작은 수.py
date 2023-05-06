a,b = map(int, input().split())
l = list(map(int, input().split()))
c=[]
for i in l:
 if b>i:
    c.append(i)
for i in c:
 print(i,end=" ")