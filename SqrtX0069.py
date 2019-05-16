class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        ansSoFar = -1
        low = 0
        high = x
        while low <= high:
            mid = (low + high) / 2
            midSq = mid * mid
            if midSq == x:
                return mid

            elif midSq < x:
                if ansSoFar < mid:
                    ansSoFar = mid
                low = mid + 1

            else:
                high = mid - 1
        return ansSoFar
