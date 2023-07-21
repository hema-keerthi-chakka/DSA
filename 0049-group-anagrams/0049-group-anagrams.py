class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        words=set()
        for s in strs:
            st=''.join(sorted(s))
            words.add(str(st))
        
        for s in strs:
            cmpr=str(''.join(sorted(s)))
            if d.get(cmpr)!=None:
                newval=d[cmpr]
                newval.append(s)
                d[cmpr]= newval
            else:
                val=[s]
                d[cmpr]=val
        
        ans= d.values()
        return ans