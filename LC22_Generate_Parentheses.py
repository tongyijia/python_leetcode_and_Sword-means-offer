class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        # 我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
        #如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号

        def backtrack(S = '', left =   0, right = 0):
            if len(S) == 2 * n:
                res.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)

            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return res
