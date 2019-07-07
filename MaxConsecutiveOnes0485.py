class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)
        ans = 0
        count = 0
        i = 0
        while i < lenOfNums:
            if nums[i] == 1:
                count = count + 1
            else:
                if count > ans:
                    ans = count
                count = 0
            i = i + 1

        if count > ans:
            return count
        else:
            return ans
