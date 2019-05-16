class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = self.findMaxSubArray(nums, 0, len(nums)-1)
        return ans[0]


    def findMaxCrossingSubArray(self, arr, low, mid, high):
        sum = 0
        leftSum = -99999
        leftIndex = -1
        for i in range(mid, low-1, -1):
            sum = sum + arr[i]
            if sum > leftSum:
                leftSum = sum
                leftIndex = i

        sum = 0
        rightSum = -99999
        rightIndex = -1
        for i in range (mid+1, high+1):
            sum = sum + arr[i]
            if sum > rightSum:
                rightSum = sum
                rightIndex = i

        return [leftSum+rightSum, leftIndex, rightIndex]


    def findMaxSubArray(self, arr, low, high):
        if low == high:
            return [arr[low], low, high]

        else:
            mid = (low + high) /  2
            leftSubArr = self.findMaxSubArray(arr, low, mid)
            leftSubArrSum = leftSubArr[0]

            rightSubArr = self.findMaxSubArray(arr, mid+1, high)
            rightSubArrSum = rightSubArr[0]

            crossArr = self.findMaxCrossingSubArray(arr, low, mid, high)
            crossArrSum = crossArr[0]

            if (leftSubArrSum > rightSubArrSum) and (leftSubArrSum > crossArrSum):
                return leftSubArr
            elif (rightSubArrSum > crossArrSum):
                return rightSubArr
            else:
                return crossArr
        
