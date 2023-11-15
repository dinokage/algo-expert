inputArray=list(map(int, input().split()))
target=int(input())
def solution(array, targetSum):
    array.sort()
    res=[]
    n=len(array)
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                if array[a]+array[b]+array[c]==targetSum:
                    res.append([array[a],array[b],array[c]])
    return res
def optimized_solution(array, targetSum):
    array.sort()
    res=[]
    for current in range(len(array)-2):
        left=current+1
        right=len(array)-1
        while left<right:
            val=array[current]+array[left]+array[right]
            if val==targetSum:
                res.append([array[current], array[left], array[right]])
                left+=1
                right-=1
            elif val<targetSum:
                left+=1
            else:
                right-=1
    return res
print(solution(inputArray, target))
print(optimized_solution(inputArray, target))
