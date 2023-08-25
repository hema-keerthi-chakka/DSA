class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # #Sorting
        # n=len(nums)
        # nums.sort()
        # return nums[n-k]
        
        maxHeap=[-i for i in nums]
        heapq.heapify(maxHeap)
        top=None 
        while k:
            top= heapq.heappop(maxHeap)
            k-=1
        return -top
        