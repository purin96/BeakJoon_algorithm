a=int(input())
b=int(input())
sum=0
for c ,d in enumerate(range(1,b+1)):
      c, d = map(int, input().split())
      sum = sum+ c*d
if sum == a:
   print("Yes")
else:
   print("No")