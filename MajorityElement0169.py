class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashTable = {}
        i = 0
        lenOfNums = len(nums)
        while i < lenOfNums:
            if nums[i] in hashTable:
                hashTable[nums[i]] = hashTable[nums[i]] + 1
            else:
                hashTable[nums[i]] = 1
            i = i+1

        maxElement = 0
        maxCount = 0
        for key in hashTable:
            if hashTable[key] > maxCount:
                maxCount = hashTable[key]
                maxElement = key

        return maxElement
