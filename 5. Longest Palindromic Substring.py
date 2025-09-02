class Solution:
    def longestPalindrome(self, s: str) -> str:
        # c=0
        ls = [0,0]
        for i in range(0,len(s)):
            for j in range(i+1+ls[1]-ls[0],len(s)+1):
                # print(s[i:j])
                # c+=1
                if s[i:j]==s[j-1:None if i == 0 else i-1:-1]:
                    if ls[1]-ls[0] < j-i:
                        ls = [i,j]
        
        # print (c)
        return s[ls[0]:ls[1]]

sol = Solution()
print (sol.longestPalindrome("babad"))