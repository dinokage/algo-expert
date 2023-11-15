import unittest
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
class TestSolution(unittest.TestCase):
    def test_one(self):
        result = optimized_solution([-1,5,10,20,28,3], [26,134,135,15,17])
        self.assertEqual(result, [28,26])
    def test_two(self):
        result = optimized_solution([-1,5,10,20,3],[26,134,135,15,17])
        self.assertEqual(result, [20,17])
    def test_three(self):
        result = optimized_solution([10,0,20,25],[1005,1006,1014,1032,1031])
        self.assertEqual(result, [25,1005])
    def test_four(self):
        result=optimized_solution([10,1000,9124,2142,59,24,596,591,124,-123],[-1441,-124,-25,1014,1500,660,410,245,530])
        self.assertEqual(result, [-123,-124])
