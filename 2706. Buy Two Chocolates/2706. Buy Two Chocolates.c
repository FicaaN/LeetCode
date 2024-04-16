int buyChoco(int* prices, int pricesSize, int money){

    // Firstly we do the bubble sort of the prices
    for (int i = 0 ; i < pricesSize - 1 ; i++) {
        for (int j = 0 ; j < pricesSize - i - 1 ; j++) {
            if (prices[j] > prices[j + 1]) {

                int temp = prices[j];
                prices[j] = prices[j + 1];
                prices[j + 1] = temp;
            }
        }
    }

    // If there're less than two chocolates, return initial money
    if (pricesSize < 2) {
        return money;
    }

    // Here we're checking if the sum of the two cheapest chocolates is less or equal than money given
    if (prices[0] + prices[1] <= money) {
        return money - (prices[0] + prices[1]);
    } else {
        return money;
    }
}