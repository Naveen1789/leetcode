class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = 1
        if x < 0:
            temp = -1
            x = x * temp

        ans = 0
        while x != 0:
            ans = (ans * 10) + (x % 10)
            x = x / 10

        if (temp == 1) and (ans > (2 ** 31)):
            return 0
        elif (ans > ((2 ** 31) - 1)):
            return 0
        else:
            return ans * temp
    #
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     isNegative = False
    #     if x < 0:
    #         isNegative = True
    #         x = x * -1
    #
    #     ans = 0
    #     while x != 0:
    #         if (not isNegative) and (ans >  214748364) or (ans == 214748364 and x >= 8):
    #             return 0
    #         if (isNegative) and (ans > 214748364) or (ans == 214748364 and x < -8 ):
    #             return 0
    #         ans = (ans * 10) + (x % 10)
    #         x = x / 10
    #
    #     if isNegative:
    #         return ans * -1
    #     else:
    #         return ans
