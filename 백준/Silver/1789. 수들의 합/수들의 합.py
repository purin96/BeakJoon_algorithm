import sys
a = int(sys.stdin.readline())
sum=0
i=1
list=[]
for i in range(a):
 sum= sum+ i
 
 if sum<=a:
   list.append(sum)
 else:
    break
if a in list:
 print(len(list)-1)
elif a==1:
 print(1)
else:
   print(len(list)-1)