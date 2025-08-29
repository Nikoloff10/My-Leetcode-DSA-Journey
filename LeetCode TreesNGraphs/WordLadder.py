from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        node = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                node[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nodeWord in node[pattern]:
                        if nodeWord not in visited:
                            visited.add(nodeWord)
                            queue.append(nodeWord)
            
            res += 1
        return 0
    
solution = Solution()
result = solution.ladderLength("hot",
"dog",
["hot","cog","dog","tot","hog","hop","pot","dot"])
print(result)
