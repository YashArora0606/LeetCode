class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset = {}
        maxLen = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if not s[j] in charset:
                charset[s[j]] = 1
                j += 1
                maxLen = max(maxLen, j-i)
            else:
                del charset[s[i]]
                i += 1
        return maxLen
