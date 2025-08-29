class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        survived = []

        for asteroid in asteroids:
            if asteroid > 0:
                survived.append(asteroid)
            else:
                while survived and survived[-1] > 0 and abs(asteroid) > survived[-1]:
                    survived.pop()
                if not survived or survived and survived[-1] < 0:
                    survived.append(asteroid)
                elif abs(asteroid) < survived[-1]:
                    pass
                elif abs(asteroid) == survived[-1]:
                    survived.pop()
                    pass

    
        return survived
solution = Solution()

result = solution.asteroidCollision([10,2,-5])
print(result)