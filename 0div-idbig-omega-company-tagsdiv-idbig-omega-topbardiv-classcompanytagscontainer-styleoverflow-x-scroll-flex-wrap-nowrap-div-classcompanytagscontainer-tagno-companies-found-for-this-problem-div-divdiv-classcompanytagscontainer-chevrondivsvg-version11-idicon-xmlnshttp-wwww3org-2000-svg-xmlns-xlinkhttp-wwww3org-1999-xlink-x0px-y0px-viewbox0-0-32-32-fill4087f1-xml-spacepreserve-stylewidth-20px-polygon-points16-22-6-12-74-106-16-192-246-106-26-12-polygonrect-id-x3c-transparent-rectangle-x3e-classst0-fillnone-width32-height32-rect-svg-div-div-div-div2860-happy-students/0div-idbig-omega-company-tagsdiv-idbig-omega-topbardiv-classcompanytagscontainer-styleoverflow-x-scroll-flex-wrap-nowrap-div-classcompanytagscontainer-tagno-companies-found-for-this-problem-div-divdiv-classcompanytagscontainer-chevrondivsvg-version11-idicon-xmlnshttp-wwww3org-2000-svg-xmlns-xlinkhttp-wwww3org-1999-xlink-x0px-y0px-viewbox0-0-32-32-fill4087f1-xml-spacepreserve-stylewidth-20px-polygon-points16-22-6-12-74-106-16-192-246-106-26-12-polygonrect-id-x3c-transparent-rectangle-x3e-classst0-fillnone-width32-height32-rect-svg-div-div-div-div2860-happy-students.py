class Solution:
    def countWays(self, nums: List[int]) -> int:
        
        def check(i):
            
            if (i-1)>=0 and (i+1)<=nums[i-1]:
                return False
            # for ind in range(0,i+1):
            #     if (i+1)>nums[ind]:
            #         continue
            #     else:
            #         return False

            if (i+1)<n and nums[i+1]<=(i+1):
                    return False
            # for ind in range(i+1,n):
            #     if nums[ind]<=(i+1):
            #         return False

            return True
        
        
        n=len(nums)
        nums.sort()
        ways=0
        
        
        if nums[0]>0 and check(-1):
            ways+=1
        
        for i,num in enumerate(nums):
            if (i+1)>num:
                if check(i):
                    ways+=1

        return ways
            