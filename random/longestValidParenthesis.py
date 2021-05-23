class Solution:
    # Solution 1, O(n^2), exceeds time limit
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if j - i > longest and self.isValid(s[i:j]):
                    longest = j - i
        return longest
                
    def isValid(self, s: str) -> bool:
        unclosed = 0
        for c in s:
            if c == '(':
                unclosed += 1
            elif c == ')':
                unclosed -= 1
            if unclosed < 0:
                return False
        return unclosed == 0