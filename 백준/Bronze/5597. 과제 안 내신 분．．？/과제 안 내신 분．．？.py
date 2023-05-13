b,a=[],[]
for i in range(28):
    i=input()
    b.append(i)
c=list(map(int,b))
for i in range(1,31):
  a.append(i)
e=list(set(a)-set(c))
e.sort()
for i in e:
 print(i,end=" ")