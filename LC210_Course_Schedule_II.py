class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]

        for i,j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)

        queue = []
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            t = queue.pop(0)
            res.append(t)
            numCourses -= 1
            for cur in adj[t]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    queue.append(cur)
        if numCourses == 0:
            return res
        else:
            return []
