class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        vals={}
        for i in range(len(nums)):
            if vals.get(nums[i]):
                indices=vals.get(nums[i])
                indices.append(i)
                vals[nums[i]]= indices
            else:
                vals[nums[i]]=[i]
                
        for num in vals.keys():
            if vals.get(num) and len(vals.get(num))>1:
                indices=vals.get(num)
                for i in range(len(indices)-1):
                    if abs(indices[i+1]-indices[i])<=k:
                        return True
        
        return False