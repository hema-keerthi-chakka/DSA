# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        h={}
        
        def findheight(root):

            if not root:
                return 0

            if root in h:
                return h[root]

            l=findheight(root.left)
            r=findheight(root.right)


            h[root]= max(l,r) +1 

            return h[root]
        
        def balance(root):
            if not root:
                return True

            if not abs(findheight(root.left)-findheight(root.right))<=1:
                return False
            
            return balance(root.left) and balance(root.right)
        
        return balance(root)
    
        