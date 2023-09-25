#User function Template for python3

class Solution:
    def countWays(self, n, s):
        # code here
        def solve(i,j,isTrue):
            if i>j:
                return 0
                
            if i==j:
                if s[i]==isTrue:
                    return 1
                else:
                    return 0
                
            if isTrue=='T' and t[i][j]!=-1:
                return t[i][j]
                
            if isTrue=='F' and f[i][j]!=-1:
                return f[i][j]
                
            ans=0
            for k in range(i+1,j,2):
                
                lt= t[i][k-1] if t[i][k-1]!=-1 else solve(i,k-1,'T')
                t[i][k-1]=lt
                rt= t[k+1][j] if t[k+1][j]!=-1 else solve(k+1,j,'T')
                t[k+1][j]=rt
                
                lf= f[i][k-1] if f[i][k-1]!=-1 else solve(i,k-1,'F')
                f[i][k-1]=lf
                rf= f[k+1][j] if f[k+1][j]!=-1 else solve(k+1,j,'F')
                f[k+1][j]=rf
                
                sym=s[k]
                if isTrue=='T':
                    if sym=='|':
                        ans+= lt*rt + lt*rf + lf*rt
                    elif sym=='&':
                        ans+= lt*rt
                    else:
                        ans+= lt*rf + lf*rt
                else:
                    if sym=='|':
                        ans+= lf*rf
                    elif sym=='&':
                        ans+= lf*rt + lt*rf + lf*rf
                    else:
                        ans+= lt*rt + lf*rf 
                 
                ans%=1003
               
            if isTrue=='T':
                t[i][j]=ans
            else:
                f[i][j]=ans 
                
            return ans
            
        t=[[-1 for j in range(n)]for i in range(n)]
        f=[[-1 for j in range(n)]for i in range(n)]
        return solve(0,n-1,'T')
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            






#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends