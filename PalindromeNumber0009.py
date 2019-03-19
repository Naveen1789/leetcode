class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Easy way
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False

        if x == 0:
            return True

        revNum = 0
        temp = x
        while x > 0:
            lastDigit = x % 10
            revNum = (revNum * (10)) + lastDigit
            x = x / 10

        return temp == revNum
