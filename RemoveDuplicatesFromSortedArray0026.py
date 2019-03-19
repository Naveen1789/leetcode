class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)
        if (nums is None) or (lenOfNums == 0):
            return 0

        key = nums[0]
        leftPtr = 1
        ptr = 1
        while ptr < lenOfNums:
            if nums[ptr] != key:
                key = nums[ptr]
                nums[leftPtr] = nums[ptr]
                leftPtr = leftPtr + 1
            ptr = ptr + 1
        return leftPtr
