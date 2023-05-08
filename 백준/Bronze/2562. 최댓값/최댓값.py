c=[]
for i in range(0,9):
     a= int(input())
     c.append(a)
b=max(c)     
print(max(c))
print(c.index(b)+1)