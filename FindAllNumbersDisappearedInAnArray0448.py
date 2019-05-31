class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tempNums = list(nums)

        for a in nums:
            tempNums[a-1] = 0

        ans = []
        lenOfTempNums = len(tempNums)
        i = 0
        while i < lenOfTempNums:
            if tempNums[i] != 0:
                ans.append(i+1)
            i = i + 1

        return ans


# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         lenOfNums = len(nums)
#         i = 0
#         while i < lenOfNums:
#             if nums[abs(nums[i]) - 1] > 0:
#                 nums[abs(nums[i]) - 1] = nums[abs(nums[i]) - 1] * -1
#             i = i+1
#
#
#         ans = []
#         i = 0
#         while i < lenOfNums:
#             if nums[i] > 0:
#                 ans.append(i+1)
#             i = i + 1
#
#         return ans
