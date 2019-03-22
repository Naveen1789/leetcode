class Solution(object):
    # def isPowerOfTwo(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     if n < 0:
    #         return False
    #
    #     numberOfOnes = 0
    #     while n != 0:
    #         if 1 == (n % 2):
    #             numberOfOnes = numberOfOnes + 1
    #
    #         n = n/2
    #
    #     return numberOfOnes == 1

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1) == 0)
