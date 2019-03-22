class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        return self.permute(S)

    def permute(self, str):

        lenOfStr = len(str)
        if lenOfStr == 0:
            return [""]

        lastElem = str[lenOfStr-1]
        str = str[:lenOfStr-1]
        tempAns = self.permute(str)
        ans = []
        for permutation in tempAns:
            if lastElem.isalpha():
                ans.append(permutation + lastElem.lower())
                ans.append(permutation + lastElem.upper())
            else:
                ans.append(permutation + lastElem)


        return ans
                
