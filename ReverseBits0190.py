class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = 1
        ans = 0
        while x <= 32:
            x = x+1
            ans = (ans * 2) + (n % 2)
            n = n / 2


        return ans
