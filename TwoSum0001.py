class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        i = 0
        while i < len(nums):
            if nums[i] in hashTable:
                return [hashTable[nums[i]], i]
            else:
                diff = target - nums[i]
                hashTable[diff] = i
            i = i+1

    # Alternate solution -

    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     i = 0
    #     lenOfNums = len(nums)
    #     while i < lenOfNums:
    #         j = i+1
    #         while j < lenOfNums:
    #             if nums[i] + nums[j] == target:
    #                 return [i,j]
    #             j = j+1
    #         i = i+1
