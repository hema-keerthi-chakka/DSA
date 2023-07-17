class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        vals={}
        for i in range(len(nums)):
            if vals.get(nums[i])!=None:
                if abs(i-vals.get(nums[i]))<=k:
                    return True
            vals[nums[i]]=i
                
        return False