class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                while nums[right] == val and right >= left:
                    right = right - 1
                if right > left:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                else:
                    return left
            else:
                left = left + 1

        return left

    # Alternate Solution
    
    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     leftPtr = 0
    #     ptr = 0
    #     lenOfNums = len(nums)
    #     while ptr < lenOfNums:
    #         if nums[ptr] != val:
    #             nums[leftPtr] = nums[ptr]
    #             leftPtr = leftPtr + 1
    #         ptr = ptr + 1
    #     return leftPtr
