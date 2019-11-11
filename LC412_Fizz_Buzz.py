class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = [str(i) for i in range(1,n+1)]

        i = 2
        while i < n:
            res[i] = "Fizz"
            i += 3

        i = 4
        while i < n:
            if res[i] == "Fizz":
                res[i] += "Buzz"
            else:
                res[i] = "Buzz"

            i += 5

        return res
