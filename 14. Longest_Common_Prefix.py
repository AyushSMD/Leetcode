class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        lcp = strs[0]
        for string in strs[1:]:
            i = 0
            while i < len(lcp) and i < len(string) and lcp[i] == string[i]:
                i += 1
            lcp = lcp[:i]
            if not lcp:
                return ""

        return lcp

sol = Solution()
print (sol.longestCommonPrefix(["ab", "a"]))