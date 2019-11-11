class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BFS
        pre = prerequisites
        indegrees = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]
        for i, j in pre:
            indegrees[i] += 1
            adj[j].append(i)

        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            p = queue.pop(0)
            numCourses -= 1
            for cur in adj[p]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses
