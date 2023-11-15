def inputArray():
    return list(map(int, input().split()))
def solution(arr1, arr2):
    res=[0, 0]
    minDiff=float('inf')
    for i in arr1:
        for j in arr2:
            if abs(i-j)==0:
                return [i,j]
            elif abs(i-j)<minDiff:
                minDiff=abs(i-j)
                res[0], res[1]=i, j
    return res
def optimized_solution(arr1, arr2):
    arr1.sort()
    arr2.sort()
    minDiff=float('inf')
    res=[0, 0]
    p1=p2=0
    while p1< len(arr1) and p2<len(arr2):
        if abs(arr1[p1]-arr2[p2])==0:
            return [arr1[p1], arr2[p2]]
        else:
            if minDiff > abs(arr1[p1]-arr2[p2]):
                minDiff = abs(arr1[p1]-arr2[p2])
                res[0], res[1] = arr1[p1], arr2[p2]
        if arr1[p1]<arr2[p2]:
            p1+=1
        else:
            p2+=1
    return res
arrayOne=inputArray()
arrayTwo=inputArray()
print(solution(arrayOne, arrayTwo))
print(optimized_solution(arrayOne, arrayTwo))

