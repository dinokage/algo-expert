array=list(map(int, input().split()))
sequence = list(map(int, input().split()))
def solution(array, sequence):
    pos = 0
    for i in array:
        if i == sequence[pos]:
            pos+=1
        if pos == len(sequence):
            return True
    return False        
print(solution(array, sequence))
