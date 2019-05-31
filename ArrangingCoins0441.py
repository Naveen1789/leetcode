class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        numOfRows = 0

        while n >= numOfRows:
            n = n - numOfRows
            numOfRows = numOfRows + 1

        return numOfRows - 1
