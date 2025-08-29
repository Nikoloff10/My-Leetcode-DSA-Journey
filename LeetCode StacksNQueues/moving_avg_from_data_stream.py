class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.queue = []
        

    def next(self, val):
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / float(min(len(queue), size))
        


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)

param_1 = obj.next(1)
print(f"Next(1): {param_1}")
param_2 = obj.next(10)
print(f"Next(10): {param_2}")
param_3 = obj.next(3)
print(f"Next(3): {param_3}")
param_4 = obj.next(5)
print(f"Next(5): {param_4}")