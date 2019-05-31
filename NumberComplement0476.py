class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        compl = 0
        i = 0
        while num != 0:
            if num % 2 == 0:
                compl = compl + (2 ** i)
            i = i + 1
            num = num / 2
        return compl
