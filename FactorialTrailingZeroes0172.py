class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        numOfFives = 0
        while n > 0:
            n = n / 5
            numOfFives = numOfFives + n

        return numOfFives
