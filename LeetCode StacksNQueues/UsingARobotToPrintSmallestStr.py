class Solution(object):
    def robotWithString(self, s):
        n = len(s)
        
        suffix_min_char = [''] * n
        suffix_min_char[n - 1] = s[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min_char[i] = min(s[i], suffix_min_char[i + 1])
        
        tStak = []
        pResult = []
        s_idx = 0

        while s_idx < n or tStak:
            if s_idx < n:
                current_s_char = s[s_idx]
                
                if not tStak or tStak[-1] > suffix_min_char[s_idx]:
                    tStak.append(current_s_char)
                    s_idx += 1
                else:
                    pResult.append(tStak.pop())
            else:
                pResult.append(tStak.pop())

        return "".join(pResult)


solution = Solution()

result = solution.robotWithString("zza")
print(result)