class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2
        powOfTwo = []
        i = 1
        while i <= 31:
            powOfTwo.append(2 ** i)
            i = i + 1

        # 3
        powOfThree = []
        i = 1
        while i <= 19:
            powOfThree.append(3 ** i)
            i = i + 1

        # 5
        powOfFive = []
        i = 1
        while i <= 13:
            powOfFive.append(5 ** i)
            i = i + 1

        arr = [1]
        tempArr = list(arr)
        for a in tempArr:
            for b in powOfTwo:
                arr.append(a*b)

        tempArr = list(arr)
        for a in tempArr:
            for b in powOfThree:
                arr.append(a*b)

        tempArr = list(arr)
        for a in tempArr:
            for b in powOfFive:
                arr.append(a*b)

        arr.sort()
        return arr[n-1]

# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         uglyNums = [1]
#         i2 = 0
#         i3 = 0
#         i5 = 0
#
#
#         i = 1
#         while i < n:
#             i = i+1
#             f2 = uglyNums[i2] * 2
#             f3 = uglyNums[i3] * 3
#             f5 = uglyNums[i5] * 5
#
#             f = min(f2,f3,f5)
#             uglyNums.append(f)
#             if f == f2:
#                 i2 = i2+1
#             if f == f3:
#                 i3 = i3+1
#                 f3 = f3 * 3
#             if f == f5:
#                 i5 = i5+1
#                 f5 = f5 * 5
#
#
#
#         return uglyNums[n-1]
