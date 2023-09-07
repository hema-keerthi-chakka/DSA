"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if root==None:
            return 0
        
        ans=0 
        
        for node in root.children:
            childval= self.maxDepth(node)
            ans=max(ans,childval)
        
        return ans+1
        