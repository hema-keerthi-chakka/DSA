class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        earr=[]
        oarr=[]
        for n in nums:
            if n&1==1:
                oarr.append(n)
            else:
                earr.append(n)
                
        earr.extend(oarr)
        return earr
        