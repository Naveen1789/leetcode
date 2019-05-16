class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenOfNums = len(nums)

        if lenOfNums == 0:
            return 0
        if lenOfNums == 1:
            return nums[0]
        if lenOfNums == 2:
            return max(nums[0], nums[1])

        temp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            a = temp[i-2] + nums[i]
            b = temp[i-1]
            temp.append(max(a,b))

        return max(temp[lenOfNums-1], temp[lenOfNums-2])
        
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return self.getMaxMoney(nums, 0, 0)
    #
    # def getMaxMoney(self, nums, left, sumSoFar):
    #     if left >= len(nums):
    #         return sumSoFar
    #     if left == (len(nums) - 1):
    #         return sumSoFar + nums[left]
    #     # if left == (len(nums) - 2):
    #     #     return max(sumSoFar)
    #     newSum = sumSoFar + nums[left]
    #     return max(self.getMaxMoney(nums, left+2, newSum), self.getMaxMoney(nums, left+1, sumSoFar))
    #
    #
