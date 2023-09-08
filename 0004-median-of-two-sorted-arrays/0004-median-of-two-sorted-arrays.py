class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        n1=len(nums1)
        n2=len(nums2)
        
        if n1>n2: 
            return self.findMedianSortedArrays(nums2, nums1)
        
        totlen= n1+n2
        
        low,high=0,n1 
        
        while(low<=high):
            
            par1= (low+high) >> 1  # ()/2
            par2= (totlen +1)//2 - par1
            
            l1= float("-inf") if par1==0 else nums1[par1-1]
            l2= float("-inf") if par2==0 else nums2[par2-1]

            r1= float("inf") if par1==n1 else nums1[par1]
            r2= float("inf") if par2==n2 else nums2[par2]
            
            if( (l1<=r2) and (l2<=r1) ):
                #Correct partition
                if totlen&1==0:
                    #even length case
                    return (max(l1,l2)+min(r1,r2)) / 2.0
                else:
                    return max(l1,l2)/1
                
            if l1>r2:
                high=par1-1 
            else:
                low=par1+1 
                
        return 0.0

            
            
        
        
        