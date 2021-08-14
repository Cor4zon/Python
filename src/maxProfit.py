from typing import List


def maxProfit(prices: List[int]) -> int:
    minPrice = max(prices)
    maxPrice = min(prices)
    for i in prices:
        for j in prices:
            if i < minPrice and prices.index(i) < prices.index(j):
                minPrice = i
            if j > maxPrice and prices.index(i) < prices.index(j):
                maxPrice = j
    return maxPrice - minPrice




print(maxProfit([7,1,5,3,6,4]) == 5)
print(maxProfit([7,6,4,3,1]) == 0)
print(maxProfit([0, 0, 0, 1, 0, 0, 1]) == 1)
print(maxProfit([0, 1, 2, 3, 4, 5]) == 5)
print(maxProfit([1, 2, 3, 0, 1, 2, 3, 4, 5]) == 5)
