# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        elif self.isEqualTree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    
    def isEqualTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        elif (t1 == None and t2 != None) or (t1 != None and t2 == None):
            return False
        elif t1.val == t2.val:
            return self.isEqualTree(t1.left, t2.left) and self.isEqualTree(t1.right, t2.right)
        else:
            return False