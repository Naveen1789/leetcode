class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        arr = [0,1]
        temp = 1
        while (temp * temp) <= c:
            temp = temp + 1
            arr.append(temp*temp)

        left = 0
        right = len(arr) - 1

        while left <= right:
            sum = arr[left] + arr[right]
            if sum == c:
                return True
            elif sum < c:
                left = left + 1
            else:
                right = right - 1

        return False
            
