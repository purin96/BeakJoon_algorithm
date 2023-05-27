import sys
import math
a,b,v = map(int,sys.stdin.readline().split())
if (v-a)/(a-b)==int:
    print(int((v-a)/(a-b)+1))
else:
    print(math.ceil((v-a)/(a-b)+1))