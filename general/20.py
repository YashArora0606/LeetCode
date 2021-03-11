class Solution(object):
        def isValid(self, s):
            brackets = {"}":"{", "]":"[", ")":"("}
            stack = []
            for b in s:
                if b in brackets.values():
                    stack.append(b)
                else:
                    if len(stack) == 0:
                        return False
                    elif stack[len(stack) - 1] == brackets[b]:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

#         """
#         :type s: str
#         :rtype: bool
#         """
