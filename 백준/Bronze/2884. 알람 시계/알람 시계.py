a, b = map(int, input().split())
x = b-45
if x<0:
    x+=60
    a -=1
    if a<0:
     a+=24
print(a,x)