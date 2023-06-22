list=[]
x, y, w, h = map(int, input().split())
x=int(x)
y=int(y)
w=int(w)
h=int(h)
a=h-y
b=w-x
list.append(x)
list.append(y)
list.append(w)
list.append(h)
list.append(a)
list.append(b)
print(min(list))