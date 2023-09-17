class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def costtomake(num,mc):
            c=0
            for i in range(n):
                if num*composition[mc][i]>stock[i]:
                    req= num*composition[mc][i]-stock[i]
                    c+= cost[i]*req 
            return c
        
        def mincost(num):
            mincost=maxsize
            for i in range(k):
                c=costtomake(num,i)
                mincost=min(mincost,c)
            return mincost 
        
        
        maxalloys=0
        l=0
        h=pow(10,9)
        
        while l<=h:
            m= (l+h)//2
            c=mincost(m)
            if c <= budget:
                maxalloys=max(maxalloys,m)
                l=m+1
            else:
                h=m-1
                
        return maxalloys
        
        
        