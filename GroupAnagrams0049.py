class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}

        for str in strs:
            sortedStr = ''.join(sorted(str))
            if h.get(sortedStr) == None:
                h[sortedStr] = [str]
            else:
                h[sortedStr].append(str)

        ans = []
        for anagramsArrKey in h:
            ans.append(h.get(anagramsArrKey))

        return ans
