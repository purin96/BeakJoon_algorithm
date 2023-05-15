b=[]
for i in range(10):
    c=int(input())
    a=c%42
    b.append(a)
print(len(list(set(b))))
