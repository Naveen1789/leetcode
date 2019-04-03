class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.getAllPermutations(n, 0, {})


    def getAllPermutations(self, stepsRemaining, ans, h):
        if stepsRemaining == 1:
            ans = ans + 1
            return ans

        if stepsRemaining == 2:
            ans = ans + 2
            return ans

        if h.get(stepsRemaining) == None:
            h[stepsRemaining] = self.getAllPermutations(stepsRemaining - 1, ans, h) + self.getAllPermutations(stepsRemaining - 2, ans, h)

        return h[stepsRemaining]

    # Fibonacci
    # def climbStairs(self, n):
    #         """
    #         :type n: int
    #         :rtype: int
    #         """
    #         if n <= 0:
    #             return 0
    #         if n == 1:
    #             return 1
    #         if n == 2:
    #             return 2
    #
    #         temp1 = 1
    #         temp2 = 2
    #         ans = 0
    #         i = 3
    #         while i <= n:
    #             ans = temp1 + temp2
    #             temp1 = temp2
    #             temp2 = ans
    #             i = i+1
    #
    #         return ans
