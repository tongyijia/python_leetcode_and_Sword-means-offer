class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def listPlus(l: List[int]) -> List[int]:

            n = len(l)
            res = [1]

            if n == 0: return [1]
            if n == 1: return [1,1]

            for i in range(n-1):
                res.append(l[i] + l[i+1])
            res.append(1)
            return res


        result = []
        tmp = []
        for i in range(numRows):

            tmp = listPlus(tmp)

            result.append(tmp)

        return result
