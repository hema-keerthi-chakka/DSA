class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        
        dp={}
        
        def lcs(m,n):
            if m==0 or n==0:
                return 0

            if text1[m-1] == text2[n-1]:
                if (m-1,n-1) not in dp:
                    dp[(m-1,n-1)] = lcs(m-1,n-1)
                return 1 + dp[(m-1,n-1)]
            
            else:
                if (m,n-1) not in dp:
                    dp[(m,n-1)] = lcs(m,n-1)
                if (m-1,n) not in dp:
                    dp[(m-1,n)] = lcs(m-1,n)
                return max( dp[(m,n-1)] , dp[(m-1,n)] )
        
        return lcs(len(text1),len(text2))