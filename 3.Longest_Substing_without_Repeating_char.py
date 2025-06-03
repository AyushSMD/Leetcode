class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxcounter = 0
        hashmap = {}
        for i,char in enumerate(s):
            if char not in substring:
                substring += char
                maxcounter=len(substring) if len(substring) > maxcounter else maxcounter
                hashmap[char]=i
            else:
                substring = s[hashmap[char]+1:i:]+char
                hashmap[char]=i

        return maxcounter

SolObj = Solution()
SolObj.lengthOfLongestSubstring("pwwkew")