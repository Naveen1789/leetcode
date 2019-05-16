class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.revArr(nums, 0, len(nums)-1)

        self.revArr(nums, 0, k-1)
        self.revArr(nums, k, len(nums)-1)

    def revArr(self, arr, left, right):
        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left = left + 1
            right = right - 1
            
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     lenOfNums = len(nums)
    #     k = k % lenOfNums
    #
    #     if k == 0:
    #         return
    #
    #     iter = 0
    #     j = 0
    #     init = 0
    #     temp2 = nums[0]
    #     while iter < lenOfNums:
    #         if j == init:
    #             j = j+1
    #             temp2 = nums[j]
    #             init = j
    #
    #         iter = iter + 1
    #         kthPos = (j + k) % lenOfNums
    #         temp1 = nums[kthPos]
    #         nums[kthPos] = temp2
    #         temp2 = temp1
    #         j = kthPos
