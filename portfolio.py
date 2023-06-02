# imports
import pandas as pd
from collections import defaultdict
class Investment(object):
    def __init__(self, InvestmentName, InvestmentCost, ROI):
        self.InvestmentName = InvestmentName
        self.InvestmentCost = InvestmentCost
        self.ROI = ROI
    
    def __str__(self):
        return "{},{},{}".format(self.InvestmentName, self.InvestmentCost, self.ROI)
    
    def __gt__(self, other):
        if type(other) == Investment:
            return self.ROI > other.ROI
        else:
            return self.ROI > other

def loadInvestments(file):
    #investments = pd.read_csv(file, skiprows=2, usecols=[2,4,9], header=None, nrows=10) # Uncomment for tests
    investments = pd.read_csv(file, skiprows=2, usecols=[2,4,9], header=None)#, nrows=10)
    res = []
    for row in investments.iterrows():
        investmentName = row[1][2]
        investmentCost = row[1][4]
        ROI = row[1][9] * investmentCost
        investment = Investment(investmentName, investmentCost, ROI)
        res.append(investment)
    return res

def optimizeInvestments(investments, money):
    n = len(investments)
    K = [[0 for x in range(money + 1)] for x in range(n + 1)]
    actualInvestments = [[[] for x in range(money + 1)] for x in range(n+1)] #defaultdict(list)
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(money + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif investments[i-1].InvestmentCost <= w:
                if (investments[i-1].ROI + K[i-1][w-investments[i-1].InvestmentCost]) > K[i-1][w]:
                    K[i][w] = investments[i-1].ROI + K[i-1][w-investments[i-1].InvestmentCost]
                    for element in actualInvestments[i-1][w-investments[i-1].InvestmentCost]:
                        actualInvestments[i][w].append(element)
                    actualInvestments[i][w].append(investments[i-1])
                else:
                    K[i][w] = K[i-1][w]
                    for element in actualInvestments[i-1][w]:
                        actualInvestments[i][w].append(element)

            else:
                K[i][w] = K[i-1][w]
                for element in actualInvestments[i-1][w]:
                    actualInvestments[i][w].append(element)
    return K[n][money], actualInvestments[n][money]


def optimizeInvestments2(investments, money):
    n = len(investments)
    costs = []
    rois = []
    for element in investments:
        costs.append(element.InvestmentCost)
        rois.append(element.ROI)
    costs.append(money)
    K = [defaultdict(int) for x in range(n + 1)]
    actualInvestments = [ defaultdict(list) for x in range(n+1)] #defaultdict(list)
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in costs:
            if i == 0 or w == 0:
                K[i][w] = 0
            elif investments[i-1].InvestmentCost <= w:
                if (investments[i-1].ROI + K[i-1][w-investments[i-1].InvestmentCost]) > K[i-1][w]:
                    K[i][w] = investments[i-1].ROI + K[i-1][w-investments[i-1].InvestmentCost]
                    for element in actualInvestments[i-1][w-investments[i-1].InvestmentCost]:
                        actualInvestments[i][w].append(element)
                    actualInvestments[i][w].append(investments[i-1])
                else:
                    K[i][w] = K[i-1][w]
                    for element in actualInvestments[i-1][w]:
                        actualInvestments[i][w].append(element)

            else:
                K[i][w] = K[i-1][w]
                for element in actualInvestments[i-1][w]:
                    actualInvestments[i][w].append(element)
    return K[n][money], actualInvestments[n][money]

if __name__ == "__main__":
    #file = "zhvi-short.csv" # Short version
    file = "state_zhvi_summary_allhomes.csv" # Long version
    #money = 15
    money = 750000
    investments = loadInvestments(file)
    # for x in investments:
    #     print(x)
    x,y = optimizeInvestments2(investments, money)
    print(x)
    roi = 0
    cost = 0
    for investment in y:
        print(investment)
        roi+=investment.ROI
        cost+=investment.InvestmentCost
    print("ROI: {}, Cost: {}, Money: {}".format(roi,cost,money))