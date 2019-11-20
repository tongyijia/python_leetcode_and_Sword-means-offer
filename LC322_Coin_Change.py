class node:
    def __init__(self, value, step = 0):
        self.value = value
        self.step = step

class Solution:
    # BFS
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        queue = [node(amount)]
        visited = set()

        while queue:
            t = queue.pop(0)
            re = [t.value - i for i in coins]

            for i in re:
                if i < 0: continue
                if i == 0:
                    return t.step + 1
                elif i not in visited:
                    queue.append(node(i, t.step + 1))
                    visited.add(i)
        return -1
