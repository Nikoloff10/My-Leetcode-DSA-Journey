class Solution(object):
    def numsSameConsecDiff(self, n, k):
        res = []
        
        def backtrack(current):
            if len(current) == n:
                res.append(int(''.join(map(str, current))))
                return
            last = current[-1] if current else None
            if last is None:
                
                for d in range(1, 10):
                    backtrack(current + [d])
            else:
               
                if k == 0:
                    if 0 <= last <= 9:
                        backtrack(current + [last])
                else:
                    for d in [last - k, last + k]:
                        if 0 <= d <= 9:
                            backtrack(current + [d])
        
        backtrack([])
        return res

solution = Solution()

result = solution.numsSameConsecDiff(3, 7)
print(result)