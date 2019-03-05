class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        a = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                a.append(ch)
            elif not a:
                return False
            elif ch == ')' and a.pop() != '(':
                return False
            elif ch == ']' and a.pop() != '[':
                return False
            elif ch == '}' and a.pop() != '{':
                return False

        if not a:
            return True
        else:
            return False

        
