class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()

        lenOfIntervals = len(intervals)
        i = 1
        while i < lenOfIntervals:
            if intervals[i][0] < intervals[i-1][1]:
                return False
            i = i + 1

        return True
