class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        i = 1
        while i <= n:
            temp = ""
            if i % 3 == 0:
                temp = temp + "Fizz"
            if i % 5 == 0:
                temp = temp + "Buzz"
            if temp == "":
                temp = str(i)
            ans.append(temp)
            i = i+1

        return ans



# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         ans = []
#         i = 1
#         while i <= n:
#             if i % 3 == 0:
#                 if i % 5 == 0:
#                     ans.append("FizzBuzz")
#                 else:
#                     ans.append("Fizz")
#             elif i % 5 == 0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#
#             i = i+1
#
#         return ans
