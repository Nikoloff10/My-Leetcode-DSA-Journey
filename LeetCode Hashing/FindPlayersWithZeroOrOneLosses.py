from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        all_players = set()
        losses = defaultdict(int)

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            losses[loser] += 1

        zero_loss_winners = sorted([player for player in all_players if player not in losses])
        one_loss_losers = sorted([player for player, count in losses.items() if count == 1])

        return [zero_loss_winners, one_loss_losers]

solution = Solution()
print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))