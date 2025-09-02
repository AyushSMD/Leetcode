class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = [0,0]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[j-1:None if i == 0 else i-1:-1]:
                    if ls[1]-ls[0] < j-i:
                        ls = [i,j]
        
        return s[ls[0]:ls[1]]

sol = Solution()
print (sol.longestPalindrome("cbbd"))