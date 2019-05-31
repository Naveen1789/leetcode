# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        myGuess = 2
        low = 0
        high = n

        while myGuess != 0:
            mid = (low + high) / 2
            myGuess = guess(mid)
            if myGuess == -1:
                high = mid-1
            elif myGuess == 1:
                low = mid+1
            else:
                ans = mid

        return ans

        
