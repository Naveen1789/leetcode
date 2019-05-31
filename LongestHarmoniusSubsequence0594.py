class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)
        h = {}

        i = 0
        while i < lenOfNums:
            if nums[i] in h:
                h[nums[i]] = h[nums[i]] + 1
            else:
                h[nums[i]] = 1
            i = i+1

        lenOfLongestHarmonicSequence = 0

        for key in h:
            if (key + 1) in h and (h[key] + h[key+1]) > lenOfLongestHarmonicSequence:
                lenOfLongestHarmonicSequence = h[key] + h[key+1]

        return lenOfLongestHarmonicSequence
