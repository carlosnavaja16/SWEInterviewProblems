"""
Given an array of integers nums and an integer target
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


nums = [3,2,4]
target = 6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsSorted = sorted(nums)

        p1 = 0
        p2 = len(numsSorted) -1
        
        found = False

        while not found:
            if numsSorted[p1] + numsSorted[p2] > target:
                p2 -= 1
            elif numsSorted[p1] + numsSorted[p2] < target:
                p1 += 1
            else:
                found = True

        i1 = nums.index(numsSorted[p1])
        i2 = nums.index(numsSorted[p2])

        indices = [i1, i2]
        
        return indices