class node:
    def __init__(self, value, step = 0):
        self.value = value
        self.step = step


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visted = set([node(n).value])

        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - i * i for i in range(1, int(vertex.value ** 0.5) + 1)]
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                if i == 0:
                    return new_vertex.step
                elif i not in visted:
                    queue.append(new_vertex)
                    visted.add(i)
        return -1
