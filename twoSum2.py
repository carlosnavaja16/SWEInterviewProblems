from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        print(hashmap.__str__())    
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                print('['+str(i)+','+str(hashmap[complement])+']')
#                return [i, hashmap[complement]]

s = Solution()

nums = [3.3]
target =6

s.twoSum(nums,target)