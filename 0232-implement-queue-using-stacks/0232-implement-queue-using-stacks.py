class MyQueue(object):

    def __init__(self):
        self.arr=[0]*200
        self.front=0
        self.rear=0
        self.size=200

    def push(self, x):
        if(self.size == self.rear):
            return 
        self.arr[self.rear]=x
        self.rear+=1

        

    def pop(self):
        if(self.empty()):
            return -1
        else:
            x=self.arr[self.front]
            self.front+=1
            return x
        

    def peek(self):
        if self.empty():
            return 0
        return self.arr[self.front]

    def empty(self):
        if(self.front==self.rear):
            self.front,self.rear=0,0
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()