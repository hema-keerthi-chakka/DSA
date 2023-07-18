class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = ''
        for i in s:
            if i.isalnum() :
                l += i
        l = l.lower()
        if l == l[::-1]:
            return True
        else:
            return False
                
            