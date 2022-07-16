
def tree(tree_list,key):
    low=1 #최소높이
    high = max(tree_list) # 최대높이
    mid = (low+high)//2
    while low<=high:
        sum = 0
        for i in tree_list:
            if (i-mid)>0: # 나무를 잘랐을때 길이가 양수여야..
                sum+=(i-mid)

        if sum>=key: # 자른 나무의 합이 key보다 크거나 같으면 low값 수정
            low=mid+1

        else:
            high=mid-1
        mid = (low+high)//2
    return mid #low가 high보다 커질때의 mid값이 최댓값이 된다.

if __name__ =="__main__":
    count, key = map(int,input().split())
    tree_list = list(map(int,input().split()))
    print(tree(tree_list,key))

