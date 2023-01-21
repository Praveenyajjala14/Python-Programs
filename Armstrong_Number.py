n=int(input())
order=len(str(n))
sum=0
temp=n
while(temp>0):
    rem=temp%10
    sum+=rem**order
    temp=temp//10
if(n==sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
