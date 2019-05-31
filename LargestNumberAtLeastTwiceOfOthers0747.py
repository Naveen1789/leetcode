class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)
        if lenOfNums == 0:
            return -1

        max = nums[0]
        indexOfLargestElem = 0
        i = 1
        while i < lenOfNums:
            if nums[i] > max:
                max = nums[i]
                indexOfLargestElem = i
            i = i + 1

        i = 0
        while i < lenOfNums:
            if (i != indexOfLargestElem) and(nums[i] * 2) > max:
                return -1
            i = i + 1

        return indexOfLargestElem
