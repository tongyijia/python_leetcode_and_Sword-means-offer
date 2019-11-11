class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2 : return 0

        hash_table = [1] * n

        hash_table[0] = hash_table[1] = 0


        for i in range(2, int(n ** 0.5) + 1):
            if hash_table[i]:
                hash_table[i*i:n:i] = [0] * ((n-1-i*i) // i + 1)
        return sum(hash_table)
