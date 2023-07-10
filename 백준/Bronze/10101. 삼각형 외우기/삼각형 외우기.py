a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
if a==b==c==60:
        print("Equilateral")
elif sum==180:
      if a==b:
            print("Isosceles")
      elif b==c:
            print("Isosceles")
      elif a==c:
            print("Isosceles")
      else:
            print("Scalene")
else:
        print("Error")