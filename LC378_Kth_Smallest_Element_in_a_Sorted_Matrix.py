from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minheap = []
        n = len(matrix)
        for i in range(min(k,n)):
            heappush(minheap, (matrix[i][0], i, 0))

        count = 0
        x,i,j = 0,0,0
        while count < k:
            count += 1
            x,i,j = heappop(minheap)
            if j < n - 1:
                heappush(minheap, (matrix[i][j+1], i, j+1))
        return x
