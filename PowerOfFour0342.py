class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num > 1:
            if num % 4 != 0:
                return False
            num = num / 4

        return True

# def isPowerOfFour(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0:
#             return False
#
#         while num != 0:
#             if num == 1:
#                 return True
#             if num & 3 != 0:
#                 return False
#             num = num / 4
#
#         return True

# class Solution {
#     public boolean isPowerOfFour(int num) {
#         if(num <= 0) return false;
#         while(num != 0){
#             if (num == 1) return true;
#             if ((num & 3) != 0) return false;
#             num = num >> 2;
#         }
#         return true;
#     }
# }
