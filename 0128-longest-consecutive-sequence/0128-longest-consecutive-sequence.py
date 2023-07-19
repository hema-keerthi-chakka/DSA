class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums.sort()
        total_max=0
        temp_max=1
        if len(nums)<=1:
            return len(nums)
        for i in range(len(nums)-1):
            temp_max+=1
            if nums[i+1]!=(nums[i]+1):
                temp_max=1
            total_max=max(temp_max,total_max)
            
        return total_max