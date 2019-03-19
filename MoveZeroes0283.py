class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        leftPtr = 0
        ptr = 0
        lenOfNums = len(nums)

        while ptr < lenOfNums:
            if nums[ptr] != 0:
                temp = nums[ptr]
                nums[ptr] = nums[leftPtr]
                nums[leftPtr] = temp
                leftPtr = leftPtr + 1
            ptr = ptr + 1
