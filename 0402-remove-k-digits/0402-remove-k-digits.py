class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        s=[]
        
        for dig in num:
            while s and int(s[-1])>int(dig) and k:
                s.pop()
                k-=1
            s.append(str(dig))
        
        while k:
            s.pop()
            k-=1
        
        ans=int(''.join(s)) if s else 0
        return str(ans)