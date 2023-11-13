array=list(map(int, input().split()))
def solution(array):
    ans=[0 for _ in array]
    small=0
    large=len(array)-1
    for i in reversed(range(len(array))):
        smallValue=abs(array[small])
        largeValue=abs(array[large])
        if smallValue > largeValue:
            ans[i]=smallValue**2
            small+=1
        else:
            ans[i]=largeValue**2
            large-=1
    return ans
print(solution(array))

