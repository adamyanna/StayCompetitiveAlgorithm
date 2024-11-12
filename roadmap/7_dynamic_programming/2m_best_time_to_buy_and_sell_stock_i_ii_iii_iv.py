#!/usr/bin/env python3
"""
买卖股票的最佳时机
best-time-to-buy-and-sell-stock
"""

import unittest

"""
i
prices[i] = stock price for i day
buy the stock at x
sell the stock at y

maximum profit = price[y] - price[x]

输入：[7,1,5,3,6,4]
输出：5
"""


class SolutionI(object):
    def max_profit(self, prices):
        """
        Dynamic Programming

        max_profit = max(max_profit, stock[i] - min(min_price, stock[i])

        dp_min_price = min(dp_min_price, stock[i])
        dp_max_profit = max(dp_max_profit, stock[i] - dp_min_price)

        :param prices:
        :return:
        """
        import sys
        dp_min_price = sys.maxsize
        dp_max_profit = 0

        for v in prices:
            dp_min_price = min(dp_min_price, v)
            dp_max_profit = max(dp_max_profit, v - dp_min_price)

        return dp_max_profit

    def max_profit_dp(self, prices):
        """
        dp[i][0] max profit without holding stock
        dp[i][1] max profit holding stock
        f:
        dp[i] = max(dp[i-1][0], dp[i][1] + prices[i])
        :param prices:
        :return:

        输入：[7,1,5,3,6,4]
        输出：5
        """
        import sys
        max_holding = - (sys.maxsize + 1)
        max_profit = 0
        for v in prices:
            max_holding = max(-v, max_holding)
            max_profit = max(max_profit, v + max_holding)

        return max_profit


class TestSolutionI(unittest.TestCase):
    def test_max_profit_dp(self):
        print(SolutionI().max_profit_dp([7, 1, 5, 3, 6, 4]))


"""
ii
prices[i] = stock price for i day
buy or sell the stock at x
max hold for stock is count=1

maximum profit

输入：prices = [7,1,5,3,6,4]
输出：7
"""


class SolutionII(object):
    def max_profit(self, prices):
        """
        1, 4, 6, 5, 8
        8 - 1 < (4 -1) + (6 -4) + (8-5)
        dp[i][0] no holding stock max profit
        dp[i][1] holding stock max profit

        # 当天不持有股票的最大收益，应该是【昨天不持有的最大收益】和【昨天持有且今天卖出的最大收益】之间的最大值
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # 当天持有股票的最大收益，应该是【昨天持有股票的最大收益】和【昨天不持有股票今天买入的最大收益】之间的最大值
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[i][0]

        :param prices:
        :return:
        """
        dp_holding_max = - prices[0]
        dp_no_holding_max = 0
        for i in range(len(prices)):
            dp_holding_max = max(dp_holding_max, dp_no_holding_max - prices[i])
            dp_no_holding_max = max(dp_no_holding_max, dp_holding_max + prices[i])

        return dp_no_holding_max


class TestSolutionII(unittest.TestCase):
    def test_max_profit(self):
        print(SolutionII().max_profit([7, 1, 5, 3, 6, 4]))


"""
iii
prices[i] = stock price for i day
buy or sell the stock at x
2 time trade, but not at same day

maximum profit

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
"""


class SolutionIII(object):
    def max_profit(self, prices):
        """
        two times trade
        current profit -> dp
        dp[i][1][0] buy one time
        dp[i][2][0] bug and sell 1st time
        dp[i][2][1] bug and sell 1st time, bug for 2nd time
        dp[i][2][2] bug and sell 1st time, bug and sell for 2nd time

        dp[i][1][0] = max(dp[i][1][0], -prices[i])
        dp[i][2][0] = max(dp[i][2][0], dp[i][1][0] + prices[i])
        dp[i][2][1] = max(dp[i][2][1], dp[i][2][0] - prices[i])
        dp[i][2][2] = max(dp[i][2][2], dp[i][2][1] + prices[i])

        :param prices:
        :return:
        """
        import sys
        # 0 -> 1st buy 1 -> 1st sell 2 -> 2nd buy 3 -> 2nd sell
        update_profit = [-(sys.maxsize + 1), 0, -(sys.maxsize + 1), 0]
        for v in prices:
            update_profit[0] = max(update_profit[0], -v)
            update_profit[1] = max(update_profit[1], update_profit[0] + v)
            update_profit[2] = max(update_profit[2], update_profit[1] - v)
            update_profit[3] = max(update_profit[3], update_profit[2] + v)

        return update_profit[3]


class TestSolutionIII(unittest.TestCase):
    def test_max_profit(self):
        """
        -> [3,3,5,0,0,3,1,4]
        [-3, 0, -3, 0]
        [-3, 0, -3, 0]
        value = 3, max profit = 0
        [-3, 2, -3, 2]
        value = 5, max profit = 2
        [0, 2, 2, 2]
        value = 0, max profit = 2
        [0, 2, 2, 2]
        value = 0, max profit = 2
        [0, 3, 2, 5]
        value = 3, first max = 3, second max = 2, result = 5
        [0, 3, 2, 5]
        value = 1, first max = 3, second max = 2, result = 5
        [0, 4, 2, 6]
        value = 4, first buy max = 0, first sell max = 3
        6
        :return:
        """
        print(SolutionIII().max_profit([3, 3, 5, 0, 0, 3, 1, 4]))


"""
iv
prices[i] = stock price for i day
buy or sell the stock at x
k time trade, but not at same day

maximum profit

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
"""


class SolutionIV(object):
    def max_profit(self, prices, k):
        """
        k time trade
        current profit -> dp
        dp[i][1][0] buy one time
        dp[i][2][0] bug and sell 1st time
        dp[i][2][1] bug and sell 1st time, bug for 2nd time
        dp[i][2][2] bug and sell 1st time, bug and sell for 2nd time
        ...
        dp[i]....[2][2] bug and sell k - 1 time, bug and sell for k time

        dp[i][1][0] = max(dp[i][1][0], -prices[i])
        dp[i][2][0] = max(dp[i][2][0], dp[i][1][0] + prices[i])
        dp[i][2][1] = max(dp[i][2][1], dp[i][2][0] - prices[i])
        dp[i][2][2] = max(dp[i][2][2], dp[i][2][1] + prices[i])
        ...
        dp[i]....[2][2] = max(dp[i]....[2][2], dp[i]..[2][1] + prices[i])

        :param stock:
        :return:
        """
        import sys
        # i % 2 == 0 -> buy time max profit (0, 2, 4)
        # i % 2 == 2 -> sell time max profit (1, 3, 5)
        update_prices = [0] * k * 2
        for i in range(k * 2):
            if i % 2 == 0:
                update_prices[i] = -sys.maxsize - 1

        for v in prices:
            for i in range(k * 2):
                if i % 2 == 0:
                    # buy stock
                    if i == 0:
                        update_prices[i] = max(update_prices[i], -v)
                    else:
                        update_prices[i] = max(update_prices[i], update_prices[i-1] - v)
                else:
                    # sell stock
                    update_prices[i] = max(update_prices[i], update_prices[i - 1] + v)

        return update_prices[-1]

class TestSolutionIV(unittest.TestCase):
    def test_max_profit(self):
        print(SolutionIV().max_profit([3,2,6,5,0,3],2))