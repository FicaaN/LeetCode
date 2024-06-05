class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list_jewels = list(jewels)
        list_stones = list(stones)

        counter = 0

        for i in list_jewels:
            for j in list_stones:
                if i == j:
                    counter += 1
        
        return counter