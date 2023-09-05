class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n=len(nums)
        dp={}
                
        def numWays(i,pending):
            
            if i==-1:
                return 1 if pending==0 else 0 
            
            if (i,pending) in dp:
                return dp[(i,pending)]
            
            dp[(i,pending)] = numWays(i-1,pending-nums[i]) + numWays(i-1,pending+nums[i])
            return dp[(i,pending)]
        
        return numWays(n-1,target)