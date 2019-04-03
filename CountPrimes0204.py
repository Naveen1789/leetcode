class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        arr = [1] * n

        arr[0] = 0
        arr[1] = 0
        x = 2
        sqrtOfN = int((n) ** (.5))
        while (x <= sqrtOfN):
            if arr[x]:
                temp = x * 2
                while temp < n:
                    arr[temp] = 0
                    temp = temp + x
            x = x+1

        x = 0
        ans = 0
        while x < n:
            if arr[x] == 1:
                ans = ans + 1
            x = x+1


        return ans




            
