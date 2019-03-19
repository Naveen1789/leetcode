class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1

        while i >= 0:
            if carry == 1:
                temp = digits[i] + 1
                digits[i] = temp % 10
                carry = temp / 10
            else:
                break
            i = i-1

        if carry == 1:
            digits.insert(0,1)

        return digits
