# Longest Valid Parentheses

## Problem Statement
Given a string containing just the characters `'('` and `')'`, return the **length** of the longest valid (well-formed) parentheses substring.

## Example
### Input:
s = "(()))())("
### Output:
4

Explanation: The longest valid parentheses substring is `"()"` or `"(())"`.

## Constraints
- `0 <= s.length <= 10^4`
- `s[i]` is either `'('` or `')'`.

## Approach
### 1️⃣ Using Stack (O(n))
- Use a **stack** to keep track of indices of `'('`.
- If we encounter `')'`, pop from the stack and compute the length.
- If the stack is empty after popping, push the current index as a **new base**.
- Keep track of the maximum length found.

### 2️⃣ Dynamic Programming (O(n))
- Maintain a DP array where `dp[i]` represents the longest valid substring ending at `i`.
- Check cases where `s[i] == ')'` and update the DP table accordingly.
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(n)`

### 3️⃣ Two-Pointer Approach (O(n))
- Use two counters (`left` and `right`) to scan the string twice (left-to-right, right-to-left).
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(1)`

