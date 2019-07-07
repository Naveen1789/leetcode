class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        while N != 0 and N % 2 != 1:
            N = N / 2

        if N == 0 or N == 1:
            return 0

        N = N / 2
        count = 1

        while N != 0:
            if N % 2 == 1:
                if (count > ans):
                    ans = count
                count = 1
            else:
                count = count + 1
            N = N / 2

        if count > ans:
            return count
        else:
            return ans
