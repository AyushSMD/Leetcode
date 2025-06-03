class Solution:
    def romanToInt(self, s: str) -> int:
        Master_Roman_int_dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        Current_Roman_int_dict = Master_Roman_int_dict
        # numval = values[s[0]]
        # for i in range(0,len(s)-1):
        #     if values[s[i]]==values[s[i+1]]:
        #         numval += values[s[i+1]]
        #     elif values[s[i]]>values[s[i+1]]:
        #         numval += values[s[i+1]]
        #     else:
        #         numval -= values[s[i+1]]
        # return numval
        for R in Current_Roman_int_dict:
            if R in s:
                

Solution = Solution()
print(Solution.romanToInt("MCMXCIV"))