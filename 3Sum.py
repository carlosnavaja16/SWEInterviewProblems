class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        triplets = []
        
        triplesMap = {}
        
        for i in range(len(nums)-2):
            
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    triple = (nums[i],nums[left],nums[right])
                    if triple not in triplesMap:
                        triplesMap[triple] = 1
                        triplet = [nums[i],nums[left],nums[right]]
                        triplets.append(triplet)
                    right -= 1
                    left += 1
        
        return triplets
