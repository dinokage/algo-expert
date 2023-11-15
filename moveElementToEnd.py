def inputArray():
    return list(map(int, input().split()))
def solution(array, toMove):
    array.sort(key = lambda x: x==toMove)
    return array
array=inputArray()
toMove = int(input())
print(solution(array, toMove))
