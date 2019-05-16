class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num % 4 == 0:
            num = num / 4

        i = 3
        while (i*i) <= num:
            iSq = i * i
            while num % iSq == 0:
                num = num / iSq
            i = i + 2

        return num == 1
