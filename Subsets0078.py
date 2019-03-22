class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenOfNums = len(nums)

        if lenOfNums == 1:
            return [[], nums]

        lastElem = nums.pop()

        ans = self.subsets(nums)
        tempAns = []
        for temp in ans:
            tempCopy = list(temp)
            tempCopy.append(lastElem)
            tempAns.append(tempCopy)
        return ans + tempAns
        
