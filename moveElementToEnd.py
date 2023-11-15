def inputArray():
    return list(map(int, input().split()))
def solution(array, toMove):
    array.sort(key = lambda x: x==toMove)
    return array
def optimized_solution(array, toMove):
    begin=0
    end=len(array)-1
    while begin<end:
        while array[begin]!=toMove and begin<end:
            begin+=1
        while array[end]==toMove and begin<end:
            end -=1
        array[begin], array[end] = array[end], array[begin]
        begin+=1
        end-=1
    return array
array=inputArray()
toMove = int(input())
print(solution(array, toMove))
print(optimized_solution(array, toMove))
