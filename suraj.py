def array():
    array=list(map(int,input("enter the numbers:").split()))
    array.sort()
    return array
def find_positon(array):
    n=int(input("enter the number you want to find its position in the list:"))
    low=0
    mid=0
    high=int(len(array))-1
    if n in array:
        while n!=array[mid]:
            mid=int((low+high)/2)
            if n==array[mid]:
               break
            elif n>array[mid]:
                low=mid+1
            else:
                high=mid-1
    else:
        print("\nEntered Number is not in the list:")
        find_positon(array)
    return mid
array=array()
ans=find_positon(array)
print("Position is:",ans)
