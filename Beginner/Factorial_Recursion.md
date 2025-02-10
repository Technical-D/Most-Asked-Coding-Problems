# Factorial Using Recursion

## Problem Statement
Given a non-negative integer `n`, compute its **factorial** using recursion.

## Example
### Input:
n = 5

### Output:
120

Explanation: `5! = 5 × 4 × 3 × 2 × 1 = 120`.

## Constraints
- `0 <= n <= 12` (to prevent integer overflow in some languages)
- The factorial of `n` is calculated as:
n! = n × (n-1) × (n-2) × ... × 1

## Approach
### 1️⃣ Recursive Approach (O(n))
- **Base Case:** If `n == 0` or `n == 1`, return `1`.
- **Recursive Case:** `factorial(n) = n * factorial(n-1)`.
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(n)` (due to recursive stack).

### 2️⃣ Iterative Approach (O(n))
- Use a loop instead of recursion to compute `factorial(n)`.
- **Better for larger `n`** since it avoids recursion depth issues.
