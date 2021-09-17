class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        
        numsLen = len(nums)
        quadruples = {}
        quadruplets = []
        
        if len(nums) < 4:
            return []
        
        else:
            for i in range(numsLen - 3):
                for j in range(i + 1, numsLen-2):
                    left = j + 1
                    right = numsLen - 1
                    while left < right:
                        sum = nums[i] + nums[j] + nums[left] + nums[right]
                        if sum == target:
                            quadruple  = (nums[i],nums[j],nums[left],nums[right])
                            quadruplet = [nums[i],nums[j],nums[left],nums[right]]
                            if quadruple not in quadruples:
                                quadruples[quadruple] = 1
                                quadruplets.append(quadruplet)
                            left += 1
                            right -= 1
                        elif sum > target:
                            right -= 1
                        else:
                            left += 1
        
        return quadruplets