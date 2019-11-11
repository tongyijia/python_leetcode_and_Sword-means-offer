class Solution:
    def countAndSay(self, n: int) -> str:

        if n < 1 or n > 30: return False

        i = 1
        res = ""

        for i in range(n):
            tmp = ""
            if i == 0:
                tmp = "1"
            else:
                j = 0
                k = 0
                while k < len(res):
                    if res[j] == res[k]:
                        if k == len(res) - 1:
                            tmp += str(k-j+1) + res[j]
                            break
                        else:
                            k += 1
                    else:

                        tmp += str(k - j) + res[j]
                        j = k

            res = tmp
        return res
