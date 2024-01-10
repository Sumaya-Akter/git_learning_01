#n,m=tuple(map(int,input().split()))

n,m=list(map(int,input().split()))

#print(n,m)

arr=list(map(int,input().split()))

A=set(map(int,input().split()))
B=set(map(int,input().split()))

hapiness=0

for x in arr:
    if x in A:
        hapiness+=1
    elif x in B:
        hapiness-=1

print(hapiness)

#fruits = ("apple", "banana", "cherry")
#more_fruits = ["orange", "kiwi", "melon", "mango"]

# fruits and more_fruits are unpacked and then their elements are packed into combined_fruits
#combined_fruits = *fruits, *more_fruits

#print(combined_fruits)