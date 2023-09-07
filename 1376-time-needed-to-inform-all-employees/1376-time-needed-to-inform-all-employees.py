class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        
        subords = { man: set() for man in manager}
        
        for i in range(n):
            subords[manager[i]].add(i)
            
        def dfs(emp):
            
            if emp not in subords:
                return 0 
            
            curMax=0
            
            for i in subords[emp]:
                curMax=max(curMax, dfs(i))
                
            return informTime[emp]+ curMax
        
        return dfs(headID)