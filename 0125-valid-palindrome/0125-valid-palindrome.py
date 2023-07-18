class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Time complexity: O(N) , space: O(N)
        # l = ''
        # for i in s:
        #     if i.isalnum() :
        #         l += i
        # l = l.lower()
        # if l == l[::-1]:
        #     return True
        # else:
        #     return False
        
        #Time Complexity: O(N) , space: O(1)
        i=0
        j=len(s)-1
        s=s.lower()
        while i<=j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            if i<len(s) and (not s[i].isalnum()):
                i+=1
            if j>=0 and (not s[j].isalnum()):
                j-=1
        return True
            
                
            