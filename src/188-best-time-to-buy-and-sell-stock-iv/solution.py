# ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=study-plan-v2&envId=top-interview-150

import copy
from dataclasses import dataclass
import enum
from typing import List


class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    """
    Problem:
      Can buy one stock at once, at most k transactions.
      Given array of prices[i] of stock on i-th day. Find max profit.

    This problem differs from previous #122 in that the actual transaction
    branches need to be stored.

    The max() function previously allowed collapsing groups of transactions.
    The actual transactions themselves weren't important, just the grouped
    outcome of each branch.

    Here we just brute force all combinations of transactions from day 0.

    Args:
      k (int): Maximum number of transactions to permit
      prices: List of stock prices on i-th day

    Returns:
      int: The maximum possible profit
    """
    print(f'Prices: {prices}')
    print(f'Max number of transactions: {k}')
    transaction_logs: list[TransactionLog] = [TransactionLog()]
    N = len(prices)
    for i in range(0, N):
      # Brute force each possible outcome at time:
      # - Do nothing
      # - Buy (if not already holding)
      # - Sell (if holding)
      new_transaction_logs: list[TransactionLog] = []
      for log in transaction_logs:
        holding = log.holding()
        log_with_wait = log
        log_with_transaction = copy.deepcopy(log)
        if not holding:
          log_with_transaction.profit -= prices[i]
          log_with_transaction.transactions.append(Transaction(i, TransactionType.BUY))
        else:
          log_with_transaction.profit += prices[i]
          log_with_transaction.transactions.append(Transaction(i, TransactionType.SELL))
        new_transaction_logs.extend([log_with_wait, log_with_transaction])
      transaction_logs = new_transaction_logs
    legal_logs = [log for log in transaction_logs if is_legal(log, k)]
    log_with_max_profit = max(legal_logs, key=lambda log: log.profit)
    print('Legal transaction logs:')
    for log in legal_logs:
      print(log.to_string())
    print(f'Max profit: {log_with_max_profit.profit}')
    return log_with_max_profit.profit


class TransactionType(enum.StrEnum):
  BUY = 'buy'
  SELL = 'sell'


@dataclass
class Transaction:
  date: int
  type: TransactionType

  def to_string(self):
    return f'{self.date}: {self.type}'


class TransactionLog:
  profit: int
  transactions: list[Transaction]

  def __init__(self, profit = 0, transactions: list[TransactionType] = []):
    self.profit = profit
    self.transactions = transactions

  def holding(self) -> bool:
    """
    Given this transaction log, are we currently holding a stock?
    """
    holding = self.transactions and self.transactions[-1].type == TransactionType.BUY
    return holding
  
  def to_string(self):
    return f'total: {self.profit} <- {", ".join([t.to_string() for t in self.transactions])}'


def is_legal(log: TransactionLog, max_transactions_per_type: int) -> bool:
  """
  Calculate whether a transaction log exceeds legal number of transactions of each type
  """
  transaction_count: dict[TransactionType, int] = {
    name: 0 for name in TransactionType
  }
  for trans in log.transactions:
    count = transaction_count[trans.type] + 1
    if count > max_transactions_per_type:
      return False
    transaction_count[trans.type] = count
  return True


if __name__ == '__main__':
  a = [3, 4, 1, 6, 10, 5, 8]
  max = Solution().maxProfit(a)
