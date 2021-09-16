class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        numsLen = len(nums)
        closest = 0
        minDelta = 10000
        
        for i in range(numsLen - 2):

            left = i + 1
            right = numsLen - 1
        
            
            while left < right:
                
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == target:
                    return target
                
                elif sum > target:
                    if abs(target - sum) < minDelta:
                        minDelta = abs(target - sum)
                        closest = sum
                    right -= 1
                else:
                    if abs(target - sum) < minDelta:
                        minDelta = abs(target - sum)
                        closest = sum
                    left += 1
            
        return closest
                    
                
