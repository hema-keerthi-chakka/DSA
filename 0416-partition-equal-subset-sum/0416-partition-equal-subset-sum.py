class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s=sum(nums)
        if s&1!=0: 
            #If sum is odd, we can't partition into equal halves 
            return False 
        
        #Check whether we can create subset with half of the sum
        
        k=s//2 
        n=len(nums)
        dp=[[False for j in range(k+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
            
        for i in range(1,n+1):
            for j in range(1,k+1):
                if nums[i-1]<=k:
                    dp[i][j]= dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        
        return dp[n][k]