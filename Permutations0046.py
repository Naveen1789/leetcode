class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]


        lastElem = nums.pop()
        tempAns = self.permute(nums)
        ans = []
        for permutation in tempAns:
            lenOfPermutation = len(permutation)
            i = 0
            while i <= lenOfPermutation:
                temp = list(permutation)
                temp.insert(i, lastElem)
                ans.append(temp)
                i = i+1


        return ans

        
