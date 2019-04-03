class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        if n <= 0:
            return 0
        if n == 1:
            return 1

        temp1 = 0
        temp2 = 1
        ans = 0
        i = 2
        while i <= n:
            ans = temp1 + temp2
            temp1 = temp2
            temp2 = ans
            i = i+1

        return ans
