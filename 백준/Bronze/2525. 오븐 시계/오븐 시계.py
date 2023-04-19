a, b = map(int, input().split())
c = int(input())
d=(a*60+b+c)//60
if d<24:
    print((a*60+b+c)//60,(a*60+b+c)%60)
else:
    print(d-24, (a*60+b+c)%60)