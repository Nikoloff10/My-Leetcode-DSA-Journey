from math import sqrt


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        points.sort(key=self.squared_distance)
        
        return points[:k]
    
    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2


solution = Solution()
result = solution.kClosest([[1,3],[-2,2]], 1)
print(result)