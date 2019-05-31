class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)

        i = 0
        arraySum = 0
        while i < lenOfNums:
            arraySum = arraySum + nums[i]
            i = i + 1

        leftSum = 0
        i = 0
        while i < lenOfNums:
            if (2 * leftSum) == (arraySum - nums[i]):
                return i
            leftSum = leftSum + nums[i]
            i = i + 1

        return -1
