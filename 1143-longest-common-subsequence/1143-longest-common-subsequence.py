class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        dp={}
        
        def lcs(m,n):
            if m==0 or n==0:
                return 0

            if (m,n) in dp:
                return dp[(m,n)]
            
            if text1[m-1] == text2[n-1]:
                dp[(m,n)]= 1+ lcs(m-1,n-1)

            else:
                dp[(m,n)]= max( lcs(m,n-1) , lcs(m-1,n) )
                
            return dp[(m,n)]
        
        return lcs(len(text1),len(text2))