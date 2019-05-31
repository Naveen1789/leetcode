class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.topIndex = -1
        self.minEle = 999999999999999999

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x >= self.minEle:
            self.arr.append(x)
        else:
            newMinEle = x
            self.arr.append((2*x) - self.minEle)
            self.minEle = newMinEle
        self.topIndex = self.topIndex + 1

    def pop(self):
        """
        :rtype: None
        """
        poppedElem = 0
        if self.topIndex < 0:
            print "Underflow."
        elif self.arr[self.topIndex] >= self.minEle:
            self.topIndex = self.topIndex - 1
            poppedElem = self.arr.pop()
        else:
            self.topIndex = self.topIndex - 1
            poppedElem = self.arr.pop()
            self.minEle = (2*self.minEle) - poppedElem

    def top(self):
        """
        :rtype: int
        """
        if self.topIndex < 0:
            return 0

        if self.arr[self.topIndex] < self.minEle:
            return self.minEle
        else:
            return self.arr[self.topIndex]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minEle



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
