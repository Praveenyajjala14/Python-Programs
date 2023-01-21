##n=364782
##m=str(n)
##sum=0
##for i in range(len(m)):
##    print(i)
##    sum=sum+int(m[i])
##print(sum)

##n=int(input())
##sum1=1
##for i in range(2,n+1):
##    sum1=sum1+((1**i)/i)
##print(round(sum1,2))

##n=input()
##n=list(n)
##print(n[::-1])


##n=input()
##b=int(n,8)
##print(b)
##b=bin(b)
##print(b)
##
####def ispalindrome(x):
####    pal_num = str(x)
####
####    while len(pal_num)>1:
####        head = pal_num[0]
####        tail = pal_num[-1]
####        pal_num = pal_num[1:-1]
####
####        if head!=tail:
####            return False
####    return True
##
##
##n=int(input())
##while(n//2):
##n=38
##sum=0
##m=str(n)
##while(n>9):
##    for i in range(len(m)):
##        sum=sum+int(m[i])
##        n=sum
##print(n)
##    if(2**n == n):
##        print("True")
##        break
##print("False")


##n=int(input())
##b=format(n,"b")
##r=b[::-1]
##d=int(r,2)
##print(d)

##n=int(input())
##arr=[]
##for i in range(n):
##    arr.append(map(int,input().split()))
##    value=0
##    for x in range(0,n):
##        value+=arr[x][x]
##        value-=arr[x][n-1-x]
##    print(abs(value))

##n=int(input())
##a=list(map(int,input().split()))
##count=0
##for i in range(0,n-2):
##    for j in range(2,n):
##        if(a[i]%2==0 and a[j]%2==0 and a[i+1]%2==0):
##            count+=1
##            i+=1
##            j+=1
##print(count)


##n=int(input())
##a=list(map(int,input().split()))
##count=0
##for i in range(0,n-2):
##    for j in range(2,n):
##        if(a[i]%2!=0 and a[j]%2!=0 and a[i+1]%2==0):
##            count+=1
##            i+=1
##            j+=1
##print(count)

##num=int(input())
##count=0
##s=0
##for i in range(2,num+1):
##    rem=i%10
##    s+=rem
##    i=i//10
##if(s%2==0):
##    count+=1
##print(count)




t=int(input())
for n,m in range(t):
    n,m=map(int,input().split())
    if(n>m):
        print("SECOND")
    elif(n==m):
        print("ANY")
    else:
        print("FIRST")






