class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #print(n)
        binl = bin(n)
        binl = binl[2:]
        n = (32 - len(binl)) * ['0']
        l = list(binl)
        n.extend(l)
        #print(n)
        #l.reverse()
        binl = "".join(n[::-1])
        res = int(binl, 2)
        return res
