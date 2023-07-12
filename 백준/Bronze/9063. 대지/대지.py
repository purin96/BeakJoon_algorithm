list=[]
n= int(input())
for i in range(n): 
 a, b =map(int,input().split())
 list.append(a)
 list.append(b)
c=int(max(list[0::2]))-min(list[0::2])
d=int(max(list[1::2]))-min(list[1::2])
print(c*d)
