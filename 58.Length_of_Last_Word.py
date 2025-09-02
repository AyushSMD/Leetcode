class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # print (s.strip(' ').split(' ')[-1])
        return len(s.strip(' ').split(' ')[-1])

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))