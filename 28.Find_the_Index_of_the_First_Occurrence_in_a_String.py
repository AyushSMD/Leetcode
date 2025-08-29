class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        found_counter = 0
        for i in range(len(haystack)):
            if needle[found_counter] == haystack[i]:
                found_counter+=1
            else:
                found_counter=0
            if found_counter==len(needle):
                return (i-found_counter+1)
            print (found_counter,haystack[i])
        
        return -1

sol = Solution()
print (sol.strStr("mississippi","issip"))