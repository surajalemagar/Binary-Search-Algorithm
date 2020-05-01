array=list(map(int,input().split()))
array.sort()
print(array)
n=int(input("enter the number you want to find its position in the list:"))
low=0
mid=0
high=int(len(array))-1
if n in array:
    while n!=array[mid]:
        mid=int((low+high)/2)
        if n==array[mid]:
            print("position is:",mid)
        elif n>array[mid]:
            low=mid+1
        else:
            high=mid-1
else:
    print("Entered Number is not in the list:")
    