class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n = n / 3

        return True

    # def isPowerOfThree(self, n):
    #     return n>0 and 3**19 % n == 0
