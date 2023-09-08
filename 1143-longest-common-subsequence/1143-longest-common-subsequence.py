class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        
        dp=[[-1 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)+1):
            dp[i][0]=0
        for j in range(len(text2)+1):
            dp[0][j]=0
        
        def lcs(m,n):
            if m==0 or n==0:
                return 0

            if dp[m][n] != -1:
                return dp[m][n]
            
            if text1[m-1] == text2[n-1]:
                dp[m][n]= 1+ lcs(m-1,n-1)

            else:
                dp[m][n]= max( lcs(m,n-1) , lcs(m-1,n) )
                
            return dp[m][n]
        
        return lcs(len(text1),len(text2))