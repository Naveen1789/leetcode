class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        lenOfList1 = len(list1)
        lenOfList2 = len(list2)
        ans = []

        h = {}

        i = 0
        while i < lenOfList1:
            h[list1[i]] = i
            i = i+1

        shortestSumOfIndexes = lenOfList1 + lenOfList2

        i = 0
        while i < lenOfList2:
            if list2[i] in h:
                if (i + h[list2[i]]) < shortestSumOfIndexes:
                    shortestSumOfIndexes = i + h[list2[i]]
                    ans = [list2[i]]
                elif (i + h[list2[i]]) == shortestSumOfIndexes:
                    ans.append(list2[i])
            i = i+1
        return ans
        
# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         """
#         :type list1: List[str]
#         :type list2: List[str]
#         :rtype: List[str]
#         """
#         lenOfList1 = len(list1)
#         lenOfList2 = len(list2)
#
#
#         ans = []
#         shortestIndexLength = (lenOfList1 + lenOfList2)
#         commonFavRestaurant = ""
#
#         print shortestIndexLength
#         i = 0
#         j = 0
#         while i < lenOfList1:
#             j = 0
#             while j < lenOfList2:
#                 if (i + j) > shortestIndexLength:
#                     break
#                 elif (i + j) == shortestIndexLength:
#                     if list1[i] == list2[j]:
#                         ans.append(list1[i])
#                 else:
#                     if list1[i] == list2[j]:
#                         shortestIndexLength = i + j
#                         ans = [list1[i]]
#                 j = j+1
#             i = i+1
#
#         return ans
