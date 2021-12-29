# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# Find and return the maximum profit you can achieve.

## Test case- 1:
    # Input: prices = [7,1,5,3,6,4]
    # Output: 7

## Test case- 2:
    # Input: prices = [1,2,3,4,5]
    # Output: 4

## Test case- 3:
    # Input: prices = [7,6,4,3,1]
    # Output: 0


def maxProfit(prices):
    maxprofit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            curprofit=prices[i]-prices[i-1] 
            maxprofit+= curprofit       
                
    return maxprofit


prices=[int(i) for i in input().split()]
print(maxProfit(prices))

