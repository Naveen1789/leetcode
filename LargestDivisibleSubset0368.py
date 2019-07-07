class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenOfNums = len(nums)
        if lenOfNums == 0:
            return []

        nums.sort()

        divMat = []
        i = 0
        while i < lenOfNums:
            divMat.append([nums[i]])
            i = i + 1

        ans = []

        i = 0
        while i < lenOfNums:
            j = 0
            while j < i:
                if nums[i] % nums[j] == 0:
                    if (len(divMat[j]) + 1) > len(divMat[i]):
                        divMat[i] = divMat[j] + [nums[i]]
                j = j + 1
            if len(divMat[i]) > len(ans):
                ans = divMat[i]
            i = i + 1

        return ans
            
