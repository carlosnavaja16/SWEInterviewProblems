"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 
"""


def findMinWrapper(self,nums:list[int]):
    print("Input: nums = "+ nums.__str__())
    print("Output: " + str(findMin(nums)))


def findMin(self,nums: list[int]) -> int:
    #base case #1: len(nums) is 1
    if len(nums) == 1: return nums[0]

    #base case #3: if len(nums) is 2 then return lowest n
    if(len(nums) == 2): 
        print("len was 2")
        if nums[0] < nums[1]:
            return nums[0]
        else: return nums[1]

    #base case #3: array is not rotated
    if nums[0] < nums[len(nums)-1]: return nums[0]

    #check if len(nums) is even or odd
    halfLen = int(len(nums)/2)

    #len(nums) is even
    if len(nums)%2 == 0:
        print("len(nums) is even")
        halfLen -= 1

        #check which side has the inflection point
        if nums[halfLen] > nums[halfLen+1]: return nums[halfLen+1]
        print("infleciton wasnt in the middle")

        #check which side has the inflection point
        if nums[0] > nums[halfLen]:
            print("returning with nums from " + str(nums[0:halfLen+1]))
            return findMin(nums[0:halfLen + 1])
        else:
            print("returning with nums from " + str(halfLen+1) +":"+str(len(nums)))
            return findMin(nums[halfLen+1:len(nums)])
    #odd
    else:
        print("len(nums) is odd")
        
        #check which side has the inflection point
        if nums[halfLen] > nums[halfLen+1]: return nums[halfLen+1]
        elif nums[halfLen-1] > nums[halfLen]: return nums[halfLen]
        print("infleciton wasnt in the middle")
        
        #check which side has the inflection point
        if nums[0] > nums[halfLen-1]:
            print("returning with nums from " + str(nums[0:halfLen]))
            return findMin(nums[0:halfLen + 1])
        else:
            print("returning with nums from " + str(halfLen+1) +":"+str(len(nums)))
            return findMin(nums[halfLen+1:len(nums)])

print(findMinWrapper([3,4,5,1,2]))
print(findMinWrapper([4,5,6,7,0,1,2]))
print(findMinWrapper([11,13,15,17]))
print(findMinWrapper([5,1,2]))