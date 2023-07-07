import sys
a=int(input())
sum=3
i=1
for i in range(1,a):
 sum=(2*sum-1)
 i+=1
print(sum**2)