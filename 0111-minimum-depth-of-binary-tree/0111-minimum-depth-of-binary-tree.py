# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        
        left= self.minDepth(root.left) if root.left else 10000000
        right= self.minDepth(root.right) if root.right else 10000000
        
        return min(left,right)+1