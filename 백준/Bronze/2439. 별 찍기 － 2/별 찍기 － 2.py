import sys
c = int(sys.stdin.readline())
a=reversed(range(c))
y=0
for e in a:
 y=y+1
 if y!=c:
  print((" ")*(e-1),"*"*(y))
  
  
 else:
  print("*"*(y))