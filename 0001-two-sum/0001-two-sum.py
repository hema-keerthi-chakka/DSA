class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # HashTable approach - Complexity- Time:O(N), Space:O(N) 
        vals={}
        for i in range(len(nums)):
            pair=target-nums[i]
            if vals.get(pair)!=None:
                return [i,vals.get(pair)]
            else:
                vals[nums[i]]=i
                
#         Brute Force: 
#             iterate through each element, 
#             compare every other element with the cur element.
#             If they match return their indices
#             Complexity: O(N^2)
                
#         Better approaches:
            
#         Sort + Binary Search for pair  O(NlogN)
#         Sort + use 2 pointers to navigate to the right pair O(NlogN)
            
                
                