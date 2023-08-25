class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        #Stores dist,x,y of each point
        minHeap=[]
        
        for point in points:
            x,y=point
            dist=x*x+y*y
            minHeap.append([dist,x,y])
            
        heapq.heapify(minHeap)
        
        ans=[]
        
        while k:
            dist,x,y=heapq.heappop(minHeap)
            ans.append([x,y])
            k-=1
        
        return ans