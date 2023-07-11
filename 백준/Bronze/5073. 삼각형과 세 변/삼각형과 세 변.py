while True:
 a, b, c=map(int,input().split())
 if a==b==c==0:
       break
 if (a+b+c-max(a,b,c))>max(a,b,c):
   if a==b==c:
        print("Equilateral")
   elif b==a or a==c or b==c:
       print("Isosceles")
   elif b!=a and a!=c and b!=c:
         print("Scalene")
  
 else:
        print("Invalid")