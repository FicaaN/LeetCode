class Solution:
    def totalMoney(self, n: int) -> int:

        day = 0
        money = 1
        total = 0

        while day < n:
            total += money
            money += 1
            day += 1

            if day % 7 == 0:
                money = day // 7 + 1
            
        return total