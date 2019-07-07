class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                del intervals[i]
            else:
                i = i + 1

        return intervals
