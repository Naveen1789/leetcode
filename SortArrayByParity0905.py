class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lenOfA = len(A)
        left = 0
        right = lenOfA - 1

        while left < right:
            while left < lenOfA and A[left] % 2 == 0:
                left = left + 1
            while right >= 0 and A[right] % 2 == 1:
                right = right - 1

            if left < right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left = left + 1
                right = right - 1

        return A
