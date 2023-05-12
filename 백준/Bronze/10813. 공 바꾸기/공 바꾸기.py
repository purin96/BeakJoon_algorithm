a,b = map(int,input().split())
list=[]
for i in range(a):
  list.append(i+1)
for i in range(b):
     c,d = map(int,input().split())
     e=c-1 
     f=d-1
     list[e],list[f] = list[f], list[e]
for i in list:
     print(i,end=" ")