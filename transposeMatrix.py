def matrixInput():
    rows=int(input())
    cols=int(input())
    matrix=[]
    for i in range(rows):
        row=list(map(int, input().split()))
        matrix.append(row)
    return matrix
def solution(matrix):
    res=[]
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        res.append(row)
    return res
input=matrixInput()
print(solution(input))
