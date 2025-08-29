from collections import defaultdict, deque


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        if endGene not in bank_set and endGene != startGene:
            return -1
        
        if startGene not in bank_set:
            bank.append(startGene)
            bank_set.add(startGene)

        
        graph = defaultdict(list)

        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                gene1, gene2 = bank[i], bank[j]

                diff_count = sum(1 for a, b in zip(gene1, gene2) if a != b)

                if diff_count == 1:
                    graph[gene1].append(gene2)
                    graph[gene2].append(gene1)
        
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current_gene, mutations = queue.popleft()

            if current_gene == endGene:
                return mutations
            
            for neighbor in graph[current_gene]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, mutations + 1))

        return -1

solution = Solution()

result = solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
print(result)