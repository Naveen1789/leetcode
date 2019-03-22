class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 0:
            lastDigit = 0
        else:
            lastDigit = 1

        n = n / 2
        while n > 0:
            temp = n % 2
            if temp == lastDigit:
                return False
            else:
                lastDigit = temp
            n = n / 2


        return True
        
