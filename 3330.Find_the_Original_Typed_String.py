class Solution:
    def possibleStringCount(self, word: str) -> int:
        no_possilbe_strings = 1
        for i in range(0,len(word)-1):
            if word[i]==word[i+1]:
                no_possilbe_strings+=1

        return no_possilbe_strings

Sol = Solution()
print (Sol.possibleStringCount('aaaa'))