import sys
a,b,c = map(int,sys.stdin.readline().split())
listt=[]
listt.append(a)
listt.append(b)
listt.append(c)
listt.sort()
if a==b==c:
    print(a+b+c)
else:
 if listt[2]<listt[1]+listt[0]:
   print(a+b+c)
 else:
  print(listt[1]+listt[0]-1+listt[1]+listt[0])
