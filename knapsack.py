from typing import List


def knapSack(W, wt: List[int], val: List[int], n):
    # Base Case if n or W is 0
    if W == 0 or n == 0:
        return 0

    elif wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1),
        )


if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapSack(W, weight, profit, n))
 