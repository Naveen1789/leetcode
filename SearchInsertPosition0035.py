class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lenOfNums = len(nums)
        i = 0

        while i < lenOfNums:
            if nums[i] >= target:
                return i
            i = i+1

        return lenOfNums

#         left = 0
#         right = len(nums) - 1

#         while left <= right and nums[left] < target:
#             left = left + 1

#         if left > right:
#             return right + 1

#         return left
