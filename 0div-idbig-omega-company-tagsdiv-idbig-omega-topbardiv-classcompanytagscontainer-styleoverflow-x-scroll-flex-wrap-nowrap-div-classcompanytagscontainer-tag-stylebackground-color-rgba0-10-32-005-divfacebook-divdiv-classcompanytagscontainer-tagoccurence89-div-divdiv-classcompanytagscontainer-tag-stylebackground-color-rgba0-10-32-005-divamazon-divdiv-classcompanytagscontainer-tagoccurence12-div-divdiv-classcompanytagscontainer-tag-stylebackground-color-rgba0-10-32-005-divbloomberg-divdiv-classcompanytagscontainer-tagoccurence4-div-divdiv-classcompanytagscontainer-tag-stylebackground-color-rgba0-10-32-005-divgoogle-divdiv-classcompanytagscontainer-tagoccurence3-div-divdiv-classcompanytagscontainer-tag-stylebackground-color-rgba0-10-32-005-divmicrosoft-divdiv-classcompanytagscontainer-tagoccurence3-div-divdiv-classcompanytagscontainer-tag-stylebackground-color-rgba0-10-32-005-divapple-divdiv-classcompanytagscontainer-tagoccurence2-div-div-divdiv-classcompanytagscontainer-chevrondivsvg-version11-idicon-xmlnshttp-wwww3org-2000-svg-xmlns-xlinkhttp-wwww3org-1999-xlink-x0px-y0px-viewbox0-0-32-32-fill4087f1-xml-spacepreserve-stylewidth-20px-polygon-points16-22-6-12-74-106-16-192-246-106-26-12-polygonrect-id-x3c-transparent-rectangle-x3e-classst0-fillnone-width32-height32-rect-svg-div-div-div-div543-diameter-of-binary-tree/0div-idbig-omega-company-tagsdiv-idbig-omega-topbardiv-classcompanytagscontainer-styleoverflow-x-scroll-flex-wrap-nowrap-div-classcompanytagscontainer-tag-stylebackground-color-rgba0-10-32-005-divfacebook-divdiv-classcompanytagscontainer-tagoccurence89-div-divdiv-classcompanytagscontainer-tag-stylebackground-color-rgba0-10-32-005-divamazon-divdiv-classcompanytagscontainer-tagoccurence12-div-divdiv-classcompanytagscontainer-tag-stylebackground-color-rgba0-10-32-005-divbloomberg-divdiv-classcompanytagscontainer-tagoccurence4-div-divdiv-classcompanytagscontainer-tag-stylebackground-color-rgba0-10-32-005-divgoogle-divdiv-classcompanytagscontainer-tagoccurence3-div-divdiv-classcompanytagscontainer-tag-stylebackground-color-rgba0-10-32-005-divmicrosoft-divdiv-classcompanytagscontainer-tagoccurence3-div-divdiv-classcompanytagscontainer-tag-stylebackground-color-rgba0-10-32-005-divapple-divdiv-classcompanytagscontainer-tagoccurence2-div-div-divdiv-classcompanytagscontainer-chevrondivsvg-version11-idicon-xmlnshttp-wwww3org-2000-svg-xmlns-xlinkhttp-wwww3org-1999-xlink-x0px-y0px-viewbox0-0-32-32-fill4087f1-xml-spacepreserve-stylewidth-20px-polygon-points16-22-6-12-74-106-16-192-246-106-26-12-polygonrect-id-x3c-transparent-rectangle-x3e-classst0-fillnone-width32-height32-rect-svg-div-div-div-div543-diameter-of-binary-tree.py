# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, R: Optional[TreeNode]) -> int:
        
        ans=[]
        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            ans.append(l+r)
            
            return 1+max(l,r)
        
        height(R)
        return max(ans)
            
            
            
            
        