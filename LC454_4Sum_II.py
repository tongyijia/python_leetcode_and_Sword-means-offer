class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        h = {}
        for a in A:
            for b in B:
                if -a -b in h:
                    h[-a - b] += 1
                else:
                    h[-a - b] = 1
        return sum([h[c + d] for c in C for d in D if c + d in h]) 
