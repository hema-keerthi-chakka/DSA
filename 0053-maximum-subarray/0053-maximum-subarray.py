class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        totsum=-100000000
        cur=0
        i=0
        n=len(nums)
        
        while i<n:
            if cur<0:
                cur=0
            cur+=nums[i]
            totsum=max(cur,totsum)
            i+=1
        
        return totsum
        