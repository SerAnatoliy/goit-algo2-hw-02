from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def helper(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        cuts = []
        for i in range(1, n + 1):
            if i <= len(prices):
                profit, sub_cuts = helper(n - i)
                profit += prices[i - 1]
                if profit > max_profit:
                    max_profit = profit
                    cuts = sub_cuts + [i]

        memo[n] = (max_profit, cuts)
        return memo[n]

    max_profit, cuts = helper(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1 if cuts else 0
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(1, n + 1):
            if i <= len(prices):
                if dp[n] < dp[n - i] + prices[i - 1]:
                    dp[n] = dp[n - i] + prices[i - 1]
                    cuts[n] = cuts[n - i] + [i]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1 if cuts[length] else 0
    }