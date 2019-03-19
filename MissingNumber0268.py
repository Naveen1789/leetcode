class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        totalSum = (n * (n+1)) / 2
        return totalSum - sum(nums)

        # Bit manipulation -
        
        # def missingNumber(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        # i = 0
        # n = len(nums)
        # ans = n
        # while i < n:
        #     ans = ans ^ i ^ nums[i]
        #     i = i+1
        #
        # return ans
