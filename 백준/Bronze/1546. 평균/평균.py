import sys
a=int(input())
data = list(map(int,sys.stdin.readline().split()))
b=max(data)
new_data=[]
for i in data:
    c=i/b*100
    new_data.append(c)
result=sum(new_data)/len(new_data)

print(round(result,15))