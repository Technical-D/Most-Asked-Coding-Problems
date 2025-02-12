# Fibonacci Series Up to N

## Problem Statement
Given an integer `n`, print the Fibonacci series up to (but not exceeding) `n`.

## Example
### Input:
n = 50

### Output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Explanation: The Fibonacci series up to `50` is listed above.

## Constraints
- `n >= 0`
- The series starts with `0, 1` and continues until the next term **exceeds** `n`.

## Approach
- **Initialize** a list with `[0, 1]` (first two Fibonacci numbers).
- **Use a while loop** to generate new terms by summing the last two elements (`list[-1] + list[-2]`).
- **Break when the next term exceeds `n`**.
- **Time Complexity:** `O(log n)` (approximately linear growth).
- **Space Complexity:** `O(1)`, as only a list is used.