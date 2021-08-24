memo = {}

def canSum(target, nums):

    if (target,tuple(nums)) in memo:
        return memo[(target,tuple(nums))]
    if target == 0:
        return True
    if target < 0:
        return False    
    for n in nums:
        memo[target,tuple(nums)] = canSum(target - n,nums)
        if memo[(target,tuple(nums))]:
            return True
    
    return False

print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))