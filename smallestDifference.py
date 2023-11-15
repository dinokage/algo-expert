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
arrayOne=inputArray()
arrayTwo=inputArray()
print(solution(arrayOne, arrayTwo))


