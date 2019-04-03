class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        lenOfNums = len(nums)
        i = 0
        while i < (lenOfNums-1):
            if nums[i] == nums[i+1]:
                return True
            i = i+1
        return False
