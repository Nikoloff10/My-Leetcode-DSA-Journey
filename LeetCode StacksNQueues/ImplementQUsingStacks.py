class MyQueue(object):

    def __init__(self):

        self.elements = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.elements.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.elements:
            return self.elements.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if self.elements:
            return self.elements[0]

    def empty(self):
        """
        :rtype: bool
        """

        if self.elements:
            return False
        else:
            return True


obj = MyQueue()
obj.push(7)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
