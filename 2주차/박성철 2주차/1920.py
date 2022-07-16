def bin_search(nums,key):
    left = 0
    right = len(nums)-1
    mid = (left + right)//2

    while left <= right:
        if nums[mid] <key :
            left = mid+1
            mid=(left+right)//2
        elif nums[mid]>key:
            right = mid -1
            mid = (left+right)//2
        else :
            break
    if nums[mid]==key:
        return 1
    else:
        return 0

if __name__ =="__main__":
    n= int(input())
    a= list(map(int,input().split()))
    a = sorted(a)

    m=int(input())
    b=list(map(int,input().split()))

    for i in range(m):
        print(bin_search(a,b[i]))

