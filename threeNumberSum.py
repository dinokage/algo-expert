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
print(solution(inputArray, target))
