class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        # Firstly we sord the prices to make it easier to find
        prices.sort()

        # In case there are less than two chocolates, we return the initial money
        if len(prices) < 2:
            return money
        
        # Here we're checking if the sum of the two cheapest chocolates is less or equal to the money given at be beginning
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        else:
            return money