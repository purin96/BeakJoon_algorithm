ara=[]
a = int(input())

for b ,c in enumerate(range(a)):
  b, c = map(int,(input().split()))
  d= b+c
  ara.append(d)
for i in ara:
  print(i)