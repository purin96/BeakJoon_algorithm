import sys
c = int(input())
for i in range(c):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")