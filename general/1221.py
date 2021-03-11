class Solution(object):
    def balancedStringSplit(self, s):
        numL = 0
        numR = 0
        output = 0
        for i in range(len(s)):
            if s[i] == 'L':
                numL += 1
            else:
                numR += 1
            if (numL == numR) and (numL != 0):
                output += 1
                numL = 0
                numR = 0

        return output
