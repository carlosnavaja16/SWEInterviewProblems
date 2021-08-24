
memo = {}
sumList = []
def howSum(target, nums) -> list[int]:

    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    
    for n in nums:
        remainder = target - n
        remainderResult = howSum(remainder,nums)
        if remainderResult is not None:
            remainderResult.append(n)
            memo[remainder] = remainderResult
            return memo[remainder]
    memo[target] = None
    return None

print(howSum(600, [3,4,5]))
"""
print(howSum(7, [2,3]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7,14]))
"""