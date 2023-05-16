a= int(input())
d=[]
for i in range(a):
 e=input()
 f=e[0],e[-1]
 d.append(f)
for i in d:
  print(*i,sep="")