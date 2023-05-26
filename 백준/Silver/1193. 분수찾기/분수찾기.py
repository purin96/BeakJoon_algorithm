a=int(input())
sum=0
num=1
while sum<a:
    sum=sum+num
    num=num+1
aa=num-1
bb=sum
cc=a-(sum-num+1)
if aa%2==0:
    print(f"{cc}/{aa-cc+1}")
else:
    print(f"{aa-cc+1}/{cc}")