# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, R: Optional[TreeNode]) -> int:
        
        ans = 0
        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            nonlocal ans
            ans=max(ans,l+r)
            
            return 1+max(l,r)
        
        height(R)
        return ans
            
            
            
            
        