def maximumToys(prices, k):
    prices.sort()
    items = 0
    itemNumber = 0
    moneyRemaining = k
    while (prices[itemNumber] <= moneyRemaining and items < len(prices)):
        moneyRemaining -= prices[itemNumber]
        items += 1
        itemNumber += 1
    return items
