##pattern1

##n=int(input())
##for i in range(0,n):
##    for j in range(0,n):
##        print("*",end=' ')
##    print()

##pattern2

##n=int(input())
##for i in range(0,n):
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()

#pattern3

##n=int(input())
##for i in range(0,n): #,0,1,2,3,4
##    for j in range(n,i,-1): #4:5,4,3,2,1
##        print("*",end=" ")
##    print()

#pattern4

##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        print(j,end=" ")
##    print()

#pattern5

n=int(input())
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print("")
    k=k-2
