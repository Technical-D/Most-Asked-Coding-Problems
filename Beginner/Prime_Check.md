# Prime Number Checker

## Problem Statement
Given an integer `n`, determine whether it is a **prime number**.

## Example
### Input:
n = 29

### Output:
True

Explanation: `29` is only divisible by `1` and `29`.

### Input:
n = 10

### Output:
False

Explanation: `10` is divisible by `1, 2, 5, 10`.

## Constraints
- `n >= 0`
- A prime number is a number **greater than 1** with no divisors other than `1` and itself.

## Approach
1. **Edge Case:** If `n < 2`, return `False`.
2. **Check divisibility:** Iterate from `2` to `sqrt(n)`, return `False` if divisible.
3. If no divisor is found, return `True`.
4. **Time Complexity:** `O(√n)`, **Space Complexity:** `O(1)`.