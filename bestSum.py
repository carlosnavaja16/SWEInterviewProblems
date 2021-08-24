memo = {}

def bestSum(target, nums) -> list[int]:

    if target in memo: return memo[target]
    if target == 0: return []
    if target <= 0: return None

    shortestList = None

    for n in nums:
        remainder = target - n
        remainderResult = bestSum(remainder, nums)
        
        if remainderResult is not None:
            remainderResult.append(n)
            if shortestList is None or len(remainderResult) < len(shortestList):
                shortestList = remainderResult
        
    shortestList
    return shortestList

print(bestSum(8, [1,4,5]))
"""
print(bestSum(7, [2,3]))
print(bestSum(7, [2,4]))
print(bestSum(8, [2,3,5]))
print(bestSum(300, [7,14]))
"""