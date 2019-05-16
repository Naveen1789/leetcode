class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashTableForRansom = {}
        hashTableForMag = {}

        for ch in ransomNote:
            if hashTableForRansom.get(str(ch)) == None:
                hashTableForRansom[str(ch)] = 1
            else:
                hashTableForRansom[str(ch)] = hashTableForRansom[str(ch)] + 1

        for ch in magazine:
            if hashTableForMag.get(str(ch)) == None:
                hashTableForMag[str(ch)] = 1
            else:
                hashTableForMag[str(ch)] = hashTableForMag[str(ch)] + 1

        for key in hashTableForRansom:
            if hashTableForMag.get(key) < hashTableForRansom.get(key):
                return False

        return True
