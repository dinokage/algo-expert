coins=list(map(int, input().split()))
def solution(coins):
    coins.sort()
    maxChange=0
    for i in coins:
        if maxChange+1 >=i:
            maxChange+=i
        else:
            return maxChange+1
    return (maxChange+1)
print(solution(coins))
