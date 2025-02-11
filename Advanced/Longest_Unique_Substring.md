# Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the **length** of the **longest substring** without repeating characters.

## Example
### Input:
s = "abcabcbb"

### Output:
3

Explanation: The longest unique substring is `"abc"`, which has a length of `3`.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of **English letters, digits, symbols, and spaces**.

## Approach
### 1️⃣ Sliding Window + Hash Map (O(n))
- Maintain a **hash map** to track the last occurrence of each character.
- Use **two pointers (`left`, `right`)** to create a sliding window.
- If a duplicate is found, **shift `left` pointer** to remove duplicates.
- Keep track of the **maximum length** of a valid substring.
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(min(n, charset))`

### 2️⃣ Brute Force (O(n²)) [Not Efficient]
- Try every substring and check for uniqueness.
- **Time Complexity:** `O(n²)`, **Space Complexity:** `O(n)`