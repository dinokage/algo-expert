def solution1(arr):
    increase = True
    decrease = True
    for i in range(1, len(arr)):
        if arr[i-1]<arr[i]:
            decrease=False
        if arr[i-1]>arr[i]:
            increase=False
    return increase or decrease
def solution2(arr):
    if len(arr) <= 2:
        return True
    flag = None
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            flag = arr[i-1] < arr[i] #equal starting elements are skipped
            break

    if flag is None:
        return True  # all elements are equal

    for j in range(i + 1, len(arr)):
        if (arr[j-1] < arr[j]) != flag and arr[j-1] != arr[j]:
            return False

    return True

array=list(map(int, input().split()))
print(solution2(array))