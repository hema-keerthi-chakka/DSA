class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        
        nums2=[]
        for i in set(nums):
            nums2.append((hm[i],i))
        
        nums2.sort(key=lambda x: x[0], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(nums2[i][1])
            
        return ans