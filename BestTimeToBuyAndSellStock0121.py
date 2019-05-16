class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) <= 1:
            return 0

        if len(prices) == 1:
            return prices[0]

        priceChanges = []
        lenOfPrices = len(prices)
        i = 1
        while i < lenOfPrices:
            priceChanges.append(prices[i] - prices[i-1])
            i = i+1

        ans = self.findMaxSubArray(priceChanges, 0, len(priceChanges)-1)
        if ans[0] < 0:
            return 0
        else:
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
            leftLow = leftSubArr[1]
            leftHigh = leftSubArr[2]

            rightSubArr = self.findMaxSubArray(arr, mid+1, high)
            rightSubArrSum = rightSubArr[0]
            rightLow = rightSubArr[1]
            rightHigh = rightSubArr[2]

            crossArr = self.findMaxCrossingSubArray(arr, low, mid, high)
            crossArrSum = crossArr[0]
            crossLow = crossArr[1]
            crossHigh = crossArr[2]

            if (leftSubArrSum > rightSubArrSum) and (leftSubArrSum > crossArrSum):
                return leftSubArr
            elif (rightSubArrSum > crossArrSum):
                return rightSubArr
            else:
                return crossArr
