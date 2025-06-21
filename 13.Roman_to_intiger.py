class Solution:
    def romanToInt(self, s: str) -> int:
        Master_Roman_int_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        number = 0

        if len(s) == 1 :
            return Master_Roman_int_dict[s[0]]

        for i in range(0,len(s)-1):
            if Master_Roman_int_dict[s[i]] < Master_Roman_int_dict[s[i+1]]:
                number = number - Master_Roman_int_dict[s[i]]
                continue
            number = number + Master_Roman_int_dict[s[i]]

        number = number + Master_Roman_int_dict[s[i+1]]

        return number

Solution = Solution()
print(Solution.romanToInt("MCMXCIV"))