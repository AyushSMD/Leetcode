class Solution:
    def longestPalindrome(self, s: str) -> str:
        # c=0
        if len(s)==1:
            return s
        for i in range(len(s),0,-1):
            # print(i)
            j=0
            while (i+j<=len(s)):
                # print(i,j,i+j,s[j:i+j],s[i+j-1:None if j == 0 else j-1:-1])
                if s[j:i+j] == s[i+j-1:None if j == 0 else j-1:-1]:
                    return s[j:i+j]
                j+=1
            # for j in range():
                # print(s[i:j])
                # c+=1
                # if s[i:j]==s[j-1:None if i == 0 else i-1:-1]:
                #     if ls[1]-ls[0] < j-i:
                #         ls = [i,j]
        
        # print (c)
        # return s[ls[0]:ls[1]]

sol = Solution()
print (sol.longestPalindrome("bb"))