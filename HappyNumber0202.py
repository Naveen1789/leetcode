class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isHappyNumber(n, [])

    def isHappyNumber(self, n, arr):
        if n == 1:
            return True

        if n in arr:
            return False

        arr.append(n)

        temp = 0
        while n != 0:
            temp = temp + ((n%10) ** 2)
            n = n/10

        return self.isHappyNumber(temp, arr)


        
