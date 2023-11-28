def spiralTraverse(array):
    ans =[]
    while array:
        ans.extend(array.pop(0)) # add first row to result and remove it
        array = list(zip(*array))[::-1] # transpose 
    return ans
print(spiralTraverse([[1,2,3],[4,5,6],[7,8,9]]))