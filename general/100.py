# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if (not p) and (not q): # if both do not exist
            return True
        if ((not p) and q) or ((not q) and p): # if only one exists
            return False
        if p.val != q.val: # if both exist but are different
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # if both are same they must be further checked
