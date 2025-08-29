class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        current_span = 1

        while self.stack and self.stack[-1][0] <= price:
            prev_span = self.stack[-1][1]
            self.stack.pop()
            current_span += prev_span

        self.stack.append((price, current_span))

        return current_span
