n=int(input())
m=int(input())
arr=list(map(int,input().split(" ")))
l=arr
for i in range(m):
    l=arr.insert(0,arr[-1])
    l=arr.pop(arr[-1])
print(arr)
