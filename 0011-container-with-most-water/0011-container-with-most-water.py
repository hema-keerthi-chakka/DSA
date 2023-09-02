class Solution:
    def maxArea(self, height: List[int]) -> int:

        ans=0
        n=len(height)
        
        # # Brute force
        # for i in range(n):
        #     for j in range(i+1,n):
        #         ans=max(ans,(j-i)*min(height[i],height[j]) )
                
            
        l=0
        r=n-1
        while l<r:
            cur= (r-l)*min(height[r],height[l])
            ans= max(ans,cur)
            
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        
        return ans
        