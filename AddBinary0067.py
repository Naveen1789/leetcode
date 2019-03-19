class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lenOfA = len(a) - 1
        lenOfB = len(b) - 1
        carry = 0
        ans = ''
        while lenOfA >= 0 or lenOfB >= 0:
            temp = carry
            if lenOfA >= 0:
                temp = temp + int(a[lenOfA])
                lenOfA = lenOfA - 1
            if lenOfB >= 0:
                temp = temp + int(b[lenOfB])
                lenOfB = lenOfB - 1

            if temp == 2:
                carry = 1
                ans = '0' + ans
            elif temp == 3:
                carry = 1
                ans = '1' + ans
            else:
                carry = 0
                ans = str(temp) + ans

        if carry == 1:
            ans = str(1) + ans
        return ans
        
