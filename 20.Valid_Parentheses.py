class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(":[")",0],"{":["}",1],"[":["]",2]}
        latest_bracket = []
        for char in s:
            for bracket in hashmap.keys():
                if char == bracket:
                    latest_bracket.append(hashmap[bracket][1])
                elif char == hashmap[bracket][0]:
                    try:
                        if hashmap[bracket][1] != latest_bracket.pop():
                            return False
                    except:
                        return False
                    
Solution = Solution()
print(Solution.isValid("(("))