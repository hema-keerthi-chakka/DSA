class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        
        scount={}
        for ch in s :
            scount[ch]= scount.get(ch,0)+1
        
        tcount={}
        for ch in t :
            tcount[ch]= tcount.get(ch,0)+1
            
        for ch in scount.keys():
            if tcount.get(ch):
                if scount[ch]!=tcount[ch]:
                    return False
            else:
                return False
            
        return True
                
            
