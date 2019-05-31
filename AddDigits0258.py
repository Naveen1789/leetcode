class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        newNum = 0
        while num != 0:
            newNum = newNum + (num % 10)
            num = num/10

        return self.addDigits(newNum)
        
