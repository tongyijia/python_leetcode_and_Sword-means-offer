class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if denominator == 0: return 'NaN'

        res = []

        if numerator * denominator < 0:
            res.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)


        tmp, yu = divmod(numerator,denominator)

        if yu == 0: return ''.join(res) + str(tmp)

        res.append(str(tmp))
        res.append('.')
        loc = {yu: len(res)}

        while yu:
            yu *= 10
            shang, yu = divmod(yu, denominator)
            res.append(str(shang))
            if yu in loc:
                res.insert(loc[yu], '(')
                res.append(')')
                break
            loc[yu] = len(res)

        return ''.join(res)
