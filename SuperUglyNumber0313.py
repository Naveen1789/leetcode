class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        superUglyNums = [1]
        lenOfPrimes = len(primes)
        indexes = [0] * lenOfPrimes

        i = 1
        while i < n:
            i = i+1
            factors = []
            j = 0
            while j < lenOfPrimes:
                factors.append(primes[j] * superUglyNums[indexes[j]])
                j = j+1


            f = min(factors)
            superUglyNums.append(f)

            x = 0
            while x < lenOfPrimes:
                if factors[x] == f:
                    indexes[x] = indexes[x] + 1
                x = x+1

        return superUglyNums[n-1]
        
