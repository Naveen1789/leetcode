class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        numberOfOnes = 0
        while n != 0:
            if 1 == (n % 2):
                numberOfOnes = numberOfOnes + 1

            n = n/2

        return numberOfOnes

        
