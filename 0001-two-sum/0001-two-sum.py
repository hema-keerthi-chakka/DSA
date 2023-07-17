class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # HashTable approach
        vals={}
        for i in range(len(nums)):
            pair=target-nums[i]
            if vals.get(pair)!=None:
                return [i,vals.get(pair)]
            else:
                vals[nums[i]]=i
                
                