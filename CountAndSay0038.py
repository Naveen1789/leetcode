class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"

        while n > 1:
            print ans
            n = n - 1

            curChar = ans[0]
            count = 0
            newAns = ''
            for c in ans:
                if c == curChar:
                    count = count + 1
                else:
                    newAns = newAns + str((count * 10) + int(curChar))
                    curChar = c
                    count = 1
            if count != 0:
                newAns = newAns + str((count * 10) + int(curChar))
            ans = newAns
        return ans
