import csv
from collections import defaultdict
class Stock: 
    # In this case, I decided that the best way to get both the max profit and the buy and sell dates was to
    # create an object Stock that had the profit, the buy, and the sell dates. Then, when adding the profits, 
    # we just had to also "add" the dates.
    def __init__(self, ticker, buy_date, sell_date, price_change, company = None):
        self.ticker = ticker
        self.company = company
        self.buy_date = buy_date
        self.sell_date = sell_date
        self.price_change = price_change
    def __gt__(self, other):
        if type(other) == Stock:
            return self.price_change > other.price_change
        else:
            return self.price_change > other
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.ticker, self.company, self.buy_date, self.sell_date, self.price_change)

def read_csv_stock(stock_data):
    res = defaultdict(list)
    with open(stock_data, "r", newline="") as file:
        lines = csv.reader(file, delimiter=' ')
        next(lines, None) # This line skips the headers
        for line in lines:
            row = line[0].split(",")
            tick = row[1]
            res[tick].append(line)
        return res

def read_csv_companies(securities):
    res = {}
    with open(securities, "r", newline="") as file:
        lines = csv.reader(file, delimiter=',')
        next(lines, None) # This line skips the headers
        for line in lines:
            tick = line[0]
            company = line[1]
            res[tick] = company
        return res

def MSSDAC(A, low = 0, high = None):
    # The algorith is basically the same as the one in the pdf, but this one uses my object Stock instead of the profit directly
    if high == None: 
        high = len(A) - 1
    # Base case
    if low == high:
        if A[low].price_change > 0 : 
            return Stock(A[0].ticker,A[0].buy_date,A[0].sell_date,A[0].price_change, A[0].company)
        else:
            return Stock(A[0].ticker,A[0].buy_date,A[0].sell_date,0, A[0].company)
    # divide
    mid = (low + high) // 2
    # conquer
    maxLeft = MSSDAC(A, low, mid)
    maxRight = MSSDAC(A, mid+1, high)
    # Combine
    maxLeft2Center = Stock(A[0].ticker,A[0].buy_date,A[0].sell_date,0, A[0].company)
    left2Center = Stock(A[mid].ticker, None, A[mid].sell_date, 0, None)
    for i in range(mid, low-1, -1):
        left2Center.price_change += A[i].price_change
        if left2Center > maxLeft2Center:
            left2Center.buy_date = A[i].buy_date
            maxLeft2Center = Stock(A[i].ticker, A[i].buy_date, A[i].sell_date, left2Center.price_change)
    maxRight2Center = Stock(A[0].ticker,A[0].buy_date,A[0].sell_date,0, A[0].company)
    right2Center = Stock(A[mid].ticker, None, A[high].sell_date, 0, None)
    for i in range(mid+1, high+1):
        right2Center.price_change += A[i].price_change
        if right2Center > maxRight2Center:
            right2Center.buy_date = A[i].buy_date
            maxRight2Center = Stock(A[i].ticker, A[i].buy_date, A[i].sell_date, right2Center.price_change)
    plus_stock = Stock(A[0].ticker,maxLeft2Center.buy_date,maxRight2Center.sell_date,maxRight2Center.price_change + maxLeft2Center.price_change, A[0].company)
    return max(maxLeft, maxRight, plus_stock)

def max_stock_profit(stocks, companies):
    res = []
    for key in stocks.keys():
        A = []
        days = stocks[key]
        for i in range(len(days)-1):
            open_sell = float(days[i+1][0].split(",")[3])
            open_buy = float(days[i][0].split(",")[3])
            date_buy = days[i][0].split(",")[0]
            date_sell = days[i+1][0].split(",")[0]
            price_change = open_sell-open_buy
            A.append(Stock(key, date_buy, date_sell, price_change, company=companies[key]))
        res.append(MSSDAC(A))
    max_profit = max(res)
    print("Best stock to buy: \"{}\" on {} and sell on {} with profit of {}".format(max_profit.company, max_profit.buy_date, max_profit.sell_date, max_profit.price_change))
    return res

if __name__ == "__main__":
    stocks = "prices-split-adjusted.csv"
    securities = "securities.csv"
    dict_stocks = read_csv_stock(stocks)
    dict_companies = read_csv_companies(securities)
    x = max_stock_profit(dict_stocks, dict_companies)
    for s in x:
        print(str(s))