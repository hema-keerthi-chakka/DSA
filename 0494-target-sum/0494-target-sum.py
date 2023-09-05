class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n=len(nums)
        dp={}
                
        def numWays(i,total):
            
            if i==n:
                if total==target:
                    return 1
                else:
                    return 0 
                
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = numWays(i+1,total+nums[i]) + numWays(i+1,total-nums[i])
            
            return dp[(i,total)]
        
        return numWays(0,0)