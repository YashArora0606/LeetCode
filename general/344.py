class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)/2):
            temp = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = s[i]
            s[i] = temp
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
