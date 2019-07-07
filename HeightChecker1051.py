class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        copyHeights = list(heights)
        heights.sort()

        lenOfHeights = len(heights)
        i = 0
        ans = 0
        while i < lenOfHeights:
            if heights[i] != copyHeights[i]:
                ans = ans + 1
            i = i +1

        return ans
