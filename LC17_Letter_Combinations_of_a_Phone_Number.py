class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        table = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        for i in digits:
            if len(res) == 0:
                for j in table[i]:
                    res.append(j)
            else:
                tmp = []
                for j in table[i]:
                    for k in res:
                        tmp.append(k + j)
                res[:] = tmp[:]
        return res
