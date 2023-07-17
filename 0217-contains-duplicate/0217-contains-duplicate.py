class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hm={}  #HashMap approach -- Faster than all
        for num in nums:
            if hm.get(num):
                hm[num]=hm.get(num)+1
                if hm.get(num)>1:
                    return True
            else:
                hm[num]=1
        return False
        
        # hs=set() #HashSet approach
        # for num in nums:
        #     if num in hs :
        #         return True
        #     else:
        #         hs.add(num)
        # return False