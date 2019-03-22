class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hammingDistance = 0
        i = 1
        while i <= 32:
            i = i+1
            hammingDistance = hammingDistance + ((x%2) ^ (y%2))
            x = x/2
            y = y/2

        return hammingDistance
