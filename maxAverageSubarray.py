"""
You are given an integer array nums consisting of n elements
and an integer k.

Find a contiguous subarray whose length is equal to k that
has the maximum average value and return this value. Any
answer with a calculation error less than 10-5 will be accepted.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currSum = maxSum = sum(nums[0:k])
        numsLen = len(nums)
        
        for n in range(k,numsLen):
            currSum -= nums[n-k]
            currSum += nums[n]
            
            maxSum = max(currSum, maxSum)
        
        return maxSum/k

            