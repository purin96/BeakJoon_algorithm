a=int(input())
list=[]
for i in range(1,a+1):
 b=int(input())
 if b==0:
  list.pop()
 else:
  list.append(b)
print(sum(list))