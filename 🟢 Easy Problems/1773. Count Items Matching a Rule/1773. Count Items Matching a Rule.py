class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKeyIndex = {"type": 0, "color": 1, "name": 2}
        index = ruleKeyIndex[ruleKey]
        total = 0
        
        for item in items:
            if item[index] == ruleValue:
                total += 1
                
        return total