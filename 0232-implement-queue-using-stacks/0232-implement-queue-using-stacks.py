class MyQueue(object):

    def __init__(self):
        self.stack=[]
        self.temp=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        ans=None 

        while self.stack:
            self.temp.append(self.stack.pop())
            
        if self.temp:
            ans=self.temp.pop()
            
        while self.temp:
            self.stack.append(self.temp.pop())
            
        return ans

    def peek(self):
        """
        :rtype: int
        """
        ans=None 
        
        while self.stack:
            self.temp.append(self.stack.pop())
            
        if self.temp:
            ans=self.temp[-1]
            
        while self.temp:
            self.stack.append(self.temp.pop())
            
        return ans

    def empty(self):
        """
        :rtype: bool
        """
        return self.peek()==None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()