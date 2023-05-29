import sys
a = int(sys.stdin.readline())
sum=1
list=[]
for i in range(a):
 sum= sum+ (6*i)
 
 if sum<a:
   list.append(sum)
 else:
   break
print(len(list)+1)