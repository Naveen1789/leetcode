class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        lenOfA = len(A)

        if lenOfA <= 2:
            return True

        isIncreasing = None
        i = 1
        while isIncreasing == None and i < lenOfA:
            if A[i-1] == A[i]:
                i = i + 1
            elif A[i-1] > A[i]:
                isIncreasing = False
                break
            else:
                isIncreasing = True
                break


        print isIncreasing

        if isIncreasing == None:
            return True

        if isIncreasing:
            i = 1
            while i < lenOfA:
                if A[i] < A[i-1]:
                    return False
                i = i + 1
        else:
            i = 1
            while i < lenOfA:
                if A[i] > A[i-1]:
                    return False
                i = i + 1
        return True
