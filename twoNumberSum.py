array=list(map(int, input().split()))
targetSum=int(input())
def solution1(array, targetSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j]==targetSum:
                return [array[i], array[j]]
    return []

print(solution1(array, targetSum))
